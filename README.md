Just a small tool to check bcrypt rounds performance on mashines to determine a good proportion between userfriendlieness and security as with each round security rises but it takes exponantially more time to hash.


```bash
poetry install
python3 check_bcrypt_rounds.py
```

sample output

```
 (main) python_tools/bcrypt_round_check $ python3 check_bcrypt_rounds.py                                                                                    24.9s 
----------Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz----------
-trying for bcryptcosts with maxtime: 1.434 seconds to hash-
     hashed 4 rounds in 0.059232473373413086 seconds
     hashed 5 rounds in 0.0025370121002197266 seconds
     hashed 6 rounds in 0.004277944564819336 seconds
     hashed 7 rounds in 0.008234977722167969 seconds
     hashed 8 rounds in 0.016252517700195312 seconds
     hashed 9 rounds in 0.03290915489196777 seconds
     hashed 10 rounds in 0.06319689750671387 seconds
     hashed 11 rounds in 0.1260676383972168 seconds
     hashed 12 rounds in 0.2526533603668213 seconds
     hashed 13 rounds in 0.5088541507720947 seconds
     hashed 14 rounds in 1.0143675804138184 seconds
--------------- rechecking last valid round ----------------
     hashed 14 rounds in 1.0169122219085693 seconds
     hashed 14 rounds in 1.0177178382873535 seconds
     hashed 14 rounds in 1.015989065170288 seconds
-------------------------- result --------------------------
     14 rounds mean 16384 iterations/bcrypt costfactor
```
