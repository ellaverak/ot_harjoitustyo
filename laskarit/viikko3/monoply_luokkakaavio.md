Pelin alussa luodaan yksi kortit olio, joka pitää kirjaa pelin korteista. Kortit-olio vastaa korttien toiminnoista ja siitä,
mikä kortti kuuluu kullekkin pelaajalle ja mitkä ovat vielä pakassa. Pelin alussa luodaan myös yksi Tontit-olio, joka pitää
kirjaa siitä, mikä tontti kuuluu kullekin pelaajalle.
Pelaajilla ei ole erillistä luokkaa tai moduulia vaan luodut Pelinappula-oliot kuvaavat pelaajia.
Jokaiseen Pelinappulaan liittyy Ruutu-olio ja OmatKortit-olio.

```mermaid
 classDiagram
      Pelinappula "*" --> "1" Ruutu
      Pelinappula "*" --> "1" OmatKortit
      class Pelinappula{
          ruutu
          omat_kortit
          raha
          iiiku()
          myy_kortti()
          siirry()
          mene_vankilaan()
          vapaudu_vankilasta()
      }
      Ruutu "*" --> "1" Kortit
      class Ruutu{
          sijainti
          seuraava_sijainti
          aloitus
          kortit
          toiminto()
      }
      Kortit --> Tontit
      class Kortit{
          yhteismaat
          sattumat
          laitokset
          asemat
          kadut
          vankila()
          osta_tontti()
          nosta_kortti()
      }
      class OmatKortit{
          laitokset
          asemat
          kadut
          muut
      }
      class Tontit{
          kadut
          asemat
          laitokset
          rakenna_talo()
          rakenna_hotelli()
      }
```

