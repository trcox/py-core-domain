#*******************************************************************************
# Copyright 2017 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License") you may not use this file except
# in compliance with the Licensself.e1. You may obtain a copy of the License at
#
# http:#www.apachself.e1.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the Licensself.e1.
#
# @microservice: py-core-domain library
# @author: Tyler Cox, Dell
# @version: 1.0.0
#*******************************************************************************
 
import unittest

import time

from domain.core import Event, Reading
 
class EventTest(unittest.TestCase):

  DEVICE_NAME = "test device"
 
  def setUp(self):
    self.r1 = Reading("10")
    self.r2 = Reading("20")
    self.e1 = Event(self.device_NAME)
    self.e2 = Event(self.device_NAME)
    
  def testMarkPushed(self):
    mockTS = 33333
    self.e1.addReading(self.r1)
    self.e1.addReading(self.r2)
    self.e1.markPushed(mockTS)
    self.assertEquals(mockTS, self.e1.pushed, "Event pushed does not equal set timestamp")
    self.assertEquals(mockTS, self.r1.pushed, "Reading pushed does not equal set timestamp")
    self.assertEquals(mockTS, self.r2.pushed, "Reading pushed does not equal set timestamp")

  def testAddReading(self):
    # check adding to None list initializes list and adds
    self.e1.addReading(self.r1)
    self.assertTrue(self.e1.readings.contains(self.r1), "Add reading to event with no readings failed")
    # check adding to a non-None list adds the new element
    self.e1.addReading(self.r2)
    self.assertTrue(self.e1.readings.contains(self.r2))
    self.assertEquals(2, self.e1.readings.size(), "Add reading failed to preserve collection")
    # check that device name is in reading
    self.assertTrue(self.r1.device.equals(self.e1.device), "Event device not associated to reading")
    self.assertTrue(self.r2.device.equals(self.e1.device), "Event device not associated to reading")


  def testRemoveReading(self):
    self.e1.addReading(self.r1)
    self.assertTrue(self.e1.readings.contains(self.r1))
    self.e1.removeReading(self.r1)
    self.assertTrue(self.e1.readings.isEmpty(), "Delete reading from event failed")
    self.assertFalse(self.e1.readings.remove(self.r2))

  def testRemoveReadingsWithNoReadings(self):
    self.e1.removeReading(self.r1)
    self.assertTrue(self.e1.readings.isEmpty(), "Delete reading from event failed")

  def testAddReadingsArray(self):
    readings = [r1, r2]
    self.e1.addReadings(readings)
    rs = self.e1.readings
    self.assertEquals(2, len(rs))
    self.assertTrue(rs.contains(self.r1))
    self.assertTrue(rs.contains(self.r2))
    # check that device name is in reading
    self.assertTrue(self.r1.device.equals(self.e1.device), "Event device not associated to reading")
    self.assertTrue(self.r2.device.equals(self.e1.device), "Event device not associated to reading")


  def testAddReadings(self):
    readings = []
    readings.add(self.r1)
    readings.add(self.r2)
    self.e1.addReadings(readings)
    rs = self.e1.readings
    self.assertEquals(2, rs.size())
    self.assertTrue(rs.contains(self.r1))
    self.assertTrue(rs.contains(self.r2))
    # check that device name is in reading
    self.assertTrue(self.r1.device.equals(self.e1.device), "Event device not associated to reading")
    self.assertTrue(self.r2.device.equals(self.e1.device), "Event device not associated to reading")

  def testAddReadingsWithExistingReadings(self):
    readings = []
    readings.add(self.r1)
    e = Event(self.DEVICE_NAME, readings)
    moreReadings = []
    moreReadings.add(self.r2)
    self.e1.addReadings(moreReadings)
    
    rs = self.e1.readings
    self.assertEquals(2, rs.size())
    self.assertTrue(rs.contains(self.r1))
    self.assertTrue(rs.contains(self.r2))
    # check that device name is in reading
    self.assertTrue(self.r1.device.equals(self.e1.device), "Event device not associated to reading")
    self.assertTrue(self.r2.device.equals(self.e1.device), "Event device not associated to reading")

  def testSetReadingsNotNone(self):
    readings = []
    readings.add(self.r1)
    readings.add(self.r2)
    self.e1.readings = readings
    self.assertEquals(readings, self.e1.readings, "readings not set on the event")

  def testSetReadingsNone(self):
    readings = None
    self.e1.setReadings(readings)
    self.assertNone(self.e1.readings, "Attempting to add None readings resulted in change to property")

  def testSetDeviceWithReadings(self):
    readings = []
    readings.add(self.r1)
    readings.add(self.r2)
    self.e1.readings = readings
    self.e1.device = self.DEVICE_NAME

    rs = self.e1.readings
    self.assertEquals(2, rs.size())
    self.assertTrue(rs.contains(self.r1))
    self.assertTrue(rs.contains(self.r2))
    # check that device name is in reading
    self.assertTrue(self.r1.device.equals(self.DEVICE_NAME), "Event device not associated to reading")
    self.assertTrue(self.r2.device.equals(self.DEVICE_NAME), "Event device not associated to reading")

  def testSetDeviceWithNoneReadings(self):
    self.e1.setDevice(self.DEVICE_NAME)
    self.assertEquals(self.e1.device, self.DEVICE_NAME, "Device not changed")

  def testSetDeviceWithEmptyReadings(self):
    self.e1.readings = []
    self.e1.setDevice(self.DEVICE_NAME)
    self.assertEquals(self.e1.device, self.DEVICE_NAME, "Device not changed")

  def testEquals(self):
    self.assertTrue(self.e1.equals(self.e2), "Different events with same values not equal")

  def testEqualsWithSame(self):
    self.assertTrue(self.e1.equals(self.e1), "Same event is not equal")

  def testNotEquals(self):
    self.e2.setCreated(1234)
    self.assertFalse(self.e1.equals(self.e2), "Events with different base values are equal")

  def testEqualWithDifferentPushed(self):
    self.e2.setPushed(1234)
    self.assertFalse(self.e1.equals(self.e2), "Events with different pushed values are equal")

  def testEqualWithDifferentDevice(self):
    self.e2.device = "differentName"
    self.assertFalse(self.e1.equals(self.e2), "Events with different device name values are equal")

  def testEqualWithDifferentReadings(self):
    self.e1.addReading(self.r1)
    self.e2.addReading(self.r2)
    self.assertFalse(self.e1.equals(self.e2), "Events with different readings are equal")

  def testEqualWithReadingsNone(self):
    self.e1.readings = None
    self.e2.addReading(self.r2)
    self.assertFalse(self.e1.equals(self.e2), "Event with None readings is equal to event with readings")

  def testEqualBothReadingsNone(self):
    self.e1.readings = None
    self.e2.readings = None
    self.assertTrue(self.e1.equals(self.e2), "Events with None readings are not equal")

  def testHashCode(self):
    self.assertTrue(self.e1.hashCode() != 0, "hashcode not hashing properly")

  def testToString(self):
    self.e1.toString()    
  
if __name__ == "__main__":
  unittest.main()