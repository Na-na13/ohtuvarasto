import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(5)
        self.negatiivinen_tilavuus = Varasto(-5)
        self.negatiivinen_alkusaldo = Varasto(2,-1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.negatiivinen_tilavuus.saldo, -5)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.negatiivinen_tilavuus.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_ottaminen_ei_muuta_saldoa(self):
        self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_ei_vie_saldoa_negatiiviseksi(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varaston_merkkijonoesitys(self):
        merkkijono = "saldo = 0, vielä tilaa 10"
        self.assertEqual(self.varasto.__str__(), merkkijono)
