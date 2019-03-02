Petlje
======

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;

        for(i=5; i<=10; i++)
            printf("%d", i);

        return 0;
    }

- 6 puta
- 0 puta
- 4 puta
- 5 puta
- 9 puta
- 10 puta
- 11 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;

        for(i=5; i>=10; i++)
            printf("%d", i);

        return 0;
    }

- 0 puta
- 4 puta
- 5 puta
- 6 puta
- 9 puta
- 10 puta
- 11 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;

        for(i==5; i<=10; i++)
            printf("%d", i);

        return 0;
    }

- 11 puta
- 0 puta
- 4 puta
- 5 puta
- 6 puta
- 9 puta
- 10 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;

        for(i=5; i=10; i++)
            printf("%d", i);

        return 0;
    }

- beskonačno mnogo puta
- 0 puta
- 4 puta
- 5 puta
- 6 puta
- 9 puta
- 10 puta
- 11 puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;

        for(i=0; i; i++)
            printf("%d", i);

        return 0;
    }

- 0 puta
- 4 puta
- 5 puta
- 6 puta
- 9 puta
- 10 puta
- 11 puta
- beskonačno mnogo puta

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a = 0;

        for(i=5; i<=10; i+=2)
            a++;

        printf("%d", a);

        return 0;
    }

- ``3``
- ``0``
- ``2``
- ``4``
- ``5``
- ``6``
- ništa neće biti ispisano, zbog beskonačne petlje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a = 0;

        for(i=10; i>=5; i-=2)
            a++;

        printf("%d", a);

        return 0;
    }

- ``3``
- ``0``
- ``2``
- ``4``
- ``5``
- ``6``
- ništa neće biti ispisano, zbog beskonačne petlje

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``i`` će biti::

    int a = 6;
    int i = 9;

    do {
        i++;
    } while(a < 5);

- 10
- 6
- 7
- 9
- 11

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``a`` će biti::

    int a = 9;
    int i = 6;

    do {
        i++;
    } while(a < 5);

    printf("%d", i);

- 9
- 6
- 7
- 10
- 11

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``i`` će biti::

    int a = 3;
    int i = 6;

    do {
        i++;
        a--;
    } while(a > 5 || i < 8);

- 8
- 2
- 3
- 6
- 7

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``a`` će biti::

    int a = 3;
    int i = 6;

    do {
        i++;
        a--;
    } while(a > 5 || i < 8);

- 1
- 0
- 3
- 6
- 7

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``i`` će biti::

    int a = 6;
    int i = 9;

    while(a > 5){
        i = --a;
    }

- 5
- 4
- 6
- 7

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``i`` će biti::

    int a = 7;
    int i = -5;

    do {
        i = --a;
    } while(a >= 5);

    printf("%d", i);

- 4
- -5
- 5
- 6
- 7

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a = 5;

        while(a >= 3) {
            a--;
            i++;
        }

        printf("%d", i);

        return 0;
    }

- 3
- 0
- 1
- 2
- 4

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a = 5;

        while(a)
            i++;

        return 0;
    }

- beskonačno mnogo puta
- 0 puta
- 1 put
- 2 puta
- 5 puta

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 5;
        int a = 0;

        while(a)
            i++;

        printf("%d", i);

        return 0;
    }

- ``5``
- ``0``
- ``1``
- ``6``
- ništa neće biti ispisano, zbog beskonačne petlje

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = -3;
        int a = 4;
        int p = 0;

        while(p = i-a+2) {
            printf("%d", i);
            i++;
        }

        return 0;
    }

- 5 puta
- 0 puta
- 1 put
- 6 puta
- beskonačno mnogo puta

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i;

        for(i=1; i<=5; i++) {
            if(i == 3) {
                break;
                continue;
            }

            printf("%d ", i);
        }

        return 0;
    }

- ``1 2``
- ``1 2 4 5``
- ``0 1 2``
- ``0 1 2 3 4 5``
- ``1 2 3 4 5``
- ``0 1 2 4 5``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i;

        for(i=1; i<=5; i++) {
            if(i == 3) {
                continue;
                break;
            }

            printf("%d ", i);
        }

        return 0;
    }

- ``1 2 4 5``
- ``1 2``
- ``0 1 2``
- ``0 1 2 3 4 5``
- ``1 2 3 4 5``
- ``0 1 2 4 5``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Ako se uporedi data ``while`` petlja::

    while(i < j) {
        i = 1;
        x--;
        i++;
    }

sa sledećom ``for`` petljom::

    for(i=1; i<j; i++) {
        x--;
    }

može se tvrditi da:

- ove dve petlje nisu ekvivalentne
- ove dve petlje jesu ekvivalentne
- ``for`` petlja nije sintaksno ispravna
- ``while`` petlja nije sintaksno ispravna

----

Ako se uporedi data ``while`` petlja::

    i = 1;
    while(i < j) {
        x--;
        i++;
    }

sa sledećom ``for`` petljom::

    for(i=1; i<j; i++) {
        x--;
    }

može se tvrditi da:

- ove dve petlje jesu ekvivalentne
- ove dve petlje nisu ekvivalentne
- ``for`` petlja nije sintaksno ispravna
- ``while`` petlja nije sintaksno ispravna

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int j;

        for(j=273; j>732; j++)
            printf("PJISP ");

        return 0;
    }

- 0 puta
- 1 put
- 459 puta
- 460 puta
- beskonačno mnogo puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int x = -1;

        for( ; x<=10; x++) {
            if(x < 5)
                continue;
            else
                break;

            printf("PJISP ");
        }

        return 0;
    }

- 0 puta
- 9 puta
- 10 puta
- 11 puta
- beskonačno mnogo puta

----

Šta od navedenog ne može da bude uslov ``while`` petlje, ukoliko je ``lower`` promenljiva tipa ``int``?

- ``if(lower <= 1)``
- ``lower <= 1``
- ``lower + 1``
- ``lower++``
- svi navedeni primeri mogu biti uslov ``while`` petlje

----

Odabrati ispravan ``USLOV``, kojim će se reč "PJISP" ispisati tačno 15 puta na standardni izlaz::

    #include <stdio.h>

    int main() {
        int j;

        for(j=2; USLOV ; j++)
            printf("PJISP ");

        return 0;
    }

- ``j <= 16``
- ``j > 15``
- ``j < 16``
- ``j == 16``
- ``j <= 17``
