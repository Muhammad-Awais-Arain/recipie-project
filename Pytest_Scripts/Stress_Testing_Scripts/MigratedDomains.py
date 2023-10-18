import requests
import concurrent.futures


# Function to check the website status and extract the desired text
def check_website(url):
    print(f"Hitting: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            if "All Menus" in response.text:
                return url, "Website is up and 3.0"
            else:
                return url, "Website is up but not on 3.0"
        else:
            return url, f"Website returned status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return url, f"Website is down with error: {e}"
    except Exception as e:
        return url, f"An unexpected error occurred: {e}"

# domains_list.py
DOMAINS = [
    "cementmasons555.com",
    "crirebar.com",
    "fortresssteel-de.com",
    "ibew354.org",
    "insulators127.org",
    "insulators19.com",
    "insulators1.org",
    "ironworkers103.org",
    "ironworkers10.com",
    "ironworkers111.org",
    "ironworkers112.org",
    "ironworkers155.org",
    "ironworkers15.org",
    "ironworkers172.com",
    "ironworkers27.com",
    "ironworkers28.org",
    "ironworkers29.org",
    "ironworkers33.org",
    "ironworkers377.com",
    "ironworkers378.org",
    "ironworkers380.org",
    "ironworkers384.com",
    "ironworkers392.org",
    "ironworkers396.org",
    "ironworkers399.org",
    "ironworkers416.org",
    "ironworkers424.org",
    "ironworkers440.com",
    "ironworkers444.com",
    "ironworkers46.org",
    "ironworkers477.org",
    "ironworkers492.org",
    "ironworkers495.org",
    "ironworkers568.org",
    "ironworkers597.com",
    "ironworkers5.org",
    "ironworkers759.org",
    "ironworkers765.com",
    "ironworkers798.org",
    "ironworkers805.org",
    "ironworkers808.com",
    "ironworkers848.org",
    "ironworkers9.org",
    "ironworkerslocal272.com",
    "ironworkerslocal404.org",
    "ironworkerslocal55.com",
    "ironworkerslocal623.org",
    "ironworkerslocal6.com",
    "ironworkerslocal709.org",
    "ironworkerslocal70.com",
    "ironworkerslocal92.org",
    "ironworkerstxms.org",
    "iuoe147.com",
    "iuoe624.com",
    "iw118.org",
    "iw17.org",
    "iw550.org",
    "iw732.org",
    "iw736.com",
    "iwdistrictcouncil.com",
    "iwl8.org",
    "iwlocal451.org",
    "iwlu89.com",
    "iwnorthcentraldistrict.org",
    "iwntf.org",
    "legacyiron.net",
    "linkedunion.org",
    "local229.org",
    "local549apprentice.org",
    "preconconstruction.com",
    "reinforcedironworkersriggerslocal405.com",
    "roofersunionlocal49.com",
    "seiu87.org",
    "sflaborcouncil.org",
    "superiorsteelkc.com",
    "teamsters348.org",
    "teamsters406.org",
    "teamsterslocal320.org",
    "teamsterslocal507.com",
    "teamsterslocal70.org",
    "waldronandsons.net"
]


# Lists to store results
up_3_0 = []
up_not_3_0 = []
other_errors = []

# Maximum number of concurrent requests
max_workers = 10

# Perform concurrent requests
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    future_to_url = {executor.submit(check_website, f"https://{url}"): url for url in DOMAINS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        result = future.result()
        if "Website is up and 3.0" in result:
            up_3_0.append(url)
        elif "Website is up but not on 3.0" in result:
            up_not_3_0.append(url)
        else:
            other_errors.append(url)

# Print the results and lengths of the lists
print("Websites Up and on 3.0:")
print(up_3_0)
print("Number of websites Up and on 3.0:", len(up_3_0))

print("\nWebsites Up but Not on 3.0:")
print(up_not_3_0)
print("Number of websites Up but Not on 3.0:", len(up_not_3_0))

print("\nOther Errors:")
print(other_errors)
print("Number of websites with Other Errors:", len(other_errors))
