import xml.etree.ElementTree as ET

def ids_by_message(xml, message):
    root = ET.fromstring(xml)
    ids = []

    for entry in root.findall('entry'):
        message_tag = entry.getchildren()[0]
        if message_tag.text == message:
            ids.append(int(entry.attrib['id']))

    return ids

xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
    <entry id="1">
        <message>Application started</message>
    </entry>
    <entry id="2">
        <message>Application ended</message>
    </entry>
</log>"""
print(ids_by_message(xml, 'Application ended'))
