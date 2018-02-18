def encrypt(temp_plain_text, key):
	plain_text = list(''.join(temp_plain_text.split()))

	#If both letters are the same, add an "X" after the first letter.
	i=0
	for c in range(int(len(plain_text)/2)):
		if(plain_text[i]==plain_text[i+1]):
			plain_text.insert(i+1,'X')
		i=i+2

	if(len(plain_text) % 2 == 1):
		plain_text.append("X")

	i=0
	new=[]
	for x in xrange(1,len(plain_text)/2+1):
		new.append(plain_text[i:i+2])
		i=i+2

	plain_text = list(new)
	key_matrix = matrix(key)

	cipher=[]

	for c in plain_text:
		p1,q1 = find_position(key_matrix, c[0])
		p2,q2 = find_position(key_matrix, c[1])

		if(p1==p2):
			cipher.append(key_matrix[p1][(q1+1)%5])
			cipher.append(key_matrix[p1][(q2+1)%5])		

		elif(q1==q2):
			cipher.append(key_matrix[(p1+1)%5][q1])
			cipher.append(key_matrix[(p2+1)%5][q2])

		else:
			cipher.append(key_matrix[p1][q2])
			cipher.append(key_matrix[p2][q1])

	return ''.join(cipher)


def decrypt(cipher):
	i=0
	new=[]
	for x in range(len(cipher)/2):
		new.append(cipher[i:i+2])
		i=i+2

	cipher = new

	key_matrix = matrix(key)

	plaintext=[]

	for c in cipher:
		p1,q1=find_position(key_matrix,c[0])
		p2,q2=find_position(key_matrix,c[1])

		if(p1==p2):
			if(q1==0):
				q1 = 5
			if(q2==0):
				q2 = 5			
			plaintext.append(key_matrix[p1][q1-1])
			plaintext.append(key_matrix[p1][q2-1])		

		elif(q1==q2):
			if(p1==0):
				p1 = 5
			if(p2==0):
				p2 = 5				
			plaintext.append(key_matrix[p1-1][q1])
			plaintext.append(key_matrix[p2-1][q2])

		else:
			plaintext.append(key_matrix[p1][q2])
			plaintext.append(key_matrix[p2][q1])

	for c in range(len(plaintext)):
		if "X" in plaintext:
			plaintext.remove("X")

	return ''.join(plaintext).lower()


def matrix(keyword):
	temp_matrix=[]

	for c in keyword.upper():
		if c not in temp_matrix:
			temp_matrix.append(c)

	alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"

	for c in alphabet:
		if c not in temp_matrix:
			temp_matrix.append(c)	

	matrix = [temp_matrix[0:5], temp_matrix[5:10], temp_matrix[10:15], temp_matrix[15:20], temp_matrix[20:25]]
	return matrix


def find_position(key_matrix,letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			if key_matrix[i][j]==letter.upper():
				x=i
				y=j
	return x,y


print("Playfair Cipher\n")

key = raw_input("Enter key : ")
message = raw_input("Enter message : ")
print("\nEncrypting: \n" + "Message: " + message)
print("Matrix: ")
print(matrix(key)) 
print("\nCipher text: ") 
cipher_text = encrypt(message, key)
print(cipher_text)

print("\nDecrypting: \n" + "Cipher: " + cipher_text)
print("Plaintext:")
print(decrypt(cipher_text))

