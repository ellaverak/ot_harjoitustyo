# Arkkitehtuuri

## Rakenne

Sovellus noudattaa kerrosarkkitehtuuri.

## Sovelluslogiikka
- ui-pakkaus vastaa käyttöliittymätoiminnoista ja kutsuu services-pakkauksen toimintoja.
- services-pakkaus vastaa sovelluslogiikasta ja kutsuu repositories pakkauksen toimintoja.
- repositories-pakkaus vastaa tietokantatoiminnoista.

- entities-pakkaus vastaa user- ja mommo-olioiden luomisesta. Services-pakkauksen meoduulit ja luokat
hoitavat sovelluslogiikkaa kutsumalla entities-pakkauksen toimintoja ja ylläpitämällä tietoa kirjautuneesta
käyttäjästä ja mömmöstä. Repositories pakkauksen moduulit kutsuvat entities-pakkauksen toimintoja palauttaakseen osan tuloksista user- ja mommo-olioina.

**Alla havainnollistava luokkakaavio:

### Luokkakaavio

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
          user
          user_repository
      }
      MommoService "1" --> "1" MommoRepository
      MommoService "1" --> "1" UserService
      class MommoService{
          mommo
          mommo_repository
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
