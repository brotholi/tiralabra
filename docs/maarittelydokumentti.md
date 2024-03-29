# Määrittelydokumentti
Tämä määrittelydokumentti määrittelee Helsingin yliopiston Aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssilla tehtävän harjoitustyön. Suoritan kurssin Tietojenkäsittelytieteen kandiohjelmassa (TKT).

## Aihe ja toteutus
Toteutan harjoitustyössä kirjoitusvirheiden korjaajan, joka korjaa käyttäjän antamassa tekstisyötteessa kirjoitusvirheet vertaamalla niiden eroavaisuutta suomen kielen sanastossa oleviin sanoihin. Hyödynnän virheiden etsimmässä merkkijonojen etäisyysmitan laskentaa, Damerau–Levenshteinin -etäisyyttä, jonka avulla etsin ne sanat, joiden etäisyysmitta korjattavasta sanasta on pienin. Suomen kielen sanasto talletetaan itse Pythonilla toteutettavaan Tre-tietorakenteeseen. Olen valinnut kyseiset tietorakenteet ja algorimit kurssin aihe-ehdotusten perusteella ajan säästämiseksi.

Sovellukselle voidaan antaa käyttöliittymällä tekstisyötteenä sanoja, jotka analysoidaan vertaamalla niiden etäisyyttä sanastossa oleviin sanoihin. Sovellus antaa korjausehdotuksen kertomalla ne sanat, joita kirjoitettu teksti on lähimpänä. Ainakin ensimmäisessä toteutuksessa sovellukselle voi antaa kerrallaan vain yhden sanan, jonka se analysoi. Tätä voidaan laajentaa tarvittaessa niin, että sovellukselle voidaan antaa tekstikentässä pitempi, mutta kuitenkin rajattu, määrä tekstiä, jonka se analysoi ja antaa käyttäjällä suoraan korjattuna.

Lähteiden mukaan trie-tietorakenteeseen tehtävät hakuoperaatiot vievät pahimmillaan O(n), kun taas Damerau-Levenshteinin etäisyyttä käyttävä algoritmi vie pahimmillaan O(M*N), jossa M ja N ovat verrattavien merkkijonojen pituuksia. Nämä ovat alustavat aikavaativuustavoitteet.

## Ohjelmointikielet
Harjoitustyö totetetaan Pythonilla.

Vertaisarvioinnissa voin arvioida ainakin myös Javalla toteutettuja harjoitustöitä, myös muut yleiset kielet onnistuvat.

## Projektin kieli

Projektin dokumentaatio kirjoitetaan suomeksi. Myös koodissa olevat  docstring-kommentit tulevat olemaan suomeksi, mutta itse koodi ja muuttujanimet englanniksi.

## Lähteet 
Harjoitustyössä käytän seuraavia lähteitä:

- [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)



