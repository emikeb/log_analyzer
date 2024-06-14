from xml.etree.ElementTree import Element, tostring

from .base_formatter import BaseFormatter


class XmlFormatter(BaseFormatter):
    def format_output(self, data):
        root = Element("data")
        for key, value in data.items():
            element = Element(key)
            element.text = str(value)
            root.append(element)
        return tostring(root, encoding="utf8").decode("utf8")
