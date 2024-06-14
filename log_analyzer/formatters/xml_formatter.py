from .base_formatter import BaseFormatter


class XmlFormatter(BaseFormatter):
    def format_output(self, data):
        xml_str = "<data>\n"

        for key, value in data.items():
            xml_str += f"  <{key}>{value}</{key}>\n"

        xml_str += "</data>"

        return xml_str

