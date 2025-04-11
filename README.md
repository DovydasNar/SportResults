===== Krepšinio rungtynių rezultatų puslapis =====

* Sukurtas Krepšinio varžybų rezultatų puslapis, kuriame yra pateikti rungtynių rezulatai, sukurta vartotojų prisijungimo, registracijos sistema. Tik prisijungę vartotojai gali pasiekti funkcijas, tokias kaip naujų rungtynių pridėjimas, redagavimas bei ištrynimas. Taip pat pateikiama komandų statistika, kurioje buvo apskaičiuoti komandų rezultatų rodikliai.
* Projekte buvo naudojamos Python, Django technologijos.

**

Projekto paleidimas:

1. Atsisiųskite repozitoriją:
https://github.com/DovydasNar/SportResults.git

2. Sukurkite virtualią aplinką:
Mac/Linux:
python -m venv venv <br>
source venv/bin/activate
Windows:
python -m venv venv <br>
venv\Scripts\activate

3. Įdiekite reikalingas bibliotekas:
pip install -r requirements.txt

4. Paleiskite projektą:
cd sport_results <br>
python manage.py runserver