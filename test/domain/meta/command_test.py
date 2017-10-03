# *******************************************************************************
# Copyright 2016-2017 Dell Inself.command1.
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
from domain.meta import command
from domain.meta import get
from domain.meta import put
from domain.meta import response


class CommandTest(unittest.TestCase):

    TEST_NAME = "test_command_name"
    TEST_PATH = "/api/v1/device/{device_id}/temp"
    TEST_CODE = "200"
    TEST_DESCRIPTION = "ok"
    TEST_EXPECTED_VALUE1 = "temperature"
    TEST_EXPECTED_VALUE2 = "humidity"
    TEST_PARAM1 = "Temperature"
    TEST_PARAM2 = "Humidity"

    def setUp(self):
        expected = []
        expected.append(self.TEST_EXPECTED_VALUE1)
        expected.append(self.TEST_EXPECTED_VALUE2)
        response1 = response.Response(self.TEST_CODE, self.TEST_DESCRIPTION, expected)
        self.command1 = command.Command()
        self.command1.name = self.TEST_NAME
        get1 = get.Get()
        get1.path = self.TEST_PATH
        get1.add_response(response1)
        self.command1.get = get1
        put1 = put.Put()
        put1.path = self.TEST_PATH
        params = []
        params.append(self.TEST_PARAM1)
        params.append(self.TEST_PARAM2)
        put1.parameterNames = params
        self.command1.put = put1
        self.command2 = command.Command()
        self.command2.name = self.TEST_NAME
        self.command2.get = get1
        self.command2.put = put1

    def test_a_value_d_g_and_p(self):
        vds = self.command1.associated_value_descriptors()
        self.assertTrue(self.TEST_PARAM1 in vds,
                        "Command does not have put param value descriptors")
        self.assertTrue(self.TEST_PARAM2 in vds,
                        "Command does not have put param value descriptors")
        self.assertTrue(self.TEST_EXPECTED_VALUE1 in vds,
                        "Command does not have expected get value descriptors")
        self.assertTrue(self.TEST_EXPECTED_VALUE2 in vds,
                        "Command does not have expected get value descriptors")

    def test_a_value_d_no_g_no_p(self):
        self.command1.put = None
        self.command1.get = None
        vds = []
        self.assertEqual(self.command1.associated_value_descriptors(), vds,
                         "Command should not have value descriptors with no gets or puts")

    def test_a_value_d_no_get(self):
        self.command1.get = None
        vds = self.command1.associated_value_descriptors()
        self.assertTrue(self.TEST_PARAM1 in vds,
                        "Command does not have put param value descriptors")
        self.assertTrue(self.TEST_PARAM2 in vds,
                        "Command does not have put param value descriptors")

    def test_a_value_d_no_put(self):
        self.command1.put = None
        vds = self.command1.associated_value_descriptors()
        self.assertTrue(self.TEST_EXPECTED_VALUE1 in vds,
                        "Command does not have expected get value descriptors")
        self.assertTrue(self.TEST_EXPECTED_VALUE2 in vds,
                        "Command does not have expected get value descriptors")

    def test_equals(self):
        self.assertTrue(self.command1 == self.command2,
                        "Different command with same values not equal")

    def test_equals_same(self):
        self.assertTrue(self.command1 == self.command1, "Same commands are not equal")

    def test_not_equals(self):
        self.command1.created = 3456
        self.assertFalse(self.command1 == self.command2,
                         "Commands with different base values are equal")

    def test_equal_different_name(self):
        self.command2.name = "foo"
        self.assertFalse(self.command1 == self.command2,
                         "Commands with different names values are equal")

    def test_equal_different_gets(self):
        self.command2.get = None
        self.assertFalse(self.command1 == self.command2,
                         "Commands with different get values are equal")

    def test_equal_different_puts(self):
        self.command2.put = None
        self.assertFalse(self.command1 == self.command2,
                         "Commands with different put values are equal")

    def test_hash_code(self):
        self.assertTrue(self.command1.__hash__() != 0, "hashcode not hashing properly")

    def test_to_string(self):
        str(self.command1)

if __name__ == "__main__":
    unittest.main()
