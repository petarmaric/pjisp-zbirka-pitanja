Tipovi
======

U programskom jeziku C konstante i promenljive mogu biti tipa ``void``.

- netačno
- tačno

----

Kog tipa će biti sledeći izraz::

    (short int)3/3.0

- ``double``
- ``int``
- ``char``
- ``short int``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg
koda, smatrati da se kod izvršava na 32-bitnoj arhitekturi::

    #include <stdio.h>

    int main() {
        printf("%d", sizeof(float));

        return 0;
    }

- 4
- float
- d
- %d
- %d32
- 2
- 16
- 32

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg
koda, smatrati da se kod izvršava na 32-bitnoj arhitekturi::

    #include <stdio.h>

    int main() {
        printf("%d", sizeof(int));

        return 0;
    }

- 4
- int
- d
- %d
- %d32
- 2
- 16
- 32

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 5;
        int b = 3;

        printf("Realni kolicnik a/b je: %d\n", a/b);

        return 0;
    }

- ``Realni kolicnik a/b je: 1``
- ``Realni kolicnik a/b je: 2``
- ``Realni kolicnik a/b je: 1.000000``
- ``Realni kolicnik a/b je: 1.666667``
- ``Realni kolicnik a/b je: 2.000000``
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 5;
        float b = 3;

        printf("Celobrojni kolicnik a/b je: %f\n", a/b);

        return 0;
    }

- ``Celobrojni kolicnik a/b je: 1.666667``
- ``Celobrojni kolicnik a/b je: 1``
- ``Celobrojni kolicnik a/b je: 2``
- ``Celobrojni kolicnik a/b je: 1.000000``
- ``Celobrojni kolicnik a/b je: 2.000000``
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 5;
        int b = 3;

        printf("Celobrojni kolicnik a/b je: %d\n", a%b);

        return 0;
    }

- ``Celobrojni kolicnik a/b je: 2``
- ``Celobrojni kolicnik a/b je: %d``
- ``Celobrojni kolicnik a/b je: 1``
- ``Celobrojni kolicnik a/b je: 1.000000``
- ``Celobrojni kolicnik a/b je: 1.666667``
- ``Celobrojni kolicnik a/b je: 2.000000``
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a = 5;
        float b = 3;

        printf("Celobrojni kolicnik a/b je: %%d\n", a/b);

        return 0;
    }

- ``Celobrojni kolicnik a/b je: %d``
- ``Celobrojni kolicnik a/b je: 1``
- ``Celobrojni kolicnik a/b je: 2``
- ``Celobrojni kolicnik a/b je: 1.000000``
- ``Celobrojni kolicnik a/b je: 1.666667``
- ``Celobrojni kolicnik a/b je: 2.000000``
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        float avr;
        int suma=10, br=3;
        avr = suma/br;

        printf("%f\n", avr);

        return 0;
    }

- 3.000000
- 3.333333
- 3
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        float avr;
        int suma=10, br=3;
        avr = suma/3.0;

        printf("%f\n", avr);

        return 0;
    }

- 3.333333
- 3.000000
- 3
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        float avr;
        int suma=10, br=3;
        avr = (float)suma/br;

        printf("%d\n", 3);

        return 0;
    }

- 3
- 3.333333
- 3.000000
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        float avr;
        int suma=10, br=3;
        avr = (float)suma/br;

        printf("%d\n", avr);

        return 0;
    }

- prilikom kompajliranja dobijamo grešku/upozorenje
- 3
- 3.333333
- 3.000000

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``fahr`` će biti::

    int celsius = 1;
    double fahr;
    fahr = celsius / 5 * 9.0 + 32.0;

- 32.0
- 33.8
- neodređena vrednost

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``fahr`` će biti::

    int celsius;
    double fahr = 1;
    fahr = celsius / 5 * 9.0 + 32.0;

- neodređena vrednost
- 32.0
- 33.8

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``x`` će biti::

    int a;
    int b = 1;
    int x;
    x = a * (a % b) + 10;

- 10
- 11
- 0
- 13
- neodređena vrednost

----

Nakon izvršavanja sledećeg dela koda vrednost promenljive ``x`` će biti::

    int a;
    int b = 3;
    int x;
    x = a * (a % b) + 10;

- neodređena vrednost
- 11
- 0
- 13
- 10

----

Koji od navedenih tipova dozvoljava najvišu numeričku vrednost?

- ``double``
- ``char``
- ``float``
- ``int``
- ``short``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i, j=0, p=1, q=2;

        printf("%d", i*j);

        return 0;
    }

- 0
- 1
- 2
- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)
- prilikom kompajliranja dobijamo grešku/upozorenje

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i, j=0, p=1, q=2;

        printf("%d", i);

        return 0;
    }

- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)
- 0
- 1
- 2
- prilikom kompajliranja dobijamo grešku/upozorenje
