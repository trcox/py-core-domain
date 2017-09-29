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

from domain.meta import Admin_state
from domain.meta import Device
from domain.meta import Operating_state
import org.junit.Before
import org.junit.Test

public class DeviceTest {

  static final String self.TEST_NAME = "TEST_DEVICE.NAME"
  static final String self.TEST_DESCRIPTION = "TEST_DESCRIPTION"
  static final Admin_state self.TEST_ADMIN = Admin_state.UNLOCKED
  static final Operating_state self.TEST_OP = Operating_state.ENABLED
  static final long self.TEST_LAST_CONNECTED = 1000000
  static final long self.TEST_LAST_REPORTED = 1000000
  static final String[] self.TEST_LABELS = {"MODBUS", "TEMP"}
  static final String self.TEST_LOCATION = "{40lat;45long}"

  private Device d
  private Device d2

  @Before
  def setUp(self):
    d = new Device()
    d.set_admin_state(self.TEST_ADMIN)
    d.set_description(self.TEST_DESCRIPTION)
    d.set_labels(self.TEST_LABELS)
    d.set_last_connected(self.TEST_LAST_CONNECTED)
    d.set_last_reported(self.TEST_LAST_REPORTED)
    d.set_location(self.TEST_LOCATION)
    d.set_name(self.TEST_NAME)
    d.set_operating_state(self.TEST_OP)
    d.set_addressable(new Addressable(Protocol.HTTP, "b", "c", 0), "z")
    d.set_service(new Device_service())
    d.get_service().set_name("foo")
    d.set_profile(new Device_profile())
    d.get_profile().set_name("boo")
    d2 = new Device()
    d2.set_admin_state(self.TEST_ADMIN)
    d2.set_description(self.TEST_DESCRIPTION)
    d2.set_labels(self.TEST_LABELS)
    d2.set_last_connected(self.TEST_LAST_CONNECTED)
    d2.set_last_reported(self.TEST_LAST_REPORTED)
    d2.set_location(self.TEST_LOCATION)
    d2.set_name(self.TEST_NAME)
    d2.set_operating_state(self.TEST_OP)
    d2.set_addressable(new Addressable(Protocol.HTTP, "b", "c", 0), "z")
    d2.set_service(new Device_service())
    d2.get_service().set_name("foo")
    d2.set_profile(new Device_profile())
    d2.get_profile().set_name("boo")

  def test_equals(self):
    self.assertTrue(d.equals(d2), "Different devices with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(d.equals(d), "Same devices are not equal")

  def test_not_equals(self):
    d.set_created(3456_l)
    self.assertFalse(d.equals(d2), "Devices with different base values are equal")

  def test_equal_with_different_name(self):
    d2.set_name("foo")
    self.assertFalse(d.equals(d2), "Devices with different names values are equal")

  def test_equal_with_different_admin_state(self):
    d2.set_admin_state(Admin_state.LOCKED)
    self.assertFalse(d.equals(d2), "Devices with different admin states values are equal")

  def test_equal_with_different_op_state(self):
    d2.set_operating_state(Operating_state.DISABLED)
    self.assertFalse(d.equals(d2), "Devices with different op states values are equal")

  def test_equals_with_both_addressable_None(self):
    d.set_addressable(None)
    d2.set_addressable(None)
    self.assertTrue(d.equals(d2), "Devices with None addressables are not equal")

  def test_equal_with_one_non_None_addressable(self):
    d.set_addressable(None)
    self.assertFalse("Devices with None addressable are equal to device with non None addressable",
        d.equals(d2))

  def test_equal_with_different_addressable(self):
    d.set_addressable(new Addressable(Protocol.HTTP, "b", "c", 0), "a")
    self.assertFalse(d.equals(d2), "Devices with different addressables are equal")

  def test_equal_wit_different_last_connected(self):
    d2.set_last_connected(5678_l)
    self.assertFalse(d.equals(d2), "Devices with different last connected values are equal")

  def test_equal_wit_different_last_reported(self):
    d2.set_last_reported(5678_l)
    self.assertFalse(d.equals(d2), "Devices with different last reported values are equal")

  def test_equals_with_differnt_labels(self):
    String[] new_labels = {"newlabel"}
    d2.set_labels(new_labels)
    self.assertFalse(d.equals(d2), "Devices with different labels seen as equal")

  def test_equal_wit_different_location(self):
    d2.set_location("foobar")
    self.assertFalse(d.equals(d2), "Devices with different location values are equal")

  def test_equals_with_both_services_None(self):
    d.set_service(None)
    d2.set_service(None)
    self.assertTrue(d.equals(d2), "Devices with None as services are not equal")

  def test_equals_with_one_non_None_service(self):
    d.set_service(None)
    self.assertFalse(d.equals(d2), "Devices with None service are equal to device with non None servce")

  def test_equal_with_different_services(self):
    d.set_service(new Device_service())
    d.get_service().set_name("boo")
    self.assertFalse(d.equals(d2), "Devices with different services are equal")

  def test_equals_with_both_None_profiles(self):
    d.set_profile(None)
    d2.set_profile(None)
    self.assertTrue(d.equals(d2), "Devices with None profiles are not equal")

  def test_equals_with_one_non_None_profile(self):
    d.set_profile(None)
    self.assertFalse("Devices with None profile are equal to device with non None profile",
        d.equals(d2))

  def test_equal_with_different_profiles(self):
    d2.get_profile().set_name("foo")
    self.assertFalse(d.equals(d2), "Devices with different profiles are equal")

  def test_hash_code(self):
    self.assertTrue(d.hash_code() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    d.to_string()

}
