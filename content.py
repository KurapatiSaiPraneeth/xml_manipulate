import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
# print(base_path)

# xml_path = os.path.join(base_path,'content_original.txt')
# print(xml_path)


with open('content_xml.xml') as content:
    content_tree = et.parse(content)


content_root = content_tree.getroot()

with open('genre_xml.xml') as genre:
    genre_tree = et.parse(genre)

genre_root = genre_tree.getroot()


# print(root.tag[:root.tag.rindex('}')+1])

xmlns=content_root.tag[:content_root.tag.rindex('}')+1]

content_publish={}

for elem in content_tree.iter(tag=xmlns+'content'):
    for child in elem:
        if child.tag == xmlns+'contentId':
            content_publish.update({'content_Id': child.text})
        elif child.tag == xmlns+'contentName':
            content_publish.update({'content_name': child.text})
        elif child.tag == xmlns+'contentType':
            content_publish.update({'content_type':child.text})

        elif child.tag == xmlns+'properties':
            for c in child:
                if c.attrib['name'] == 'language':
                    content_publish.update({'language':[i.attrib['value'] for i in c]})
                    # for i in c:
                    #     (c.attrib['name'],i.attrib['value'])
                elif c.attrib['name'] == 'duration':
                    content_publish.update({c.attrib['name']:c.attrib['value']})
                    # print(c.attrib['name'],c.attrib['value'])
                elif c.attrib['name'] == 'Genre':
                    # content_publish.update({'genre': [i.attrib['value'] for i in c]})
                    for i in c:
                        for tag in genre_root:
                            if i.attrib['value'] == tag.attrib.get("id"):
                                content_publish.update({c.attrib['name']: tag.attrib.get("id")})

                        # print(c.attrib['name'],i.attrib['value'])

                elif c.attrib['name'] == 'Person':
                    content_publish.update({'actor':[i.attrib['value'] for i in c if i.attrib['name'] == 'Actor']})
                    # for i in c:
                    #     if i.attrib['name'] == 'Actor':
                    #         print(i.attrib['name'],i.attrib['value'])







# print(root.tag[:root.tag.rindex('}')+1])


# print(content_publish.get("genre"))


print(content_publish)





