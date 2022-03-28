import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_luodussa_kassapaatteessa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_lounaita_myyty_0(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_kateisosto_rahamaarat_toimivat(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihto, 60)

    def test_edullisen_kateisosto_edullisten_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_kateisosto_rahamaarat_toimivat_kun_kateista_ei_tarpeeksi(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihto, 100)

    def test_edullisen_kateisosto_edullisten_maara_ei_kasvaa_kun_kateista_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_kateisosto_rahamaarat_toimivat(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihto, 100)

    def test_maukkaan_kateisosto_maukkaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_kateisosto_rahamaarat_toimivat_kun_kateista_ei_tarpeeksi(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihto, 200)

    def test_maukkaan_kateisosto_maukkaiden_maara_ei_kasvaa_kun_kateista_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_korttiosto_rahamaarat_toimivat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 260)

    def test_edullisen_korttiosto_edullisten_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_korttiosto_rahamaarat_toimivat_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_edullisen_korttiosto_edullisten_maara_ei_kasva_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 2)

    def test_maukkaan_korttiosto_rahamaarat_toimivat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_maukkaan_korttiosto_maukkaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_korttiosto_rahamaarat_toimivat_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_maukkaan_korttiosto_maukkaan_maara_ei_kasva_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_saldon_lataaminen_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_saldon_lataaminen_kortille_ei_muuta_rahamaaria_kun_summa_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 500)