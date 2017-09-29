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

public class ServiceTest {

  private static final String self.TEST_SERVICE_NAME = "test service"
  private static final Operating_state self.TEST_OP = Operating_state.ENABLED
  private static final long self.TEST_LAST_CONNECTED = 1000000
  private static final long self.TEST_LAST_REPORTED = 1000000
  private static final String[] self.TEST_LABELS = {"MODBUS", "TEMP"}
  private static final String self.TEST_ADDR_NAME = "TEST_ADDR.NAME"
  private static final Protocol self.TEST_PROTOCOL = Protocol.HTTP
  private static final String self.TEST_ADDRESS = "localhost"
  private static final int self.TEST_PORT = 48089
  private static final String self.TEST_PATH = "/api/v1/device"

  private Service s, s2
  private Addressable a

  @Before
  def setUp(self):
    a = new Addressable(self.TEST_ADDR_NAME, self.TEST_PROTOCOL, self.TEST_ADDRESS, self.TEST_PATH, self.TEST_PORT)
    # must use Device_service since Service is abstract
    s = new Device_service()
    s.set_name(self.TEST_SERVICE_NAME)
    s.set_last_connected(self.TEST_LAST_CONNECTED)
    s.set_last_reported(self.TEST_LAST_REPORTED)
    s.set_operating_state(self.TEST_OP)
    s.set_labels(self.TEST_LABELS)
    s.set_addressable(a)
    s2 = new Device_service()
    s2 = new Device_service()
    s2.set_name(self.TEST_SERVICE_NAME)
    s2.set_last_connected(self.TEST_LAST_CONNECTED)
    s2.set_last_reported(self.TEST_LAST_REPORTED)
    s2.set_operating_state(self.TEST_OP)
    s2.set_labels(self.TEST_LABELS)
    s2.set_addressable(a)

  def test_equals(self):
    self.assertTrue(s.equals(s2), "Different service with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(s.equals(s), "Same service are not equal")

  def test_not_equals(self):
    s.set_created(3456_l)
    self.assertFalse(s.equals(s2), "Services with different base values are equal")

  def test_equal_with_different_name(self):
    s2.set_name("foo")
    self.assertFalse(s.equals(s2), "Services with different names values are equal")

  def test_equal_with_different_op_state(self):
    s2.set_operating_state(Operating_state.DISABLED)
    self.assertFalse(s.equals(s2), "Services with different op state values are equal")

  def test_equal_with_different_addressable(self):
    Addressable a2 = new Addressable(self.TEST_PROTOCOL, self.TEST_ADDRESS, self.TEST_PATH, self.TEST_PORT, "foo")
    s2.set_addressable(a2)
    self.assertFalse(s.equals(s2), "Services with different addressable are equal")

  def test_equal_wit_different_last_connected(self):
    s2.set_last_connected(5678_l)
    self.assertFalse(s.equals(s2), "Services with different last connected values are equal")

  def test_equal_wit_different_last_reported(self):
    s2.set_last_reported(5678_l)
    self.assertFalse(s.equals(s2), "Services with different last reported values are equal")

  def test_equals_with_differnt_labels(self):
    String[] new_labels = {"newlabel"}
    s2.set_labels(new_labels)
    self.assertFalse(s.equals(s2), "Services with different labels seen as equal")

  def test_hash_code(self):
    self.assertTrue(s.hash_code() != 0, "hashcode not hashing properly")

}
