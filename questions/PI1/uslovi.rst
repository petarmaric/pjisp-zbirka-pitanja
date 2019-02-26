Uslovi
======

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 2;
        int b = 1;

        if (a = b)
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je b``
- ``Veci je a``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 2;

        if (a==b)
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je a``
- ``Veci je b``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 2;
        int b = 1;

        if (a > b)
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je b``
- ``Veci je a``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 0;

        if (a ? b : a)
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je a``
- ``Veci je b``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 0;
        int b = 1;

        if ((a > b) ? a : b)
            printf("Veci je b");
        else
            printf("Veci je a");

        return 0;
    }

- ``Veci je b``
- ``Veci je a``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int ocena = 1;

        switch (ocena) {
            case 5:  printf("Odlican!");
            case 4:  printf("Vrlo dobar!");
            case 3:  printf("Dobar!");
            case 2:  printf("Dovoljan!");
            case 1:  printf("Nedovoljan!");
            default: printf("Ocena mora biti izmedju 1 i 5.");
        }

        return 0;
    }

- ``Nedovoljan!Ocena mora biti izmedju 1 i 5.``
- ``Nedovoljan!``
- ``Ocena mora biti izmedju 1 i 5.``
- ništa neće biti ispisano

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int ocena = 3;

        switch (ocena) {
            case 5:  break;printf("Odlican!");
            case 4:  break;printf("Vrlo dobar!");
            case 3:  break;printf("Dobar!");
            case 2:  break;printf("Dovoljan!");
            case 1:  break;printf("Nedovoljan!");
            default: break;printf("Ocena mora biti izmedju 1 i 5.");
        }

        return 0;
    }

- ništa neće biti ispisano
- ``Dobar!Ocena mora biti izmedju 1 i 5.``
- ``Dobar!``
- ``Ocena mora biti izmedju 1 i 5.``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 0;

        if (!b)
            printf("Jednaki! ");
        else
            printf("Razliciti! ");
        printf("%d\n", b);

        return 0;
    }

- ``Jednaki! 0``
- ``Razliciti! 1``
- ``Razliciti! 0``
- ``Jednaki! 1``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 0;

        if (b = a)
            printf("Jednaki! ");
        else
            printf("Razliciti! ");
        printf("%d\n", b);

        return 0;
    }

- ``Jednaki! 1``
- ``Razliciti! 1``
- ``Razliciti! 0``
- ``Jednaki! 0``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 1;
        int b = 0;

        if (a = b)
            printf("Jednaki! ");
        else
            printf("Razliciti! ");
        printf("%d\n", a);

        return 0;
    }

- ``Razliciti! 0``
- ``Jednaki! 1``
- ``Razliciti! 1``
- ``Jednaki! 0``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 5;
        int b = 3;

        if ((b > a) || (b = a))
            printf("Manje! ");
        else
            printf("Vece! ");
            printf("Razlicito! ");

        return 0;
    }

- ``Manje! Razlicito!``
- ``Manje!``
- ``Vece! Razlicito!``
- ``Razlicito!``
- ``Vece!``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 5;
        int b = 3;

        if ((b > a) || (b == a))
            printf("Manje! ");
        else
            printf("Vece! ");
            printf("Razlicito! ");

        return 0;
    }

- ``Vece! Razlicito!``
- ``Manje!``
- ``Razlicito!``
- ``Vece!``
- ``Manje! Razlicito!``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 5;
        int b = 3;

        if (b = a)
            printf("Manje! ");
        else if (b < a)
            printf("Vece! ");
            printf("Razlicito! ");

        return 0;
    }

- ``Manje! Razlicito!``
- ``Manje!``
- ``Vece! Razlicito!``
- ``Razlicito!``
- ``Vece!``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int x = -3;

        if (x + 3)
            printf("istina");
        else
            printf("neistina");

        return 0;
    }

- ``neistina``
- ``istina``
- ``istinaneistina``
- ništa neće biti ispisano
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg dela koda::

    int x = 10, y = 20, z = 30;
    if(x == 10) x = 20; y = 30; z = 40;
    if(y == 20) x = 30; y = 40; z = 50;
    if(z == 50) x = 10; y = 20; z = 30;

    printf("%d %d %d", x, y, z);

- ``10 20 30``
- ``30 40 50``
- ``20 30 40``
