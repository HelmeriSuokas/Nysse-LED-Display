Tampereen Ratikka – Reaaliaikainen aikataulunäyttö

Python-sovellus, joka hakee Tampereen joukkoliikenteen (Nysse) reaaliaikaiset ratikka-aikataulut avoimesta rajapinnasta ja esittää ne 24/7 LED-matriisinäytöllä.

Toimintaperiaate
1. Hakee säännöllisin väliajoin pysäkkikohtaiset lähtöajat Nyssen / Digitransitin rajapinnasta.
2. Jäsentää datan ja laskee jäljellä olevan ajan seuraaviin vuoroihin.
3. Piirtää aikataulut LED-matriisille ja käsittelee mahdolliset verkkokatkokset taustalla.
