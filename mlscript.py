import os
from email.parser import Parser
import pandas as pd
import numpy as np
import json

rootdir = "C:/Users/arjun/Desktop/Code/EmailClassifier/enron_mail_20150507/maildir"

def analyze(inputfile, tolist, fromlist, body, id, subject):
    with open(inputfile, "r") as f:
        data = f.read()
    email = Parser().parsestr(data)
    if email['to']:
        email_to = email['to']
        email_to = email_to.replace("\n", " ")
        email_to = email_to.replace("\t", " ")
        email_to = email_to.replace(" ", " ")

    tolist.append(email['to'])
    fromlist.append(email['from'])
    body.append(email.get_payload())
    id.append(email['message-id'])
    subject.append(email['subject'])

directorylist = []
tolist = []
fromlist = []
body = []
id= []
subject = []
for directory, subdirectory, filenames in os.walk(rootdir):
    for filename in filenames:
        analyze(os.path.join(directory, filename), tolist, fromlist, body, id, subject)
        directorylist.append(directory)

emailsdf = pd.DataFrame()
emailsdf['ID'] = id
emailsdf['To'] = tolist
emailsdf['From'] = fromlist
emailsdf['Body'] = body
emailsdf['Subject'] = subject
emailsdf['Directory'] = directorylist
pd.set_option('display.max.columns', None)
emailsdf.to_pickle('emailsdf.pkl')


emailsdf['Thread Bool'] = " "

a = 0
identifier1 = '''



'''
identifier2 = '-----Original Message-----'
for i in range(emailsdf.shape[0]):
    if emailsdf['Directory'][i].split('\\')[1] == 'sent':
         if identifier1 in str(emailsdf['Body'][i]) or identifier2 in str(emailsdf['Body'][i]):
            a+= 1
            emailsdf['Thread Bool'][i] = 'Replied'

for i in range(emailsdf.shape[0]):
    print(emailsdf['Thread Bool'][i])
print(a)