Standardni ulaz/izlaz
=====================

Kako se pravilno ispisuje promenljiva dužine osam bita, u decimalnom formatu:

- ``printf("%d",  promenljiva);``
- ``printf("%b",  promenljiva);``
- ``printf("%c",  promenljiva);``
- ``printf("%c", &promenljiva);``
- ``printf("%d", &promenljiva);``
- ``scanf("%b",  promenljiva);``
- ``scanf("%c",  promenljiva);``
- ``scanf("%c", &promenljiva);``
- ``scanf("%d",  promenljiva);``
- ``scanf("%d", &promenljiva);``

----

Kako se pravilno ispisuje promenljiva dužine jedan bajt, u ASCII formatu:

- ``printf("%c",  promenljiva);``
- ``printf("%b",  promenljiva);``
- ``printf("%c", &promenljiva);``
- ``printf("%d",  promenljiva);``
- ``printf("%d", &promenljiva);``
- ``scanf("%b",  promenljiva);``
- ``scanf("%c",  promenljiva);``
- ``scanf("%c", &promenljiva);``
- ``scanf("%d",  promenljiva);``
- ``scanf("%d", &promenljiva);``

----

Kako se pravilno učitava promenljiva dužine jedan bajt, u decimalnom formatu:

- ``scanf("%d", &promenljiva);``
- ``printf("%b",  promenljiva);``
- ``printf("%c",  promenljiva);``
- ``printf("%c", &promenljiva);``
- ``printf("%d",  promenljiva);``
- ``printf("%d", &promenljiva);``
- ``scanf("%b",  promenljiva);``
- ``scanf("%c",  promenljiva);``
- ``scanf("%c", &promenljiva);``
- ``scanf("%d",  promenljiva);``

----

Kako se pravilno učitava promenljiva dužine osam bita, u ASCII formatu:

- ``scanf("%c", &promenljiva);``
- ``printf("%b",  promenljiva);``
- ``printf("%c",  promenljiva);``
- ``printf("%c", &promenljiva);``
- ``printf("%d",  promenljiva);``
- ``printf("%d", &promenljiva);``
- ``scanf("%b",  promenljiva);``
- ``scanf("%c",  promenljiva);``
- ``scanf("%d",  promenljiva);``
- ``scanf("%d", &promenljiva);``

----

Kako se pravilno učitava celobrojna promenljiva ``n``:

- ``scanf("%d", &n);``
- ``scanf("%d",  n);``
- ``scanf("%d", %n);``
- ``scanf("%f", &n);``
- ``scanf("%n");``
- ``scanf("d", &n);``
- ``scanf(n);``
- ``scanf(&n);``

----

Kako se pravilno ispisuje promenljiva tipa ``double``:

- ``printf("%lf",  celzijusi);``
- ``printf("%.2",  celzijusi);``
- ``printf("%.2", &celzijusi);``
- ``printf("%d",   celzijusi);``
- ``printf("%d",  &celzijusi);``
- ``printf("%lf", &celzijusi);``
