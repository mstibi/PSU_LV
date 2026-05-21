## Dataset

Za treniranje i testiranje koristi se German Traffic Sign Recognition Dataset (GTSRB).

Dataset nije uključen u GitHub repozitorij jer zauzima previše prostora, otprilike 400 MB.

Prije pokretanja skripti potrebno je ručno dodati folder `gtsrb` u root direktorij projekta.

Struktura foldera treba biti sljedeća:

```text
PSU_LV9/
│
├── zd1.py
├── zd3.py
├── README.md
│
└── gtsrb/
    ├── Train/
    │   ├── 0/
    │   ├── 1/
    │   ├── ...
    │   └── 42/
    │
    └── Test/
        ├── 0/
        ├── 1/
        ├── ...
        └── 42/