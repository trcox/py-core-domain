#*******************************************************************************
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
#*******************************************************************************

from enum import Enum

# TODO - someday, we may need to refactor addressable based on needs of protocol. Other is a
# placeholder today.
# HTTP - for REST communications
# TCP - for MQTT and other general TCP based communications
# MAC - MAC address - low level (example serial) communications
# ZMQ - Zero MQ communications
class Protocol(Enum):
  HTTP = 1
  TCP = 2
  MAC = 3
  ZMQ = 4
  OTHER = 5
