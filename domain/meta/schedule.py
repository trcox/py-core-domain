#*******************************************************************************
# Copyright 2017 Dell Inc.
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
# @microservice: py-core-domain library
# @author: Tyler Cox, Dell
# @version: 1.0.0
#*******************************************************************************


import org.apache.commons.lang3.builder.Hash_code_builder
from domain.common import BaseObject
import org.springframework.data.mongodb.core.index.Indexed
import org.springframework.data.mongodb.core.mapping.Document


@Document
@Suppress_warnings("serial")
public class Schedule extends BaseObject {

  # TODO - make protected after changes to test package
  public static final String[] DATETIME_FORMATS = {"yyyy_mMdd'T'HHmmss"}

  # non-database identifier for a schedule- must be unique
  @Indexed(unique = true)
  private String name

  # Start time in ISO 8601 format YYYYMMDD'T'HHmmss
  # @Json_format(shape = Json_format.Shape.STRING, pattern = "yyyymmdd'T'HHmmss")
  private String start

  # Start time in ISO 8601 format YYYYMMDD'T'HHmmss
  # @Json_format(shape = Json_format.Shape.STRING, pattern = "yyyymmdd'T'HHmmss")
  private String end

  # how frequently should the event occur
  private String frequency

  # cron styled regular expression indicating how often the action under schedule should occur. Use
  # either run_once, frequency or cron and not all.
  private String cron

  # boolean indicating that this schedules runs one time - at the time indicated by the start
  private boolean run_once

  public Schedule(String name, String start, String end, String frequency, String cron,
      boolean run_once):
    super()
    self.name = name
    self.start = start
    self.end = end
    self.frequency = frequency
    self.cron = cron
    self.run_once = run_once

  @Suppress_warnings("unused")
  # used by spring container
  private Schedule():}

  public String get_name():
    return name

  def set_name(String name):
    self.name = name

  public String get_start():
    return start

  def set_start(String start):
    self.start = start

  public String get_end():
    return end

  def set_end(String end):
    self.end = end

  public String get_frequency():
    return frequency

  def set_frequency(String frequency):
    self.frequency = frequency

  public String get_cron():
    return cron

  def set_cron(String cron):
    self.cron = cron

  public boolean get_run_once():
    return run_once

  def set_run_once(boolean run_once):
    self.run_once = run_once

  @Override
  public String to_string():
    return "Schedule [name=" + name + ", start=" + start + ", end=" + end + ", frequency="
        + frequency + ", cron=" + cron + ", run_once=" + run_once + ", to_string()=" + super.to_string()
        + "]"

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(name).append(start)
        .append(end).append(frequency).append(cron).append(run_once).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Schedule other = (Schedule) obj
    return property_match(other)

  private boolean property_match(Schedule other):
    if (!string_property_match(name, other.name))
      return false
    if (!string_property_match(start, other.start))
      return false
    if (!string_property_match(end, other.end))
      return false
    if (!string_property_match(frequency, other.frequency))
      return false
    if (!string_property_match(cron, other.cron))
      return false
    return (run_once == other.run_once)

}
