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


import java.util.Hash_map
import java.util.Map

import org.apache.commons.lang3.builder.Hash_code_builder
from domain.common import BaseObject
import org.springframework.data.mongodb.core.index.Indexed
import org.springframework.data.mongodb.core.mapping.DBRef
import org.springframework.data.mongodb.core.mapping.Document

@Document
@Suppress_warnings("serial")
public class Provision_watcher extends BaseObject {

  # non-database identifier for a provision watcher - must be unique
  @Indexed(unique = true)

  # unique name and identifier of the addressable
  private String name

  #*
  #*  set of key value pairs that identify type of of address (MAC, HTTP,...) and address to watch
  #* for (00-05-1_b-A1-99-99, 10.0.0.1,...)
  #*
  private Map<String, String> identifiers

  @DBRef
  # device profile that should be applied to the devices available at the
  # identifier addresses
  private Device_profile profile

  @DBRef
  # device service that owns the watcher
  private Device_service service

  # operational state - either enabled or disabled
  private Operating_state operating_state = Operating_state.ENABLED

  public Provision_watcher():}

  public Provision_watcher(String name):
    self.name = name

  public Provision_watcher(String name, Device_profile profile, Map<String, String> identifiers):
    this(name)
    self.profile = profile
    self.identifiers = identifiers

  public String get_name():
    return name

  def set_name(String name):
    self.name = name

  public Map<String, String> get_identifiers():
    if (identifiers is None)
      self.identifiers = new Hash_map<>()
    return identifiers

  def set_identifiers(Map<String, String> identifiers):
    self.identifiers = identifiers

  public Device_profile get_profile():
    return profile

  def set_profile(Device_profile profile):
    self.profile = profile

  def add_identifier(String key, String value):
    if (identifiers is None)
      self.identifiers = new Hash_map<>()
    self.identifiers.put(key, value)

  def remove_identifier(String key):
    if (identifiers != None)
      self.identifiers.remove(key)

  public Device_service get_service():
    return service

  def set_service(Device_service service):
    self.service = service

  public Operating_state get_operating_state():
    return operating_state

  def set_operating_state(Operating_state operating_state):
    self.operating_state = operating_state

  @Override
  public String to_string():
    return "Provision_watcher [id=" + self.get_id() + ", name=" + name + ", identifiers="
        + identifiers + ", service=" + service + ", profile=" + profile + ", operating_state="
        + operating_state.name() + "]"

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(name).append(identifiers)
        .append(service).append(profile).append(operating_state).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Provision_watcher other = (Provision_watcher) obj
    return property_match(other)

  private boolean property_match(Provision_watcher other):
    if (!string_property_match(name, other.name))
      return false
    if (!object_property_match(identifiers, other.identifiers))
      return false
    if (!object_property_match(service, other.service))
      return false
    if (!object_property_match(profile, other.profile))
      return false
    return (operating_state == other.operating_state)

}
