

with open('content_xml.txt') as file:
    read = file.read()
    print(file)
    with open('content_xml.xml','w',encoding='UTF-8') as xml:
        xml.write(read)