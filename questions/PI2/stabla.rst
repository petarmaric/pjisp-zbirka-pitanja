Stabla
======

Kod kompletnog stabla (reda n):

- svi elementi, osim listova, imaju izlazni stepen n
- svi putevi od korena do listova su iste dužine
- broj elemenata na istom nivou stabla razlikuje se najviše za 1

----

Obilazak binarnog stabla u sledećem redosledu je::

    pristupi levom podstablu
    pristupi desnom podstablu
    pristupi nadredjenom

- obilazak sa dna ka vrhu
- obilazak sa vrha ka dnu
- obilazak sleva-udesno

----

Obilazak binarnog stabla u sledećem redosledu je::

    pristupi nadredjenom
    pristupi levom podstablu
    pristupi desnom podstablu

- obilazak sa vrha ka dnu
- obilazak sa dna ka vrhu
- obilazak sleva-udesno

----

Kako se naziva orijentisani skup čvorova uopštenog stabla, koji su povezani granama:

- put
- lanac
- graf
- digraf

----

Koju operaciju nad binarnim stablom pristupa, uređenim tako da vrednost
elemenata ne opada prilikom obilaska stabla sleva-udesno, implementira sledeći
deo koda::

    int f(BCVOR* node) {
        while (node->left != NULL) {
            node = node->left;
        }

        return node->data;
    }

- pronalaženje najmanje vrednosti u stablu
- balansiranje stabla
- određivanje maksimalne dubine stabla
- proverava da li postoji putanja od korena do lista sa zadatom sumom elemenata
- računanje broja elemenata na zadatom nivou stabla
- računanje broja elemenata u stablu
- računanje sume elemenata stabla
- zamenu levog i desnog podstabla, za svaki element u stablu

----

Koju operaciju nad binarnim stablom pristupa, uređenim tako da vrednost
elemenata ne opada prilikom obilaska stabla sleva-udesno, implementira sledeći
deo koda::

    int f(BCVOR* node) {
        while (node->right != NULL) {
            node = node->right;
        }

        return node->data;
    }

- pronalaženje najveće vrednosti u stablu
- balansiranje stabla
- određivanje maksimalne dubine stabla
- proverava da li postoji putanja od korena do lista sa zadatom sumom elemenata
- računanje broja elemenata na zadatom nivou stabla
- računanje broja elemenata u stablu
- računanje sume elemenata stabla
- zamenu levog i desnog podstabla, za svaki element u stablu

----

Koju operaciju nad binarnim stablom pristupa, uređenim tako da vrednost
elemenata ne opada prilikom obilaska stabla sleva-udesno, implementira sledeći
deo koda::

    int f(BCVOR* node) {
        if (node == NULL) {
            return 0;
        }

        int l = f(node->left);
        int r = f(node->right);

        return 1 + ((l > r) ? l : r);
    }

- određivanje maksimalne dubine stabla
- balansiranje stabla
- pronalaženje najmanje vrednosti u stablu
- proverava da li postoji putanja od korena do lista sa zadatom sumom elemenata
- računanje broja elemenata na zadatom nivou stabla
- računanje broja elemenata u stablu
- računanje sume elemenata stabla
- zamenu levog i desnog podstabla, za svaki element u stablu

----

Koju operaciju nad binarnim stablom pristupa, uređenim tako da vrednost
elemenata ne opada prilikom obilaska stabla sleva-udesno, implementira sledeći
deo koda::

    int f(BCVOR* node) {
        if (node == NULL) {
            return 0;
        }

        return 1 + f(node->left) + f(node->right);
    }

- računanje broja elemenata u stablu
- balansiranje stabla
- određivanje maksimalne dubine stabla
- pronalaženje najmanje vrednosti u stablu
- proverava da li postoji putanja od korena do lista sa zadatom sumom elemenata
- računanje broja elemenata na zadatom nivou stabla
- računanje sume elemenata stabla
- zamenu levog i desnog podstabla, za svaki element u stablu

----

Koju operaciju nad binarnim stablom pristupa, uređenim tako da vrednost
elemenata ne opada prilikom obilaska stabla sleva-udesno, implementira sledeći
deo koda::

    int f(BCVOR* node) {
        if (node == NULL) {
            return 0;
        }

        return node->data + f(node->left) + f(node->right);
    }

- računanje sume elemenata stabla
- balansiranje stabla
- određivanje maksimalne dubine stabla
- pronalaženje najmanje vrednosti u stablu
- proverava da li postoji putanja od korena do lista sa zadatom sumom elemenata
- računanje broja elemenata na zadatom nivou stabla
- računanje broja elemenata u stablu
- zamenu levog i desnog podstabla, za svaki element u stablu

----

Koju operaciju nad binarnim stablom pristupa, uređenim tako da vrednost
elemenata ne opada prilikom obilaska stabla sleva-udesno, implementira sledeći
deo koda::

    int f(BCVOR* node, int t) {
        if(node == NULL)
            return 0;

        if(t == 0)
            return 1;

        return f(node->left, t-1) + f(node->right, t-1);
    }

- računanje broja elemenata na zadatom nivou stabla
- balansiranje stabla
- određivanje maksimalne dubine stabla
- pronalaženje najmanje vrednosti u stablu
- proverava da li postoji putanja od korena do lista sa zadatom sumom elemenata
- računanje broja elemenata u stablu
- računanje sume elemenata stabla
- zamenu levog i desnog podstabla, za svaki element u stablu
