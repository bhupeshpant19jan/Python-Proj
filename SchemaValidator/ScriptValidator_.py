from lxml import etree

input_path = 'C:\\Users\\LT-BPant\\Desktop\\Del\\Schema\\'
schema_file = input_path + 'search.xsd'
xml_file  = input_path + 'input1.xml'

def validate(xmlparser, xmlfilename):
    try:
        with open(xmlfilename, 'r') as f:
            etree.fromstring(f.read(), xmlparser)
        return True
    except Exception, extraInfo:
        print str(extraInfo)
        return False

def createSchemaTree(schema_file_path):
    with open(schema_file_path, 'r') as f:
        schema_root = etree.XML(f.read())

    schema = etree.XMLSchema(schema_root)
    xmlparser = etree.XMLParser(schema=schema)
    return xmlparser

#filenames = ['input1.xml']
def main():
    xmlSchemaTree = createSchemaTree(schema_file)
    if validate(xmlSchemaTree, xml_file):
        print "%s validates" % xml_file
    else:
        print "%s doesn't validate" % xml_file


main()


