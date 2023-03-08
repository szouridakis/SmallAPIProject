import bz2


class InputReader:

    def __init__(self):
        # Read from input file
        self.file = bz2.BZ2File("/code/app/managed-object-index.yaml.bz2", "r")
        self.data = self.file.read().decode('UTF-8')
        self.file.close()

        # Split data with new line seperator
        self.data_list = self.data.split('\n')
        self.objects_dict = {}

    # Create nested dictionary {Object:{Attribute:DataType}}

    def readInputFile(self):
        for s in self.data_list:

        # All Objects end with ':'. We split that line and take only the object name as Dictionaries key.
        # We create an empty dictionary as value to that key.
            if ":" in s:
                obj_key = s.split(':')
                attr_dict = {}
                self.objects_dict[obj_key[0]] = attr_dict
        # All Attributes start with '- - '. We split that line and take only the attribute name.
        # We set it as key on the empty dictionary with an empty value waiting for datatype.
            elif "- - " in s:
                attr_key = s.split('- - ')
                attr_dict[attr_key[1]] = None
        # All Datatypes start with '  - '. We split that line and we take only datatype.
        # We set it as value on the previous key
            elif "  - " in s:
                attr_datatype = s.split('  - ')
                attr_dict[attr_key[1]] = attr_datatype[1]

        return self.objects_dict

#if __name__ == '__main__':

#    d = InputReader()
#    data = d.readInputFile()
#    print(data)

