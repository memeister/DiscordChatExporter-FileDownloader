# DiscordChatExporter-AttachmentDownloader
This script developed in Python3 on a Windows-type operating system downloads all files/images/videos/audios/webpages linked in the result file created by the DiscordChatExporter program which is provided and maintained by Tyrrrz (link below).
https://github.com/Tyrrrz/DiscordChatExporter

The AttachmentDownloader script is still under development but works fine. I thought that I might as well upload it since I was making it for saving the chat history with a beloved friend that I now miss, and automatically downloading the eventual files with it.

Tested on a chat export HTML-file containing 45,500 messages sizing up to 30MB. It takes some minutes for it to process the file and then download all the linked web files so let it work. UwU

## How to use

Run the script files in a python 3.x interpreter. Ensure you have renamed and moved the export html to working directory as 'source.html' before running. Execute each script individually one at a time in a number ordered fashion 1 to 2.

1. ```python 1.py```
2. ```python 2.py```

If run successfully without errors, it produces a 'results.txt' file which is for temporary use by script, and a directory named 'downloads' containing downloaded image/video/gif files from export. That directory is your end product.
