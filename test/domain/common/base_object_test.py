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

import time
import unittest
from domain.core import event


class BaseObjectTest(unittest.TestCase):

    def setUp(self):
        self.bo1 = event.Event("test device")
        self.bo2 = event.Event("test device")
        self.bo3 = event.Event("test device")
        current_time = time.time()
        self.bo1.created = current_time
        self.bo3.created = current_time
        self.bo1.origin = current_time
        self.bo3.origin = current_time
        self.bo2.created = current_time + 1000

    def test_equals_same_object(self):
        self.assertEqual(self.bo1, self.bo1, "Same object not equals")

    def test_equals_different_object(self):
        self.assertEqual(self.bo1, self.bo3, "same object not equals")

    def test_not_equals_none(self):
        self.assertNotEqual(self.bo1, None, "base object was equal to null")

    def test_not_equals_wrong_type(self):
        self.assertNotEqual(self.bo1, "string", ("Base object was equal when "
                                                 "compared to object of type string"))

    def test_not_equals_wrong_created(self):
        self.assertNotEqual(self.bo1, self.bo2, ("Base objects with different "
                                                 "created time are equal"))

    def test_not_equals_wrong_origin(self):
        self.bo3.origin = 1234
        self.assertNotEqual(self.bo1, self.bo3, "Objects with different origin times are equal")

    def test_compare_to(self):
        self.assertEqual(1, self.bo1.compare_to(self.bo2), ("Base object compare to method "
                                                            "not working property"))
        self.assertEqual(-1, self.bo2.compare_to(self.bo1), ("Base object compare to method "
                                                             "not working property"))
        self.assertEqual(-1, self.bo1.compare_to(self.bo3), ("Base object compare to method "
                                                             "not working property"))

    def test_to_string(self):
        str(self.bo1)

if __name__ == "__main__":
    unittest.main()
