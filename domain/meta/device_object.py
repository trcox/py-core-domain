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


import java.io.Serializable

@Suppress_warnings("serial")
public class Device_object implements Serializable{

  private String name
  private String tag
  private String description
  private Profile_property properties

  private Object attributes

  public String get_name():
    return name

  def set_name(String name):
    self.name = name

  public String get_tag():
    return tag

  def set_tag(String tag):
    self.tag = tag

  public String get_description():
    return description

  def set_description(String description):
    self.description = description

  public Profile_property get_properties():
    return properties

  def set_properties(Profile_property properties):
    self.properties = properties

  public Object get_attributes():
    return attributes

  def set_attributes(Object attributes):
    self.attributes = attributes

  @Override
  public String to_string():
    return "Device_object [name=" + name + ", tag=" + tag + ", description=" + description
        + ", properties=" + properties + ", attributes=" + attributes + "]"
}
