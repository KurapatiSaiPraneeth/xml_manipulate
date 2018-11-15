import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
# print(base_path)

# xml_path = os.path.join(base_path,'content_original.txt')
# print(xml_path)


with open('content_xml.xml') as content,open('genre_xml.xml') as genre,open('person_xml.xml') as person:
    content_tree = et.parse(content)
    genre_tree = et.parse(genre)
    person_tree = et.parse(person)

content_root = content_tree.getroot()
genre_root = genre_tree.getroot()
person_root = person_tree.getroot()


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
                    content_publish.update({'genre':[tag.attrib.get("value") for tag in genre_root for i in c if i.attrib['value'] == tag.attrib.get("id")]})
                        # for tag in genre_root:
                        #
                        #     if i.attrib['value'] == tag.attrib.get("id"):
                        #
                        #         content_publish.update({c.attrib['name']: tag.attrib.get("id")})

                        # print(c.attrib['name'],i.attrib['value'])

                elif c.attrib['name'] == 'Person':
                    print()

                    # content_publish.update({'actor': [tag.attrib for tag in person_root for i in c if i.attrib['value'] == tag.attrib.get("id")]})

                    actor ={'actor':[]}
                    for i in c:
                        if i.attrib['name'] == 'Actor':
                            # print(i.attrib['name'],i.attrib['value'])
                            for tag in person_root:
                                if i.attrib['value'] == tag.attrib.get("id"):
                                    for t in tag:
                                        # print(t.attrib.get('value'))
                                        actor['actor'].append(t.attrib.get('value'))

                    content_publish.update(actor)



print(content_publish)