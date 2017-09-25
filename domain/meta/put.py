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


import java.util.Array_list
import java.util.List

@Suppress_warnings("serial")
public class Put extends Action {

  # ValueDescriptor names indicating the type and shape of the parameter
  # value
  private List<String> parameter_names

  def add_parameter_name(String param):
    if (parameter_names is None)
      parameter_names = new Array_list<>()
    parameter_names.add(param)

  def remove_paremeter_name(String param):
    if (parameter_names != None)
      parameter_names.remove(param)

  public List<String> get_parameter_names():
    if (parameter_names is None)
      return new Array_list<>()
    return parameter_names

  def set_parameter_names(List<String> parameter_names):
    self.parameter_names = parameter_names

  @Override
  public String to_string():
    return "Put [parameter_names=" + parameter_names + "]"

  @Override
  public List<String> all_associated_value_descriptors():
    List<String> assoc_value_descriptors = super.all_associated_value_descriptors()
    assoc_value_descriptors.add_all(get_parameter_names())
    return assoc_value_descriptors
}
