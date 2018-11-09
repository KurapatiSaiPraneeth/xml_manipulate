import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
# print(base_path)

xml_path = os.path.join(base_path,'content_xml.xml')
# print(xml_path)


tree = et.parse(xml_path)

root = tree.getroot()

print(root.tag[:root.tag.rindex('}')+1])




content_publish={}
for elem in tree.iter(tag='{http://content.cms.myplex.tv/1}content'):
    for child in elem:
        if child.tag == '{http://content.cms.myplex.tv/1}contentId':
            content_publish.update({'content_Id': child.text})
        elif child.tag == '{http://content.cms.myplex.tv/1}contentName':
            content_publish.update({'content_name': child.text})
        elif child.tag == '{http://content.cms.myplex.tv/1}contentType':
            content_publish.update({'content_type':child.text})

        elif child.tag == '{http://content.cms.myplex.tv/1}properties':
            for c in child:
                if c.attrib['name'] == 'language':


                    content_publish.update({'language':[i.attrib['value'] for i in c]})
                    # for i in c:
                    #     (c.attrib['name'],i.attrib['value'])
                elif c.attrib['name'] == 'duration':
                    content_publish.update({c.attrib['name']:c.attrib['value']})
                    # print(c.attrib['name'],c.attrib['value'])
                elif c.attrib['name'] == 'Genre':
                    content_publish.update({'genre': [i.attrib['value'] for i in c]})
                    # for i in c:
                    #     print(c.attrib['name'],i.attrib['value'])

                elif c.attrib['name'] == 'Person':
                    content_publish.update({'actor':[i.attrib['value'] for i in c if i.attrib['name'] == 'Actor']})
                    # for i in c:
                    #     if i.attrib['name'] == 'Actor':
                    #         print(i.attrib['name'],i.attrib['value'])


# print(content_publish)





