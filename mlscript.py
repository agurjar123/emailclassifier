import os
import re
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
id = []
subject = []

emailsdf = pd.read_pickle('emailsdf.pkl')
pd.set_option('display.max.columns', None)

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

ischain = 'To: Kate Symes'
xfromname = ''
xtoname = ''
separator = '''




'''
number = 0
num2 = 0
emailsdf['Reply'] = None
emailsdf['No Reply'] = None
for i in range(emailsdf.shape[0]):
    xfromname = emailsdf['X-From'][i]
    xtoname = emailsdf['X-To'][i]
    if emailsdf['Directory'][
        i] == 'C:/Users/arjun/Desktop/Folders/Internship/emailclassifier-main/enron_mail_20150507/maildir\\symes-k\\sent':
        if ischain in emailsdf['Body'][i]:
            if re.search('[0-9]{2}/[0-9]{2}/[0-9]+\s\n?[0-9]{2}:[0-9]{2}\s(am|pm|AM|PM)', emailsdf['Body'][i]) != None:
                breakchain = re.split('[0-9]{2}/[0-9]{2}/[0-9]+\s\n?[0-9]{2}:[0-9]{2}\s(am|pm|AM|PM)',
                                      emailsdf['Body'][i])
                splitted = re.split('Subject:\sR?e?:?\s[a-zA-Z:\s0-9\-]+\n', breakchain[2])
                emailsdf['Reply'][i] = splitted
                number += 1
                for j in range(len(emailsdf['Reply'][i])):
                    emailsdf['Reply'][i][j].replace('\n', ' ')

            else:
                pass
        else:
            pass
    else:
        if emailsdf['X-To'][i] == 'Kate Symes':
            if re.search('[0-9]{2}/[0-9]{2}/[0-9]+\s\n?[0-9]{2}:[0-9]{2}\s(am|pm|AM|PM)', emailsdf['Body'][i]) == None:
                emailsdf['No Reply'][i] = emailsdf['Body'][i]
                num2 += 1
                print(emailsdf['No Reply'][i])
                if num2 == 918:
                    break
data = pd.DataFrame()
data['Replied'] = emailsdf['Reply']
data['Not Replied'] = emailsdf['No Reply']
data = data.dropna(axis=0, how='all')
print(data.shape)

import nltk
nltk.download('nps_chat')
nltk.download('punkt')
posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features

featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]

# 10% of the total data
size = int(len(featuresets) * 0.1)

# first 10% for test_set to check the accuracy, and rest 90% after the first 10% for training
train_set, test_set = featuresets[size:], featuresets[:size]

# get the classifer from the training set
classifier = nltk.NaiveBayesClassifier.train(train_set)
# to check the accuracy - 0.67
# print(nltk.classify.accuracy(classifier, test_set))

question_types = ["whQuestion","ynQuestion"]
def is_ques_using_nltk(ques):
    question_type = classifier.classify(dialogue_act_features(ques))
    return question_type in question_types
question_pattern = ["do i", "do you", "what", "who", "is it", "why","would you", "how","is there",
                    "are there", "is it so", "is this true" ,"to know", "is that true", "are we", "am i",
                   "question is", "tell me more", "can i", "can we", "tell me", "can you explain",
                   "question","answer", "questions", "answers", "ask"]

helping_verbs = ["is","am","can", "are", "do", "does"]
# check with custom pipeline if still this is a question mark it as a question
def is_question(question):
    question = question.lower().strip()
    if not is_ques_using_nltk(question):
        is_ques = False
        # check if any of pattern exist in sentence
        for pattern in question_pattern:
            is_ques  = pattern in question
            if is_ques:
                break

        # there could be multiple sentences so divide the sentence
        sentence_arr = question.split(".")
        for sentence in sentence_arr:
            if len(sentence.strip()):
                # if question ends with ? or start with any helping verb
                # word_tokenize will strip by default
                first_word = nltk.word_tokenize(sentence)[0]
                if sentence.endswith("?") or first_word in helping_verbs:
                    is_ques = True
                    break
        return is_ques
    else:
        return True

is_question('How is the moon?')
