import tempfile

import requests
from smolagents import tool


@tool
def download_file_to_temp(url: str) -> str:
    """
    This function downloads a file from the given URL to a temporary file and returns its path.

    Args:
        url: The URL of the file to download.

    Returns:
        A string containing the path to the downloaded file.
    """
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_path = temp_file.name

    # Download the file
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        with open(temp_file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except requests.exceptions.RequestException as e:
        raise e

    return temp_file_path
