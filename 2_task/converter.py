import xmltodict, json
#Open XML file and parse it in fp json
with open('mpc.sz.xml') as xmlfile:
    jsonparse = xmltodict.parse(xmlfile.read())
#Format json file
jsonparse = json.dumps(jsonparse, ensure_ascii=False, indent=4)
filejson = open("mpc.sz.json", 'w')
#Write in file and save new converted xml file
filejson.write(jsonparse)