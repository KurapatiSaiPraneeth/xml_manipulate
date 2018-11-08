import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))

xml_path =  os.path.join(base_path,'content_xml.xml')

print(xml_path)



tree = et.parse(xml_path )
print(tree)