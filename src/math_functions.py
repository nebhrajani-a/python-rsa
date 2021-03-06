import sys
sys.setrecursionlimit(10**6)
from math import ceil

def poweroftwocheck(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
    return True

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
def lcm(a,b):
    return (a*b) // gcd(a,b)

def eea(a, b):
    '''Extended Euclidean algorithm'''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = eea(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    '''Find modular multiplicative inverse using EEA'''
    g, x, y = eea(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    else:
        return x % m
def cra(c, p, q, d_p, d_q, q_inv):
    '''Chinese Remainder Algorithm'''
    m_1 = pow(c, d_p, p)
    m_2 = pow(c, d_q, q)
    if m_1 >= m_2:
        h = q_inv*(m_1-m_2) % p
    else:
        h = q_inv*((m_1 + (ceil(q/p))*p) - m_2) % p
    return pow((m_2 + h*q), 1, p*q)
