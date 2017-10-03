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


import static org.junit.Assert.self.assertEqual

import java.util.Array_list
import java.util.List

import org.junit.Before
import org.junit.Test

public class ResponseTest {

  private static final String self.TEST_CODE = "200"
  private static final String self.TEST_DECRIPTION = "ok"
  private static final String self.TEST_VALUE1 = "temperature"
  private static final String self.TEST_VALUE2 = "humidity"
  private Response r

  @Before
  def setUp(self):
    List<String> exp_values = new Array_list<>()
    exp_values.add(self.TEST_VALUE1)
    exp_values.add(self.TEST_VALUE2)
    r = new Response(self.TEST_CODE, self.TEST_DECRIPTION, exp_values)

  def test_add_expected_value(self):
    r.add_expected_value("moisture")
    self.assertEqual("Expected values list was not added to appropriately", 3,
        len(r.get_expected_values()))

  def test_remove_expected_value(self):
    r.remove_expected_value(self.TEST_VALUE1)
    self.assertEqual("Expected value was not removed from list appropriately", 1,
        len(r.get_expected_values()))

}
