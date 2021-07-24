import os
from email.parser import Parser
import pandas as pd
import numpy as np
import json

rootdir = "C:/Users/arjun/Desktop/Folders/Internship/emailclassifier-main/enron_mail_20150507/maildir"

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

emailsdf = pd.read_pickle('emailsdf.pkl')
pd.set_option('display.max.columns', None)

for i in range(5):
    print(emailsdf['Directory'][i])

emailsdf['Thread Bool'] = " "

a = 0
identifier1 = '''



'''
identifier2 = '-----Original Message-----'
identifier3 = 'kate.symes@enron.com'
bool = False
symesid = '''



'''
split = []
repltext = ''
triggersymes = 'cc:'
triggersymes2 = '''
'''
triggersymes3 = 'Subject:'
hi = []
def emailsplit(body, directory, fromdef, todef, poi, table):
    if directory.split('\\')[2] == 'sent':
        print('yes')
        if identifier1 in str(body) or identifier2 in str(body):
            bool = True
            print('yes')
            if identifier3 in fromdef or identifier3 in todef or identifier3 in body:
                split = body.split(symesid)
                print('yes')
                for i in split:
                    if identifier3 in split[i-1]:
                        repltext = split[i]
                        emailsdf['Reply'][i] = repltext.split('Subject:')
                        return hi
emailsdf['Reply'] =''
for i in range(emailsdf.shape[1]):
    emailsdf['Reply'][i] = emailsplit(emailsdf['Body'][i], emailsdf['Directory'][i], emailsdf['From'][i], emailsdf['To'][i], 'kate.symes@enron.com', emailsdf)

for i in range(emailsdf.shape[1]):
    if emailsdf['Directory'][i].split('\\') == 'symes-k':
        print(emailsdf['Reply'][i])

