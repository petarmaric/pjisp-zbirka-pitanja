Dvostruko spregnute liste
=========================

U poslednjem čvoru dvostruko spregnute liste, vrednost pokazivača na sledeći čvor je:

- ``NULL``
- ``END``
- ``EOF``
- ``FF``
- ``glava``
- ``void``

----

Koju operaciju nad dvostruko spregnutom listom implementira sledeći deo koda::

    typedef struct element_st {
        int broj;

        struct element_st *pret;
        struct element_st *sled;
    } ELEMENT;

    typedef struct lista_st {
        ELEMENT *prvi;
        ELEMENT *posl;
    } LISTA;

    // ... nebitan kod ...

    LISTA *lst;

    // ... nebitan kod ...

    ELEMENT *tek;
    for (tek=lst.posl; tek; tek=tek->pret);

- obilazak liste unazad
- inicijalizacija liste
- obilazak liste unapred
- unos novog elementa na početak liste
- unos novog elementa na kraj liste
- brisanje elementa iz liste
- brisanje liste

----

Koju operaciju nad dvostruko spregnutom listom implementira sledeći deo koda::

    typedef struct element_st {
        int broj;

        struct element_st *pret;
        struct element_st *sled;
    } ELEMENT;

    typedef struct lista_st {
        ELEMENT *prvi;
        ELEMENT *posl;
    } LISTA;

    // ... nebitan kod ...

    LISTA *lst;

    // ... nebitan kod ...

    ELEMENT *tek;
    for (tek=lst.prvi; tek; tek=tek->sled);

- obilazak liste unapred
- inicijalizacija liste
- obilazak liste unazad
- unos novog elementa na početak liste
- unos novog elementa na kraj liste
- brisanje elementa iz liste
- brisanje liste

----

Drugi naziv za dvostruko spregnute liste je:

- simetrična lista
- lista sa zaglavljem
- pokazivačka lista
- težinska lista

----

Za operaciju brisanja čvora iz dvostruko spregnute liste dovoljno je znati:

- pokazivač na čvor koji brišemo (``TEKUCI``)
- pokazivač na prethodni čvor (``PRETHODNI``)
- pokazivač na prethodni čvor (``PRETHODNI``) i pokazivač na čvor koji brišemo (``TEKUCI``)
- pokazivač na sledeci čvor (``SLEDECI``)
- pokazivač na sledeci čvor (``SLEDECI``) i pokazivač na čvor koji brišemo (``TEKUCI``)
- pokazivač na sledeci čvor (``SLEDECI``) i pokazivač na prethodni čvor (``PRETHODNI``)
