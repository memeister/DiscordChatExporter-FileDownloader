import requests
import validators
import random
import string
import os

#if(not os.isdir("downloads")):
#    os.mkdir("downloads")

def sanitize_filename(filename):
    # Remove all non-alphanumeric characters from the filename using isalnum() and join()
    sanitized_filename = "".join(c for c in filename if c.isalnum() or c in ["_", "-", "."])

    # Limit the filename length to 255 characters (maximum length for Windows filenames)
    sanitized_filename = sanitized_filename[:255]

    return sanitized_filename

def download_file(url, folder):
    # Get the file name from the url by splitting it by "/" and taking the last element
    file_name = url.split("/")[-1]

    # Get the file extension from the file name by splitting it by "." and taking the last element
    file_extension = file_name.split(".")[-1] if "." in file_name else "none"

    # Sanitize the file name
    file_name = sanitize_filename(file_name)

    # Generate a random 10-digit string for the file name
    random_string = "".join(random.choices(string.digits, k=10))

    # Create the full path for the file by joining the folder, the random string, and the file extension
    file_path = os.path.join(folder, f"{random_string}.{file_extension}")

    try:
        # Send a GET request to the url and get the response
        response = requests.get(url)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Open the file in binary mode and write the response content to it
            with open(file_path, "wb") as f:
                f.write(response.content)
            # Print a success message
            print(f"Downloaded {file_name} from {url} and saved to {file_path}")
        else:
            # Print an error message
            print(f"Failed to download {file_name} from {url}: {response.status_code}")
    except OSError as e:
        print(f"Failed to download {file_name} from {url}: {str(e)}")

# Define the name of the list file and the folder to save the files
list_file = "results.txt"
folder = "downloads"

# Open the list file and read its lines
with open(list_file, "r") as f:
    lines = f.readlines()

# Loop through each line in the list file
for line in lines:
    # Strip the newline character from the line and assign it to url
    url = line.strip()

    # Check if the URL is valid and starts with http or https
    if validators.url(url) and url.startswith(("http://", "https://")):
        # Call the download_file function with the url and the folder
        download_file(url, folder)
    else:
        print(f'Invalid URL: {url}')
