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

import unittest

from domain.core import Event, Reading

class EventTest(unittest.TestCase):

  DEVICE_NAME = "test device"

  def setUp(self):
    self.r1 = Reading("10")
    self.r2 = Reading("20")
    self.e1 = Event(self.DEVICE_NAME)
    self.e2 = Event(self.DEVICE_NAME)

  def test_mark_pushed(self):
    mock_tS = 33333
    self.e1.add_reading(self.r1)
    self.e1.add_reading(self.r2)
    self.e1.mark_pushed(mock_tS)
    self.assertEqual(mock_tS, self.e1.pushed, "Event pushed does not equal set timestamp")
    self.assertEqual(mock_tS, self.r1.pushed, "Reading pushed does not equal set timestamp")
    self.assertEqual(mock_tS, self.r2.pushed, "Reading pushed does not equal set timestamp")

  def test_add_reading(self):
    # check adding to None list initializes list and adds
    self.e1.add_reading(self.r1)
    self.assertTrue(self.r1 in self.e1.readings, "Add reading to event with no readings failed")
    # check adding to a non-None list adds the new element
    self.e1.add_reading(self.r2)
    self.assertTrue(self.r2 in self.e1.readings)
    self.assertEqual(2, len(self.e1.readings), "Add reading failed to preserve collection")
    # check that device name is in reading
    self.assertTrue(self.r1.device == self.e1.device, "Event device not associated to reading")
    self.assertTrue(self.r2.device == self.e1.device, "Event device not associated to reading")


  def test_remove_reading(self):
    self.e1.add_reading(self.r1)
    self.assertTrue(self.r1 in self.e1.readings)
    self.e1.remove_reading(self.r1)
    self.assertEqual(0, len(self.e1.readings), "Delete reading from event failed")
    self.assertFalse(self.e1.remove_reading(self.r2))

  def test_remove_readings_with_no_readings(self):
    self.e1.remove_reading(self.r1)
    self.assertEqual(0, len(self.e1.readings), "Delete reading from event failed")

  def test_add_readings_array(self):
    readings = [self.r1, self.r2]
    self.e1.add_readings(readings)
    rs = self.e1.readings
    self.assertEqual(2, len(rs))
    self.assertTrue(self.r1 in rs)
    self.assertTrue(self.r2 in rs)
    # check that device name is in reading
    self.assertTrue(self.r1.device == self.e1.device, "Event device not associated to reading")
    self.assertTrue(self.r2.device == self.e1.device, "Event device not associated to reading")


  def test_add_readings(self):
    readings = []
    readings.append(self.r1)
    readings.append(self.r2)
    self.e1.add_readings(readings)
    rs = self.e1.readings
    self.assertEqual(2, len(rs))
    self.assertTrue(self.r1 in rs)
    self.assertTrue(self.r2 in rs)
    # check that device name is in reading
    self.assertTrue(self.r1.device == self.e1.device, "Event device not associated to reading")
    self.assertTrue(self.r2.device == self.e1.device, "Event device not associated to reading")

  def test_add_readings_with_existing_readings(self):
    readings = []
    readings.append(self.r1)
    self.e1 = Event(self.DEVICE_NAME, readings)
    more_readings = []
    more_readings.append(self.r2)
    self.e1.add_readings(more_readings)

    rs = self.e1.readings
    self.assertEqual(2, len(rs))
    self.assertTrue(self.r1 in rs)
    self.assertTrue(self.r2 in rs)
    # check that device name is in reading
    self.assertTrue(self.r1.device == self.e1.device, "Event device not associated to reading")
    self.assertTrue(self.r2.device == self.e1.device, "Event device not associated to reading")

  def test_set_readings_not_none(self):
    readings = []
    readings.append(self.r1)
    readings.append(self.r2)
    self.e1.readings = readings
    self.assertEqual(readings, self.e1.readings, "readings not set on the event")

  def test_set_readings_none(self):
    readings = None
    self.e1.readings = readings
    self.assertEqual(None, self.e1.readings, "Attempting to add None readings resulted in change to property")

  def test_set_device_with_readings(self):
    readings = []
    readings.append(self.r1)
    readings.append(self.r2)
    self.e1.readings = readings
    self.e1.device = self.DEVICE_NAME

    rs = self.e1.readings
    self.assertEqual(2, len(rs))
    self.assertTrue(self.r1 in rs)
    self.assertTrue(self.r2 in rs)
    # check that device name is in reading
    self.assertTrue(self.r1.device == self.DEVICE_NAME, "Event device not associated to reading")
    self.assertTrue(self.r2.device == self.DEVICE_NAME, "Event device not associated to reading")

  def test_set_device_with_none_readings(self):
    self.e1.device = self.DEVICE_NAME
    self.assertEqual(self.e1.device, self.DEVICE_NAME, "Device not changed")

  def test_set_device_with_empty_readings(self):
    self.e1.readings = []
    self.e1.device = self.DEVICE_NAME
    self.assertEqual(self.e1.device, self.DEVICE_NAME, "Device not changed")

  def test_equal(self):
    self.assertTrue(self.e1 == self.e2, "Different events with same values not equal")

  def test_equal_with_same(self):
    self.assertTrue(self.e1 == self.e1, "Same event is not equal")

  def test_not_equal(self):
    self.e2.created = 1234
    self.assertFalse(self.e1 == self.e2, "Events with different base values are equal")

  def test_equal_with_different_pushed(self):
    self.e2.pushed = 1234
    self.assertFalse(self.e1 == self.e2, "Events with different pushed values are equal")

  def test_equal_with_different_device(self):
    self.e2.device = "different_name"
    self.assertFalse(self.e1 == self.e2, "Events with different device name values are equal")

  def test_equal_with_different_readings(self):
    self.e1.add_reading(self.r1)
    self.e2.add_reading(self.r2)
    self.assertFalse(self.e1 == self.e2, "Events with different readings are equal")

  def test_equal_with_readings_none(self):
    self.e1.readings = None
    self.e2.add_reading(self.r2)
    self.assertFalse(self.e1 == self.e2, "Event with None readings is equal to event with readings")

  def test_equal_both_readings_none(self):
    self.e1.readings = None
    self.e2.readings = None
    self.assertTrue(self.e1 == self.e2, "Events with None readings are not equal")

  def test_hash_code(self):
    self.assertTrue(self.e1.__hash__() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    str(self.e1)

if __name__ == "__main__":
  unittest.main()