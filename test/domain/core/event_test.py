# *******************************************************************************
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
# *******************************************************************************

import unittest
from domain.core import event
from domain.core import reading

# pylint: disable=R0904


class EventTest(unittest.TestCase):

    DEVICE_NAME = "test device"

    def setUp(self):
        self.reading1 = reading.Reading("10")
        self.reading2 = reading.Reading("20")
        self.event1 = event.Event(self.DEVICE_NAME)
        self.event2 = event.Event(self.DEVICE_NAME)

    def test_mark_pushed(self):
        mock_ts = 33333
        self.event1.add_reading(self.reading1)
        self.event1.add_reading(self.reading2)
        self.event1.mark_pushed(mock_ts)
        self.assertEqual(mock_ts, self.event1.pushed, "Event pushed does not equal set timestamp")
        self.assertEqual(mock_ts, self.reading1.pushed,
                         "Reading pushed does not equal set timestamp")
        self.assertEqual(mock_ts, self.reading2.pushed,
                         "Reading pushed does not equal set timestamp")

    def test_add_reading(self):
        # check adding to None list initializes list and adds
        self.event1.add_reading(self.reading1)
        self.assertTrue(self.reading1 in self.event1.readings,
                        "Add reading to event with no readings failed")
        # check adding to a non-None list adds the new element
        self.event1.add_reading(self.reading2)
        self.assertTrue(self.reading2 in self.event1.readings)
        self.assertEqual(2, len(self.event1.readings), "Add reading failed to preserve collection")
        # check that device name is in reading
        self.assertTrue(self.reading1.device == self.event1.device,
                        "Event device not associated to reading")
        self.assertTrue(self.reading2.device == self.event1.device,
                        "Event device not associated to reading")


    def test_remove_reading(self):
        self.event1.add_reading(self.reading1)
        self.assertTrue(self.reading1 in self.event1.readings)
        self.event1.remove_reading(self.reading1)
        self.assertEqual(0, len(self.event1.readings), "Delete reading from event failed")
        self.assertFalse(self.event1.remove_reading(self.reading2))

    def test_remove_no_readings(self):
        self.event1.remove_reading(self.reading1)
        self.assertEqual(0, len(self.event1.readings), "Delete reading from event failed")

    def test_add_readings_array(self):
        readings = [self.reading1, self.reading2]
        self.event1.add_readings(readings)
        readings = self.event1.readings
        self.assertEqual(2, len(readings))
        self.assertTrue(self.reading1 in readings)
        self.assertTrue(self.reading2 in readings)
        # check that device name is in reading
        self.assertTrue(self.reading1.device == self.event1.device,
                        "Event device not associated to reading")
        self.assertTrue(self.reading2.device == self.event1.device,
                        "Event device not associated to reading")


    def test_add_readings(self):
        readings = []
        readings.append(self.reading1)
        readings.append(self.reading2)
        self.event1.add_readings(readings)
        readings = self.event1.readings
        self.assertEqual(2, len(readings))
        self.assertTrue(self.reading1 in readings)
        self.assertTrue(self.reading2 in readings)
        # check that device name is in reading
        self.assertTrue(self.reading1.device == self.event1.device,
                        "Event device not associated to reading")
        self.assertTrue(self.reading2.device == self.event1.device,
                        "Event device not associated to reading")

    def test_add_existing_readings(self):
        readings = []
        readings.append(self.reading1)
        self.event1 = event.Event(self.DEVICE_NAME, readings)
        more_readings = []
        more_readings.append(self.reading2)
        self.event1.add_readings(more_readings)

        readings = self.event1.readings
        self.assertEqual(2, len(readings))
        self.assertTrue(self.reading1 in readings)
        self.assertTrue(self.reading2 in readings)
        # check that device name is in reading
        self.assertTrue(self.reading1.device == self.event1.device,
                        "Event device not associated to reading")
        self.assertTrue(self.reading2.device == self.event1.device,
                        "Event device not associated to reading")

    def test_set_readings_not_none(self):
        readings = []
        readings.append(self.reading1)
        readings.append(self.reading2)
        self.event1.readings = readings
        self.assertEqual(readings, self.event1.readings, "readings not set on the event")

    def test_set_readings_none(self):
        readings = None
        self.event1.readings = readings
        self.assertEqual(None, self.event1.readings,
                         "Attempting to add None readings resulted in change to property")

    def test_set_device_readings(self):
        readings = []
        readings.append(self.reading1)
        readings.append(self.reading2)
        self.event1.readings = readings
        self.event1.device = self.DEVICE_NAME
        readings = self.event1.readings
        self.assertEqual(2, len(readings))
        self.assertTrue(self.reading1 in readings)
        self.assertTrue(self.reading2 in readings)
        # check that device name is in reading
        self.assertTrue(self.reading1.device == self.DEVICE_NAME,
                        "Event device not associated to reading")
        self.assertTrue(self.reading2.device == self.DEVICE_NAME,
                        "Event device not associated to reading")

    def test_set_device_none_readings(self):
        self.event1.device = self.DEVICE_NAME
        self.assertEqual(self.event1.device, self.DEVICE_NAME, "Device not changed")

    def test_set_device_empty_readings(self):
        self.event1.readings = []
        self.event1.device = self.DEVICE_NAME
        self.assertEqual(self.event1.device, self.DEVICE_NAME, "Device not changed")

    def test_equal(self):
        self.assertTrue(self.event1 == self.event2, "Different events with same values not equal")

    def test_equal_same(self):
        self.assertTrue(self.event1 == self.event1, "Same event is not equal")

    def test_not_equal(self):
        self.event2.created = 1234
        self.assertFalse(self.event1 == self.event2, "Events with different base values are equal")

    def test_equal_different_pushed(self):
        self.event2.pushed = 1234
        self.assertFalse(self.event1 == self.event2,
                         "Events with different pushed values are equal")

    def test_equal_different_device(self):
        self.event2.device = "different_name"
        self.assertFalse(self.event1 == self.event2,
                         "Events with different device name values are equal")

    def test_equal_different_readings(self):
        self.event1.add_reading(self.reading1)
        self.event2.add_reading(self.reading2)
        self.assertFalse(self.event1 == self.event2, "Events with different readings are equal")

    def test_equal_readings_none(self):
        self.event1.readings = None
        self.event2.add_reading(self.reading2)
        self.assertFalse(self.event1 == self.event2,
                         "Event with None readings is equal to event with readings")

    def test_equal_both_readings_none(self):
        self.event1.readings = None
        self.event2.readings = None
        self.assertTrue(self.event1 == self.event2, "Events with None readings are not equal")

    def test_hash_code(self):
        self.assertTrue(self.event1.__hash__() != 0, "hashcode not hashing properly")

    def test_to_string(self):
        str(self.event1)

if __name__ == "__main__":
    unittest.main()
