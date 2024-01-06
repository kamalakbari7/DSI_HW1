import yaml
import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


# A function to read 'yaml' file containing token
def load_config(file_path):
    """ This function reads the api token saved in yaml file.

    This function checks whether the file exists and the token code is saved in the YAML file. 
    
    Parameters
    ----------
        file_path (str): [description]

    Returns
    -------
    INFO, WARNING, ERROR messages
    GitHub User information such as "login", "id", "email", etc.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {file_path}, {e}")
        return None

# Load the token from the YAML file
config = load_config('api.yml')
if config is None or 'github' not in config or 'token' not in config['github']:
    logger.error("Invalid configuration or missing token.")
else:
    token = config['github']['token']
    logger.info("GitHub token loaded successfully.")

    # Initialize request parameters
    url = 'https://api.github.com/user'
    headers = {'Authorization': 'Bearer ' + token}

    try:
        # Send request to GitHub
        r = requests.get(url, headers=headers)

        # Check if the request was successful
        if r.status_code != 200:
            logger.warning(f"Request returned a non-200 status code: {r.status_code}")
        else:
            logger.info("Request to GitHub API successful.")

        # Print responses
        print('Status Code is:', r.status_code)
        r_json = json.loads(r.text)
        print(json.dumps(r_json, indent=4))

    except requests.exceptions.RequestException as e:
        logger.error(f"Error during request to GitHub: {e}")

