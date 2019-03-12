Jednostruko spregnute liste
===========================

U poslednjem čvoru jednostruko spregnute liste, vrednost pokazivača na sledeći čvor je:

- ``NULL``
- ``END``
- ``EOF``
- ``FF``
- ``glava``
- ``void``

----

Koju operaciju nad jednostruko spregnutom listom karaktera implementira sledeći deo koda::

    tek = glava;
    while(tek != NULL) {
        printf("%c", tek->znak);

        tek = tek->sledeci;
    }

- listanje liste
- inicijalizacija liste
- unos novog elementa na početak liste
- unos novog elementa na kraj liste
- brisanje elementa iz liste
- brisanje liste

----

Koju operaciju nad jednostruko spregnutom listom karaktera implementira sledeći deo koda::

    tek = glava;
    while(tek != NULL) {
        tek = tek->sledeci;
    }

- prolazak do kraja liste
- inicijalizacija liste
- unos novog elementa na početak liste
- unos novog elementa na kraj liste
- brisanje elementa iz liste
- brisanje liste

----

Koju operaciju nad jednostruko spregnutom listom karaktera implementira sledeći deo koda::

    tek = glava;
    pret = glava;
    while(tek != NULL && (tek->znak != c)) {
        pret = tek;
        tek = tek->sledeci;
    }

- traženje elementa u listi
- inicijalizacija liste
- unos novog elementa na početak liste
- unos novog elementa na kraj liste
- brisanje elementa iz liste
- brisanje liste

----

Koju operaciju nad jednostruko spregnutom listom karaktera implementira sledeći deo koda::

    while(glava != NULL) {
        tek = glava;
        glava = tek->sledeci;

        free(tek);
    }

- brisanje liste
- inicijalizacija liste
- listanje liste
- unos novog elementa na početak liste
- unos novog elementa na kraj liste
- brisanje elementa iz liste

----

Koju operaciju nad jednostruko spregnutom listom karaktera implementira sledeći deo koda::

    int f(BCVOR* node, int t) {
        if(node == NULL)
            return 0;

        if(t == 0)
            return 1;

        return foobar(node->left, t-1) + foobar(node->right, t-1);
    }

- ovo nije operacija nad listom
- inicijalizacija liste
- listanje liste
- unos novog elementa na početak liste
- unos novog elementa na kraj liste
- brisanje elementa iz liste
- brisanje liste
