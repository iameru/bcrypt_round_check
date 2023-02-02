#!/usr/bin/python3
# depends on passlib[bcrypt]

from passlib.context import CryptContext
import time
import subprocess


pw = "Our AverageE Joe'Zz Pasword123!"


def time_bcrypt_hash(rounds):

    start = time.time()
    crypt_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto',
                    bcrypt__default_rounds=rounds)
    __hash = crypt_ctx.hash(pw)
    return (time.time() - start)


def try_and_time_password_hashing(maxtime=1.234):
    """ maxtime in miliseconds """

    print(f'trying for bcryptcosts with maxtime: {maxtime} seconds to hash'.center(60,"-"))

    for rounds in range(4,20):

        result = time_bcrypt_hash(rounds)

        if result > maxtime:

            rounds = rounds-1
            print(" rechecking last valid round ".center(60,"-"))
            for _ in range(3):
                result = time_bcrypt_hash(rounds)
                print(" "*5+f'hashed {rounds} rounds in {result} seconds')

            print(" result ".center(60,"-"))
            print(" "*5+f'{rounds} rounds mean {2**rounds} iterations/bcrypt costfactor')
            print()

            break

        print(" "*5+f'hashed {rounds} rounds in {result} seconds')
    

def get_processor_information():
    lscpu = subprocess.check_output("lscpu", shell=True).strip().decode().split("\n")
    for line in lscpu:
        if line.startswith('Model name:'):
            result = line.lstrip('Model name:')
            result.lstrip()
            print(result.center(60,"-"))
    

if __name__ == "__main__":
    
    get_processor_information()
    try_and_time_password_hashing()
