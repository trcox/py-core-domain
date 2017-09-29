# *******************************************************************************
# Copyright 2017 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License") you may not use this file except
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
from domain.common import described_object


class DescribedObjectTest(unittest.TestCase):

    TEST_DESC = "test description"

    def setUp(self):
        self.obj1 = described_object.DescribedObject()
        self.obj1.description = self.TEST_DESC
        self.obj2 = described_object.DescribedObject()

    def test_hash_code(self):
        self.assertTrue(self.obj1.__hash__() != 0, "hashcode not hashing properly")

    def test_equals_on_same_object(self):
        self.assertEqual(self.obj1, self.obj1, "same object not equal to itself")

    def test_equals(self):
        self.obj2.description = self.TEST_DESC
        self.assertEqual(self.obj1, self.obj2, "equal not working properly")

    def test_equals_on_description_none(self):
        self.obj1.description = None
        self.assertEqual(self.obj1, self.obj2, ("equal not working when comparing "
                                                "different objects with null description"))

    def test_not_equals_based_on_super(self):
        self.obj2.description = self.TEST_DESC
        self.obj2.origin = 1234
        self.assertNotEqual(self.obj1, self.obj2, "equal not working at super level")

    def test_not_equals_on_description(self):
        self.obj2.description = "another description"
        self.assertNotEqual(self.obj1, self.obj2, ("equal not work when comparing different "
                                                   "objects with different description"))

    def test_differ_on_null_description(self):
        self.obj2.description = "some description"
        self.obj1.description = None
        self.assertNotEqual(self.obj1, self.obj2, ("equal not working when comparing null "
                                                   "to different description"))

if __name__ == "__main__":
    unittest.main()
