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

from domain.common import IoTType, ValueDescriptor

class ValueDescriptorTest(unittest.TestCase):

  TEST_NAME = "Temperature"
  TEST_MIN = -70
  TEST_MAX = 140
  TEST_TYPE = IoTType.I
  TEST_UOMLABEL = "C"
  TEST_DEF_VALUE = 32
  TEST_FORMATTING = "%d"
  TEST_LABELS = ["temp", "room temp"]
  TEST_DESCRIPTION = "test description"

  def setUp(self):
    self.descriptors = []
    self.val_desc1 = ValueDescriptor(self.TEST_NAME, self.TEST_MIN, self.TEST_MAX, self.TEST_TYPE, self.TEST_UOMLABEL,
        self.TEST_DEF_VALUE, self.TEST_FORMATTING, self.TEST_LABELS, self.TEST_DESCRIPTION)
    self.descriptors.append(self.val_desc1)
    self.val_desc2 = ValueDescriptor(self.TEST_NAME, self.TEST_MIN, self.TEST_MAX, self.TEST_TYPE, self.TEST_UOMLABEL,
        self.TEST_DEF_VALUE, self.TEST_FORMATTING, self.TEST_LABELS, self.TEST_DESCRIPTION)
    self.descriptors.append(self.val_desc2)

  def test_get_names(self):
    self.val_desc2.name = "Humidity"
    names = [self.TEST_NAME, "Humidity"]
    self.assertEqual(names, ValueDescriptor.get_names(self.descriptors),
      "ValueDescriptor names list does not match expected list")

  def test_to_string(self):
    str(self.val_desc1)

  def test_hash_code(self):
    self.assertTrue(self.val_desc1.__hash__() != 0, "hashcode not hashing properly")

  def test_equals_with_same(self):
    self.assertTrue(self.val_desc1 == self.val_desc1, "same value descriptor not seen as equal")

  def test_equals_with_different_vDs(self):
    self.assertTrue(self.val_desc1 == self.val_desc2, "value self.descriptors with same values seen as not equal")

  def test_not_equals(self):
    self.val_desc1.created = 1234
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different base values seen as equal")

  def test_equals_with_different_name(self):
    self.val_desc2.name = "different_name"
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different names seen as equal")

  def test_equals_with_different_min(self):
    self.val_desc2.min = self.TEST_MIN + 1
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different mins seen as equal")

  def test_equals_with_different_max(self):
    self.val_desc2.max = self.TEST_MAX + 1
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different max seen as equal")

  def test_equals_with_different_type(self):
    self.val_desc2.type = IoTType.S
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different types seen as equal")

  def test_equals_with_different_labels(self):
    new_labels = ["newlabel"]
    self.val_desc2.labels = new_labels
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different labels seen as equal")

  def test_equals_with_different_defaultValue(self):
    self.val_desc2.defaultValue = "default"
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different default values seen as equal")

  def test_equals_with_none_defaultValue(self):
    self.val_desc1.defaultValue = None
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with None default values seen as equal")

  def test_equals_with_none_defaultValues(self):
    self.val_desc1.defaultValue = None
    self.val_desc2.defaultValue = None
    self.assertTrue(self.val_desc1 == self.val_desc2, "value self.descriptors both with None default values seen as not equal")

  def test_equals_with_differnt_uomLabels(self):
    self.val_desc2.uomLabel = "newUoM"
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different default values seen as equal")

  def test_equals_with_differnt_formatting(self):
    self.val_desc2.formatting = "newformat"
    self.assertFalse(self.val_desc1 == self.val_desc2, "value self.descriptors with different formatting seen as equal")

if __name__ == "__main__":
  unittest.main()