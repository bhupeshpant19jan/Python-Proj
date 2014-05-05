import argparse
import xmlValidator
import jsonValidator

def validateJsonSchema(schema, jsonData):
    try:
        validate(jsonData, schema)
    except Exception, extraInfo:
        print str(extraInfo)

def parseInputs():
    '''This will have parse all the mandatoryn params.'''
    argument_parser = argparse.ArgumentParser(description='Schema Validator')
    argument_parser.add_argument('type'  , help='Specify the type of schema'\
              ' you wanted to validate.', type=str)
    argument_parser.add_argument('schema', help='Schema file name/path', type=str)
    argument_parser.add_argument('output', help='output file name/path', type=str)

    sys = __import__('sys')

    return argument_parser.parse_args(sys.argv[1:])


data_file_path = 'C:\\Users\\LT-BPant\\Desktop\\Del\\Schema\\new schema\\sample_output\\'
schema_path = 'C:\\Users\\LT-BPant\\Desktop\\Del\\Schema\\new schema\\'
def main():
    args = parseInputs()

    type_ = args.type
    schema = schema_path + args.schema
    data_file = data_file_path + args.output

    if type_  == 'xml':
        validation_obj = xmlValidator.XMLSchemaValidator(schema)
    elif type_  == 'json':
        validation_obj = jsonValidator.jsonSchemaValidator(schema)
    validation_obj.validate(data_file)


main()