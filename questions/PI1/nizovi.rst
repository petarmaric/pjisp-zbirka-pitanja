Nizovi
======

Odabrati ispravan ``USLOV``::

    do {
        printf("Unesite broj elemenata");
        scanf("%d", &n);
    } while( USLOV );

- ``n <= 0 || n >  MAX_SIZE``
- ``n <  0 || n >  MAX_SIZE``
- ``n <  0 || n >= MAX_SIZE``
- ``n >= 0 || n <  MAX_SIZE``
- ``n <= 0 && n >  MAX_SIZE``
- ``n <  0 && n >  MAX_SIZE``
- ``n <  0 && n >= MAX_SIZE``
- ``n >= 0 && n <  MAX_SIZE``

----

Kako se može deklarisati niz celobrojnih vrednosti sa jednim članom?

- ``int niz[1];``
- ``int niz(1);``
- ``int niz{1};``
- nije moguće deklarisati niz sa jednim članom

----

Kako se pravilno deklariše celobrojni niz ``a``?

- ``int a[5];``
- ``int [5]a;``
- ``int a;[5];``
- ``int [a:5];``
- ``int []a;``
- ``int a(5);``
- ``int a{5};``

----

Kako se pravilno učitava drugi član celobrojnog niza ``a``?

- ``scanf("%d", &a[1]);``
- ``scanf(&a[2]);``
- ``scanf("%d", %a[2]);``
- ``scanf("%d", a[1]);``
- ``scanf("%d", &a+1);``
- ``scanf("%d", *a+1);``
- ``scanf("%d", a+2);``
- ``scanf("%d", &a[2]);``
- ``scanf("%d", &(a+1));``
- ``scanf("d", &a[2]);``

----

Kako se pravilno učitava prvi član celobrojnog niza ``a``?

- ``scanf("%d", &a[0]);``
- ``scanf(&a[1]);``
- ``scanf("%d", %a[1]);``
- ``scanf("%d", a[0]);``
- ``scanf("%d", &a);``
- ``scanf("%d", *a);``
- ``scanf("%d", a+1);``
- ``scanf("%d", &a[1]);``
- ``scanf("%d", &(a+1));``
- ``scanf("d", &a[1]);``

----

Odabrati ispravan ``SNIPPET`` za ispis niza u obrnutom redosledu::

    for (SNIPPET) {
        printf("a[%d] = %d\n", j, a[j]);
    }

- ``j = n-1; j >= 0; j--``
- ``i = n-1; i >= 0; i--``
- ``j = n-1; j > 0; j--``
- ``i = n-1; i > 0; i--``
- ``j = n; j >= 0; j--``
- ``i = n; i >= 0; i--``
- ``j = n; j > 0; j--``
- ``i = n; i > 0; i--``
- ``j = n-1; j > 0; j++``
- ``i = n-1; i > 0; i++``

----

Odabrati ispravan ``SNIPPET`` za ispis svakog 3. člana niza::

    for (SNIPPET) {
        printf("a[%d] = %d\n", j, a[j]);
    }

- ``j = 0; j < n; j+=3``
- ``i = 0; i < n; i+=3``
- ``i = 0; i < n; i++3``
- ``i = 0; i < n; i+3``
- ``j = 0; j < n; j+3``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i=1;
        int a[10]={-2,-1,0,1,2,3,4,5,8,0};

        printf("%d", a[i]);

        return 0;
    }

- -1
- -2
- 0
- 1
- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i=4;
        int a[10]={-2,-1,0,1,2,3,4,5,8,0};

        printf("%d", a[i]);

        return 0;
    }

- 2
- -1
- 0
- 1
- 3
- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i;
        int a[10];

        for (i=0;i<10;i++){
            a[i]=0;
            if(i==2 || i==4)
                a[i]=5;
        }

        printf("%d", a[0]+a[1]+a[2]);

        return 0;
    }

- 5
- 0
- 10
- 1
- 15
- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i;
        int a[10];

        for (i=0;i<10;i++){
            a[i]=0;
            if(i<2)
                a[i]=5;
        }

        printf("%d", a[0]+a[1]+a[2]);

        return 0;
    }

- 10
- 0
- 5
- 1
- 15
- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i, a[10];

        for(i=0;i<10;i++)
            a[i]=i+2;

        printf("%d", a[0]+a[5]);

        return 0;
    }

- 9
- 0
- 2
- 5
- 7

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a[10];

        printf("%d", a[0]);

        return 0;
    }

- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)
- 0
- 1
- 10

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int a[5];
        for (i=2;i<5;i++)
            a[i]=5;

        printf("%d", a[0]);

        return 0;
    }

- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)
- 0
- 1
- 5
- 10

----

Kako se može uneti prvih 8 vrednosti niza realnih brojeva ``a``?

- ``for(i=0;i<8;i++) scanf("%f",&a[i]);``
- ``for(i=0;i<8;i++) scanf("%f",a[i]);``
- ``for(i=0;i<9;i++) scanf("%f",a[i]);``
- ``for(i=0;i<9;i++) scanf("%f",&a[i]);``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i;
        int a[5];
        int suma=0;

        for (i=2;i<5;i++)
            a[i]=5;
            suma += a[i];

        printf("%d", suma);

        return 0;
    }

- ne možemo znati koji broj će biti ispisan (vrednost zatečena u memoriji)
- 5
- 10
- 15
- 25

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int j = 2;
        int a[7] = {0, 1, 2, 3, 2, 1, 0};

        while(a[i] != a[j]) i++; j++; printf("%d %d ", a[i], a[j]);

        return 0;
    }

- ``2 3``
- ``0``
- ``1``
- ``2``
- ``0 2 1 3``
- program će prilikom izvršavanja ući u beskonačnu petlju

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        int i = 0;
        int j = 2;
        int a[7] = {0, 1, 2, 3, 2, 1, 0};

        while(a[i] = a[j]) i++; j++; printf("%d %d ", a[i], a[j]);

        return 0;
    }

- program će prilikom izvršavanja ući u beskonačnu petlju
- ``2 1``
- ``2 3``
- ``0 3``
- ``0 1``
- ``1 2``
