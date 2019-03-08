Strukture
=========

U programskom jeziku C jedna struktura ima isto memorijsko zauzeće kao i:

- zbirno memorijsko zauzeće svih njenih elemenata
- zauzeće njenog memorijski najzahtevnijeg elementa
- zauzeće memorijski najzahtevnijeg podržanog tipa podatka u programskom jeziku C
- zauzeće srodne joj unije, koja se sastoji od istovetnih elemenata

----

U programskom jeziku C jedna unija ima isto memorijsko zauzeće kao i:

- zauzeće njenog memorijski najzahtevnijeg elementa
- zbirno memorijsko zauzeće svih njenih elemenata
- zauzeće memorijski najzahtevnijeg podržanog tipa podatka u programskom jeziku C
- zauzeće srodne joj strukture, koja se sastoji od istovetnih elemenata

----

Od koliko polja se sastoji sledeća struktura::

    struct osoba_st {
       char ime[50];
       char adresa[20];
       int godine;
    };

- 3
- 1
- 2
- 4
- 71
- 74
- struktura nije pravilno deklarisana

----

Od koliko polja se sastoji sledeća struktura::

    struct osoba_st {
       char ime[50];
       char adresa[20];
       int godine;
       int jmbg;
    };

- 4
- 1
- 2
- 3
- 72
- 78
- struktura nije pravilno deklarisana

----

Od koliko polja se sastoji sledeća struktura::

    struct {
       char ime[50];
       char adresa[20];
       int godine;
       int jmbg;
    }

- struktura nije pravilno deklarisana
- 1
- 2
- 3
- 4
- 72
- 78

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    struct tacka_st {
       int x;
       int y;
    };

    int main() {
        struct tacka_st t;
        t.x = 3;
        t.y = 5;

        int i;
        for(i=0; i<t.x; i++){
            t.y += t.y;
        }

        printf("%d", t.y);

        return 0;
    }

- ``40``
- ``15``
- ``20``
- greška prilikom kompajliranja: promenljiva ``t`` nije pravilno deklarisana
- greška prilikom kompajliranja: struktura nije pravilno deklarisana

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    struct tacka_st {
       int x;
       int y;
    };

    int main() {
        tacka_st t;
        t.x = 3;
        t.y = 5;

        int i;
        for(i=0; i<t.x; i++){
            t.y += t.y;
        }

        printf("%d", t.y);

        return 0;
    }

- greška prilikom kompajliranja: promenljiva ``t`` nije pravilno deklarisana
- ``15``
- ``20``
- ``40``
- greška prilikom kompajliranja: struktura nije pravilno deklarisana

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    struct {
       int x;
       int y;
    }

    int main() {
        struct tacka_st t;
        t.x = 3;
        t.y = 5;

        int i;
        for(i=0; i<t.x; i++){
            t.y += t.y;
        }

        printf("%d", t.y);

        return 0;
    }

- greška prilikom kompajliranja: struktura nije pravilno deklarisana
- ``15``
- ``20``
- ``40``
- greška prilikom kompajliranja: promenljiva ``t`` nije pravilno deklarisana

----

U sledećoj strukturi identifikator ``tacka_st`` je::

    struct tacka_st {
        int x;
        int y;
    };

- obavezan
- opcion
- u ovom slučaju struktura nije pravilno deklarisana

----

U sledećoj strukturi identifikator ``tacka_st`` je::

    typedef struct tacka_st {
        int x;
        int y;
    } TACKA;

- opcion
- obavezan
- u ovom slučaju ``tacka_st`` nije identifikator
- u ovom slučaju struktura nije pravilno deklarisana

----

U sledećoj strukturi identifikator ``tacka_st`` je::

    typedef struct tacka_st {
        int x;
        int y;
        struct tacka_st *mama;
    } TACKA;

- obavezan
- opcion
- u ovom slučaju ``tacka_st`` nije identifikator
- u ovom slučaju struktura nije pravilno deklarisana

----

U sledećoj strukturi identifikator ``TACKA`` je::

    typedef struct tacka_st {
        int x;
        int y;
    } TACKA;

- obavezan
- opcion
- u ovom slučaju ``TACKA`` nije identifikator
- u ovom slučaju struktura nije pravilno deklarisana

----

U sledećoj strukturi identifikator ``TACKA`` je::

    typedef struct {
        int x;
        int y;
    } TACKA;

- obavezan
- opcion
- u ovom slučaju ``TACKA`` nije identifikator
- u ovom slučaju struktura nije pravilno deklarisana

----

Kako se pravilno ispisuje polje ``x``, koje se nalazi unutar promenljive ``a``::

    #include <stdio.h>

    typedef struct tacka_st {
        int x;
        int y;
    } TACKA;

    int main() {
        TACKA a;

        TACKA *pa = &a;
        a.x = 1;
        a.y = 2;

        return 0;
    }

- ``printf("%d", pa->x);``
- ``printf("%d", a->x);``
- ``printf("%d", &a.x);``
- ``printf("%d", pa.x);``
- ``printf("%d", &pa.x);``

----

Kako se pravilno učitava polje ``y``, koje se nalazi unutar promenljive ``a``::

    #include <stdio.h>

    typedef struct tacka_st {
        int x;
        int y;
    } TACKA;

    int main() {
        TACKA a;

        TACKA *pa = &a;

        return 0;
    }

- ``scanf("%d", &pa->y);``
- ``scanf("%d", &pa.y);``
- ``scanf("%d", pa.y);``
- ``scanf("%d", pa->y);``
