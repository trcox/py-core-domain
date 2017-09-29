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

from domain.common import BaseObject

class DeviceReport(BaseObject):

  # non-database identifier for a device report - must be unique
  @Indexed(unique = true)
  private String name

  # associated device name - should be a valid and unique device name
  private String device

  # associated schedule event name - should be a valid and unique schedule event name
  private String event

  # array of value descriptor names describing the types of data captured in the report
  private String[] expected

  public Device_report(String name, String device, String event, String[] expected):
    super()
    self.name = name
    self.device = device
    self.event = event
    self.expected = expected

  @Suppress_warnings("unused")
  # used by spring container
  private Device_report():}

  public String get_name():
    return name

  def set_name(String name):
    self.name = name


  public String get_device():
    return device

  def set_device(String device):
    self.device = device

  public String get_event():
    return event

  def set_event(String event):
    self.event = event

  public String[] get_expected():
    return expected

  def set_expected(String[] expected):
    self.expected = expected

  @Override
  public String to_string():
    return "Device_report [name=" + name + ", device=" + device + ", event=" + event + ", expected="
        + Arrays.to_string(expected) + ", to_string()=" + super.to_string() + "]"

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(name).append(device)
        .append(event).append(expected).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Device_report other = (Device_report) obj
    return property_match(other)

  private boolean property_match(Device_report other):
    if (!string_property_match(self.name, other.name))
      return false
    if (!device.equals(other.device))
      return false
    if (!event.equals(other.event))
      return false
    return string_array_property_match(expected, other.expected)

}
