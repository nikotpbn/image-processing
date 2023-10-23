import json

file = open('randomimage.json')
image = json.load(file)
data = image['data']

test = 0
for index, value in enumerate(data):
    if value['count'] > 5:
        print(value)