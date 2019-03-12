Vektori
=======

Za identifikaciju pojedine pozicije u vektoru koristi se:

- indeks
- pokazivač
- generički pokazivač
- viseći pokazivač

----

Dvodimenzionalna generalizacija vektora zove se:

- matrica
- binarno stablo
- stek
- dek

----

Čemu je ekvivalentan izraz ``p[i][j]``, ako je dvostruki pokazivač ``p`` definisan na sledeći način::

    int **p;
    p = calloc(10, sizeof(int*));

- ``*(*(p+i)+j)``
- ``*(*p+i+j)``
- ``**(p+i+j)``
- ``**p+i+j``
- ``**p+(i+j)``
- ``*p+(i+j)``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>
    #include <stdlib.h>

    int main() {
        int n;
        printf("n = ");
        scanf("%d", &n);

        int **a;
        a = calloc(n, sizeof(int*));
        if(a == NULL) {
            puts("Greska 1 prilikom zauzimanja memorije!");
            exit(41);
        }

        int i, j;
        for (i=0; i<n; i++) {
            *(a+i) = calloc(n, sizeof(int));
            if(*(a+i) == NULL) {
                puts("Greska 2 prilikom zauzimanja memorije!");
                exit(42);
            }

            for (j=0; j<n; j++) {
                *(*(a+i)+j) = rand()/((double)RAND_MAX + 1) * 10;
            }
        }

        for (i=0; i<n; i++) {
            for (j=0; j<n; j++) {
                printf("%d ", *(*(a+i)+j));
            }

            printf("\n");
        }

        return 0;
    }

- sadržaj matrice vrstu po vrstu
- sadržaj matrice vrstu po vrstu, a potom glavna dijagonala, sleva-udesno
- sadržaj matrice vrstu po vrstu, a potom sporedna dijagonala, sleva-udesno
- glavna dijagonala sdesna-ulevo
- glavna dijagonala sleva-udesno
- sporedna dijagonala sdesna-ulevo
- sporedna dijagonala sleva-udesno

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>
    #include <stdlib.h>

    int main() {
        int n;
        printf("n = ");
        scanf("%d", &n);

        int **a;
        a = calloc(n, sizeof(int*));
        if(a == NULL) {
            puts("Greska 1 prilikom zauzimanja memorije!");
            exit(41);
        }

        int i, j;
        for (i=0; i<n; i++) {
            *(a+i) = calloc(n, sizeof(int));
            if(*(a+i) == NULL) {
                puts("Greska 2 prilikom zauzimanja memorije!");
                exit(42);
            }

            for (j=0; j<n; j++) {
                *(*(a+i)+j) = rand()/((double)RAND_MAX + 1) * 10;
            }
        }

        for (i=0; i<n; i++) {
            for (j=0; j<n; j++) {
                printf("%d ", *(*(a+i)+j));
            }

            printf("\n");
        }

        for (i=n-1; i>=0; i--) {
            printf("%d ", *(*(a+i)+n-1-i));
        }
        printf("\n");

        return 0;
    }

- sadržaj matrice vrstu po vrstu, a potom sporedna dijagonala, sleva-udesno
- sadržaj matrice vrstu po vrstu
- sadržaj matrice vrstu po vrstu, a potom glavna dijagonala, sleva-udesno
- glavna dijagonala sdesna-ulevo
- glavna dijagonala sleva-udesno
- sporedna dijagonala sdesna-ulevo
- sporedna dijagonala sleva-udesno
