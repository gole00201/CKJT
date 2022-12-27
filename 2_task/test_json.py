import json
#Load json file
with open("mpc.sz.json", 'r') as json_file:
    json_load = json.load(json_file)
#Read some data from json file
for i in  json_load["sz:context"]["sz:bus"]["sz:ins"]["sz:ig"]:
    print(i)


