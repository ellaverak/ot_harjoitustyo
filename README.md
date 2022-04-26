# ot_harjoitutustyo

## Mömmöystävä

Mömmöystävä on ikioma virtuaalilemmikkisi!

## Dokumentaatio

[vaatimusmaarittely.md](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[changelog.md](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/changelog.md)

[kayttöohje.md](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/kaytt%C3%B6ohje.md)

[arkkitehtuuri.md](https://github.com/ellaverak/ot_harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

Sovellus noudattaa kerrosarkkitehtuuria.

### Release

[release viikko 5](https://github.com/ellaverak/ot_harjoitustyo/releases/tag/viikko5)

## Sovelluksen asennus

1. Lataa zip-tiedosto koneelle kohdasta **Release:
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
3. Katsele testikattavuusraportti komennolla
```bash
poetry run coverage report -m
```
