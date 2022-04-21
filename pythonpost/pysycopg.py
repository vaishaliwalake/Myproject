import psycopg2
from configparser import ConfigParser
global connection
def get_connection_by_config( config_file_path, section_name):
        if(len(config_file_path) > 0 and len(section_name) > 0):
            # Create an instance of ConfigParser class.
            config_parser = ConfigParser()
            config_parser.read(config_file_path)
            # if the configuration file contains the provided section name.
            if(config_parser.has_section(section_name)):
                # read the options of the section. the config_params is a list object.
                config_params = config_parser.items(section_name)
                db_conn_dict = {}
                # loop in the list.
                for config_param in config_params:
                    # get options key and value.
                    key = config_param[0]
                    value = config_param[1]
                    # add the key value pair in the dictionary object.
                    db_conn_dict[key] = value
                # get connection object use above dictionary object.
                connection = psycopg2.connect(**db_conn_dict)

                return connection
            print("******* get postgresql database connection with configuration file ********", "\n")

