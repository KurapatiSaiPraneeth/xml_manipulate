import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
# print(base_path)

# xml_path = os.path.join(base_path,'content_original.txt')
# print(xml_path)


with open('genre_xml.xml') as genre:
    genre_tree = et.parse(genre)


root = genre_tree.getroot()

print(root.tag[:root.tag.rindex('}')+1])



for i in root:
    print(i.tag,i.attrib)