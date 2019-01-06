from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client,tools,file

# SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
SCOPES = 'https://mail.google.com/'

def main():
    store = file.Storage('credentials.json')
    creds = None
    try:
        creds = store.get()
    except Exception as e:
        print(e)
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json',SCOPES)
        creds = tools.run_flow(flow, store)

    service = build('gmail','v1',http=creds.authorize(Http()))

    #llamada a Gmail api
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels',[])

    if not labels:
        print('sin labels encontrados')
    else:
        print('labels')
        for label in labels:
            print(label['name'])
    
    return service
# if __name__ == '__main__':
#     main()