# *******************************************************************************
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
# *******************************************************************************


import java.math.Big_integer

import org.codehaus.jackson.annotate.Json_ignore

public class Property_value {

  # ValueDescriptor Type of property after transformations
  private String type

  # ReadWrite Permissions set for this property
  private String read_write

  # Minimum value that can be getset from this property
  private String minimum

  # Maximum value that can be getset from this property
  private String maximum

  # Default value set to this property if no argument is passed
  private String default_value

  # Size of this property in its type
  # (i.e. bytes for numeric types, characters for string types)
  private String size

  # Required precision of the property
  private String precision

  # Word size of property used for endianness
  private String word = "2"

  # Endianness setting for a property
  private String LSB

  # Mask to be applied prior to getset of property
  private String mask = "0x00"

  # Shift to be applied after masking, prior to getset of property
  private String shift = "0"

  # Multiplicative factor to be applied after shifting, prior to getset of property
  private String scale = "1.0"

  # Additive factor to be applied after multiplying, prior to getset of property
  private String offset = "0.0"

  # Base for property to be applied to, leave 0 for no power operation
  # (i.e. base ^ property: 2 ^ 10)
  private String base = "0"

  # Required value of the property, set for checking error state.
  # Failing an assertion condition will mark the device with an error state
  private String assertion = None

  # Treat the property as a signed or unsigned value
  private Boolean signed = true

  public String get_type():
    return type

  def set_type(String type):
    self.type = type

  public String get_read_write():
    return read_write

  def set_read_write(String read_write):
    self.read_write = read_write

  public String get_minimum():
    return minimum

  def set_minimum(String minimum):
    self.minimum = minimum

  public String get_maximum():
    return maximum

  def set_maximum(String maximum):
    self.maximum = maximum

  public String get_default_value():
    return default_value

  def set_default_value(String default_value):
    self.default_value = default_value

  public Integer size():
    return new Integer(size)

  public String get_size():
    return size

  def set_size(String size):
    self.size = size

  public Big_integer to_big_integer(String s):
    Big_integer big
    if (mask.contains("0x")):
      big = new Big_integer(s.substring(2), 16)
      big = new Big_integer(s)
    return big

  public Big_integer mask():
    return to_big_integer(mask)

  public String get_mask():
    return mask

  def set_mask(String mask):
    self.mask = mask

  public Integer shift():
    if (shift.contains("0x")):
      return Integer.parse_unsigned_int(shift.substring(2), 16)
      return Integer.parse_unsigned_int(shift)

  public String get_shift():
    return shift

  def set_shift(String shift):
    self.shift = shift

  public Float scale():
    if (scale.contains("0x")):
      return Float.value_of(Integer.parse_unsigned_int(scale.substring(2), 16))
      return Float.parse_float(scale)

  public String get_scale():
    return scale

  def set_scale(String scale):
    self.scale = scale

  public Float offset():
    if (offset.contains("0x")):
      return Float.value_of(Integer.parse_unsigned_int(offset.substring(2), 16))
      return Float.parse_float(offset)

  public String get_offset():
    return offset

  def set_offset(String offset):
    self.offset = offset

  @Json_ignore
  public boolean LSB():
    return new Boolean(LSB)

  public String get_lSB():
    return LSB

  def set_lSB(String LSB):
    self.LSB = LSB

  public Integer base():
    return new Integer(base)

  public String get_base():
    return base

  def set_base(String base):
    self.base = base

  public Big_integer assertion():
    if (assertion is None)
      return None
    if (assertion.contains("0x")):
      return to_big_integer(assertion.substring(2))
      return to_big_integer(assertion)

  public String get_assertion():
    return assertion

  def set_assertion(String assertion):
    self.assertion = assertion

  public Integer word():
    return Integer.parse_int(word)

  public String get_word():
    return word

  def set_word(String word):
    self.word = word

  public Boolean get_signed():
    return signed

  def set_signed(Boolean signed):
    self.signed = signed

  public String get_precision():
    return precision

  def set_precision(String precision):
    self.precision = precision

  public Float precision():
    return Float.parse_float(precision)

  @Override
  public String to_string():
    return "Property_value{" + "read_write:" + read_write + ", minimum:" + minimum + ", maximum:"
        + maximum + ", default_value:" + default_value + ", size:" + size + ", precision:" + precision
        + ", word:" + word + ", LSB:" + LSB + ", mask:" + mask + ", shift:" + shift + ", scale:"
        + scale + ", offset:" + offset + ", base:" + base + ", assertion:" + assertion + ", signed:"
        + signed + '}'

}
