Datoteke
========

U programskom jeziku C za pristup datotekama koriste se:

- funkcije standardne biblioteke
- naredbe programskog jezika
- programski jezik C ne podržava rad sa datotekama, već samo sa standardnim tokovima podataka

----

Kog tipa treba biti promenljiva ``abc`` u sledećem delu koda::

    xyz = fopen(abc, "w");
    if(xyz == NULL) {
        exit(EXIT_FAILURE);
    }

- string (tj. ``char *``)
- ``char``
- ``FILE``
- ``FILE *``
- ``float``
- ``int``
- ``unsigned``
- režim za čitanje
- režim za pisanje
- režim za dodavanje

----

Kog tipa treba biti promenljiva ``xyz`` u sledećem delu koda::

    xyz = fopen(abc, "w");
    if(xyz == NULL) {
        exit(EXIT_FAILURE);
    }

- ``FILE *``
- ``char``
- ``FILE``
- ``float``
- ``int``
- string (tj. ``char *``)
- ``unsigned``
- režim za čitanje
- režim za pisanje
- režim za dodavanje

----

Šta će biti sadržaj tekstualne datoteke "pjisp.txt" nakon izvršavanja sledećeg
koda, ukoliko je u datoteci prethodno bio zapisan tekst "123"::

    #include <stdio.h>

    int main() {
        FILE *out = fopen("pjisp.txt", "a");
        fprintf(out, "456");

        fclose(out);

        return 0;
    }

- ``123456``
- ``123``
- ``456``
- ``456123``
- datoteka će biti prazna

----

Šta će biti sadržaj tekstualne datoteke "pjisp.txt" nakon izvršavanja sledećeg
koda, ukoliko je u datoteci prethodno bio zapisan tekst "123"::

    #include <stdio.h>

    int main() {
        FILE *out = fopen("pjisp.txt", "w");
        fprintf(out, "456");

        fclose(out);

        return 0;
    }

- ``456``
- ``123``
- ``123456``
- ``456123``
- datoteka će biti prazna

----

Šta će biti sadržaj tekstualne datoteke "pjisp.txt" nakon izvršavanja sledećeg
koda, ukoliko je u datoteci prethodno bio zapisan tekst "123"::

    #include <stdio.h>

    int main() {
        FILE *out = fopen("pjisp.txt", "r");
        fprintf(out, "456");

        fclose(out);

        return 0;
    }

- ``123``
- ``456``
- ``123456``
- ``456123``
- datoteka će biti prazna

----

Šta će biti sadržaj tekstualne datoteke "pjisp.txt" nakon izvršavanja sledećeg
koda, ukoliko je u datoteci prethodno bio zapisan tekst "123"::

    #include <stdio.h>

    int main() {
        FILE *out = fopen("pjisp.txt", "w");
        fprintf(stdout, "456");

        fclose(out);

        return 0;
    }

- datoteka će biti prazna
- ``123``
- ``456``
- ``123456``
- ``456123``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg
koda, ukoliko je u datoteci "pjisp.txt" prethodno bio zapisan tekst "123456"::

    #include <stdio.h>

    #define BUFF_SIZE 4096

    int main() {
        char buff[BUFF_SIZE];
        FILE *in = fopen("pjisp.txt", "r");

        fscanf(in, "%c", buff);
        printf("%c", *buff);

        fclose(in);

        return 0;
    }

- ``1``
- ``12``
- ``123``
- ``1234``
- ``12345``
- ``123456``
- ništa neće biti ispisano

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg
koda, ukoliko je u datoteci "pjisp.txt" prethodno bio zapisan tekst "123 456"::

    #include <stdio.h>

    #define BUFF_SIZE 4096

    int main() {
        char buff[BUFF_SIZE];
        FILE *in = fopen("pjisp.txt", "r");

        fscanf(in, "%s", buff);
        printf("%s", buff);

        fclose(in);

        return 0;
    }

- ``123``
- ``1``
- ``12``
- ``1234``
- ``12345``
- ``123456``
- ništa neće biti ispisano
