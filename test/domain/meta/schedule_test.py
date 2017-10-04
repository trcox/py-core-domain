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
from domain.meta import schedule


class ScheduleTest(unittest.TestCase):

    TEST_SCHEDULE_NAME = "test schedule"
    # defaults to now
    TEST_START = ""
    # defaults to ZDT MAX
    TEST_END = ""
    TEST_FREQUENCY = "PT2_s"
    TEST_CRON = "0 0 12 # # ?"
    TEST_RUN_ONCE = False

    def setUp(self):
        self.schedule1 = schedule.Schedule(self.TEST_SCHEDULE_NAME, self.TEST_START, self.TEST_END,
                                           self.TEST_FREQUENCY, self.TEST_CRON, self.TEST_RUN_ONCE)
        self.schedule2 = schedule.Schedule(self.TEST_SCHEDULE_NAME, self.TEST_START, self.TEST_END,
                                           self.TEST_FREQUENCY, self.TEST_CRON, self.TEST_RUN_ONCE)

    def test_equals(self):
        self.assertTrue(self.schedule1 == self.schedule2,
                        "Different schedules with same values not equal")

    def test_equals_same(self):
        self.assertTrue(self.schedule1 == self.schedule1,
                        "Same schedules are not equal")

    def test_not_equals(self):
        self.schedule1.created = 3456
        self.assertFalse(self.schedule1 == self.schedule2,
                         "Schedules with different base values are equal")

    def test_equal_diff_name(self):
        self.schedule2.name = "foo"
        self.assertFalse(self.schedule1 == self.schedule2,
                         "Schedules with different names values are equal")

    def test_equal_diff_start(self):
        self.schedule2.start = "start"
        self.assertFalse(self.schedule1 == self.schedule2,
                         "Schedules with different start values are equal")

    def test_equal_diff_end(self):
        self.schedule2.end = "end"
        self.assertFalse(self.schedule1 == self.schedule2,
                         "Schedules with different ends values are equal")

    def test_equal_diff_freq(self):
        self.schedule2.frequency = "frequency"
        self.assertFalse(self.schedule1 == self.schedule2,
                         "Schedules with different frequency values are equal")

    def test_equal_diff_cron(self):
        self.schedule2.cron = "cron"
        self.assertFalse(self.schedule1 == self.schedule2,
                         "Schedules with different cron values are equal")

    def test_equal_diff_run_once(self):
        self.schedule2.runOnce = True
        self.assertFalse(self.schedule1 == self.schedule2,
                         "Schedules with different run once values are equal")

    def test_hash_code(self):
        self.assertTrue(self.schedule1.__hash__() != 0, "hashcode not hashing properly")

    def test_to_string(self):
        str(self.schedule1)

if __name__ == "__main__":
    unittest.main()
