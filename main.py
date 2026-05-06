# These two functions will help determine if two numbers are coprimes #
# Returns the greatest common denominator for two numbers
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
# Determines if two numbers are coprime. Returns True or False
def is_coprime(x, y):
    return gcd(x, y) == 1

# Returns a list of all the prime numbers from 2 to n
def primes_less_than(n):
	all_primes=[]
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p ** 2, n + 1, p):
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers
	for p in range(n + 1):
		if prime[p]:
			all_primes.append(p)
	return all_primes

print("All primes less than 100:\n"+str(primes_less_than(100)))

def calculate_N(p,q):
	n_up = p*q
	return n_up

def calculate_T(p,q):
	t_up = (p-1)*(q-1)
	return t_up

def pick_e_d(p,q):
	T = calculate_T(p,q)
	for e in range(2, T):
		if is_coprime(e, T):
			break
	for d in range(2, T):
		if (e*d) % T == 1:
			return e, d
		
def encrypt(n,e,letter):
	v = ord(letter)
	enc = (v**e) % n
	return enc

def encrypt_message(n, e, message):
	enc_message = []
	for letter in message:
		enc_message.append(encrypt(n,e,letter))
	return enc_message

def decrypt(n,d,enc):
	dec = (enc**d) % n
	




