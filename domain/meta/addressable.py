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

from domain.common import BaseObject, HTTPMethod
from .protocol import Protocol

class Addressable (BaseObject):

  def __init__(self, name, protocol, address, port, publisher=None,
      user=None, password=None, topic=None, path=None, method=HTTPMethod.POST, 
      created=None, modified=None, origin=None):
    super(Addressable, self).__init__(created, modified, origin)
    self.name = name
    self.protocol = protocol
    self.address = address
    self.port = port
    self.publisher = publisher
    self.user = user
    self.password = password
    self.topic = topic
    self.path = path
    self.method = method

  # unique name and identifier of the addressable
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name

  # HTTP method used with the addressable (default is POST)
  @property
  def method(self):
    return self.__method

  @method.setter
  def method(self, method):
    if not isinstance(method, HTTPMethod):
      raise TypeError("Addressable method must be of type HTTPMethod")
    self.__method = method

  # protocol used using the addressable
  @property
  def protocol(self):
    return self.__protocol

  @protocol.setter
  def protocol(self, protocol):
    if not isinstance(protocol, Protocol):
      raise TypeError("Addressable protocol must be of type Protocol")
    self.__protocol = protocol

  # address (in either tcp or http format) of the addressable
  @property
  def address(self):
    return self.__address

  @address.setter
  def address(self, address):
    self.__address = address

  # port on the address for the addressable
  @property
  def port(self):
    return self.__port

  @port.setter
  def port(self, port):
    self.__port = port

  # for callbacks
  @property
  def path(self):
    return self.__path

  @path.setter
  def path(self, path):
    self.__path = path

  # for MQTT or other message bus addressables
  @property
  def publisher(self):
    return self.__publisher

  @publisher.setter
  def publisher(self, publisher):
    self.__publisher = publisher

  # user id for authentication to addressable
  @property
  def user(self):
    return self.__user

  @user.setter
  def user(self, user):
    self.__user = user

  # password for the user for authentication to addressable
  @property
  def password(self):
    return self.__password

  @password.setter
  def password(self, password):
    self.__password = password

  # topic for MQTT message bus addressables or routing token for REST calls
  @property
  def topic(self):
    return self.__topic

  @topic.setter
  def topic(self, topic):
    self.__topic = topic

  def get_base_url(self):
    return "%s://%s:%s" % (self.protocol.name, self.address, self.port)
    
  # TODO - is this method used anywhere? If so, it does not appear to be setup correctly and makes
  # no sense. Remove if found to not be used
  # @deprecated removed if not used and if it is used, make sure it returns the right information
  def get_url(self):
    builder = self.get_base_url()
    if (self.publisher is None and self.topic is not None):
      builder += "%s/" % (self.topic)
    builder += self.path
    return builder

  def __str__(self):
    return "Addressable [name=%s, protocol=%s, address=%s, port=%s, path=%s, publisher=%s, user=%s, password=%s, topic=%s, to_string()=%s]" \
      % (self.name, self.protocol.name, self.address, self.port, self.path, self.publisher, self.user, self.password, self.topic, super(Addressable, self).__str__())
