Funkcije
========

Parametri funkcije su:

- lokalne promenljive
- globalne promenljive
- nisu promenljive
- neinicijalizovane lokalne promenljive
- neinicijalizovane globalne promenljive

----

Oblast važenja parametra funkcije je:

- funkcija
- oblast važenja parametra nije ograničena
- zaglavlje funkcije
- celokupna datoteka izvornog koda

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    void f(int a) {
        a = 3;
    }

    int main() {
        int a = 5;
        f(a);

        printf("%i", a);

        return 0;
    }

- 5
- 3
- prilikom kompajliranja dobijamo upozorenje da u pokazivač upisujemo ceo broj

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    void f(int *i) {
       *i = 3;
    }

    int main() {
       int a = 5;
       f(&a);

       printf("%d", a);

       return 0;
    }

- 3
- 5
- prilikom kompajliranja dobijamo upozorenje da u pokazivač upisujemo ceo broj

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    void f(int *i) {
       i = 3;
    }

    int main() {
       int a = 5;
       f(&a);

       printf("%i", a);

       return 0;
    }

- prilikom kompajliranja dobijamo upozorenje da u pokazivač upisujemo ceo broj
- 5
- 3

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    void f(int *i) {
        int a = 1;
        *i = 5;
    }

    int main() {
        int a = 2;
        int i = 3;

        printf("a = %d", a);

        f(&a);

        return 0;
    }

- ``a = 2``
- ``a = 1``
- ``a = 5``
- ``a = 3``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    void f(int *i) {
        int a = 1;
        *i = 5;
    }

    int main() {
        int a = 2;
        int i = a;
        f(&a);

        printf("a = %d", i);

        return 0;
    }

- ``a = 2``
- ``a = 1``
- ``a = 5``
- ``a = 3``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int f(int *i) {
        int b = 1;
        *i = 5;

        return b;
    }

    int main() {
        int a = 2;
        int i = 3;
        a = f(&a);

        printf("a = %d", a);

        return 0;
    }

- ``a = 1``
- ``a = 2``
- ``a = 5``
- ``a = 3``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int f(int *i) {
        int a = 1;
        *i = 5;

        return a;
    }

    int main() {
        int a = 2;
        int i = 3;

        printf("a = %d", a);

        a = f(&a);

        return 0;
    }

- ``a = 2``
- ``a = 1``
- ``a = 5``
- ``a = 3``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int f(int *i, int a) {
        a = *i;
        *i = 5;

        return a;
    }

    int main() {
        int a = 2;
        int i = 3;
        a = f(&i, a);

        printf("%d", a);

        return 0;
    }

- 3
- 5
- 1
- 2

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int f(int *i, int a) {
        a = *i;
        *i = 5;

        return a;
    }

    int main() {
        int a = 2;
        int i = 3;
        a = f(&i, a);

        printf("%d", i);

        return 0;
    }

- 5
- 3
- 1
- 2

----

Kako treba da izgleda deklaracija funkcije ``unesi_niz``, koja nema povratnu vrednost i poziva se iz sledećeg dela koda::

    #include <stdio.h>

    int main() {
        unsigned n;
        unsigned niz[1000];

        unesi_niz(niz, &n);
        ispisi_niz(niz, n);

        return 0;
    }

- ``void unesi_niz(unsigned *,  unsigned *);``
- ``void unesi_niz(unsigned *,  unsigned  );``
- ``void unesi_niz(unsigned  ,  unsigned *);``
- ``void unesi_niz(unsigned  , &unsigned  );``
- ``int  unesi_niz(unsigned *,  unsigned *);``

----

Kako treba da izgleda deklaracija funkcije ``ispisi_niz``, koja nema povratnu vrednost i poziva se iz sledećeg dela koda::

    #include <stdio.h>

    int main() {
        unsigned n;
        unsigned niz[1000];

        unesi_niz(niz, &n);
        ispisi_niz(niz, n);

        return 0;
    }

- ``void ispisi_niz(unsigned *,  unsigned  );``
- ``void ispisi_niz(unsigned *,  unsigned *);``
- ``void ispisi_niz(unsigned  ,  unsigned *);``
- ``void ispisi_niz(unsigned  , &unsigned  );``
- ``int  ispisi_niz(unsigned *,  unsigned *);``

----

Kog je tipa povratna vrednost sledeće funkcije::

    void zbir(int x, int y, int *k) {
        *k = x + y;
    }

- ova funkcija nema povratnu vrednost
- ``int``
- ``int *``
- ``float``

----

Kog je tipa povratna vrednost sledeće funkcije::

    int *zbir(int x, int y, int *k) {
        *k = x + y;
    }

- ``int *``
- ``int``
- ``float``
- ova funkcija nema povratnu vrednost
