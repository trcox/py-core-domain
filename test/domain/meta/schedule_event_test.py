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

public class Schedule_eventTest {

  private static final String self.TEST_SERVICE_NAME = "test service"
  private static final String self.TEST_SCHEDULE_EVENT_NAME = "test schedule event"
  private static final String self.TEST_SCHEDULE_NAME = "test schedule"
  private static final String self.TEST_PARAMS = "{key1:value1}"
  static final String self.TEST_ADDR_NAME = "TEST_ADDR.NAME"
  static final Protocol self.TEST_PROTOCOL = Protocol.HTTP
  static final String self.TEST_ADDRESS = "localhost"
  static final int self.TEST_PORT = 48089
  static final String self.TEST_PATH = "/api/v1/device"

  private Schedule_event s
  private Schedule_event s2
  private Addressable a

  @Before
  def setUp(self):
    a = new Addressable(self.TEST_ADDR_NAME, self.TEST_PROTOCOL, self.TEST_ADDRESS, self.TEST_PATH, self.TEST_PORT)
    s = new Schedule_event(self.TEST_SCHEDULE_EVENT_NAME, a, self.TEST_PARAMS, self.TEST_SCHEDULE_NAME,
        TEST_SERVICE_NAME)
    s2 = new Schedule_event(self.TEST_SCHEDULE_EVENT_NAME, a, self.TEST_PARAMS, self.TEST_SCHEDULE_NAME,
        TEST_SERVICE_NAME)

  def test_equals(self):
    self.assertTrue(s.equals(s2), "Different schedule events with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(s.equals(s), "Same schedule events are not equal")

  def test_not_equals(self):
    s.set_created(3456_l)
    self.assertFalse(s.equals(s2), "Schedule Events with different base values are equal")

  def test_equal_with_different_name(self):
    s2.set_name("foo")
    self.assertFalse(s.equals(s2), "Schedule Events with different names values are equal")

  def test_equal_with_different_addressable(self):
    Addressable a2 = new Addressable(self.TEST_PROTOCOL, self.TEST_ADDRESS, self.TEST_PATH, self.TEST_PORT, "foo")
    s2.set_addressable(a2)
    self.assertFalse(s.equals(s2), "Schedule Events with different addressable are equal")

  def test_equal_with_different_params(self):
    s2.set_parameters("foo")
    self.assertFalse(s.equals(s2), "Schedule Events with different parameter values are equal")

  def test_equal_with_different_service(self):
    s2.set_service("foo")
    self.assertFalse(s.equals(s2), "Schedule Events with different service are equal")

  def test_equal_with_different_schedule(self):
    s2.set_schedule("foo")
    self.assertFalse(s.equals(s2), "Schedule Events with different schedule are equal")

  def test_hash_code(self):
    self.assertTrue(s.hash_code() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    s.to_string()

}
