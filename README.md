# sos
Samodejni ocenjevalni sistem.

Uporablja najnovejšo tehnologijo in tako oceni (zaenkrat le) python program.

## Funkcije
### Dodaj nalogo
Na podstrani /admin dodamo nalogo z vnosom imena, navodil in testnih podatkov v obliki {n}.in za vnos ter {n}.out za izhod, n od 0 naprej.

### Oceni
Seznam nalog se nahaj na podstrani
/naloge, izberete nalogo in oddate .py datoteko. Rezultati primerjanja se prikažejo po oddaji.

V kolikor kaj ne dela, nisem jaz kriv. Naložiti je potrebno določene knjižnice, da se lahko poganja z `uvicorn main:app`.