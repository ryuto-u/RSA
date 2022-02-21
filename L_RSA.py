#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import math
  
def sympy_prime( N ):
  while True:
    n = (random.randint( 11, N ))
    s = 2
    flag = True
    while s*s <= n and flag:
      if n % s == 0:
        flag = False
      s += 1
    if flag:
      return n

def generate_keys( k ):
  b = 1 << int( k/2 )
  e = 7
  flag = True
  while flag:
    p = sympy_prime( b )
    q = p
    while p == q:
      q = sympy_prime( b )
    N = p * q
    phi = ( p-1 ) * ( q-1 )
    d = gcd( phi, e )
    if phi%e != 0:
      flag = False
  return ( N, e ), d



def encrypt( m, public_key ):
  cipher = []
  N, e = public_key
  for l in m:
    c = ord(l)
    for s in range( e-1 ):
      c = ( c*ord(l) ) % N
    cipher.append( c )
  return cipher

def decrypt( c, public_key, private_key ):
  decode = ''
  N = public_key[0]
  for c1 in c:
  	m = c1
  	for s in range( private_key-1 ):
  	  m = ( m*c1 ) % N
  	decode += chr( m )
  return decode

if __name__ == '__main__':
  public_key, private_key = generate_keys(8)
  plain_text = 'sato'
  cipher = encrypt( plain_text, public_key )
  decode = decrypt( cipher, public_key, private_key )
  print( 'N =', public_key[0] )
  print( 'e =', public_key[1] )
  print( 'd =', private_key, '\n' )
  print( 'plain　　　　　　　　→　cipher　           →　decode' )
  for s in range( len(plain_text) ):
    print( plain_text[s], ord(plain_text[s]), '(', format(ord(plain_text[s]), '08b'), ')→',
     cipher[s], '(', format(cipher[s], '08b'), ')→',
     ord(decode[s]), '(', format(ord(decode[s]),'08b'), ')', decode[s] )
     




# In[ ]:





# In[ ]:





# In[ ]:




