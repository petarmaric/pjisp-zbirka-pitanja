Pokazivači
==========

Da li je ``NULL`` pokazivač isto što i neinicijalizovani pokazivač?

- ne
- da

----

Unarni operator referenciranja ``&``:

- vraća adresu promenljive
- omogućuje posredan pristup nekom podatku putem njegove memorijske adrese
- vraća sadržaj pokazivačke promenljive

----

Unarni operator dereferenciranja ``*``:

- omogućuje posredan pristup nekom podatku putem njegove memorijske adrese
- vraća adresu promenljive
- vraća sadržaj pokazivačke promenljive

----

Pokazivač tipa ``void *`` može da predstavlja:

- adresu bilo kog objekta
- vrednost bilo kog objekta
- tip bilo kog objekta

----

Ograničeni pokazivač dobija se primenom kvalifikatora:

- ``restrict``
- ``extern``
- ``const``
- ``inline``

----

Između ograničenog pokazivača i objekta na koji on pokazuje postoji sledeća veza:

- tokom životnog veka pokazivača, objekat se može menjati ili mu se može pristupati samo putem tog pokazivača
- tokom životnog veka pokazivača, objekat se ne može menjati
- tokom životnog veka objekta, pokazivač se ne može menjati

----

Promenljivi pokazivač na promenljive podatke se deklariše sa:

- ``tip *p``
- ``tip *const p``
- ``const tip *p``
- ``const tip *const p``

----

Nepromenljivi pokazivač na promenljive podatke se deklariše sa:

- ``tip *const p``
- ``tip *p``
- ``const tip *p``
- ``const tip *const p``

----

Promenljivi pokazivač na nepromenljive podatke se deklariše sa:

- ``const tip *p``
- ``tip *p``
- ``tip *const p``
- ``const tip *const p``

----

Nepromenljivi pokazivač na nepromenljive podatke se deklariše sa:

- ``const tip *const p``
- ``tip *p``
- ``tip *const p``
- ``const tip *p``

----

Pokazivač ``p`` iz izraza ``tip *p`` je:

- promenljivi pokazivač na promenljive podatke
- nepromenljivi pokazivač na promenljive podatke
- promenljivi pokazivač na nepromenljive podatke
- nepromenljivi pokazivač na nepromenljive podatke

----

Pokazivač ``p`` iz izraza ``tip *const p`` je:

- nepromenljivi pokazivač na promenljive podatke
- promenljivi pokazivač na promenljive podatke
- promenljivi pokazivač na nepromenljive podatke
- nepromenljivi pokazivač na nepromenljive podatke

----

Pokazivač ``p`` iz izraza ``const tip *p`` je:

- promenljivi pokazivač na nepromenljive podatke
- promenljivi pokazivač na promenljive podatke
- nepromenljivi pokazivač na promenljive podatke
- nepromenljivi pokazivač na nepromenljive podatke

----

Pokazivač ``p`` iz izraza ``const tip *const p`` je:

- nepromenljivi pokazivač na nepromenljive podatke
- promenljivi pokazivač na promenljive podatke
- nepromenljivi pokazivač na promenljive podatke
- promenljivi pokazivač na nepromenljive podatke

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 2;

        if (&a == &b)
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je a``
- ``Veci je b``
- prilikom kompajliranja dobijamo grešku/upozorenje (ne možemo porediti adrese!)

----

Kako se pravilno uvezuje pokazivač ``pi`` na promenljivu ``i``?

- ``pi = &i;``
- ``pi = i;``
- ``*pi = i;``
- ``*pi = &i;``

----

U programskom jeziku C dozvoljeno je dodavanje proizvoljne celobrojne vrednosti na postojeću vrednost pokazivača.

- tačno
- netačno
- dozvoljena je isključivo upotreba operatora inkrementatora i dekrementatora
