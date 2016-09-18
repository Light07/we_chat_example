# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os

class XMLHelper(object):

    def __init__(self):
        self.xml_folder = os.path.dirname(__file__)

    def read_xml(self, xml_file):
        xml_file_path = os.path.join(self.xml_folder, xml_file)
        f = open(xml_file_path, 'r')
        xml_string = ''
        for l in f.readlines()[::-1]:
            xml_string = l.strip() + xml_string
        return xml_string.strip()

if __name__ == "__main__":

    xml_t = XMLHelper()
    print xml_t.read_xml("txt_message.xml")