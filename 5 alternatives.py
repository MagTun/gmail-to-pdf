# source  = https://developers.google.com/gmail/api/quickstart/python?authuser=2


#*************************************  Improvement needed
# add preview of attachment 



#*************************************
#  ressources for *list* email by labels
# https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/index.html 
# https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/gmail_v1.users.messages.html#list
# example of code for list: https://developers.google.com/gmail/api/v1/reference/users/messages/list?apix_params=%7B%22userId%22%3A%22me%22%2C%22includeSpamTrash%22%3Afalse%2C%22labelIds%22%3A%5B%22LM%22%5D%7D
#*************************************

#*************************************
# ressources for *get* email 
# https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/gmail_v1.users.messages.html#get
# code example for decode https://developers.google.com/gmail/api/v1/reference/users/messages/get 
#  + decode for python 3 https://python-forum.io/Thread-TypeError-initial-value-must-be-str-or-None-not-bytes--12161
#*************************************

#*************************************
# ressources for *thread*  
# https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/gmail_v1.users.threads.html#get
#*************************************


# connect to gmail api 
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# decode response from Gmail api and save a email
import base64
import email

#for working dir and path for saving file 
import os

# for renaming folder
import shutil

# valid filename
import string

# convert date
from datetime import datetime


# CUSTOM VAR 
dname = r"C:\Users\user\Desktop\gmail as pdf"
folder_to_save_all_emails= working_folder_path+r"\label1"
labelid = "Label_45"

# set working directory  https://stackoverflow.com/a/1432949/3154274
# abspath = os.path.abspath(__file__)
# working_folder_path = os.path.dirname(abspath)
os.chdir(working_folder_path)
print("working dir set to ", working_folder_path)

# create folder to save email 
if not os.path.exists(folder_to_save_all_emails):
    os.makedirs(folder_to_save_all_emails)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def valid_path_name(path):
    valid_chars = f"-_.() ' à â ç è é ê î ô ù û  {string.ascii_letters} {string.digits}" 
    return ''.join(c for c in path if c in valid_chars)


def convert_date(date_var, with_time=True):
    # possible format 
    # Thu 27 Oct 2016 153051 0200
    # Wed 1 Feb 2017 110109 0100 (CET)
    # Mon 10 Oct 2016 153833 0200 (CEST)
    # 15 Jun 2017 092429


    date_var=date_var.replace(' (CET)', '')
    date_var=date_var.replace(' (CEST)', '')
    date_var=date_var[:-5]
    try:
        datetime_object = datetime.strptime(date_var, '%a %d %b %Y %H%M%S')  #Thu 27 Oct 2016 153051 0200
        if with_time == True:
            date_var = datetime_object.strftime('%Y_%m_%d %Hh%Mm%S')
        else:
            date_var = datetime_object.strftime('%Y_%m_%d')
        return date_var
    except:
        # datetime_object = datetime.strptime(date_var, '%d %a %b %Y %H%M%S') #15 Jun 2017 092429
        return date_var+" zzz"


def main():

    # create the credential the first time and save it in token.pickle
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    #create the service 
    service = build('gmail', 'v1', credentials=creds)


    # get the *list* of all emails in the labels (if there are multiple pages, navigate to them)
    response= service.users().messages().list(userId="me", labelIds=labelid, q=None, pageToken=None, maxResults=None, includeSpamTrash=None).execute()
    all_message_in_label = []
    if 'messages' in response:
        all_message_in_label.extend(response['messages'])

    # if several page of message (ex more than 100 message, the first request will only return the first 20. so we need to make another request starting at the nextPageToken)
    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId="me", labelIds=labelid, q=None, pageToken=page_token, maxResults=None, includeSpamTrash=None).execute()
      all_message_in_label.extend(response['messages'])


    # all_message_in_label looks like this 
            # for email in all_message_in_label:
                # print(email)
                #{'id': 'xxxxxx', 'threadId': 'xxxxxx'}
                #{'id': 'xxxxxx', 'threadId': 'xxxxxx'}    

    if not all_message_in_label:
        print('No email LM found.')
    else:

        # for each ID in all_message_in_label we *get* the message 
        for emails in all_message_in_label: 



            #  ----------------   folder = same for every email and filename =  date (converted into " 2017_02_04 05-45-32")  + subject   ( )

            # # get the entire email message in an RFC 2822 formatted and base64url encoded string that can be converted to .eml
            # messageraw= service.users().messages().get(userId="me", id=emails["id"], format="raw", metadataHeaders=None).execute()
            # # get the headers of the message 
            # messageheader= service.users().messages().get(userId="me", id=emails["id"], format="full", metadataHeaders=None).execute()

            # # retrieve headers
            # headers=messageheader["payload"]["headers"]

            # #retrieve date  
            # date= [i['value'] for i in headers if i["name"]=="Date"]
            # date_as_valid_filename= valid_path_name(date[0])
            # date_as_filename= convert_date(date_as_valid_filename)
            # # print(date_as_filename)
  
            # #retrieve subject 
            # subject= [i['value'] for i in headers if i["name"]=="Subject"]
            # print(subject)  
            # if subject == []:
            #     subject = ["(no subject)"]
            # subject_as_foldername=valid_path_name(subject[0])
            # # print(subject_as_foldername)

            # try:
            #     #convert the raw format into a string format
            #     msg_str = base64.urlsafe_b64decode(messageraw['raw'].encode('ASCII')) 
            #     mime_msg = email.message_from_string(msg_str.decode())  


            #     # set path+filename of the .eml file and save it

            #     path_to_folder = folder_to_save_all_emails
            #     if not os.path.exists(path_to_folder):
            #         os.makedirs(path_to_folder)
                
            #     emlfile = os.path.join(path_to_folder, f'{date_as_filename} {subject_as_foldername}.eml')

            #     with open(emlfile, 'w') as outfile:
            #         gen = email.generator.Generator(outfile)
            #         gen.flatten(mime_msg)
            #         print(f"mail saved: {emails['id']} {date_as_filename}")

            # except:
            #     print("error in message ", messageraw["snippet"])

            #  ----------------    END





            # ---------------- folder = threadID  filename =  emailID

            # # get the entire email message in an RFC 2822 formatted and base64url encoded string that can be converted to .eml
            # messageraw= service.users().messages().get(userId="me", id=emails["id"], format="raw", metadataHeaders=None).execute()


            # try:
            #     #convert the raw format into a string format
            #     msg_str = base64.urlsafe_b64decode(messageraw['raw'].encode('ASCII')) 
            #     mime_msg = email.message_from_string(msg_str.decode())  

            #     path_to_folder = folder_to_save_all_emails + "\\"+ messageraw["threadId"]
            #     if not os.path.exists(path_to_folder):
            #         os.makedirs(path_to_folder)

            #     emlfile = os.path.join(path_to_folder, f'{emails["id"]}.eml')
            #     with open(emlfile, 'w') as outfile:
            #         gen = email.generator.Generator(outfile)
            #         gen.flatten(mime_msg)
            #         print(f"mail saved: {emails['id']}")

            # except:
            #     print("error in message ", messageraw["snippet"])

            #  ----------------    END




            # ----------------     folder = subject /   filename = date 

            # # get the entire email message in an RFC 2822 formatted and base64url encoded string that can be converted to .eml
            # messageraw= service.users().messages().get(userId="me", id=emails["id"], format="raw", metadataHeaders=None).execute()
            # # get the headers of the message 
            # messageheader= service.users().messages().get(userId="me", id=emails["id"], format="full", metadataHeaders=None).execute()

            # #retrieve header for subject and date 
            # headers=messageheader["payload"]["headers"]

            # #retrieve subject 
            # subject= [i['value'] for i in headers if i["name"]=="Subject"]
            # print(subject)  
            # if subject == []:
            #     subject = ["(no subject)"]
            # subject_as_foldername=valid_path_name(subject[0])
            # print(subject_as_foldername)
            # path_to_folder_by_subject = folder_to_save_all_emails + "\\"+ subject_as_foldername
            # if not os.path.exists(path_to_folder_by_subject):
            #     os.makedirs(path_to_folder_by_subject)

            # # retrieve date     ( !!!!! a verifier because didn't test with the  try !!!!)
            # date= [i['value'] for i in headers if i["name"]=="Date"]
            # date_as_filename= valid_path_name(date[0])
            # print(date_as_filename)
            # try:
            #     #convert the raw format into a string format
            #     msg_str = base64.urlsafe_b64decode(messageraw['raw'].encode('ASCII')) 
            #     mime_msg = email.message_from_string(msg_str.decode())  
            #     # set path+filename of the .eml file and save it
            #     emlfile = os.path.join(path_to_folder_by_subject, f'{date_as_filename}.eml')

            #     with open(emlfile, 'w') as outfile:
            #         gen = email.generator.Generator(outfile)
            #         gen.flatten(mime_msg)
            #         print(f"mail saved: {subject_as_foldername} {date_as_filename}")

            # except:
            #     print("error in message ", messageraw["snippet"])

            # ----------------  

if __name__ == '__main__':
    main()

