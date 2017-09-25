#*******************************************************************************
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
# @author: Jim White, Dell
# @version: 1.0.0
#******************************************************************************/

import unittest

from domain.meta import Action, Response

class ActionTest(unittest.TestCase):

  TEST_CODE = "200"
  TEST_DECRIPTION = "ok"
  TEST_VALUE1 = "temperature"
  TEST_VALUE2 = "humidity"
  TEST_CODE2 = "404"
  TEST_DECRIPTION2 = "not found"

  def setUp(self):
    self.r1 = Response(self.TEST_CODE, self.TEST_DECRIPTION)
    self.r1.add_expected_value(self.TEST_VALUE1)
    self.r1.add_expected_value(self.TEST_VALUE2)
    self.r2 = Response(self.TEST_CODE2, self.TEST_DECRIPTION2)
    self.a1 = Action()
    self.responses = []
    self.responses.append(self.r1)
    self.responses.append(self.r2)
    self.a1.responses = self.responses

  def test_add_response(self):
    self.a1.add_response(Response("bar", "foo"))
    self.assertEqual(3, len(self.a1.responses), "Response not added to action correctly")

  def test_add_response_with_None_responses(self):
    self.a1.responses = None
    self.a1.add_response(Response("bar", "foo"))
    self.assertEqual(1, len(self.a1.responses), "Response not added to action correctly")

  def test_all_expected_values(self):
    values = self.a1.all_expected_values()
    self.assertEqual(len(values), 2, "Size of values does not match expected")
    self.assertTrue(self.TEST_VALUE1 in values, "expected values does not include value 1")
    self.assertTrue(self.TEST_VALUE2 in values, "expected values does not include value 2")

  def test_all_associated_value_descriptors(self):
    values = self.a1.all_associated_value_descriptors()
    self.assertEqual(len(values), 2, "Size of values does not match expected")
    self.assertTrue(self.TEST_VALUE1 in values, "expected values does not include value 1")
    self.assertTrue(self.TEST_VALUE2 in values, "expected values does not include value 2")

  def test_remove_response(self):
    self.a1.remove_response(self.r1)
    self.assertEqual(1, len(self.a1.responses), "Response was not removed from action correctly")

  def test_remove_response_with_None_responses(self):
    self.a1.responses = None
    self.a1.remove_response(self.r1)
    self.assertEqual(0, len(self.a1.responses), "Response was not removed from action correctly")

  def test_to_string(self):
    str(self.a1)