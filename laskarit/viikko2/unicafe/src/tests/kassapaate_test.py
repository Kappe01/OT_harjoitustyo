import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_lounaiden_maara_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
    
    def test_kassapaatteen_rahan_maara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassassa_oikean_verran_rahaa_edullisilla_raha_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_vaihtoraha_oikea_maara_edullisilla_raha_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_lounaiden_oikea_maara_edullisilla_raha_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kassassa_oikean_verran_rahaa_edullisilla_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_vaihtoraha_oikea_maara_edullisilla_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_lounaiden_oikea_maara_edullisilla_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassassa_oikean_verran_rahaa_maukkailla_raha_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_vaihtoraha_oikea_maara_maukkaasti_raha_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_lounaiden_oikea_maara_maukkaasti_raha_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kassassa_oikean_verran_rahaa_maukkaat_raha_ei_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_vaihtoraha_oikea_maara_maukkaasti_raha_ei_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_lounaiden_oikea_maara_maukkaasti_raha_ei_riitta(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisten_lounaiden_maara_kasvaa_kortilla_raha_riittaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisten_lounaiden_osto_onnistuu_kun_kortilla_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_kortilla_oikea_maara_rahaa_edullisen_jalkeen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)
    
    def test_edullisten_lounaiden_maara_kasvaa_kortilla_raha_ei_riittaa(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_edullisten_lounaiden_osto_ei_onnistu(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
    
    def test_kortilla_oikea_maara_rahaa_edullisen_jalkeen_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
    
    def test_maukkaitten_lounaiden_maara_kasvaa_kortilla_raha_riittaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaaniden_lounaiden_osto_onnistuu_kun_kortilla_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_kortilla_oikea_maara_rahaa_maukkaan_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
    
    def test_maukkaiden_lounaiden_maara_kasvaa_kortilla_raha_ei_riittaa(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maukkaan_lounaan_osto_ei_onnistu(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
    
    def test_kortilla_oikea_maara_rahaa_maukkaan_jalkeen_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_kortille_lataaminen_onnistuu_kassassa_oikea_maara(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    
    def test_kortille_lataaminen_ei_onnistu_negatiivisella_arvolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
