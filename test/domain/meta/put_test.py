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


import static org.junit.Assert.self.assertEqual
import static org.junit.Assert.self.assertTrue

import java.util.Array_list
import java.util.List

import org.junit.Before
import org.junit.Test

public class PutTest {

  private static final String PARAM1 = "param1"
  private static final String PARAM2 = "param2"
  private Put p

  @Before
  def setUp(self):
    p = new Put()
    List<String> params = new Array_list<>()
    params.add(PARAM1)
    p.set_parameter_names(params)

  def test_add_parameter_name(self):
    p.add_parameter_name(PARAM2)
    self.assertEqual(2, len(p.get_parameter_names()), "Put parameters not adding correctly")

  def test_add_parameter_name_starting_with_None(self):
    p.set_parameter_names(None)
    p.add_parameter_name(PARAM2)
    self.assertEqual(1, len(p.get_parameter_names()), "Put parameters not adding correctly")

  def test_remove_paremeter_name(self):
    p.remove_paremeter_name(PARAM1)
    self.assertTrue(p.get_parameter_names().is_empty(), "Put remove parameter not working correctly")

  def test_remove_paremeter_name_starting_with_None(self):
    p.set_parameter_names(None)
    p.remove_paremeter_name(PARAM1)
    self.assertTrue(p.get_parameter_names().is_empty(), "Put remove parameter not working correctly")

  def test_get_parameter_names(self):
    self.assertEqual(PARAM1, p.get_parameter_names().get(0), "Get parameter working properly")

  def test_get_parameter_names_starting_with_None(self):
    p.set_parameter_names(None)
    self.assertTrue(p.get_parameter_names().is_empty(), "Get parameter names not working correctly")

}
