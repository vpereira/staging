from xml.etree import cElementTree as ET


class XMLParser(object):
    @staticmethod
    def dump(root):
        root = ET.parse(root).getroot()
        if root:
            return ET.tostring(root)
        else:
            return ''
