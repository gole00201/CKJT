from logging import root
import xml.etree.ElementTree as ET
#Parse some xml file
xml_load = ET.parse("mpc.sz.xml")
#Get root tree from xml file
root = xml_load.getroot()
#Read some data from xml file
for i in root[0][0]:
    print(i.tag, i.attrib)