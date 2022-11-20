import xmltodict, json
with open('mpc.sz.xml') as xmlfile:
    jsonparse = xmltodict.parse(xmlfile.read())
jsonparse = json.dumps(jsonparse, ensure_ascii=False, indent=4)
filejson = open("mpc.sz.json", 'w')
filejson.write(jsonparse)

with open('mpc.sz.json', 'r') as json_file:
    json_load = json.load(json_file)

print(json_load['sz:context']['sz:bus']['sz:ins']['sz:ig'][0]['@n'])