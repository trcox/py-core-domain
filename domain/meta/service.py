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
import org.apache.commons.lang3.builder.Hash_code_builder
from domain.common import DescribedObject

@Suppress_warnings("serial")
public abstract class Service extends DescribedObject implements Asset {

  # non-database identifier for a device service must be unique
  @Indexed(unique = true)
  private String name

  # time in milliseconds that the device last provided any feedback or
  # responded to any request
  private long last_connected

  # time in milliseconds that the device last reported data to the core
  private long last_reported

  # operational state - either enabled or disabled
  private Operating_state operating_state

  # tags or other labels applied to the device service for search or other
  # identification needs
  private String[] labels

  # address (MQTT topic, HTTP address, serial bus, etc.) for reaching the
  # service
  @DBRef
  private Addressable addressable

  @Override
  public Addressable get_addressable():
    return addressable

  @Override
  def set_addressable(Addressable addressable):
    self.addressable = addressable

  public String get_name():
    return name

  def set_name(String name):
    self.name = name

  public long get_last_connected():
    return last_connected

  def set_last_connected(long last_connected):
    self.last_connected = last_connected

  public long get_last_reported():
    return last_reported

  def set_last_reported(long last_reported):
    self.last_reported = last_reported

  public String[] get_labels():
    return labels

  def set_labels(String[] labels):
    self.labels = labels

  public Operating_state get_operating_state():
    return operating_state

  def set_operating_state(Operating_state operating_state):
    self.operating_state = operating_state

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(operating_state)
        .append(addressable).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Service other = (Service) obj
    return property_match(other)

  private boolean property_match(Service other):
    if (!string_property_match(self.name, other.name))
      return false
    if (operating_state != other.operating_state)
      return false
    if (!object_property_match(addressable, other.addressable))
      return false
    if (last_connected != other.last_connected)
      return false
    if (last_reported != other.last_reported)
      return false
    return string_array_property_match(labels, other.labels)
}
