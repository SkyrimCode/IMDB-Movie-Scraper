import json

with open('imdbData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    if int(i['year'])>=2019:
        print (i['movie_title'])
