# Testausdokumentti

Testit keskittyvät sovelluksen päätoiminnallisuuksista vastaaviin luokkiin `UserService` ja `MommoService`

## Testit

### Konfiguroinnin testaus

Luokka `TestConfig`, moduulissa `config_test.py`, testaa tietokantayhdeyden muodostamista.

### Luokka UserService testaus

Luokka `TestUserService`, moduulissa `user_service_test.py`, testaa `UserService` luokkaa, joka
vastaa sovelluksen käyttäjätoiminnoista. Luokkaa testataan laajasti ja kaikki mahdolliset virhetilanteet
on pyritty huomioimaan testeissä. Löydetyt virhetilanteet on kartoitettu ja nille on asetettu sopivat
virheviestit. `UserRepository` ja `User` luokka tulevat näiden testejen kautta myös laajasti testatuksi. Testikattavuus on 100%

### Luokka MommoService testaus

Luokka `TestMommoService`, moduulissa `mommo_service_test.py`, testaa `MommoService` luokkaa, joka vastaa
sovelluksen mömmötoiminnoista. Luokkaa testataan mahdollisimman laajasti, mutta säikeet jätetään testaamatta,
sillä niiden testaaminen on tässä projektissa epäoleellista ja liaan haasteellista. Löydetyt virhetilanteet on jälleen kartoitettu ja niille on asetettu virheviestit. `MommoRepository` ja `Mommo` luokka tulevat näiden testejen kautta myös laajasti testatuksi. Testikattavuus on 64%.

### Testauskattavuus

(https://user-images.githubusercontent.com/75887936/168489723-babefc72-6d7f-4089-b4b6-1495aec87f01.png)

Testien ulkopuolelle jää käyttöliittymä ja sovelluksen käynnistävä moduuli. Lopullinen haarautumakattavuus
on 83%


