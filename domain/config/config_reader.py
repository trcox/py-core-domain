# *******************************************************************************
# Copyright 2017 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
#
# @microservice: py-core-domain library
# @author: Tyler Cox, Dell
# @version: 1.0.0
# *******************************************************************************

"""Configuration File module.

Manages configuration for EdgeX Foundry Python Services.
Contains a method for loading property files into the global configuration store and
a method for retrieving configuration parameters with an optional default value.

Todo:
    Add methods for updating configuration dynamically.
    Add methods for reading from other types of configuration files.

"""


import logging
import yaml

_CONFIG = {}

def read_property(name, default=None):
    """Reads property from all loaded config files.

    Looks for the named property in the global config.
    A default value may also be passed to be returned if it is not defined.

    Args:
        name: The property name to be read from the configuration files
        default: The return value if the name is not found [default: None]

    Returns:
        The value from the config files if it is found, otherwise the default if it is set.
    """
    value = None
    if name in _CONFIG:
        value = _CONFIG[name]
        logging.info("Property %s was not found in configuration files, using default value: %s.",
                     name, default)
    return value if value is not None else default

def add_yaml_config_file(config_file="resources/application.properties", environment=""):
    """Reads the specified YAML config and updates the global configuration.

    Loads the target YAML file specified and updates the existing global configuration.
    An environment argument may be set to read from a specified environment directory
    such as a test or Docker environment.

    Args:
        config_file: The relative or absolute path to the file to be loaded
            [default: resources/application.properties]
        environment: The environment path to prepend to the config file (i.e. test, Docker)
            [default: ""]

    """
    config_file_name = environment + config_file
    try:
        with open(config_file_name, 'r') as ymlfile:
            _CONFIG.update(yaml.load(ymlfile))
    except FileNotFoundError:
        logging.error("Configuration file %s was not found, skipping it.", config_file_name)
