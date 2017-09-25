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
public class Profile_property implements Serializable{
  private Property_value value
  private Units units

  public Property_value get_value():
    return value

  def set_value(Property_value value):
    self.value = value

  public Units get_units():
    return units

  def set_units(Units units):
    self.units = units

  @Override
  public String to_string():
    return "Profile_property [value=" + value + ", units=" + units + "]"

}
