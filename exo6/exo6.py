import json

f = open('file.json', 'w', encoding='utf-8', newline="")
print(json.dumps('{"key":"test"}'))
f.write( json.dumps('{"key":"test"}'))

with open('toto.json') as f:
    data = json.load(f)

sourceFile = open('python.txt', 'a')
for key, el in enumerate(data) :
    print(data['members'][key]['name'], file = sourceFile)
    print(data['members'][key]['name'])

sourceFile.close()