import random


def is_prime(n: int) -> bool:  
    z=bool
    Check=0
    for i in range(1,n+1):
        if (n % i)==0:
            Check=Check+1
    if Check==2:
        z=True
    else:
        print("Your number is wrong!!!",n)
    pass

def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p*q
    phi = (p-1)(q-1)
    e = random.randrange(1, phi)


    def gcd(a: int, b: int) -> int:
        x=a
        y=b
        while y>0:
            z=x%y
            x,y=y,z
        a=x                        
        return a
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)


    def multiplicative_inverse(e: int, phi: int) -> int:
        x=e
        y=phi
        z=2 
        while z*x%y!=1:
             z+=1
        d=z         
    pass
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))
