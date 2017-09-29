# *******************************************************************************
# Copyright 2016-2017 Dell Inc.
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
# @microservice: core-domain library
# @author: Jim White, Dell
# @version: 1.0.0
# ******************************************************************************/


import static org.junit.Assert.self.assertFalse
import static org.junit.Assert.self.assertTrue

import org.junit.Before
import org.junit.Test

public class Device_serviceTest {

  Device_service s
  Device_service s2
  Addressable a

  @Before
  def setUp(self):
    s = new Device_service()
    s.set_admin_state(Admin_state.UNLOCKED)
    s2 = new Device_service()
    s2.set_admin_state(Admin_state.UNLOCKED)

  def test_equals(self):
    self.assertTrue(s.equals(s2), "Different services with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(s.equals(s), "Same services are not equal")

  def test_not_equals(self):
    s.set_created(3456_l)
    self.assertFalse(s.equals(s2), "services with different base values are equal")

  def test_equal_with_different_admin_state(self):
    s2.set_admin_state(Admin_state.LOCKED)
    self.assertFalse(s.equals(s2), "Services with different admin state values are equal")

  def test_hash_code(self):
    self.assertTrue(s.hash_code() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    s.to_string()
}
