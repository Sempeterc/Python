dnk = open("dnk.txt", "r").read()
print dnk

dnk1 = dnk.find("CCAGCAATCGC")
dnk2 = dnk.find("GCCAGTGCCG")
dnk3 = dnk.find("TTAGCTATCGC")
dnk4 = dnk.find("GCCACGG")
dnk5 = dnk.find("ACCACAA")
dnk6 = dnk.find("AGGCCTCA")
dnk7 = dnk.find("TTGTGGTGGC")
dnk8 = dnk.find("GGGAGGTGGC")
dnk9 = dnk.find("AAGTAGTGAC")
dnk10 = dnk.find("TGCAGGAACTTC")
dnk11 = dnk.find("TGAAGGACCTTC")
dnk12 = dnk.find("AAAACCTCA")
dnk13 = dnk.find("CGACTACAG")
dnk14 = dnk.find("CGCGGGCCG")

print "osumljenec ima naslednje lastnosti:"
if dnk1 == -1 and dnk2 == -1:
    print "lasje so korencek barve"
    print "lastnosti od Zigeta"
elif dnk2 == -1 and dnk3 == -1:
    print "lasje so crni"
    print "lastnosti od Mateja"
else:
    print "lasje so rjavi"
    print "lastnosti od Mihe"

if dnk4 == -1 and dnk5 == -1:
    print "oblika obraza je ovalna"
    print "lastnosti od Mateja"
elif dnk5 == -1 and dnk6 == -1:
    print "oblika obraza je kvadratna"
    print "lastnosti od Mihe"
else:
   print "oblika obraza je okrogla"
   print "lastnosti od Zigeta"

if dnk7 == -1 and dnk8 == -1:
    print "oci rjave"
    print "lastnosti od Zigeta"
elif dnk8 == -1 and dnk9 == -1:
    print "oci so modre"
    print "lastnosti od Mateja"
else:
   print "oci so zelene"
   print "lastnosti od Miheta"

if dnk10 == -1:
    print "spol:zenska"
else:
   print "spol:moski"

if dnk12 == -1 and dnk13 == -1:
    print "rasa:Azijec"
elif dnk13 == -1 and dnk14 == -1:
    print "rasa:Belec"
else:
   print "rasa:Crnec"