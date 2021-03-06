import os 
import json

import argparse
from re import L

from flask import jsonify

parser = argparse.ArgumentParser()
# parser.add_argument("--dzikir_type", dest="dzikir_type", type=str, help="Please Add Al Matsurat Type")
# parser.add_argument("--lang", dest="lang", type=str, help="Please Add Al Matsurat Type")

args = parser.parse_args()

# dzikir_type = args.dzikir_type
# lang = args.lang

# if dzikir_type == None:
#     dzikir_type = "sugro"

__dir__ = os.path.dirname(__file__)


def generateGroup(lang, dzikir_type):
    dzikir_type_locale_file = open(f"{__dir__}/{lang}/{dzikir_type}.json")
    dzikirDataLocale_file = json.loads(dzikir_type_locale_file.read())

    count = 0
    # print(dzikirDataLocale_file)

    groups = []

    for ayat in dzikirDataLocale_file:
        group = {}
        group["title"] = ayat['title']
        group['contents'] = {}

        for content in ayat['contents']:
            group['contents'][str(count)] = content['ayat']
            count+=1
        
        groups.append(group)

    # print(groups)

    with open(f"{__dir__}/{lang}/{dzikir_type}_groups.json", "w") as groupFile:
        groupFile.write(json.dumps(groups))


langs = [f for f in os.listdir(__dir__) if not f.endswith('.py') ]

for lang in langs:
    if lang in ["data", "license", ".DS_Store", ".git"]:
    
        langs.remove(lang)
    elif lang.endswith('.md'):
        langs.remove(lang)

langs = langs[1:len(langs)-1]


for lang in langs:
    generateGroup(lang, "sugro")
    generateGroup(lang, "kubro")

