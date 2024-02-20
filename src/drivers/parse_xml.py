from typing import Dict
import xmltodict

def parse_xml(xml_doc) -> Dict:
    return xmltodict.parse(xml_doc)