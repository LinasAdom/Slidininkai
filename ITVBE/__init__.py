# ŽINGSNIS 1.1.
import check50

# ŽINGSNIS 1.2.
@check50.check()
def pradiniaiFailai():
# ŽINGSNIS 1.3.
    """C++ failas yra sėkmingai sukurtas."""
    check50.exists("slidininkai.cpp")

# ŽINGSNIS 2.1.
@check50.check(pradiniaiFailai)
def kompiliavimas():
# ŽINGSNIS 2.2.
    """slidininkai.cpp buvo sukompiliuotas sėkmingai!"""
    check50.run("g++     slidininkai.cpp  -lcrypt -lcs50 -lm -o slidininkai").exit(0) 

# ŽINGSNIS 3.1.
@check50.check(pradiniaiFailai)
def duomenuIvedimas():
    """Duomenų įvedimo failas paruoštas sėkmingai!"""
    check50.exists("Duomenys.txt")
    
# ŽINGSNIS 3.2.
@check50.check(pradiniaiFailai)
def duomenuIsvedimas():
     """Duomenų išvedimo failas paruoštas sėkmingai!"""
     check50.exists("Rezultatai.txt")

# ŽINGSNIS 4.1.
@check50.check(pradiniaiFailai)
def test0():
  """Duomenų įvedimo failo informacija surašyta teisingai."""
# ŽINGSNIS 4.2.
  ivestosEilutes = len(open("Duomenys.txt").readlines())
# ŽINGSNIS 4.3.
  pateiktosEilutes = 13
# ŽINGSNIS 4.4.
  if not ivestosEilutes:
    raise check50.Failure("Duomenų įvedime yra klaida. Patikrinkite Duomenys.txt")
# ŽINGSNIS 4.5.
  if ivestosEilutes != pateiktosEilutes:
   raise check50.Failure("Duomenų įvedime yra klaida. Patikrinkite Duomenys.txt")



# ŽINGSNIS 5.1.
@check50.check(pradiniaiFailai)
def test1():
  """Duomenų išvedimo failo informacija surašyta teisingai."""
  check50.run("./slidininkai")
# ŽINGSNIS 5.2.
  ivestosEilutes = len(open("Rezultatai.txt").readlines())
# ŽINGSNIS 5.3.
  pateiktosEilutes = 5
# ŽINGSNIS 5.4.
  if not ivestosEilutes:
    raise check50.Failure("Duomenų įvedime yra klaida. Patikrinkite Rezultatai.txt")
# ŽINGSNIS 5.5.
  if ivestosEilutes != pateiktosEilutes:
    raise check50.Failure("Duomenų išvedime yra klaida. Patikrinkite Rezultatai.txt")

# ŽINGSNIS 6.1.
@check50.check(pradiniaiFailai)
def pvz1():
  """Pateiktas pirmo pavyzdžio atsakymas yra pateiktas teisingai. Sveikinimai!"""
  check50.run("> Duomenys.txt")
  duomenys = open("Duomenys.txt", "w")
# ŽINGSNIS 6.2.
  Duom = ["6 \n", "Petras A. Petraitis 15 20 00 \n", "Jurgis Jurgutis 16 12 12 \n", "Rimas Jonas 15 15 59 \n", "Zigmas Nosis 16 23 9 \n", "Romas Senasis 15 15 15 \n", "Rytis Uosis Ainis 16 23 9 \n", "5 \n", "Zigmas Nosis 16 43 15 \n" , "Petras A. Petraitis 15 50 10 \n", "Romas Senasis 16 5 35 \n", "Rytis Uosis Ainis 16 55 59 \n", "Jurgis Jurgutis 16 42 22 \n"]
# ŽINGSNIS 6.3.
  duomenys.writelines(Duom)
  duomenys.close()
# ŽINGSNIS 6.4.
  check50.run("./slidininkai")
# ŽINGSNIS 6.5.
  with open("Rezultatai.txt") as m:
    rez = m.read().split()
# ŽINGSNIS 6.6.
  ats = ["Zigmas", "Nosis", "20", "6", "Jurgis", "Jurgutis", "30", "10", "Petras", "A.", "Petraitis", "30", "10", "Rytis", "Uosis", "Ainis", "32", "50", "Romas", "Senasis", "50", "20"]
# ŽINGSNIS 6.7.
  if ats == rez:
    pass
  else:
    raise check50.Mismatch(ats, rez)
