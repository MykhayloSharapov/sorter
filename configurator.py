import configparser
import os

def createConfig(path):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set ("Settings", "input_mode", "file_input")
    config.set ("Settings", "sort_algorythm_type", "DSU")

    with open (path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = "configfile"
    createConfig(path)
    
