from xml.etree import ElementTree as ET


class Parser:

    """
    Parses an XML object from a string.
    """

    def __init__(self, xml):
        self.xml = xml

    def parse(self):
        """
        Parses the XML object.
        """
        return ET.fromstring(self.xml)

    def search_for_element(self, element):
        """
        Searches for an element in the XML object.
        """
        return self.parse().find(element)

    def search_for_tag(self, tag):
        """
        Searches for a tag in the XML object.
        """
        return self.parse().find(tag)

    def jsonify(self):
        """
        Converts the XML object to a JSON object.
        """
        return ET.tostring(self.parse(), encoding="unicode")