from num_system import Number_system as Ns
from number import Number


def ket_szam_osszehasonlito():
  """
  Két számot hasonlít össze,
  ha egyenlőek akkor igaz értéket ad vissza.
  """
  # itt tudod beállítani melyik legyen az a két szám,
  # amit összeszeretnél hasonlítani.
  # num = a szám str típusban
  # radix = milyen számrendszerben adtad meg a számot
  a = Number(num="45", radix=10)
  b = Number(num="55", radix=8)
  # itt kapod vissza az eredményt.
  print(f"{Ns.equal_number(a, b)}")


def elojeles_abrazolasok():
  """
  Egy megadott szám, egy megadott számrendszerben (radix)
  kiszámolja:
    - bináris számot
    - előjeles absztrakt értékét
    - előjeles 1-es komplemens értékét
    - előjeles 2-es komplemens értékét
    - n-többletes értékét
  """
  # a szám aminek az előjeles ábrázolásait kiszámolja.
  a = Number(num="45", radix=10)
  # többletes szám
  tobblet = 128
  # itt kapod vissza az eredményeket
  binary = Ns.binary_length_number(Ns.number_system_number(a, 2))
  print(f"szám = {a}")
  print(f"bináris szám = {binary}")
  print(f"előjeles absztrakt értéke = {Ns.signed_abstract_number(binary)}")
  print(f"előjeles 1-es komplemens érétke = {Ns.signed_complement_1_number(binary)}")
  print(f"előjeles 2-es komplemens értéke = {Ns.signed_complement_2_number(binary)}")
  print(f"{tobblet}-többletes értéke = {Ns.binary_length_number(Ns.redundant_number(Number(str(tobblet), 10), binary, 2))}")


if __name__ == "__main__":
  ket_szam_osszehasonlito()
  print()
  elojeles_abrazolasok()