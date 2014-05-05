import jsonschema
import json

class jsonSchemaValidator(object):
    def __init__(self, schema_file):
        self.__schema_file = open(schema_file)
        self.__json_schema_obj = json.load(self.__schema_file)

    def validate(self, json_file):
        json_data_obj = json.load(open(json_file))

        try:
            jsonschema.validate(json_data_obj, self.__json_schema_obj)
            print 'The JSON data follows the schema'
        except jsonschema.exceptions.ValidationError as extraInfo:
            print str(extraInfo.schema_path)
            print extraInfo.validator
            print extraInfo.validator_value


