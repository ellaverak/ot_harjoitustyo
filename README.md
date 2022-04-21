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

## Sovelluksen asennus

1. Kloonaa git-repositorio haluamaasi hakemistoon komennolla:
```bash
git clone https://github.com/ellaverak/ot_harjoitustyo
```
2. Asenna poetry komennolla:
```bash
poetry install
```
3. Käynnistä poetry-virtuaaliympäristö komennolla:
```bash
poetry shell
```
4. Rakenna tietokanta komennolla:
```bash
invoke build
```
5. Avaa sovellus komennolla:
```bash
invoke start
```

## Sovelluksen testaaminen

1. Siirry sovelluksen juurihakemistoon
 
2. Käynnistä poetry-virtuaaliympäristö komennolla:
```bash
poetry shell
```
3. Suorita testit komennolla:
```bash
invoke test
```

## Testikattavuuden tarkistaminen
1. Siirry sovelluksen juurihakemistoon
 
2. Käynnistä poetry-virtuaaliympäristö komennolla:
```bash
poetry shell
```
3. Suorita testikattavuuden tarkistaminen ja tallentaminen komennolla:
```bash
invoke coverage-report
```
4. Katsele testikattavuusraportti komennolla
```bash
coverage report -m
```
