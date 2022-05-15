# Mömmöystävä

Mömmöystävä on ikioma virtuaalilemmikkisi!

## Dokumentaatio

[Vaatimusmaarittely](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Käyttöohje](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/kaytt%C3%B6ohje.md)

[Arkkitehtuuri](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/testausdokumentti.md)

### Release

[release viikko 5](https://github.com/ellaverak/ot_harjoitustyo/releases/tag/viikko5)

[release viikko 6](https://github.com/ellaverak/ot_harjoitustyo/releases/tag/viiko6)

[Mömmöystävä v1.0 **viikko 7**](https://github.com/ellaverak/ot_harjoitustyo/releases/tag/viikko7)

## Sovelluksen asennus

1. Lataa zip-tiedosto koneelle kohdasta **Release**:
2. Pura zip-tiedosto haluamassasi hakemistossa
3. Siirry terminaalissa puretun hakemiston sisälle
4. Asenna poetry komennolla:
```bash
poetry install
```
5. Rakenna tietokanta komennolla:
```bash
poetry run invoke build
```
6. Avaa sovellus komennolla:
```bash
poetry run invoke start
```

## Sovelluksen testaaminen

1. Siirry sovelluksen juurihakemistoon
 
2. Suorita testit komennolla:
```bash
poetry run invoke test
```

## Testikattavuuden tarkistaminen
1. Siirry sovelluksen juurihakemistoon
 
2. Suorita testikattavuuden tarkistaminen ja tallentaminen komennolla:
```bash
poetry run invoke coverage-report
```
Tai komennolla:
```bash
poetry run invoke coverage
```
3 Katsele testikattavuusraporttia komennolla:
```bash
poetry run coverage report -m
```
