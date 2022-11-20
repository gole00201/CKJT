from logging import root
import xml.etree.ElementTree as ET

xml_load = ET.parse("mpc.sz.xml")

root = xml_load.getroot()

for i in root[0][0]:
    print(i.tag, i.attrib)