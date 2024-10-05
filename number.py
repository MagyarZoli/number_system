class Number:

  def __init__(self, num: str, radix: int):
    self.num = num
    self.radix = radix

  def __str__(self):
    return f"Number(num={self.num}, radix={self.radix})"