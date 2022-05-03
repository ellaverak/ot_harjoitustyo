# Käyttöohje

## Aloittaminen

Uusi pelaaja voi aloittaa pelin luomalla uuden käyttäjän. Käyttäjän luomisen jälkeen, pelaaja pääsee luomaan
itselleen mömmöystävän ja nimeämään sen. Jokaisella pelaajalla voi olla vain yksi oma mömmöystävä.

Jo käyttäjätilin omistava pelaaja voi kirjautua sisään ja päästä suoraan oman mömmönsä mömmönäkymään.

## Mömmönäkymä

Mömmöystävä näyttäytyy mömmönäkymässä. Mömmönäkymässä voi seurata mömmön hyvinvointia neljällä eri tilastolla:
Nälkäisyys, Janoisuus, Puhtaus, Onnellisuus. Nämä laskevat ajan kuluessa.

Mömmön kanssa voi lisäksi puuhailla. Sitä voi syöttää, juottaa, puhdistaa ja silittää.
Piakkoin mömmölle voi opettaa myös temppuja ja itse mömmön voi toivottovasti pian nähdä tässä näkymässä.

## Muut mömmöt

Mömmönäkymästä on mahdollisuus siirtyä selaamaan muita mömmöystäviä. Niitä voi lisäksi katsella niiden
omassa näkymässä. (Tämä toiminnallisuus ei vielä ole valmis.) Kuka tahansa pelaaja voi silittää mömmöä,
jonka luona vierailee ja tehdä sen kanssa temppuja, joita se osaa, mutta vain ylläpitäjä voi
hoitaa muiden mömmöjä.

## Asennetun sovelluksen käynnistäminen

1. Rakenna tietokanta komennolla:
```bash
poetry run invoke build
```

**Huom!**
komento "poetry run invoke build" rakentaa tietokannan, jos sitä ei ole olemassa ja korvaa vanhan tietokannan,
jos sellainen jo on. Aja komento siis ainoastaan ennen sovelluksen ensimmäistä käynnistyskertaa. Tai
halutessasi tyhjentäää tietokannan.

2. Avaa sovellus komennolla:
```bash
poetry run invoke start
```

