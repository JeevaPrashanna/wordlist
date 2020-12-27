import pandas as pd
import csv
import os
import json
import requests

app_id = "84b3b205"
app_key = "0817557bb06e9b2cac6c794f72b53f1b"
language = "en-gb"
word_id = "mountain"
strictMatch = 'false'


path_uml = os.getcwd() + '\std 7 term 1 English uwl.csv'
words = []
with open(path_uml) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row[1] != '':
            words.append(row[1])


path_antonyms = os.getcwd() + '\\' + 'antonyms.csv'  # Alternate file -->  'antonyms master.csv'
antonym_dict = {}
with open(path_antonyms) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        antonym_dict.update({row[0]: row[2]})


path_synonyms = os.getcwd() + '\\' + 'synonyms.csv'
synonym_dict = {}
with open(path_synonyms) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        synonym_dict.update({row[0]: row[2]})


"""def synonyms(word_id):
    print(f'word_id = {word_id}')
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower()
    req = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    if str(req) == "<Response [200]>":
        op = req.json()
        synonym = op['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]

    else:
        synonym = '-'

    print('Synonym',synonym)
    return synonym"""

keys_antonyms = list(antonym_dict.keys())


def synonyms_csv(word_id):

    if word_id in synonym_dict:
        synonym = synonym_dict[word]

    else:
        synonym = '-'

    return synonym


def antonyms(word_id):

    global antonym
    if word_id in antonym_dict:
        antonym = antonym_dict[word]
        return antonym

    elif word_id not in antonym_dict:
        for i in keys_antonyms:
            if i.startswith(word_id):
                antonym = antonym_dict[i]

                return antonym

    else:
        antonym = '-'
        return antonym


to_excel_dict = {}

for word in words:
    to_excel_dict.update({word: [antonyms(word), synonyms_csv(word)]})


df = pd.DataFrame.from_dict(to_excel_dict, orient='index', columns=['Antonym', 'Synonym'])

with pd.ExcelWriter('check_file.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1')

writer.save()