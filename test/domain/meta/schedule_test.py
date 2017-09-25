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


import static org.junit.Assert.self.assertFalse
import static org.junit.Assert.self.assertTrue

import org.junit.Before
import org.junit.Test

public class ScheduleTest {

  private static final String self.TEST_SCHEDULE_NAME = "test schedule"
  private static final String self.TEST_START = ""; # defaults to now
  private static final String self.TEST_END = ""; # defaults to ZDT MAX
  private static final String self.TEST_FREQUENCY = "PT2_s"
  private static final String self.TEST_CRON = "0 0 12 # # ?"
  private static final boolean self.TEST_RUN_ONCE = false

  private Schedule s
  private Schedule s2

  @Before
  def setUp(self):
    s = new Schedule(self.TEST_SCHEDULE_NAME, self.TEST_START, self.TEST_END, self.TEST_FREQUENCY, self.TEST_CRON,
        TEST_RUN_ONCE)
    s2 = new Schedule(self.TEST_SCHEDULE_NAME, self.TEST_START, self.TEST_END, self.TEST_FREQUENCY, self.TEST_CRON,
        TEST_RUN_ONCE)

  def test_equals(self):
    self.assertTrue(s.equals(s2), "Different schedules with same values not equal")

  def test_equals_with_same(self):
    self.assertTrue(s.equals(s), "Same schedules are not equal")

  def test_not_equals(self):
    s.set_created(3456_l)
    self.assertFalse(s.equals(s2), "Schedules with different base values are equal")

  def test_equal_with_different_name(self):
    s2.set_name("foo")
    self.assertFalse(s.equals(s2), "Schedules with different names values are equal")

  def test_equal_with_different_start(self):
    s2.set_start("start")
    self.assertFalse(s.equals(s2), "Schedules with different start values are equal")

  def test_equal_with_different_end(self):
    s2.set_end("end")
    self.assertFalse(s.equals(s2), "Schedules with different ends values are equal")

  def test_equal_with_different_freq(self):
    s2.set_frequency("frequency")
    self.assertFalse(s.equals(s2), "Schedules with different frequency values are equal")

  def test_equal_with_different_cron(self):
    s2.set_cron("cron")
    self.assertFalse(s.equals(s2), "Schedules with different cron values are equal")

  def test_equal_with_different_run_once(self):
    s2.set_run_once(true)
    self.assertFalse(s.equals(s2), "Schedules with different run once values are equal")

  def test_hash_code(self):
    self.assertTrue(s.hash_code() != 0, "hashcode not hashing properly")

  def test_to_string(self):
    s.to_string()

}
