import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldon_kasvattamien_onnistuu(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_saldon_vaheneminen_onnistuu_jos_saldoa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")

    def test_saldon_vahentaminen_ei_onnistu_jos_saloda_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldon_jos_saldon_vahentaminen_onnistuu_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)
    
    def test_jos_saldon_vahentaminen_ei_onnistu_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)