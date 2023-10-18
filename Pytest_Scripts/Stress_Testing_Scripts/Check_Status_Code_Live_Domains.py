import requests
import concurrent.futures
import time
import json
import urllib3
from tqdm import tqdm
from website_domains_production import DOMAINS
from jira import JIRA

# Disable insecure request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

result = DOMAINS
alive_domains = []
missing_main_menu_domains = []
connection_errors = []
slow_domains = []
errors = []

jira = JIRA(server='https://linkedunion.atlassian.net', basic_auth=('arbish@linkedunion.com', 'ATATT3xFfGF0e-WOoGJAiDy-VdYd1TYf-hAlDQfOTLgpo7gv7VCr1uDO2l2RGrCG311dTvbZcJM74zCstvJfmhIaFbWgeatykhhmeDQJd2IgO1UiBwZWHJ7tCpLJQcZuH_vCzhj1yBbMEAty_xGItOsG3GVnI2XtAxQcb-OMvkWI8bjZv8E90JY=74D0A404'))
slack_message = ""


def issue_exists_with_summary(jira, summary):
    issues = jira.search_issues(f'summary ~ "{summary}"')
    return bool(issues)


def get_issue_summary_and_status(jira, summary):
    issues = jira.search_issues(f'summary ~ "{summary}"')
    if issues:
        issue = issues[0]  # Assuming there is at most one issue with the same summary
        return issue.fields.status.name, issue.permalink()
    return None, None


def create_jira_issue(errors, label=None, jira=None):
    summary = "Domain Issues Detected"
    description = "\n\n".join(errors)

    existing_issue_status, existing_issue_url = get_issue_summary_and_status(jira, summary)

    if existing_issue_status in ("Verified", "Deployed"):
        print(f"An issue with the same summary exists and is in '{existing_issue_status}' status. Creating a new issue.")
        new_issue = jira.create_issue(
            project='LU',
            summary=summary,
            description=description,
            issuetype={'name': 'Bug'},
            labels=[label] if label else None  # Add the label here
        )
        print(f"New issue created with key: {new_issue.key}")
        print(f"Link to new issue: {new_issue.permalink()}")
        return new_issue.key, new_issue.permalink()

    elif not issue_exists_with_summary(jira, summary):
        new_issue = jira.create_issue(
            project='LU',
            summary=summary,
            description=description,
            issuetype={'name': 'Bug'},
            labels=[label] if label else None  # Add the label here
        )
        print(f"New issue created with key: {new_issue.key}")
        print(f"Link to new issue: {new_issue.permalink()}")
        return new_issue.key, new_issue.permalink()
    else:
        print("An issue with the same summary already exists.")
        slack_message = f"An issue with the same summary already exists. {existing_issue_url}"
        return None, slack_message


def check_domain(url):
    print(f"Checking domain: {url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    max_retries = 3
    retry_delay = 5  # seconds

    for _ in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=30, verify=True)

            if "Main Menu" not in response.text:
                missing_main_menu_domains.append(url)

            alive_domains.append(url)
            return

        except requests.exceptions.Timeout as e:
            print(f"Timeout error checking domain {url}: {str(e)}")
            time.sleep(retry_delay)

        except requests.exceptions.RequestException as e:
            print(f"Error checking domain {url}: {str(e)}")
            time.sleep(retry_delay)

        except requests.exceptions.SSLError as e:
            connection_errors.append(url)
            print(f"SSL verification error checking domain {url}: {str(e)}")
            time.sleep(retry_delay)

        except Exception as e:
            print(f"Error checking domain {url}: {str(e)}")
            time.sleep(retry_delay)

    connection_errors.append(url)


if __name__ == "__main__":
    max_threads = 30
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor, \
            tqdm(total=len(result), desc="Checking Domains") as pbar:
        futures = [executor.submit(check_domain, domain_url) for domain_url in result]
        for future in concurrent.futures.as_completed(futures):
            pbar.update(1)

    end_time = time.time()
    execution_time = end_time - start_time

    minutes = int(execution_time // 60)
    seconds = int(round(execution_time % 60))
    
    # Send the results to Slack
    url = "https://hooks.slack.com/services/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"
    headers = {
        "Authorization": "Bearer",
        "Content-Type": "application/json"
    }

    if missing_main_menu_domains or connection_errors or slow_domains:
        alive_count = len(alive_domains)
        text = f":rocket: *Check Live Domains Script Result* :rocket:\n\n"
        text += f":white_check_mark: *Alive Domains:*\n{alive_count} out of {len(result)} domains are alive\n\n"

        if missing_main_menu_domains:
            errors.append("Domains Missing Main Menu:\n" + "\n".join(missing_main_menu_domains))
            text += ":x: *Domains Missing Main Menu:*\n"
            for domain in missing_main_menu_domains:
                text += f"{domain}\n"

        if connection_errors:
            errors.append("Connection Errors/SSL:\n" + "\n".join(connection_errors))
            text += "\n:x: *Connection Errors/SSL:*\n"
            for domain in connection_errors:
                text += f"{domain}\n"

        if slow_domains:
            text += "\n:x: *Slow Domains (taking more than 30 seconds to load):*\n"
            for domain, response_time in slow_domains:
                text += f"{domain} (Response Time: {response_time:.2f} seconds)\n"

        if errors:
            label = "backend"
            existing_issue_status, existing_issue_url = get_issue_summary_and_status(jira, "Domain Issues Detected")

            if existing_issue_status:
                if existing_issue_status in ("Verified", "Deployed"):
                    print(f"An issue with the same summary exists and is in '{existing_issue_status}' status. Creating a new issue.")
                    jira_issue_key, jira_issue_url = create_jira_issue(errors, label, jira)
                    if jira_issue_key:
                        print(f"Jira issue created with key: {jira_issue_key}")
                        print(f"Link to new issue: {jira_issue_url}")
                        slack_message = f"Jira issue created with key: {jira_issue_key}\nLink to new issue: {jira_issue_url}"
                    else:
                        print("No new Jira issue created due to existing issue with the same Summary.")
                        slack_message = f"No new Jira issue created due to existing issue with the same Summary."
                else:
                    print(f"An issue with the same summary exists and is in '{existing_issue_status}' status. Link to existing issue: {existing_issue_url}")
                    slack_message = f"An issue with the same summary exists and is in '{existing_issue_status}' status. Link to existing issue: {existing_issue_url}"
            else:
                jira_issue_key, jira_issue_url = create_jira_issue(errors, label, jira)
                if jira_issue_key:
                    print(f"Jira issue created with key: {jira_issue_key}")
                    print(f"Link to new issue: {jira_issue_url}")
                    slack_message = f"Jira issue created with key: {jira_issue_key}\nLink to new issue: {jira_issue_url}"
                else:
                    print("No new Jira issue created due to existing issue with the same Summary.")
                    slack_message = f"No new Jira issue created due to existing issue with the same Summary."
        else:
            slack_message = "All domains are functioning correctly."

        text += f"\n\n:information_source: {slack_message}"
        text += f"\n\n:stopwatch: *Execution time: {minutes} minutes {seconds} seconds*"
    else:
        alive_count = len(alive_domains)
        text = f":rocket: *Check Live Domains Script Results* :rocket:\n\n"
        text += f":white_check_mark: *Alive Domains:*\nAll {alive_count} domains are alive\n\n"
        text += f"\n:information_source: {slack_message}"
        text += f":stopwatch: *Execution time: {minutes} minutes {seconds} seconds*"

    payload = {
        "channel": "staging",
        "text": text
    }
    response = requests.post(url, data=json.dumps(payload))
