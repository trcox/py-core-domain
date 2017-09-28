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
from domain.common import HTTPMethod
from domain.meta import Addressable, Protocol

class AddressableTest(unittest.TestCase):

  TEST_NAME = "test_addressable"
  TEST_HTTP_PROTOCOL = Protocol.HTTP
  TEST_MQTT_PROTOCOL = Protocol.TCP
  TEST_ADDR = "localhost"
  TEST_PATH = "/pathtosomething"
  TEST_PORT = 49888
  TEST_PUBLISHER = "test_publisher"
  TEST_TOPIC = "test_topic"
  TEST_USER = "fred"
  TEST_PASS = "password"
  TEST_METHOD = HTTPMethod.POST

  def setUp(self):
    self.a1 = Addressable(self.TEST_NAME, self.TEST_HTTP_PROTOCOL, self.TEST_ADDR, self.TEST_PORT, path=self.TEST_PATH, method=self.TEST_METHOD)
    self.a2 = Addressable(self.TEST_NAME, self.TEST_HTTP_PROTOCOL, self.TEST_ADDR, self.TEST_PORT, path=self.TEST_PATH, method=self.TEST_METHOD)
    self.a_for_mqtt = Addressable(self.TEST_NAME, self.TEST_MQTT_PROTOCOL, self.TEST_ADDR, self.TEST_PORT, self.TEST_PUBLISHER,
        self.TEST_USER, self.TEST_PASS, self.TEST_TOPIC, path=self.TEST_PATH)

  def test_get_base_url(self):
    self.assertEqual("%s://%s:%s" % (self.TEST_HTTP_PROTOCOL.name, self.TEST_ADDR, self.TEST_PORT), self.a1.get_base_url(), 
        "base url for addressable not correct")

  def test_get_url(self):
    self.assertEqual("%s://%s:%s%s" % (self.TEST_HTTP_PROTOCOL.name, self.TEST_ADDR, self.TEST_PORT, self.TEST_PATH), self.a1.get_url(), 
        "url for addressable not correct")

  def test_get_url_with_topic_and_publisher(self):
    self.assertEqual("%s://%s:%s%s" % (self.TEST_MQTT_PROTOCOL.name, self.TEST_ADDR, self.TEST_PORT, self.TEST_PATH), self.a_for_mqtt.get_url(), 
        "url for addressable not correct")

  def test_get_url_with_topic_and_no_publisher(self):
    self.a_for_mqtt.publisher = None
    self.assertEqual("%s://%s:%s%s/%s" % (self.TEST_MQTT_PROTOCOL.name, self.TEST_ADDR, self.TEST_PORT, self.TEST_TOPIC, self.TEST_PATH), 
        self.a_for_mqtt.get_url(), "url for addressable not correct")

  def test_get_url_with_no_topic_and_no_publisher(self):
    self.a_for_mqtt.publisher = None
    self.a_for_mqtt.topic = None
    self.assertEqual("%s://%s:%s%s" % (self.TEST_MQTT_PROTOCOL.name, self.TEST_ADDR, self.TEST_PORT, self.TEST_PATH), self.a_for_mqtt.get_url(), 
        "url for addressable not correct")

  def test_equals(self):
    self.assertTrue(self.a1 == self.a2, "Different addressable with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(self.a1 == self.a1, "Same addressable are not equal")

  def test_not_equals(self):
    self.a1.created = 3456
    self.assertFalse(self.a1 == self.a2, "Addressable with different base values are equal")

  def test_equal_with_different_name(self):
    self.a2.name = "foo"
    self.assertFalse(self.a1 == self.a2, "Addressable with different names values are equal")

  def test_equal_with_different_protocol(self):
    self.a2.protocol = Protocol.MAC
    self.assertFalse(self.a1 == self.a2, "Addressable with different protocol values are equal")

  def test_equal_with_different_address(self):
    self.a2.address = "different_address"
    self.assertFalse(self.a1 == self.a2, "Addressable with different address values are equal")

  def test_equal_with_different_port(self):
    self.a2.port = 99
    self.assertFalse(self.a1 == self.a2, "Addressable with different port values are equal")

  def test_equal_with_different_publisher(self):
    self.a2.publisher = "new_pub"
    self.assertFalse(self.a1 == self.a2, "Addressable with different publisher values are equal")

  def test_equal_with_different_user(self):
    self.a2.user = "newuser"
    self.assertFalse(self.a1 == self.a2, "Addressable with different user values are equal")

  def test_equal_with_different_password(self):
    self.a2.password = "new_pass"
    self.assertFalse(self.a1 == self.a2, "Addressable with different password values are equal")

  def test_equal_with_different_topic(self):
    self.a2.topic = "new_topic"
    self.assertFalse(self.a1 == self.a2, "Addressable with different topic values are equal")

  def test_hash_code(self):
    self.assertTrue(self.a1.__hash__() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    str(self.a1)

if __name__ == "__main__":
  unittest.main()
