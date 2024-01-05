
# Importing required Python packages
import yaml
import requests
import json

# list of system and user configs to load
CONFIG_PATHS = ['system_config.yml', 'user_config.yml']


# A function to read 'ymal' file containing token
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Load the token from the YAML file
config = load_config('api.yml')
token = config['github']['token']

# Initialize request parameters
url = 'https://api.github.com/user'
headers = {'Authorization': 'Bearer ' + token}

# Send request to GitHub
r = requests.get(url, headers=headers)

# Print responses
print('Status Code is:', r.status_code)

r_json = json.loads(r.text)
print(json.dumps(r_json, indent=4))