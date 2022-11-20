import xmltodict, json
with open('mpc.sz.xml') as xmlfile:
    jsonparse = xmltodict.parse(xmlfile.read())
jsonparse = json.dumps(jsonparse, ensure_ascii=False, indent=4)
filejson = open("mpc.sz.json", 'w')
filejson.write(jsonparse)