Stringovi
=========

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>
    #include <string.h>

    int main() {
        char a[]={'1','2','3','\0','4','\0'};

        printf("%d", strlen(a));

        return 0;
    }

- 3
- 5
- 4
- 6

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>
    #include <string.h>

    int main() {
        char a[]={'1','2','3','0','4','\0'};

        printf("%d", strlen(a));

        return 0;
    }

- 5
- 4
- 6
- 3

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>
    #include <string.h>

    int main() {
        char a[]={'0','1','2','3','\0','4','0'};

        printf("%d", strlen(a));

        return 0;
    }

- 4
- 5
- 6
- 3

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>
    #include <string.h>

    int main() {
        char a[]={'\0','1','2','3','0','4','\0'};

        printf("%d", strlen(a));

        return 0;
    }

- 0
- 5
- 4
- 6
- 3

----

Data je reč ``"0123456789"``, najmanji string u koji se ona može upisati u celosti je:

- ``char str[11]``
- ``char str[9]``
- ``char str[10]``

----

Data je reč ``"012346789"``, najmanji string u koji se ona može upisati u celosti je:

- ``char str[10]``
- ``char str[9]``
- ``char str[11]``

----

Data je reč ``"123456789"``, najmanji string u koji se ona može upisati u celosti je:

- ``char str[10]``
- ``char str[9]``
- ``char str[11]``

----

Data je reč ``"12346789"``, najmanji string u koji se ona može upisati u celosti je:

- ``char str[9]``
- ``char str[10]``
- ``char str[11]``

----

Najmanji string u koji se podatak ``""`` može upisati u celosti je:

- ``char str[1]``
- ``char str[0]``
- ``char str[2]``

----

Kako se sledeći string može ispisati u celosti na standardni izlaz::

    char str[] = "Primer prvog stringa";

- sa oba ponuđena
- isključivo sa ``printf("%s", str);``
- isključivo sa ``puts(str);``

----

Kako se sledeći string može ispisati u celosti na standardni izlaz::

    char str[] = "Primer prvog stringa";

- isključivo sa ``puts(str);``
- isključivo sa ``gets(str);``
- sa oba ponuđena

----

Kako se sledeći string može učitati u celosti sa standardnog ulaza::

    char str[] = "Primer prvog stringa";

- isključivo sa ``gets(str);``
- isključivo sa ``scanf("%s", str);``
- sa oba ponuđena

----

Kako se sledeći string može učitati u celosti sa standardnog ulaza::

    char str[] = "Primer_prvog_stringa";

- sa oba ponuđena
- isključivo sa ``gets(str);``
- isključivo sa ``scanf("%s", str);``

----

Kako se sledeći string može učitati u celosti sa standardnog ulaza::

    char str[] = "Primer prvog stringa";

- isključivo sa ``gets(str);``
- isključivo sa ``puts(str);``
- sa oba ponuđena

----

Nakon poziva funkcije ``strcmp(str1, str2)`` dobili smo povratnu vrednost 0, što nam govori da:

- su ``str1`` i ``str2`` istog sadržaja
- su ``str1`` i ``str2`` različiti
- je ``str1`` manji od ``str2``
- je ``str2`` manji od ``str1``
- smo uspešno kopirali vrednost stringa ``str2`` u ``str1``
- smo uspešno kopirali vrednost stringa ``str1`` u ``str2``

----

Nakon poziva funkcije ``strcmp(str1, str2)`` dobili smo povratnu vrednost 1, što nam govori da:

- su ``str1`` i ``str2`` različiti
- su ``str1`` i ``str2`` istog sadržaja
- smo uspešno kopirali vrednost stringa ``str2`` u ``str1``
- smo uspešno kopirali vrednost stringa ``str1`` u ``str2``
