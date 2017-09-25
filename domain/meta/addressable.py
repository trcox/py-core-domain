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


import org.apache.commons.lang3.builder.Hash_code_builder
import org.codehaus.jackson.annotate.Json_ignore
import org.edgexfoundry.domain.common.BaseObject
import org.edgexfoundry.domain.common.HTTPMethod
import org.springframework.data.mongodb.core.index.Indexed
import org.springframework.data.mongodb.core.mapping.Document

@Document
@Suppress_warnings("serial")
public class Addressable extends BaseObject {

  # non-database identifier for a addressable - must be unique
  @Indexed(unique = true)

  # unique name and identifier of the addressable
  private String name

  # HTTP method used with the addressable (default is POST)
  private HTTPMethod method

  # protocol used using the addressable
  private Protocol protocol

  # address (in either tcp or http format) of the addressable
  private String address

  # port on the address for the addressable
  private int port

  # for callbacks
  private String path

  # for MQTT or other message bus addressables
  private String publisher

  # user id for authentication to addressable
  private String user

  # password for the user for authentication to addressable
  private String password

  # topic for MQTT message bus addressables or routing token for REST calls
  private String topic

  public Addressable(String name, Protocol protocol, String address, String path, int port):
    super()
    self.name = name
    self.protocol = protocol
    self.address = address
    self.path = path
    self.port = port
    self.method = HTTPMethod.POST

  public Addressable(String name, Protocol protocol, String address, int port, String publisher,
      String user, String password, String topic):
    super()
    self.name = name
    self.protocol = protocol
    self.address = address
    self.port = port
    self.publisher = publisher
    self.user = user
    self.password = password
    self.topic = topic
    self.method = HTTPMethod.POST

  @Suppress_warnings("unused")
  # used by spring container
  private Addressable():}

  public String get_name():
    return name

  def set_name(String name):
    self.name = name

  public Protocol get_protocol():
    return protocol

  def set_protocol(Protocol protocol):
    self.protocol = protocol

  public String get_address():
    return address

  def set_address(String address):
    self.address = address

  public String get_path():
    return path

  def set_path(String path):
    self.path = path

  public int get_port():
    return port

  def set_port(int port):
    self.port = port

  public String get_publisher():
    return publisher

  def set_publisher(String publisher):
    self.publisher = publisher

  public String get_user():
    return user

  def set_user(String user):
    self.user = user

  public String get_password():
    return password

  def set_password(String password):
    self.password = password

  public String get_topic():
    return topic

  def set_topic(String topic):
    self.topic = topic

  public HTTPMethod get_method():
    return method

  def set_method(HTTPMethod method):
    self.method = method

  @Json_ignore
  public String get_base_uRL():
    String_builder builder = new String_builder(protocol.to_string())
    builder.append(":#")
    builder.append(address)
    builder.append(":")
    builder.append(port)
    return builder.to_string()

  # TODO - is this method used anywhere? If so, it does not appear to be setup correctly and makes
  # no sense. Remove if found to not be used
  #*
  #* @deprecated removed if not used and if it is used, make sure it returns the right information
  #*
  @Json_ignore
  @Deprecated
  public String get_uRL():
    String_builder builder = new String_builder(get_base_uRL())
    if (publisher is None && topic != None):
      builder.append(topic)
      builder.append("")
    builder.append(path)
    return builder.to_string()

  @Override
  public String to_string():
    return "Addressable [name=" + name + ", protocol=" + protocol + ", address=" + address
        + ", port=" + port + ", path=" + path + ", publisher=" + publisher + ", user=" + user
        + ", password=" + password + ", topic=" + topic + ", to_string()=" + super.to_string() + "]"

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(name).append(protocol)
        .append(address).append(port).append(path).append(publisher).append(user).append(password)
        .append(topic).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Addressable other = (Addressable) obj
    return property_match(other)

  private boolean property_match(Addressable other):
    if (!string_property_match(self.name, other.name))
      return false
    if (protocol != other.protocol)
      return false
    if (!string_property_match(self.address, other.address))
      return false
    if (self.port != other.port)
      return false
    if (!string_property_match(self.publisher, other.publisher))
      return false
    if (!string_property_match(self.user, other.user))
      return false
    if (!string_property_match(self.password, other.password))
      return false
    return string_property_match(self.topic, other.topic)

}
