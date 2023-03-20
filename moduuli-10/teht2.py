'''
    Esimerkissä on alkua tehtävän 1 ja 2 ratkaisua varten.
    - lue tehtävän määritykset, tästä puuttuu jopa kokonaisia metodeja..
    - esimerkin koodeissa ei tarkisteta, että yritetäänkö mennä liian ylös tai maan alle..
'''

class Hissi:

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin      # kerros, jossa hissi on; aluksi alimmassa

    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def siirry_kerrokseen(self, uusi_kerros):
        # siirrytään tarvittaessa ylöspäin
        while uusi_kerros > self.kerros:
            self.kerros_ylös()
        # siirrytään tarvittaessa alaspäin
        while uusi_kerros < self.kerros:
            pass    # TODO
        # xtra: ilmoitus että ollaan halutussa kerroksessa
        print("Hissi on perillä.")
        return


class Talo:

    def __init__(self, alin, ylin, lkm):
        # luodaan lista talon hisseille
        self.hissit = []
        # lisätään listan alkuun 'ylimääräinen hissi', jotta hissien nummerot menevät halutusti
        self.hissit.append(Hissi(alin, alin))
        # luodaan uudelle talolle sen varsinaiset hissit, hissit saavat nyt numerot 1, 2, 3, 4
        for nro in range(lkm):
            hissi = Hissi(alin, ylin)
            # huom: hissien numerointi, se ei ala nyt nollasta
            self.hissit.append(hissi)  # lisätään uusi hissi talon hissien listalle



# -- pääohjelma alkaa --
# TODO: luo uusi talo-olio, esim kerrokset 1-7 ja hissejä 3 kpl
# TODO: aja talon eri hissejä ja tsekkaa että ne liikkuvat halutusti.
