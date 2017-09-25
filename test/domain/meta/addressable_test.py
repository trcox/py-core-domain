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

import org.edgexfoundry.domain.common.HTTPMethod
import org.junit.Before
import org.junit.Test

@Suppress_warnings("deprecation")
public class AddressableTest {

  private static final String self.TEST_NAME = "test_addressable"
  private static final Protocol self.TEST_HTTP_PROTOCOL = Protocol.HTTP
  private static final Protocol self.TEST_MQTT_PROTOCOL = Protocol.TCP
  private static final String self.TEST_ADDR = "localhost"
  private static final String self.TEST_PATH = "/pathtosomething"
  private static final int self.TEST_PORT = 49888
  private static final String self.TEST_PUBLISHER = "test_publisher"
  private static final String self.TEST_TOPIC = "test_topic"
  private static final String self.TEST_USER = "fred"
  private static final String self.TEST_PASS = "password"
  private static final HTTPMethod self.TEST_METHOD = HTTPMethod.POST

  private Addressable a, a2
  private Addressable a_for_mQTT

  @Before
  def setUp(self):
    a = new Addressable(self.TEST_NAME, self.TEST_HTTP_PROTOCOL, self.TEST_ADDR, self.TEST_PATH, self.TEST_PORT)
    a.set_method(self.TEST_METHOD)
    a2 = new Addressable(self.TEST_NAME, self.TEST_HTTP_PROTOCOL, self.TEST_ADDR, self.TEST_PATH, self.TEST_PORT)
    a2.set_method(self.TEST_METHOD)
    a_for_mQTT = new Addressable(self.TEST_NAME, self.TEST_MQTT_PROTOCOL, self.TEST_ADDR, self.TEST_PORT, self.TEST_PUBLISHER,
        TEST_USER, self.TEST_PASS, self.TEST_TOPIC)
    a_for_mQTT.set_path(self.TEST_PATH)

  def test_get_base_uRL(self):
    self.assertEqual("base url for addressable not correct",
        TEST_HTTP_PROTOCOL + ":#" + self.TEST_ADDR + ":" + self.TEST_PORT, a.get_base_uRL())

  def test_get_uRL(self):
    self.assertEqual("url for addressable not correct",
        TEST_HTTP_PROTOCOL + ":#" + self.TEST_ADDR + ":" + self.TEST_PORT + self.TEST_PATH, a.get_uRL())

  def test_get_uRLWith_topic_and_publisher(self):
    self.assertEqual("url for addressable not correct",
        TEST_MQTT_PROTOCOL + ":#" + self.TEST_ADDR + ":" + self.TEST_PORT + self.TEST_PATH, a_for_mQTT.get_uRL())

  def test_get_uRLWith_topic_and_no_publisher(self):
    a_for_mQTT.set_publisher(None)
    self.assertEqual("url for addressable not correct",
        TEST_MQTT_PROTOCOL + ":#" + self.TEST_ADDR + ":" + self.TEST_PORT + self.TEST_TOPIC + "/" + self.TEST_PATH,
        a_for_mQTT.get_uRL())

  def test_get_uRLWith_no_topic_and_no_publisher(self):
    a_for_mQTT.set_publisher(None)
    a_for_mQTT.set_topic(None)
    self.assertEqual("url for addressable not correct",
        TEST_MQTT_PROTOCOL + ":#" + self.TEST_ADDR + ":" + self.TEST_PORT + self.TEST_PATH, a_for_mQTT.get_uRL())

  def test_equals(self):
    self.assertTrue(a.equals(a2), "Different addressable with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(a.equals(a), "Same addressable are not equal")

  def test_not_equals(self):
    a.set_created(3456_l)
    self.assertFalse(a.equals(a2), "Addressable with different base values are equal")

  def test_equal_with_different_name(self):
    a2.set_name("foo")
    self.assertFalse(a.equals(a2), "Addressable with different names values are equal")

  def test_equal_with_different_protocol(self):
    a2.set_protocol(Protocol.MAC)
    self.assertFalse(a.equals(a2), "Addressable with different protocol values are equal")

  def test_equal_with_different_address(self):
    a2.set_address("different_address")
    self.assertFalse(a.equals(a2), "Addressable with different address values are equal")

  def test_equal_with_different_port(self):
    a2.set_port(99)
    self.assertFalse(a.equals(a2), "Addressable with different port values are equal")

  def test_equal_with_different_publisher(self):
    a2.set_publisher("new_pub")
    self.assertFalse(a.equals(a2), "Addressable with different publisher values are equal")

  def test_equal_with_different_user(self):
    a2.set_user("newuser")
    self.assertFalse(a.equals(a2), "Addressable with different user values are equal")

  def test_equal_with_different_password(self):
    a2.set_password("new_pass")
    self.assertFalse(a.equals(a2), "Addressable with different password values are equal")

  def test_equal_with_different_topic(self):
    a2.set_topic("new_topic")
    self.assertFalse(a.equals(a2), "Addressable with different topic values are equal")

  def test_hash_code(self):
    self.assertTrue(a.hash_code() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    a.to_string()

}
