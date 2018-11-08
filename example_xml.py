import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
# print(base_path)

xml_path = os.path.join(base_path,'movies.xml')
# print(xml_path)

tree = et.parse(xml_path)
# print(tree)

root = tree.getroot()
print(root)

for child in root:
    # print(child.tag, child.attrib)
    for element in child:
        print(element.tag,':',element.text)


 # create new subelement

new_movie = et.SubElement(root,'movie',attrib={'title':'robo 2.0'})
new_movie_type = et.SubElement(new_movie,'type')
new_movie_format = et.SubElement(new_movie,'format')
new_movie_episodes = et.SubElement(new_movie,'episodes')
new_movie_rating = et.SubElement(new_movie,'rating')
new_movie_stars = et.SubElement(new_movie,'stars')
new_movie_description = et.SubElement(new_movie,'description')

new_movie_type.text = 'scientific'
new_movie_format.text = 'DVD'
new_movie_episodes.text = '20'
new_movie_rating.text = '4.4'
new_movie_stars.text = '3'
new_movie_description.text = 'super hit'

tree.write(xml_path)

for child in root:
    print(child.tag, child.attrib)
    for element in child:
        print(element.tag,':',element.text)