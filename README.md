# OHTE, harjoitustyö, LearningApp

Sovelluksen avulla käyttäjä voi harjoitella valitsemiaan aiheita. Sekä lisätä omia aiheita ja uusia kysymyksiä ja voi täten harjoitella esimerkiksi tenttiin lisäämällä kertaus kysymyksiä sovellukselle. Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä.

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.8`.

## Release

- [Release 1](https://github.com/Kappe01/OT_harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

- [Työaikakirjanpito](./Dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](./Dokumentaatio/vaatimusmaarittely.md)
- [Changlelog](./Dokumentaatio/changelog.md)
- [Arkkitehtuuri](./Dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:
```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet:
```bash
poetry run invoke build
```

3. Käynnistä sovellus:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tarkistukset koodin laadusta voi suorittaa komennolla:

```bash
poetry run invoke lint
```

