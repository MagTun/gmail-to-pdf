# Download all Gmail emails from a label and save them as `PDF`
This script will connect to your Gmail account and download as .eml files all your email from a specified label.   
Then you can convert the .eml files to pdf with this open source program:  https://github.com/nickrussler/eml-to-pdf-converter


## Setting up the credentials
Go to this link https://developers.google.com/gmail/api/quickstart/python and click on "Enable Gmail API", then click on "Download client configuration" and save this .json file in the same folder as these scripts.  
Then run the script `1 get labels ids.py`. You will be sent to a consent screen: choose your Gmail account where you want to download your email and accept the credential (this will save a token file so that the next time, you don't have to go through this consent screen). 


## How to use
Because GMAIL API doesn't use Label name but ID you need to know to first get all the labels' IDs with the script `1 get labels ids.py`  
Then copy the ID for the label you need `2 download email as eml files.py`  
Run `2 download email as eml files.py`: your emails will be save as `.eml` file in a subfolder "emails as eml"  
Open the program eml-to-pdf-converter and load your folder to convert the `.eml` files to `.pdf` files.  
If you want to only keep the last conversation of each thread, run `4 delete all emails.py`  

## Alternatives 
For different ways of downloading the emails: cf `5 alternatives.py` 