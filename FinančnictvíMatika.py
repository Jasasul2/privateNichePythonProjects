# Author : Ondřej Maceška 
# Date : 18.10.2020
# Description : some random functions used to verify the combinatorics algorhitms 
# Language : cz 

import math 

def find_last_payment(start, pay, q, order = 0):
    start *= q 
    order += 1 
    print("current money: ", start, "current payment: ", order, "th")
    if(start - pay <= 0):
        print("")
        s = "last, " + str(order) + "th payment: " + str(int(math.ceil(start)))
        return s
    return find_last_payment(start - pay, pay, q, order)

def euklid_algorithm(A, B):
    Ad = max(A, B)
    Bd = min(A, B)
    mod = Ad % Bd
    if(mod == 0):
        return Bd 
    return(euklid_algorithm(Bd, mod))

def soucet_rady(a1, q):
    if(abs(q) < 1):
        return a1 / (1 - q)
    return "not řada"

def difference_aplspsti(a1, an, n):
    d = (an - a1) / (n - 1)
    return d

def prvni_clen_aplspsti(an, n, d):
    a1 = an - (n - 1) * d
    return a1

def prvni_clen_ze_souctu(s, an, n):
    a1 = (2 * s) / n - an
    return a1

def prvni_clen_ze_souctu_d(s, d, n):
    a1 = (((2 * s) / n) - d * (n - 1)) / 2
    return a1 

def difference_aplspsti_n(an1, n1, an2, n2):
    if(n1 > n2):
        return "wrong order bitch"
    d = (an2 - an1) / (n2 - n1)
    return d 

def nty_clen_aplspsti(a1, d, n):
    an = a1 + (n - 1) * d
    return an

def soucet_aplspsti(a1, d, n):
    s = ((a1 + nty_clen_aplspsti(a1, d, n)) / 2) * n
    return s

find_last_payment(60000, 4950, 1.014)