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


import java.util.Hash_set
import java.util.Set

import org.apache.commons.lang3.builder.Hash_code_builder
import org.edgexfoundry.domain.common.BaseObject
import org.springframework.data.mongodb.core.mapping.Document

@Document
@Suppress_warnings("serial")
public class Command extends BaseObject {

  # command name which should be unique on a profile but not necessarily
  # unique for all -profiles
  private String name

  # get command details
  private Get get

  # put command details
  private Put put

  public String get_name():
    return name

  def set_name(String name):
    self.name = name

  public Get get_get():
    return get

  def set_get(Get get):
    self.get = get

  public Put get_put():
    return put

  def set_put(Put put):
    self.put = put

  @Override
  public String to_string():
    return "Command [name=" + name + ", get=" + get + ", put=" + put + ", " + super.to_string()
        + "]"

  public Set<String> associated_value_descriptors():
    Set<String> assoc_vD = new Hash_set<>()
    if (self.get_get() != None)
      assoc_vD.add_all(self.get_get().all_associated_value_descriptors())
    if (self.get_put() != None)
      assoc_vD.add_all(self.get_put().all_associated_value_descriptors())
    return assoc_vD

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(name).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Command other = (Command) obj
    return property_match(other)

  private boolean property_match(Command other):
    if (!string_property_match(self.name, other.name))
      return false
    if (!object_property_match(get, other.get))
      return false
    if (!object_property_match(put, other.put))
      return false
    return true

}
