import pandas as pd
find_words = pd.read_csv(r"C:\Users\HP\Desktop\TranslateWords Challenge\find_words.txt",header=None)
excel = pd.read_csv(r"C:\Users\HP\Desktop\TranslateWords Challenge\french_dictionary.csv",header=None)
dictionary = {}
for i in find_words[0]:
    dictionary[i] = {}
    index = excel.loc[excel[0]==i].index[0]
    dictionary[i]['value'] = excel.loc[excel[0]==i][1][index]
    dictionary[i]['count'] = 0
j = 0
result_excel = pd.DataFrame()
result_excel["English word"] = excel[0]
result_excel["French word"] = excel[1]

string = open(r'C:\Users\HP\Desktop\TranslateWords Challenge\t8.shakespeare.txt').read()
for i in find_words[0]:
    dictionary[i]['count'] += string.count(i.capitalize())
    dictionary[i]['count'] += string.count(i.upper())
    dictionary[i]['count'] += string.count(i.lower())
    result_excel.at[j,"Frequency"] =  dictionary[i]['count']
    j += 1
    if i.capitalize() in string:
        string = string.replace(i.capitalize(),str(dictionary[i]["value"]).capitalize())
    if i.upper() in string:
        string = string.replace(i.upper(),str(dictionary[i]["value"]).upper())
    if i.lower() in string:
        string = string.replace(i.lower(),str(dictionary[i]["value"].lower()))

result_excel.to_csv("frequency.csv",index = False)
open('t8.shakespeare.translated.txt', 'w').write(string)



