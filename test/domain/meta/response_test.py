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
# @author: Tyler Cox, Dell
# @version: 1.0.0
# ******************************************************************************/

import unittest
from domain.meta import response


class ResponseTest(unittest.TestCase):

    TEST_CODE = "200"
    TEST_DECRIPTION = "ok"
    TEST_VALUE1 = "temperature"
    TEST_VALUE2 = "humidity"

    def setUp(self):
        exp_values = []
        exp_values.append(self.TEST_VALUE1)
        exp_values.append(self.TEST_VALUE2)
        self.response1 = response.Response(self.TEST_CODE, self.TEST_DECRIPTION, exp_values)

    def test_add_expected_value(self):
        self.response1.add_expected_value("moisture")
        self.assertEqual(3, len(self.response1.expectedValues),
                         "Expected values list was not appended to appropriately")

    def test_remove_expected_value(self):
        self.response1.remove_expected_value(self.TEST_VALUE1)
        self.assertEqual(1, len(self.response1.expectedValues),
                         "Expected value was not removed from list appropriately")

if __name__ == "__main__":
    unittest.main()
