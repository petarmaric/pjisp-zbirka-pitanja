Dinamičko upravljanje memorijom
===============================

U programskom jeziku C za dinamičko upravljanje memorijom koriste se:

- funkcije standardne biblioteke
- naredbe programskog jezika
- programski jezik C ne podržava dinamičko upravljanje memorijom

----

Kako se pravilno zauzima memorija za promenljivu ``genesis_block``::

    typedef struct block_st {
        int index;
        int hash;
        char num_tx;
        int timestamp;
        int nonce;

        struct block_st *parent_block;
    } BLOCK;

    BLOCK *genesis_block;

- ``genesis_block = malloc(sizeof(BLOCK));``
- ``genesis_block = malloc(sizeof(BLOCK*));``
- ``genesis_block = malloc(sizeof(block_st));``
- ``genesis_block = malloc(sizeof(block_st*));``
- ``genesis_block = malloc(sizeof(int));``
- ``free(genesis_block);``

----

Kako se pravilno oslobađa memorija zauzeta za promenljivu ``genesis_block``::

    typedef struct block_st {
        int index;
        int hash;
        char num_tx;
        int timestamp;
        int nonce;

        struct block_st *parent_block;
    } BLOCK;

    BLOCK *genesis_block;

- ``free(genesis_block);``
- ``genesis_block = malloc(sizeof(BLOCK));``
- ``genesis_block = malloc(sizeof(BLOCK*));``
- ``genesis_block = malloc(sizeof(block_st));``
- ``genesis_block = malloc(sizeof(block_st*));``
- ``genesis_block = malloc(sizeof(int));``

----

Koliko bajtova memorije će zauzeti sledeći (uspešni) poziv ``malloc`` funkcije::

    struct grupa_st {
        int a;
        char b[30];
        char c;
    };

    struct grupa_st *g = malloc(sizeof(struct grupa_st));

- 35
- 4
- 30
- 31
- 34
- 36

----

Koliko bajtova memorije će zauzeti sledeći (uspešni) poziv ``malloc`` funkcije::

    union grupa_st {
        int a;
        char b[30];
        char c;
    };

    union grupa_st *g = malloc(sizeof(union grupa_st));

- 30
- 4
- 31
- 34
- 35
- 36

----

Prilikom definisanja skalarnih promenljiva memorija se zauzima:

- statički
- dinamički
- upotrebom funkcije ``malloc``
- upotrebom funkcije ``free``

----

Prilikom definisanja spregnutih struktura memorija se zauzima:

- dinamički
- statički
- sekvencijalno

----

"Curenje" memorije je efekat koji nastaje u slučaju:

- dinamičkog zauzimanja memorije, bez njenog pravovremenog oslobađanja
- statičkog zauzimanja memorije
- nedovoljne količine memorije u računaru
- čestih poziva funkcije ``free``

----

U programskom jeziku C viseći pokazivači:

- pokazuju na deo memorije koji više nije zauzet
- nalaze se na kraju kružne liste
- koriste se za završetak deka
- koriste se za završetak liste
- rešavaju problem lažne popunjenosti liste
- rešavaju problem lažne popunjenosti reda
