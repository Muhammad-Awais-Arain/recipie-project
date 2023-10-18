import json

# Step 1: Read JSON data from the file
json_file_path = "website_domains_staging.json"

with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Step 2: Write the Python data to a new Python file
python_file_path = "website_domains_staging.py"

with open(python_file_path, "w") as python_file:
    python_file.write("DOMAINS = [\n")
    for domain in json_data:
        python_file.write(f'    "{domain}",\n')
    python_file.write("]\n")
