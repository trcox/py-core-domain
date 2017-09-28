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
from domain.core import Reading

class ReadingTest(unittest.TestCase):

  TEST_VALUE = "10"
  TEST_NAME = "Temperature"
  TEST_PUSHED = 1234

  def setUp(self):
    self.r1 = Reading(self.TEST_NAME, self.TEST_VALUE, self.TEST_PUSHED)
    self.r2 = Reading(self.TEST_NAME, self.TEST_VALUE, self.TEST_PUSHED)

  def test_change_value_type(self):
    self.r1.value = "Foo"
    self.assertEqual("Foo", self.r1.value)

  def test_equal(self):
    self.assertTrue(self.r1 == self.r2, "Different readings with same values not equal")

  def test_equal_with_same(self):
    self.assertTrue(self.r1 == self.r1, "Same readings are not equal")

  def test_not_equal(self):
    self.r2.created = 3456
    self.assertFalse(self.r1 == self.r2, "Readings with different base values are equal")

  def test_equal_with_different_pushed(self):
    self.r2.pushed = 4567
    self.assertFalse(self.r1 == self.r2, "Readings with different pushed values are equal")

  def test_equal_with_different_names(self):
    self.r2.name = "foo"
    self.assertFalse(self.r1 == self.r2, "Readings with different name values are equal")

  def test_equal_with_different_values(self):
    self.r2.value = "foo"
    self.assertFalse(self.r1 == self.r2, "Readings with different value values are equal")

  def test_hash_code(self):
    self.assertTrue(self.r1.__hash__() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    str(self.r1)

if __name__ == "__main__":
  unittest.main()