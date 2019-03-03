Nizovi i pokazivači
===================

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a[10] = {0, 1, 2, 3, 4, 5, 6, 8, 9, 0};

        int *p = a;
        while(*p) {
            printf("%d", i);

            p++;
            i++;
        }

        return 0;
    }

- 0 puta
- 1 put
- 10 puta
- 11 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a[10] = {-2, -1, 0, 1, 2, 3, 4, 5, 8, 0};

        int *p = a;
        while(*p) {
            printf("%d", i);

            p++;
            i++;
        }

        return 0;
    }

- 2 puta
- 0 puta
- 1 put
- 10 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};

        int *p = a;
        while(*p) {
            printf("%d", i);

            p++;
            i++;
        }

        return 0;
    }

- 9 puta
- 0 puta
- 1 put
- 10 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0};

        int *p = a;
        while(*p) {
            printf("%d", i);

            p++;
            i++;
        }

        return 0;
    }

- 10 puta
- 0 puta
- 9 puta
- 11 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0};

        int *p = a + 1;
        while(*p){
            printf("%d", i);

            p++;
            i++;
        }

        return 0;
    }

- 9 puta
- 0 puta
- 10 puta
- 11 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a[10] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};

        int *p = a;
        while(*p-4){
            printf("%d", i);

            p++;
            i++;
        }

        return 0;
    }

- 5 puta
- 0 puta
- 6 puta
- 9 puta
- 11 puta
- beskonačno mnogo puta

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a[10] = {9, 8, 7, 6, 5, 4, 3, 2, 0};

        int *p = a;
        while(*(p+4)) {
            printf("%d", i);

            p++;
            i++;
        }

        return 0;
    }

- 4 puta
- 0 puta
- 5 puta
- 6 puta
- 9 puta
- 11 puta
- beskonačno mnogo puta

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};

        int *p = a;
        while(*p){
            p++;
            i--;
        }

        printf("%d", i);

        return 0;
    }

- ``1``
- ``0``
- ``5``
- ``6``
- ``9``
- ``11``
- ništa neće biti ispisano, zbog beskonačne petlje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int j = 2;
        int a[7] = {0, 1, 2, 3, 2, 1, 0};

        while(a+i != a+j) i++; j--; printf("%d %d ", a[i], a[j]);

        return 0;
    }

- ``2 1``
- ``0 0``
- ``0 2``
- ``1 0``
- ``2 3``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int j = 2;
        int a[7] = {0, 1, 2, 3, 2, 1, 0};

        while(a+i != a+j) i++; j++; printf("%d %d ", a[i], a[j]);

        return 0;
    }

- ``2 3``
- ``0 1``
- ``0 2``
- ``1 2``
- ``2 1``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int j = 2;
        int a[7] = {0, 1, 2, 3, 2, 1, 0};

        while(a+i == a+j) i++; j++; printf("%d %d ", a[i], a[j]);

        return 0;
    }

- ``0 3``
- ``0 1``
- ``1 2``
- ``2 1``
- ``2 3``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 10;
        int a[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 0};

        int *p = a;
        while(*p) {
            p += *p;
            i--;
        }

        printf("%d", i);

        return 0;
    }

- ``1``
- ``0``
- ``3``
- ``6``
- ``9``
- ``11``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i;
        int a[10] = {2, 1, 10, 7, 10, 0, 8, 3, 9, 5};

        int *p = a + 2;
        for(i=0; i<10; i++)
            a[i] = i + 2;

        printf("%d", *p);

        return 0;
    }

- ``4``
- ``0``
- ``1``
- ``2``
- ``10``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Koliko puta će se izvršiti telo petlje u sledećem kodu::

    #include <stdio.h>

    int main() {
        int i = 5;
        int a[10] = {-4, -2, 0, 1, 2, 3, 4, 5, 8, 0};

        int *p = a + 2;
        do {
            printf("%d", i);

            p++;
            i--;
        } while(*p);

        return 0;
    }

- 7 puta
- 0 puta
- 1 put
- 2 puta
- 5 puta
- 8 puta
- 10 puta
- beskonačno mnogo puta
