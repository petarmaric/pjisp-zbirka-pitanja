Znakovi
=======

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // 'j' == 106
        // 'k' == 107

        char promenljiva_1 = 'j';
        int promenljiva_2;
        int promenljiva_3 = 1;

        printf("%c", promenljiva_1 + promenljiva_3);

        return 0;
    }

- ``k``
- ``j``
- ``106``
- ``107``
- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // 'j' == 106
        // 'k' == 107

        char promenljiva_1 = 'j';
        int promenljiva_2;
        int promenljiva_3 = 1;

        printf("%d", promenljiva_1 + promenljiva_3);

        return 0;
    }

- ``107``
- ``j``
- ``k``
- ``106``
- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // 'j' == 106
        // 'k' == 107

        char promenljiva_1 = 'j';
        int promenljiva_2;
        int promenljiva_3 = 1;

        printf("%d", promenljiva_1 + promenljiva_2);

        return 0;
    }

- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)
- ``j``
- ``k``
- ``106``
- ``107``

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // 'J' ==  74
        // 'K' ==  75
        // 'j' == 106
        // 'k' == 107

        char promenljiva_1 = 'j';
        int promenljiva_2 = -32;
        int promenljiva_3 = 1;

        printf("%c", promenljiva_1 + promenljiva_2 + promenljiva_3);

        return 0;
    }

- ``K``
- ``J``
- ``j``
- ``k``
- ``106``
- ``107``
- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // 'J' ==  74
        // 'K' ==  75
        // 'j' == 106
        // 'k' == 107

        char promenljiva_1 = 'j';
        int promenljiva_2 = -32;
        int promenljiva_3 = 1;

        printf("%c", promenljiva_1 + promenljiva_2);

        return 0;
    }

- ``J``
- ``K``
- ``j``
- ``k``
- ``106``
- ``107``
- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // '1' ==  49
        // '2' ==  50
        // 'b' ==  98

        char promenljiva_1 = '1';
        int promenljiva_2;
        int promenljiva_3 = 1;

        printf("%c", promenljiva_1 + promenljiva_3);

        return 0;
    }

- ``2``
- ``1``
- ``11``
- ``b``
- ``49``
- ``50``
- ``98``
- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // '1' ==  49
        // '2' ==  50
        // 'b' ==  98

        char promenljiva_1 = '1';
        int promenljiva_2;
        int promenljiva_3 = '1';

        printf("%c", promenljiva_1 + promenljiva_3);

        return 0;
    }

- ``b``
- ``1``
- ``2``
- ``11``
- ``49``
- ``50``
- ``98``
- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // '1' ==  49
        // '2' ==  50
        // 'b' ==  98

        char promenljiva_1 = '1';
        int promenljiva_2;
        int promenljiva_3 = '1';

        printf("%d", promenljiva_1 + promenljiva_3);

        return 0;
    }

- ``98``
- ``1``
- ``2``
- ``11``
- ``b``
- ``49``
- ``50``
- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)

----

Šta će biti ispisano na standardni izlaz kao rezultat izvršavanja sledećeg koda::

    #include <stdio.h>

    int main() {
        // '1' ==  49
        // '2' ==  50
        // 'b' ==  98

        char promenljiva_1 = '1';
        int promenljiva_2;
        int promenljiva_3 = '1';

        printf("%c", promenljiva_1 + promenljiva_2);

        return 0;
    }

- ne možemo znati koji podatak će biti ispisan (vrednost zatečena u memoriji)
- ``1``
- ``2``
- ``11``
- ``b``
- ``49``
- ``50``
- ``98``

----

Koji od navedenih znakova nije podržan u tipu ``char``?

- svi navedeni znakovi su podržani
- ``'0'``
- ``'Q'``
- ``'#'``
- ``'?'``
- ``'%'``
