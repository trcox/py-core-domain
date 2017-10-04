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
from domain.meta import addressable
from domain.meta import protocol
from domain.meta import schedule_event



class ScheduleEventTest(unittest.TestCase):

    TEST_SERVICE_NAME = "test service"
    TEST_SCHEDULE_EVENT_NAME = "test schedule event"
    TEST_SCHEDULE_NAME = "test schedule"
    TEST_PARAMS = "{key1:value1}"
    TEST_ADDR_NAME = "TEST_ADDR.NAME"
    TEST_PROTOCOL = protocol.Protocol.HTTP
    TEST_ADDRESS = "localhost"
    TEST_PORT = 48089
    TEST_PATH = "/api/v1/device"

    def setUp(self):
        self.addressable1 = addressable.Addressable(self.TEST_ADDR_NAME, self.TEST_PROTOCOL,
                                                    self.TEST_ADDRESS, self.TEST_PATH,
                                                    self.TEST_PORT)
        self.schedule_event1 = schedule_event.ScheduleEvent(self.TEST_SCHEDULE_EVENT_NAME,
                                                            self.addressable1, self.TEST_PARAMS,
                                                            self.TEST_SCHEDULE_NAME,
                                                            self.TEST_SERVICE_NAME)
        self.schedule_event2 = schedule_event.ScheduleEvent(self.TEST_SCHEDULE_EVENT_NAME,
                                                            self.addressable1, self.TEST_PARAMS,
                                                            self.TEST_SCHEDULE_NAME,
                                                            self.TEST_SERVICE_NAME)

    def test_equals(self):
        self.assertTrue(self.schedule_event1 == self.schedule_event2,
                        "Different schedule events with same values not equal")

    def test_equals_same(self):
        self.assertTrue(self.schedule_event1 == self.schedule_event1,
                        "Same schedule events are not equal")

    def test_not_equals(self):
        self.schedule_event1.created = 3456
        self.assertFalse(self.schedule_event1 == self.schedule_event2,
                         "Schedule Events with different base values are equal")

    def test_equal_diff_name(self):
        self.schedule_event2.name = "foo"
        self.assertFalse(self.schedule_event1 == self.schedule_event2,
                         "Schedule Events with different names values are equal")

    def test_equal_diff_addressable(self):
        addressable2 = addressable.Addressable(self.TEST_PROTOCOL, self.TEST_ADDRESS,
                                               self.TEST_PATH, self.TEST_PORT, "foo")
        self.schedule_event2.addressable = addressable2
        self.assertFalse(self.schedule_event1 == self.schedule_event2,
                         "Schedule Events with different addressable are equal")

    def test_equal_diff_params(self):
        self.schedule_event2.parameters = "foo"
        self.assertFalse(self.schedule_event1 == self.schedule_event2,
                         "Schedule Events with different parameter values are equal")

    def test_equal_diff_service(self):
        self.schedule_event2.service = "foo"
        self.assertFalse(self.schedule_event1 == self.schedule_event2,
                         "Schedule Events with different service are equal")

    def test_equal_diff_schedule(self):
        self.schedule_event2.schedule = "foo"
        self.assertFalse(self.schedule_event1 == self.schedule_event2,
                         "Schedule Events with different schedule are equal")

    def test_hash_code(self):
        self.assertTrue(self.schedule_event1.__hash__() != 0, "hashcode not hashing properly")

    def test_to_string(self):
        str(self.schedule_event1)

if __name__ == "__main__":
    unittest.main()
