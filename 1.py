# Import the BeautifulSoup library
from bs4 import BeautifulSoup

nfile = open("results.txt","a")

# Define a function that extracts all links from an html file and prints them out in a list
def extract_links(filename):
    # Open the html file and read its contents with utf-8 encoding
    print("Reading file")
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # Create a BeautifulSoup object to parse the html
    print("Create a BeautifulSoup object to parse the html")
    soup = BeautifulSoup(html, "html.parser")

    # Find all the <a> tags that have an href attribute
    print("Find all the <a> tags that have an href attribute")
    links = soup.find_all("a", href=True)

    # Create an empty list to store the links
    link_list = []

    # Loop through the links and append their href values to the list
    print("Loop through the links and append their href values to the list")
    for link in links:
        link_list.append(link["href"])
        nfile.write(f'{link["href"]}\n')

    # Print out the list of links
    print(link_list)

# Call the function with the source file name
extract_links("source.html")
nfile.close()