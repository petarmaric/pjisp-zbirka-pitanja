Bitwise operatori
=================

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 72; // 72 == 0100 1000

        while(x = 0) {
            puts("PJISP");

            x>>=1;
        }

        puts("PJISP");

        return 0;
    }

- 1 put
- 3 puta
- 4 puta
- 5 puta
- 6 puta
- 7 puta
- 8 puta
- 16 puta
- beskonačno mnogo puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 72; // 72 == 0100 1000

        while(x != 0) {
            puts("PJISP");

            x>>=1;
        }

        return 0;
    }

- 7 puta
- 1 put
- 3 puta
- 4 puta
- 5 puta
- 6 puta
- 8 puta
- 16 puta
- beskonačno mnogo puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 72; // 72 == 0100 1000

        while(x != 0) {
            puts("PJISP");

            x>>=2;
        }

        return 0;
    }

- 4 puta
- 1 put
- 3 puta
- 5 puta
- 6 puta
- 7 puta
- 8 puta
- 16 puta
- beskonačno mnogo puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 72; // 72 == 0100 1000

        while(x != 0) {
            puts("PJISP");

            x<<=1;
        }

        return 0;
    }

- 5 puta
- 1 put
- 3 puta
- 4 puta
- 6 puta
- 7 puta
- 8 puta
- 16 puta
- beskonačno mnogo puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 72; // 72 == 0100 1000

        while(x != 0) {
            puts("PJISP");

            x<<=2;
        }

        return 0;
    }

- 3 puta
- 1 put
- 4 puta
- 5 puta
- 6 puta
- 7 puta
- 8 puta
- 16 puta
- beskonačno mnogo puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 0x8;

        while(x != 0) {
            puts("PJISP");

            x<<=1;
        }

        return 0;
    }

- 5 puta
- 1 puta
- 3 puta
- 8 puta
- 13 puta
- 16 puta
- beskonačno mnogo puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        short x = 0x8;

        while(x != 0) {
            puts("PJISP");

            x<<=1;
        }

        return 0;
    }

- 13 puta
- 1 puta
- 3 puta
- 5 puta
- 8 puta
- 16 puta
- beskonačno mnogo puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 72; // 72 == 0100 1000

        while(x != 0) {
            puts("PJISP");

            x<<2;
        }

        return 0;
    }

- beskonačno mnogo puta
- 1 put
- 3 puta
- 4 puta
- 5 puta
- 6 puta
- 7 puta
- 8 puta
- 16 puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 72; // 72 == 0100 1000

        while(x != 0) {
            puts("PJISP");

            x>>1;
        }

        return 0;
    }

- beskonačno mnogo puta
- 1 put
- 3 puta
- 4 puta
- 5 puta
- 6 puta
- 7 puta
- 8 puta
- 16 puta

----

Koliko puta će se ispisati reč "PJISP" na standardni izlaz, kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        char x = 72; // 72 == 0100 1000

        while(x = 0) {
            puts("PJISP");

            x>>1;
        }

        puts("PJISP");

        return 0;
    }

- 1 put
- 3 puta
- 4 puta
- 5 puta
- 6 puta
- 7 puta
- 8 puta
- 16 puta
- beskonačno mnogo puta

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        unsigned x = 72; // 72 == 0100 1000
        char i;

        i^=i;
        while(x != 0) {
            i++;
            x<<=1;
        }

        printf("%i", i);

        return 0;
    }

- ``29``
- ``1``
- ``3``
- ``4``
- ``6``
- ``7``
- ``8``
- ``13``
- ``30``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 2;

        if ((a ^ a))
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je a``
- ``Veci je b``
- ništa neće biti ispisano
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 2;

        if (!(a ^ a))
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je b``
- ``Veci je a``
- ništa neće biti ispisano
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 2;

        if (!!(a ^ a))
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je a``
- ``Veci je b``
- ništa neće biti ispisano
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 2;

        if (!!!(a ^ a))
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je b``
- ``Veci je a``
- ništa neće biti ispisano
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Kojim bitwise operatorom se postavlja vrednost željenog bita na 1?

- ``|``
- ``~``
- ``!``
- ``&``
- ``&&``
- ``||``
- ``^``

----

Kojim bitwise operatorom se postavlja vrednost željenog bita na 0?

- ``&``
- ``~``
- ``!``
- ``&&``
- ``|``
- ``||``
- ``^``

----

Kojim bitwise operatorom se dobavlja vrednost željenog bita?

- ``&``
- ``~``
- ``!``
- ``&&``
- ``|``
- ``||``
- ``^``

----

Kojim bitwise operatorom se invertuje vrednost željenog bita?

- ``^``
- ``~``
- ``!``
- ``&``
- ``&&``
- ``|``
- ``||``

----

Koja će biti vrednost izraza ``1 & 31``?

- 1
- 0
- 30
- 31
- 32
- 33

----

Koja će biti vrednost izraza ``0 && 31``?

- 0
- 1
- 30
- 31
- 32
- 33

----

Koja će biti vrednost izraza ``1 | 32``?

- 33
- 0
- 1
- 30
- 31
- 32

----

Koja će biti vrednost izraza ``0 || 31``?

- 31
- 0
- 1
- 30
- 32
- 33

----

Koja će biti vrednost izraza ``1 ^ 31``?

- 30
- 0
- 1
- 31
- 32
- 33
