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

from domain.core import Reading
 
class ReadingTest(unittest.TestCase):

  TEST_VALUE = "10"
  TEST_NAME = "Temperature"
  TEST_PUSHED = 1234
 
  def setUp(self):
    self.r1 = Reading(self.TEST_NAME, self.TEST_VALUE, self.TEST_PUSHED)
    self.r2 = Reading(self.TEST_NAME, self.TEST_VALUE, self.TEST_PUSHED)
    
  def testChangeValueType(self):
    self.r1.value = "Foo"
    self.assertEqual("Foo", self.r1.value)

  def testEqual(self):
    self.assertTrue(self.r1 == self.r2, "Different readings with same values not equal")

  def testEqualWithSame(self):
    self.assertTrue(self.r1 == self.r1, "Same readings are not equal")

  def testNotEqual(self):
    self.r2.created = 3456
    self.assertFalse(self.r1 == self.r2, "Readings with different base values are equal")

  def testEqualWithDifferentPushed(self):
    self.r2.pushed = 4567
    self.assertFalse(self.r1 == self.r2, "Readings with different pushed values are equal")

  def testEqualWithDifferentNames(self):
    self.r2.name = "foo"
    self.assertFalse(self.r1 == self.r2, "Readings with different name values are equal")

  def testEqualWithDifferentValues(self):
    self.r2.value = "foo"
    self.assertFalse(self.r1 == self.r2, "Readings with different value values are equal")

  def testHashCode(self):
    self.assertTrue(self.r1.__hash__() != 0, "hashcode not hashing properly")

  def testToString(self):
    str(self.r1)
  
if __name__ == "__main__":
  unittest.main()