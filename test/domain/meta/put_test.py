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
from domain.meta import put


class PutTest(unittest.TestCase):

    PARAM1 = "param1"
    PARAM2 = "param2"

    def setUp(self):
        self.put1 = put.Put()
        params = []
        params.append(self.PARAM1)
        self.put1.parameterNames = params

    def test_add_parameter_name(self):
        self.put1.add_parameterName(self.PARAM2)
        self.assertEqual(2, len(self.put1.parameterNames),
                         "Put parameters not adding correctly")

    def test_add_no_parameter_name(self):
        self.put1.parameterNames = None
        self.put1.add_parameterName(self.PARAM2)
        self.assertEqual(1, len(self.put1.parameterNames),
                         "Put parameters not adding correctly")

    def test_remove_parameter_name(self):
        self.put1.remove_parameterName(self.PARAM1)
        self.assertEqual([], self.put1.parameterNames,
                         "Put remove parameter not working correctly")

    def test_remove_no_parameter_name(self):
        self.put1.parameterNames = None
        self.put1.remove_parameterName(self.PARAM1)
        self.assertEqual([], self.put1.parameterNames,
                         "Put remove parameter not working correctly")

    def test_get_parameter_names(self):
        self.assertEqual(self.PARAM1, self.put1.parameterNames[0],
                         "Get parameter working properly")

    def test_get_no_parameter_names(self):
        self.put1.parameterNames = None
        self.assertEqual([], self.put1.parameterNames,
                         "Get parameter names not working correctly")

if __name__ == "__main__":
    unittest.main()
