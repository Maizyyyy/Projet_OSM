import requests


def get_latest_info(owner, repo):
    """
    Fetches information about the latest release of a GitHub repository.

    Args:
        owner (str): The owner of the GitHub repository.
        repo (str): The name of the GitHub repository.

    Returns:
        dict or None: A dictionary containing information about the latest release
                      if successful, otherwise None.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    headers = {'Accept': 'application/vnd.github+json'}

    try:
        response = requests.get(url, headers=headers)
         # Raise an exception for HTTP errors
        response.raise_for_status()  
        info = response.json()
        return info
    except requests.exceptions.RequestException as e:
        print(f'Error fetching release information from GitHub: {e}')
        return None
