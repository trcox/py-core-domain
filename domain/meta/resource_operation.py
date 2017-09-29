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


import java.util.Array_list
import java.util.Hash_map
import java.util.List
import java.util.Map

public class Resource_operation {

  private String index
  private String operation
  private String object
  private String property
  private String parameter
  private String resource
  private List<String> secondary = new Array_list<>()
  private Map<String, String> mappings = new Hash_map<>()

  public Resource_operation():}

  public Resource_operation(String operation, String object):
    self.operation = operation
    self.object = object
    self.property = "value"
    self.parameter = object
    self.index = "1"

  public String get_operation():
    return operation

  def set_operation(String operation):
    self.operation = operation

  public String get_object():
    return object

  def set_object(String object):
    self.object = object

  public String get_property():
    return property

  def set_property(String property):
    self.property = property

  public String get_parameter():
    return parameter

  def set_parameter(String parameter):
    self.parameter = parameter

  public String get_index():
    return index

  def set_index(String index):
    self.index = index

  @Override
  public String to_string():
    return "Resource_operation [operation=" + operation + ", object=" + object + ", property="
        + property + ", parameter=" + parameter + ", mappings=" + mappings + ", index=" + index
        + "]"

  public List<String> get_secondary():
    return secondary

  def set_secondary(List<String> secondary):
    self.secondary = secondary

  public Map<String, String> get_mappings():
    return mappings

  def set_mappings(Map<String, String> mappings):
    self.mappings = mappings

  public String get_resource():
    return resource

  def set_resource(String resource):
    self.resource = resource

}
