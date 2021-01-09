# SingleUserPastebin
Download files from a users pastebin. This is run on a constant loop and checks every second. This means if someone uploads a new file it will download the file (Unfortunately it will also download all of the files again if there is more than one on the pastebin account)

# Usage
Use SinglePastebinScan.py -h to see the option.

# Stuff to work on
Right now there is a check in place to make sure that it doesnt download files every second on the host machine. However, there is no check to see if a file has already been downloaded. This causes already downloaded files to be redownloaded if a new file is uploaded to the users pastebin. It would also be cool to implement the ability to do multiple pastebin accounts instead of just one.
