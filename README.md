![GHA workflow badge](https://github.com/brotholi/tiralabra/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/brotholi/tiralabra/graph/badge.svg?token=7cq8g1NoTP)](https://codecov.io/gh/brotholi/tiralabra)

# Tiralabra - Kirjoitusvirheiden korjaaja

Tämä on Algoritmit ja tekoäly -kurssilla tehtävä kirjoitusvirheitä korjaava sovellus.

## Dokumentaatio
[Määrittelydokumentti](./docs/maarittelydokumentti.md)

[Testausraportti](./docs/testausraportti.md)

[Toteutusraportti](./docs/toteutusraportti.md)


## Viikkoraportit
[Viikko 1](./docs/viikkoraportit/viikkoraportti1.md)

[Viikko 2](./docs/viikkoraportit/viikkoraportti2.md)

[Viikko 3](./docs/viikkoraportit/viikkoraportti3.md)

[Viikko 4](./docs/viikkoraportit/viikkoraportti4.md)

[Viikko 5](./docs/viikkoraportit/viikkoraportti5.md)



# Käyttöohje

Kun olet kloonannut repositorion omalle koneellesi, käynnistä virtuaaliymäristö projektin juurihakemistossa komennolla

```bash
poetry shell
```

Tämä vaatii siis, että koneelle on asennettu poetry. Lataa tämän jälkeen projektin riippuvuudet poetrylla komennolla
```bash
poetry install
```

Sovelluksen voi tämän jälkeen käynnistää komennolla

```bash
poetry run invoke start
```	

Sovelluksen web-käyttöliittymä aukeaa terminaalin antamaan osoitteeseen, josta klikkaamalla pääsee etusivulle. Lokaalisti pyörivän sovelluksen saa suljettua antamalla terminaaliin ctrl + C.

Jos haluat ajaa sovellukselle yksikkötestejä, sen voi tehdä komennolla

```bash
poetry run invoke test
```

Testikattavuusraportin voi muodostaa komennolla

```bash
poetry run invoke coverage
```
