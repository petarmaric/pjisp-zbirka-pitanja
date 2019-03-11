Argumenti komandne linije
=========================

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda,
ukoliko je dobijena izvršna datoteka pokrenuta komandom ``./program a b``::

    #include <stdio.h>

    int main(int num_args, char *args[]) {
       puts(args[0]);

       return 0;
    }

- ``./program``
- ``./program a``
- ``./program a b``
- ``a``
- ``a b``
- ``b``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda,
ukoliko je dobijena izvršna datoteka pokrenuta komandom ``./program a``::

    #include <stdio.h>

    int main(int num_args, char *args[]) {
        puts(args[1]);

        return 0;
    }

- ``a``
- ``./program``
- ``./program a``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda,
ukoliko je dobijena izvršna datoteka pokrenuta komandom ``./program a``::

    #include <stdio.h>

    int main(int num_args, char *args[]) {
        printf("%d, %s", num_args, args[1]);

        return 0;
    }

- ``2, a``
- ``1, a``
- ``1, ./program``
- ``2, ./program``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda,
ukoliko je dobijena izvršna datoteka pokrenuta komandom ``./program a``::

    #include <stdio.h>

    int main(int num_args, char *args[]) {
        printf("%d, %s", num_args, args[0]);

        return 0;
    }

- ``2, ./program``
- ``1, a``
- ``2, a``
- ``1, ./program``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda,
ukoliko je dobijena izvršna datoteka pokrenuta komandom ``./program a b c d``::

    #include <stdio.h>

    int main(int num_args, char *args[]) {
        char **p = args;

        puts(*args);

        return 0;
    }

- ``./program``
- ``./program a b c d``
- ``a``
- ``b``
- ``c``
- ``d``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda,
ukoliko je dobijena izvršna datoteka pokrenuta komandom ``./program a b c d``::

    #include <stdio.h>

    int main(int num_args, char *args[]) {
        char **p = args;

        puts(*(args+num_args-1));

        return 0;
    }

- ``d``
- ``./program``
- ``./program a b c d``
- ``a``
- ``b``
- ``c``
- ``d c b a ./program``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda,
ukoliko je dobijena izvršna datoteka pokrenuta komandom ``./program a b``::

    #include <stdio.h>

    int main(int num_args, char **args) {
        char **p = args;

        while(num_args) {
            printf("%s ", *args);

            num_args--;
        }

        return 0;
    }

- ``./program ./program ./program``
- ``./program``
- ``./program ./program``
- ``./program a b``
- ``a b``
- ``b a``
- ``b a ./program``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda,
ukoliko je dobijena izvršna datoteka pokrenuta komandom ``./program a b``::

    #include <stdio.h>

    int main(int num_args, char **args) {
        char **p = args;

        while(num_args) {
            num_args--;

            printf("%s ", *(args+num_args));
        }

        return 0;
    }

- ``b a ./program``
- ``./program``
- ``./program ./program``
- ``./program ./program ./program``
- ``./program a b``
- ``a b``
- ``b a``
