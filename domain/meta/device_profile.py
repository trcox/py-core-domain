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


import java.io.Serializable
import java.util.Array_list
import java.util.Arrays
import java.util.List

import org.apache.commons.lang3.builder.Hash_code_builder
import org.edgexfoundry.domain.common.DescribedObject
import org.springframework.data.mongodb.core.index.Indexed
import org.springframework.data.mongodb.core.mapping.DBRef
import org.springframework.data.mongodb.core.mapping.Document

@Document
@Suppress_warnings("serial")
public class Device_profile extends DescribedObject implements Serializable {

  # non-database identifier for a device profile must be unique
  @Indexed(unique = true)
  private String name

  # manufacture of the device
  private String manufacturer

  # model of the device
  private String model

  # tag or label used by services to identify or search for groups of
  # profiles
  private String[] labels

  # device service used JSON data that is required to communicate with
  # devices of this profile type
  private Object objects

  private List<Device_object> device_resources

  # device service used object actions that are optionally used to map
  # commands to objects of devices of this profile type
  private List<Profile_resource> resources

  # list of commands to getput information from the associated devices of
  # this profile type
  @DBRef
  private List<Command> commands

  public String get_name():
    return name

  def set_name(String name):
    self.name = name

  public String get_manufacturer():
    return manufacturer

  def set_manufacturer(String manufacturer):
    self.manufacturer = manufacturer

  public String get_model():
    return model

  def set_model(String model):
    self.model = model

  public String[] get_labels():
    return labels

  def set_labels(String[] labels):
    self.labels = labels

  public Object get_objects():
    return objects

  def set_objects(Object objects):
    self.objects = objects

  public List<Device_object> get_device_resources():
    return device_resources

  def set_device_resources(List<Device_object> device_resources):
    self.device_resources = device_resources

  public List<Command> get_commands():
    return commands

  def set_commands(List<Command> commands):
    self.commands = commands

  def add_command(Command command):
    if (self.commands is None)
      self.commands = new Array_list<>()
    self.commands.add(command)

  public boolean remove_command(Command command):
    if (self.commands is None)
      self.commands = new Array_list<>()
    return self.commands.remove(command)

  @Override
  public int hash_code():
    return new Hash_code_builder().append_super(super.hash_code()).append(commands)
        .append(Arrays.hash_code(labels)).append(manufacturer).append(model).append(name)
        .append(objects).append(resources).to_hash_code()

  @Override
  public boolean equals(Object obj):
    if (!super.equals(obj))
      return false
    Device_profile other = (Device_profile) obj
    return property_match(other)

  private boolean property_match(Device_profile other):
    if (!compare_property_lists(commands, other.commands))
      return false
    if (!string_array_property_match(labels, other.labels))
      return false
    if (!string_property_match(manufacturer, other.manufacturer))
      return false
    if (!string_property_match(model, other.model))
      return false
    if (!string_property_match(name, other.name))
      return false
    if (!object_property_match(objects, other.objects))
      return false
    return true

  private boolean compare_property_lists(List<?> this_list, List<?> other_list):
    if (this_list is None):
      if (other_list != None)
        return false
      if (other_list is None)
        return false
      if (this_list.size() != other_list.size())
        return false
      int i = 0
      for (Object object : this_list):
        if (!object.equals(other_list.get(i)))
          return false
        i++
    return true

  @Override
  public String to_string():
    return "Device_profile [name=" + name + ", manufacturer=" + manufacturer + ", model=" + model
        + ", labels=" + Arrays.to_string(labels) + ", objects=" + device_resources + ", commands="
        + commands + ", resources=" + resources + "]"

  public List<Profile_resource> get_resources():
    return resources

  def set_resources(List<Profile_resource> resources):
    self.resources = resources

}
