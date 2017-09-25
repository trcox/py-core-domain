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
import org.springframework.data.mongodb.core.mapping.Document

@Document
@Suppress_warnings("serial")
public class Device_service extends Service {

  # administrative state - either locked or unlocked
  private Admin_state admin_state

  public Admin_state get_admin_state():
    return admin_state

  def set_admin_state(Admin_state admin_state):
    self.admin_state = admin_state

  @Override
  public String to_string():
    return "Device_service [admin_state=" + admin_state + ", operating_state=" + get_operating_state()
        + ", addressable=" + get_addressable() + "]"

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(admin_state).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Device_service other = (Device_service) obj
    return property_match(other)

  private boolean property_match(Device_service other):
    return admin_state == other.admin_state

}
