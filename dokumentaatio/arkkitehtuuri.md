## Sovelluslogiikka

MommoService ja UserService hoitavat Mommo- ja User-olentoihin liittyviä toimintoja. Ne pääsevät olentoihin käsiksi MommoRepository- ja UserRepository-luokkien välityksellä. Nämä luokat käsittelevät suoraan Mommo- ja User-olentoihin liittyviä tietokantatoimintoja.

Lisäksi MommoService käyttää joitain UserServicen toimintoja.

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
