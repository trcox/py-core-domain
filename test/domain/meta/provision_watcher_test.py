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
import static org.junit.Assert.self.assertFalse
import static org.junit.Assert.self.assertTrue

import java.util.Hash_map
import java.util.Map

import org.junit.Before
import org.junit.Test

public class Provision_watcherTest {

  private static final String self.TEST_NAME = "test pw"

  private Provision_watcher w
  private Provision_watcher w2

  @Before
  def setUp(self):
    Map<String, String> ids = new Hash_map<>()
    ids.put("z", "y")
    Device_profile p = new Device_profile()
    Device_service s = new Device_service()
    w = new Provision_watcher(self.TEST_NAME)
    w.set_identifiers(ids)
    w.set_profile(p)
    w.set_service(s)
    w.set_operating_state(Operating_state.ENABLED)
    w2 = new Provision_watcher(self.TEST_NAME)
    w2.set_identifiers(ids)
    w2.set_profile(p)
    w2.set_service(s)
    w2.set_operating_state(Operating_state.ENABLED)


  def test_add_identifier_starting_with_None(self):
    w.set_identifiers(None)
    w.add_identifier("a", "b")
    self.assertEqual("Provision_watcher identifers not added correctly", "b",
        w.get_identifiers().get("a"))

  def test_add_identifier(self):
    w.add_identifier("a", "b")
    self.assertEqual("Provision_watcher identifers not added correctly", "b",
        w.get_identifiers().get("a"))

  def test_remove_identifier_starting_with_None(self):
    w.set_identifiers(None)
    w.remove_identifier("z")
    self.assertTrue("Provision_watcher remove identifier not working properly",
        w.get_identifiers().is_empty())

  def test_remove_identifier(self):
    w.remove_identifier("z")
    self.assertTrue("Provision_watcher remove identifier not working properly",
        w.get_identifiers().is_empty())

  def test_equals(self):
    self.assertTrue(w.equals(w2), "Different watchers with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(w.equals(w), "Same watcher are not equal")

  def test_not_equals(self):
    w2.set_created(3456_l)
    self.assertFalse(w.equals(w2), "Watchers with different base values are equal")

  def test_equal_with_different_name(self):
    w2.set_name("foo")
    self.assertFalse(w.equals(w2), "Watchers with different names values are equal")

  def test_equal_with_different_identifiers(self):
    Map<String, String> ids = new Hash_map<>()
    ids.put("a", "b")
    w2.set_identifiers(ids)
    self.assertFalse(w.equals(w2), "Watchers with different identifer values are equal")

  def test_equal_with_different_profiles(self):
    Device_profile p = new Device_profile()
    p.set_name("foo")
    w2.set_profile(p)
    self.assertFalse(w.equals(w2), "Watchers with different profiles are equal")

  def test_equal_with_different_services(self):
    Device_service s = new Device_service()
    s.set_name("foo")
    w2.set_service(s)
    self.assertFalse(w.equals(w2), "Watchers with different services are equal")

  def test_equal_with_different_op_state(self):
    w2.set_operating_state(Operating_state.DISABLED)
    self.assertFalse(w.equals(w2), "Watchers with different op states are equal")

  def test_hash_code(self):
    self.assertTrue(w.hash_code() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    w.to_string()

}
