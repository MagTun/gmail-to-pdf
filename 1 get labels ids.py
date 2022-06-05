
# source  = https://developers.google.com/gmail/api/quickstart/python?authuser=2

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# set working directory  https://stackoverflow.com/a/1432949/3154274
# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# dname = r"C:\Users\user\Desktop\gmail as pdf"
# os.chdir(dname)


def main():
    # check / create the credential 
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

    service = build('gmail', 'v1', credentials=creds)

    # Get list of all labels
    #  https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/index.html
    # https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/gmail_v1.users.labels.html#list
    # code example: https://developers.google.com/gmail/api/v1/reference/users/labels/list


    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
    for label in labels:
        print(label['name'] + " "+label['id'])


if __name__ == '__main__':
    main()
