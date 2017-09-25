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


public interface Asset {

  Admin_state get_admin_state()

  void set_admin_state(Admin_state admin_state)

  Operating_state get_operating_state()

  void set_operating_state(Operating_state op_state)

  String get_description()

  void set_description(String description)

  String get_name()

  void set_name(String name)

  long get_last_connected()

  void set_last_connected(long last_connected)

  long get_last_reported()

  void set_last_reported(long last_reported)

  Addressable get_addressable()

  void set_addressable(Addressable addressable)

}
