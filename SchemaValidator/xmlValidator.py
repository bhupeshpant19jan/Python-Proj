from lxml import etree

class XMLSchemaValidator(object):
    def __init__(self, schema_file):
        self.__schema_file = schema_file
        self.__createSchemaTree()

    def __createSchemaTree(self):
        with open(self.__schema_file, 'r') as f:
            schema_root = etree.XML(f.read())

        schema = etree.XMLSchema(schema_root)
        self.__xml_parser = etree.XMLParser(schema=schema)

    def validate(self, xml_file):
        try:
            with open(xml_file, 'r') as f:
               etree.fromstring(f.read(), self.__xml_parser)
            return True
        except Exception, extraInfo:
            print str(extraInfo)
            return False

