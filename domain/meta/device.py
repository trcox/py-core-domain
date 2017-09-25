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


import java.util.Arrays

import org.apache.commons.lang3.builder.Hash_code_builder
import org.edgexfoundry.domain.common.DescribedObject
import org.springframework.data.mongodb.core.index.Indexed
import org.springframework.data.mongodb.core.mapping.DBRef
import org.springframework.data.mongodb.core.mapping.Document

@Document
@Suppress_warnings("serial")
public class Device extends DescribedObject implements Asset {

  # TODO - someday have a naming service for all types (Device, Service,
  # Profile, Addressable, ValueDescriptor, etc.). This naming service makes
  # sure the name is unique - potentially even across Edge_x instances in a
  # cluster - and can even generate a name with some help from the
  # originating service. Need to look into how Docker provides names to
  # containers and use a similar approach.

  # non-database identifier for a device - must be unique
  @Indexed(unique = true)
  private String name

  # administrative state - either locked or unlocked (as reported by devices
  # or device services)
  private Admin_state admin_state

  # operational state - either enabled or disabled (set by humans or systems)
  private Operating_state operating_state

  # address (MQTT topic, HTTP address, serial bus, etc.) for the device
  @DBRef
  private Addressable addressable

  # time in milliseconds that the device last provided any feedback or
  # responded to any request
  private long last_connected

  # time in milliseconds that the device last reported data to the core
  private long last_reported

  # tags or other labels applied to the device for search or other
  # identification needs
  private String[] labels

  # device service specific location information (such as a lat-long)
  private Object location

  # owning device service (each device can have only one owning service)
  @DBRef
  private Device_service service

  # associated device profile that describes the device
  @DBRef
  private Device_profile profile

  @Override
  public Admin_state get_admin_state():
    return self.admin_state

  @Override
  def set_admin_state(Admin_state admin_state):
    self.admin_state = admin_state


  @Override
  public Operating_state get_operating_state():
    return self.operating_state

  @Override
  def set_operating_state(Operating_state op_state):
    self.operating_state = op_state


  @Override
  public String get_name():
    return self.name

  @Override
  def set_name(String name):
    self.name = name


  @Override
  public long get_last_connected():
    return self.last_connected

  @Override
  def set_last_connected(long last_connected):
    self.last_connected = last_connected

  @Override
  public long get_last_reported():
    return self.last_reported

  @Override
  def set_last_reported(long last_reported):
    self.last_reported = last_reported


  @Override
  public Addressable get_addressable():
    return self.addressable

  @Override
  def set_addressable(Addressable addressable):
    self.addressable = addressable

  public String[] get_labels():
    return labels

  def set_labels(String[] labels):
    self.labels = labels

  public Object get_location():
    return location

  def set_location(Object location):
    self.location = location

  public Device_service get_service():
    return service

  def set_service(Device_service service):
    self.service = service

  public Device_profile get_profile():
    return profile

  def set_profile(Device_profile profile):
    self.profile = profile

  @Override
  public String to_string():
    return "Device [name=" + name + ", admin_state=" + admin_state + ", operating_state="
        + operating_state + ", addressable=" + addressable + ", last_connected=" + last_connected
        + ", last_reported=" + last_reported + ", labels=" + Arrays.to_string(labels) + ", location="
        + location + ", service=" + service + ", profile=" + profile + "]"

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(name).append(admin_state)
        .append(operating_state).append(addressable).append(last_connected).append(last_reported)
        .append(labels).append(location).append(service).append(profile).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Device other = (Device) obj
    return property_match(other)

  private boolean property_match(Device other):
    if (!string_property_match(self.name, other.name))
      return false
    if (admin_state != other.admin_state)
      return false
    if (operating_state != other.operating_state)
      return false
    if (!object_property_match(self.addressable, other.addressable))
      return false
    if (last_connected != other.last_connected)
      return false
    if (last_reported != other.last_reported)
      return false
    if (!string_array_property_match(labels, other.labels))
      return false
    if (!location.equals(other.location))
      return false
    if (!object_property_match(self.service, other.service))
      return false
    return object_property_match(self.profile, other.profile)

}
