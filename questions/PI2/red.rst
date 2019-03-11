Red
===

Red je struktura tipa:

- FIFO
- LIFO
- FUFI

----

Deskriptor spregnute realizacije reda sadrži:

- dva pokazivača
- jedan pokazivač
- tri pokazivača
- deskriptor reda ne sadrži pokazivače

----

Provera da li je red prazan je:

- izvedena operacija nad redom
- osnovna operacija nad redom
- operacija koja se ne može izvršiti nad redom
- primitivna funkcija nad redom

----

Šta radi sledeća funkcija::

    void f(struct node **front, struct node **rear, int value) {
        struct node *temp = malloc(sizeof(struct node));
        if(temp == NULL) {
            puts("Greska prilikom zauzimanja memorije!");
            exit(42);
        }

        temp->data = value;
        temp->link = NULL;

        if(*rear == NULL) {
            *rear = temp;
            *front = *rear;
        } else {
            (*rear)->link = temp;
            *rear = temp;
        }
    }

- ubacuje novi element u red
- ubacuje novi element u binarni hip
- ubacuje novi element u stek
- uklanja element uz binarnog hipa
- uklanja element uz reda
- uklanja element iz steka
