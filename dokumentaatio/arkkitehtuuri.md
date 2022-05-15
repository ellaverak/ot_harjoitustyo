# Arkkitehtuuri

## Rakenne

Sovellus noudattaa kerrosarkkitehtuuri.

## Sovelluslogiikka
- ui-pakkaus vastaa käyttöliittymätoiminnoista ja kutsuu services-pakkauksen toimintoja.
- services-pakkaus vastaa sovelluslogiikasta ja kutsuu repositories pakkauksen toimintoja.
- repositories-pakkaus vastaa tietokantatoiminnoista.

- entities-pakkaus vastaa user- ja mommo-olioiden luomisesta. Services-pakkauksen moduulit ja luokat
hoitavat sovelluslogiikkaa kutsumalla entities-pakkauksen toimintoja ja ylläpitämällä tietoa kirjautuneesta
käyttäjästä ja mömmöstä. Repositories pakkauksen moduulit kutsuvat entities-pakkauksen toimintoja palauttaakseen osan tuloksista user- ja mommo-olioina.

**Alla havainnollistava luokkakaavio:**

### Luokkakaavio

`MommoService` ja `UserService` hoitavat Mommo- ja User-olentoihin liittyviä toimintoja. Ne pääsevät olentoihin käsiksi `MommoRepository` ja `UserRepository` -luokkien välityksellä. Nämä luokat käsittelevät suoraan Mommo- ja User-olentoihin liittyviä tietokantatoimintoja.

Lisäksi `MommoService` käyttää joitain `UserService`-luokan toimintoja.

```mermaid
 classDiagram
      class User{
          username
          password
          role
      }
      class Mommo{
          user_id
          name
          hunger
          thirst
          clenliness
          happiness
      }
      UserService "1" --> "1" UserRepository
      class UserService{
          user_repository
          user
          user_id
          visit_id
          
      }
      MommoService "1" --> "1" MommoRepository
      MommoService "1" --> "1" UserService
      class MommoService{
          mommo_repository
          mommo
          mommo_id
          visit_state
          _hunger_thread
          _thirst_thread
          _clenliness_thread          
      }
      UserRepository "1" --> "*" User
      class UserRepository{
          db_
      }
      MommoRepository "1" --> "*" Mommo
      class MommoRepository{
          db_
      }
```

### Sekvenssikaaviot
Esimerkkejä toiminnallisuuksista

**Uuden mömmön luominen**
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant MommoService
  participant MommoRepository
  User->>UI: click "Hyväksy" button
  UI->>MommoService: create_mommo(name)
  MommoService->>MommoRepository: create_mommo(name)
  MommoRepository-->>MommoService: mommo
  MommoService-->>UI: mommo
  UI->UI: mommo_view()
```
**Tempun tekeminen**
`MommoService` luokalle välitetään tieto siitä, mikä temppu suorittetaan. `MommoRepository` palauttaa listan,
joka sisältää tiedot mömmön tempuista. Jos mömmö osaa tempun, eli tempun arvo on 100, `MommoService` palauttaa arvon True ja `DrawMommo` piirtää tempun. Muuten `MommoService` kasvattaa tempun osaamisarvoa, jonka `MommoRepository` tallentaa. Lisäksi `MommoService` palauttaa arvon False käyttöliittymälle, joka piirtää käyttöliittymään viestin: "Mömmö harjoittelee..." 
```mermaid
sequenceDiagram
  actor User
  participant DrawMommo
  participant UI
  participant MommoService
  participant MommoRepository
  User->>UI: click "Hyppää" button
  UI->>MommoService: do_trick(trick)
  MommoService->>MommoRepository: do_trick(trick)
  MommoRepository-->>MommoService: trick_list
  MommoService-->>UI: False
  MommoService-->>MommoRepository: save_trick(mommo_id, trick_list)
  UI->UI: _show_message()
  MommoService-->>UI: True
  UI->DrawMommo: draw_jump()
```

## Käyttöliittymä

Käyttöliittymä sisältää seuraavat näkymät (luokat suluissa):
- Päänäkymä (`MainView`)
- Kirjautumisnäkymä (`LoginView`)
- Rekisteröitymisnäkymä (`RegisterView`)
- Uusi mömmö -näkymä (`NewMommoView`)
- Mömmö-näkymä (`MommoView`)
- Kaikki mömmöt -näkymä (`AllMommosView`)

Lisäksi käyttöliittymän muodostamiseen osallistuvat luokat `UiTheme` ja `DrawMommo`.

Kaikkien näkymien lopullisesta näyttämisestä vastaa `ui.py`:n luokka `UI`. Näkymät kutsuvat service-paketin toimintoja.

## Toiminnallisuus

**UserService-luokka**

Luokka vastaa käyttäjätoiminnallisuudesta.

**Funktioesimerkkejä**

```bash
create_user() Args: username, password, role
```
- luo uuden käyttäjän ja kirjaa sen sisään.

```bash
login() Args: username, password
```
- kirjaa käyttäjän sisään.
```bash
logout()
```
- kirjaa käyttäjän ulos.
```bash
visit() Args: visit_id
```
- asettaa vierailtavan käyttäjän id-tunnuksen.

**MommoService-luokka**

Luokka vastaa mömmötoiminnallisuudesta ja hyödyntää säikeita
mömmön tilastojen muuttamiseen ajan kuluessa.

**Funktioesimerkkejä**

```bash
start()
```
- käynnistää säikeet

```bash
create_mommo() Args: name
```
- luo uuden mömmön
```bash
login_mommo() Args: visit_user_id
```
- kirjaa mömmön sisään
```bash
logout_mommo()
```
- kirjaa mömmön ulos
```bash
feed_mommo()
```
- vähentää mömmön nälkäisyyttä.


**Säikeitä hyödyntävät funktiot**
```bash
increase_hunger()
```
```bash
increase_thirst()
```
```bash
decrease_clenliness()
```
```bash
decrease_happiness()
```

## Tiedon tallennus

**UserRepository-luokka**

Luokka vastaa käyttäjätietojen talletuksesta tietokantaan ja niiden hakemisesta.

**MommoRepository-luokka**

Luokka vastaa mömmötietojen talletuksesta tietokantaan ja niiden hakemisesta.
