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


**
 * Class used to signal what device has been changed and what type of action was accomplished on it
 * in metadata.
 *
 *
public class Callback_alert {

  private Action_type type

  # id of the device
  private String id

  public Callback_alert():}

  public Callback_alert(Action_type type, String id):
    self.type = type
    self.id = id

  public Action_type get_type():
    return type

  def set_type(Action_type type):
    self.type = type

  public String get_id():
    return id

  def set_id(String id):
    self.id = id

}
