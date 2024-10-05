from number import Number


class Number_system:

  CHARACTER = {
    "0": 0,  "1": 1,  "2": 2,  "3": 3,  "4": 4,  "5": 5,  "6": 6,  "7": 7,  "8": 8,  "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
    "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
    "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35, "a": 36, "b": 37, "c": 38, "d": 39,
    "e": 40, "f": 41, "g": 42, "h": 43, "i": 44, "j": 45, "k": 46, "l": 47, "m": 48, "n": 49,
    "o": 50, "p": 51, "q": 52, "r": 53, "s": 54, "t": 55, "u": 56, "v": 57, "w": 58, "x": 59,
    "y": 60, "z": 61}

  @staticmethod
  def get_key(value: int) -> str:
    for i in Number_system.CHARACTER:
      if Number_system.CHARACTER[i] == value:
        return i
    return None

  @staticmethod
  def number_system_dec(num: str, radix: int = 10) -> str:
    result = "0"
    index = len(num) - 1
    for i in num:
      result = str(int(result) + (Number_system.CHARACTER[i] * (radix ** index)))
      index -= 1
    return result

  @staticmethod
  def number_system_dec_number(number: Number) -> Number:
    result = Number_system.number_system_dec(number.num, number.radix)
    return Number(result, 10)

  @staticmethod
  def number_system(num: str, radix_num: int = 10, radix_result: int = 10) -> str:
    result = ""
    result_10 = int(Number_system.number_system_dec(num, radix_num))
    if radix_result == 10:
      return str(result_10)
    while result_10 + 1 > radix_result:
      result += Number_system.get_key(int(result_10 % radix_result))
      result_10 = int(result_10 / radix_result)
    if result_10 != 0:
      result += str(result_10)
    return result[::-1]

  @staticmethod
  def number_system_number(number: Number, radix_result: int = 10) -> Number:
    result = Number_system.number_system(number.num, number.radix, radix_result)
    return Number(result, radix_result)

  @staticmethod
  def binary_length(num: str, length: int = 8, dynamic: bool = False) -> str:
    if length <= 0:
      return ""
    new_length = length
    result = ""
    while dynamic and new_length < len(num):
      new_length += length
    for i in range(len(num), new_length):
      result += "0"
    return result + num

  @staticmethod
  def binary_length_number(number: Number, length: int = 8, dynamic: bool = False) -> Number:
    num = Number_system.number_system(number.num, number.radix, 2)
    return Number(Number_system.binary_length(num, length, dynamic), 2)

  @staticmethod
  def signed_abstract(num: str, radix: int = 10) -> str:
    binary = Number_system.binary_length(Number_system.number_system(num, radix, 2), dynamic=True)
    result = ""
    is_first = True
    binary_first_letter = "1" if binary[0] == "0" else "0"
    for i in binary:
      if is_first:
        result += binary_first_letter
        is_first = False
        continue
      result += i
    return result

  @staticmethod
  def signed_abstract_number(number: Number) -> Number:
    binary = Number_system.signed_abstract(number.num, number.radix)
    return Number(binary, 2)

  @staticmethod
  def signed_complement_1(num: str, radix: int = 10) -> str:
    binary = Number_system.binary_length(Number_system.number_system(num, radix, 2), dynamic=True)
    result = ""
    for i in binary:
      result += "1" if i == "0" else "0"
    return result

  @staticmethod
  def signed_complement_1_number(number: Number) -> Number:
    binary = Number_system.signed_complement_1(number.num, number.radix)
    return Number(binary, 2)

  @staticmethod
  def signed_complement_2(num: str, radix: int = 10) -> str:
    binary = Number_system.binary_length(Number_system.number_system(num, radix, 2), dynamic=True)
    binary = Number_system.signed_complement_1(binary, 2)[::-1]
    result = ""
    t = 1
    for i in binary:
      if i == "1" and t == 1:
        result += "0"
      elif i == "0" and t == 1:
        result += "1"
        t = 0
      elif i == "0" and t == 0:
        result += "0"
      elif i == "1" and t == 0:
        result += "1"
    return result[::-1]

  @staticmethod
  def signed_complement_2_number(number: Number) -> Number:
    binary = Number_system.signed_complement_2(number.num, number.radix)
    return Number(binary, 2)

  @staticmethod
  def redundant(redundant_num: str, num: str, radix_redundant_num: int = 10, radix_num: int = 10, radix_result: int = 10) -> str:
    if radix_redundant_num <= 0 or radix_num <= 0 or radix_result <= 0:
      return ""
    if radix_redundant_num != 10:
      redundant_num = str(int(Number_system.number_system_dec(redundant_num, radix_redundant_num)))
    if radix_num != 10:
      num = str(int(Number_system.number_system_dec(num, radix_num)))
    return Number_system.number_system(str(int(redundant_num) - int(num)), 10, radix_result)

  @staticmethod
  def redundant_number(redundant_number: Number, number: Number, radix_result: int = 10) -> Number:
    result = Number_system.redundant(redundant_number.num, number.num, redundant_number.radix, number.radix, radix_result)
    return Number(result, radix_result)

  @staticmethod
  def binary_addition(num_a: str, num_b: str, radix_a: int = 10, radix_b: int = 10) -> str:
    result = ""
    binary_a = Number_system.binary_length(Number_system.number_system(num_a, radix_a, 2), 1, True) if radix_a != 2 else num_a
    binary_b = Number_system.binary_length(Number_system.number_system(num_b, radix_b, 2), 1, True) if radix_b != 2 else num_b
    len_a = len(binary_a)
    len_b = len(binary_b)
    if len_a != len_b:
      if len_a > len_b:
        binary_b = Number_system.binary_length(binary_b, len_a)
        len_b = len_a
      else:
        binary_a = Number_system.binary_length(binary_a, len_b)
        len_a = len_b
    for i in range(len_a - 1, -1, -1):
      if binary_a[i] == "1":
        result += "0" if binary_b[i] == "1" else "1"
      else:
        result += "1" if binary_b[i] == "1" else "0"
    return result[::-1]

  @staticmethod
  def binary_addition_number(number_a: Number, number_b: Number) -> Number:
    result = Number_system.binary_addition(number_a.num, number_b.num, number_a.radix, number_b.radix)
    return Number(result, 2)

  @staticmethod
  def equal(num_a: str, num_b: str, radix_a: int = 10, radix_b: int = 10) -> bool:
    a = int(Number_system.number_system_dec(num_a, radix_a)) if radix_a != 10 else int(num_a)
    b = int(Number_system.number_system_dec(num_b, radix_b)) if radix_b != 10 else int(num_b)
    return True if a == b else False

  @staticmethod
  def equal_number(number_a: Number, number_b: Number) -> bool:
    return Number_system.equal(number_a.num, number_b.num, number_a.radix, number_b.radix)