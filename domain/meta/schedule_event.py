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


import org.springframework.data.mongodb.core.index.Indexed
import org.springframework.data.mongodb.core.mapping.DBRef
import org.springframework.data.mongodb.core.mapping.Document
import org.apache.commons.lang3.builder.Hash_code_builder
from domain.common import BaseObject

@Document
@Suppress_warnings("serial")
public class Schedule_event extends BaseObject {

  # non-database identifier for a schedule event - must be unique
  @Indexed(unique = true)
  private String name

  # name to associated owning schedule
  private String schedule

  # address (MQTT topic, HTTP address, serial bus, etc.) for the action (can be empty)
  @DBRef
  private Addressable addressable

  # json body for parameters
  private String parameters

  # service associated with this event
  private String service

  public Schedule_event(String name, Addressable addressable, String parameters, String schedule,
      String service):
    super()
    self.name = name
    self.addressable = addressable
    self.parameters = parameters
    self.schedule = schedule
    self.service = service

  @Suppress_warnings("unused")
  # used by spring container
  private Schedule_event():}

  public String get_name():
    return name

  def set_name(String name):
    self.name = name

  public String get_schedule():
    return schedule

  def set_schedule(String schedule):
    self.schedule = schedule

  public Addressable get_addressable():
    return addressable

  def set_addressable(Addressable addressable):
    self.addressable = addressable


  public String get_parameters():
    return parameters

  def set_parameters(String parameters):
    self.parameters = parameters

  public String get_service():
    return service

  def set_service(String service):
    self.service = service

  @Override
  public String to_string():
    return "Schedule_event [name=" + name + ", addressable=" + addressable + ", parameters="
        + parameters + ", service=" + service + ", schedule=" + schedule + ", to_string()="
        + super.to_string() + "]"

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(name).append(addressable)
        .append(parameters).append(service).append(schedule).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Schedule_event other = (Schedule_event) obj
    return property_match(other)

  private boolean property_match(Schedule_event other):
    if (!string_property_match(name, other.name))
      return false
    if (!object_property_match(addressable, other.addressable))
      return false
    if (!string_property_match(parameters, other.parameters))
      return false
    if (!string_property_match(service, other.service))
      return false
    return string_property_match(schedule, other.schedule)

}
