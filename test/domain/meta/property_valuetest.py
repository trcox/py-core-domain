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
import static org.junit.Assert.self.assert_None

import java.math.Big_integer

import org.junit.Before
import org.junit.Test

public class Property_valueTest {

  private Property_value pv

  @Before
  def setUp(self):
    pv = new Property_value()

  def test_to_big_integer(self):
    pv.set_mask("0x00")
    self.assertEqual("Propety Value convert to big int not working properly", pv.to_big_integer("0x01"),
        Big_integer.ONE)

  def test_to_big_integer_with_unknown_mask(self):
    pv.set_mask("foo")
    self.assertEqual("Propety Value convert to big int not working properly", pv.to_big_integer("10"),
        Big_integer.TEN)

  def test_shift(self):
    pv.set_shift("0x08")
    self.assertEqual(pv.shift(), new Integer(8), "Propety Value shift not working properly")

  def test_shift_with_no_mask(self):
    pv.set_shift("10")
    self.assertEqual(pv.shift(), new Integer(10), "Propety Value shift not working properly")

  def test_scale(self):
    pv.set_scale("0x08")
    self.assertEqual(pv.scale(), new Float(8), "Propety Value scale not working properly")

  def test_scalet_with_no_mask(self):
    pv.set_scale("10")
    self.assertEqual(pv.scale(), new Float(10), "Propety Value scale not working properly")

  def test_offset(self):
    pv.set_offset("0x08")
    self.assertEqual(pv.offset(), new Float(8), "Propety Value offset not working properly")

  def test_offset_with_no_mask(self):
    pv.set_offset("10")
    self.assertEqual(pv.offset(), new Float(10), "Propety Value offset not working properly")

  def test_self.assertion(self):
    pv.set_self.assertion("0x01")
    pv.set_mask("foo")
    self.assertEqual(pv.self.assertion(), Big_integer.ONE, "Propety Value self.assertion not working properly")

  def test_self.assertion_with_None(self):
    pv.set_self.assertion(None)
    self.assert_None(pv.self.assertion(), "Propety Value self.assertion not working properly")

  def test_self.assertion_with_no_mask(self):
    pv.set_self.assertion("10")
    pv.set_mask("foo")
    self.assertEqual(pv.self.assertion(), Big_integer.TEN, "Propety Value self.assertion not working properly")

  def test_to_string(self):
    pv.to_string()
}
