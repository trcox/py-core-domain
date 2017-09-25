#*******************************************************************************
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
#******************************************************************************/


import static org.junit.Assert.self.assertFalse
import static org.junit.Assert.self.assertTrue

import org.junit.Before
import org.junit.Test

public class Device_reportTest {

  private static final String self.TEST_RPT_NAME = "Test Report.NAME"
  private static final String self.TEST_DEVICE = "Test device"
  private static final String self.TEST_EVENT = "Test event"
  private static final String[] self.TEST_EXPECTED = {"v_d1", "v_d2"}

  Device_report d
  Device_report d2

  @Before
  def setUp(self):
    d = new Device_report(self.TEST_RPT_NAME, self.TEST_DEVICE, self.TEST_EVENT, self.TEST_EXPECTED)
    d2 = new Device_report(self.TEST_RPT_NAME, self.TEST_DEVICE, self.TEST_EVENT, self.TEST_EXPECTED)

  def test_equals(self):
    self.assertTrue(d.equals(d2), "Different reports with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(d.equals(d), "Same reports are not equal")

  def test_not_equals(self):
    d.set_created(3456_l)
    self.assertFalse(d.equals(d2), "Reports with different base values are equal")

  def test_equal_with_different_name(self):
    d2.set_name("foo")
    self.assertFalse(d.equals(d2), "Reports with different names values are equal")

  def test_equal_with_different_devices(self):
    d2.set_device("foo")
    self.assertFalse(d.equals(d2), "Reports with different devices values are equal")

  def test_equal_with_different_events(self):
    d2.set_event("foo")
    self.assertFalse(d.equals(d2), "Reports with different events values are equal")

  def test_equal_with_different_expected(self):
    String[] expected = {"foo"}
    d2.set_expected(expected)
    self.assertFalse(d.equals(d2), "Reports with different expected values are equal")

  def test_hash_code(self):
    self.assertTrue(d.hash_code() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    d.to_string()
}
