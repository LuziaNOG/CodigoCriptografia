arquivo_c = open('/home/luzia/vigenere/texto_cifrado.txt', 'r')
texto = arquivo_c.read().replace(" ","").replace(",",'').upper()
arquivo_c.close()

chave = raw_input('DIGITE A CHAVE PARA DECIFRAR: ').upper()
cifrado=""
decifrado=""
alfa="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

tam_p = len(texto)
tam_c= len(chave)

if (tam_p > tam_c):
	i=0
	t=len(chave)-1;
	while (len(chave) < tam_p):
		chave=chave+chave[i]
		if (i==t):
			i=0
		else:
			i=i+1

p=0
while(len(decifrado)<len(texto)):
	aux=alfa.find(texto[p])-alfa.find(chave[p])+26
	if (aux > 25):
		aux=abs(aux-26)
	decifrado=decifrado+alfa[aux]
	p=p+1

arquivo_d = open('/home/luzia/vigenere/texto_decifrado.txt', 'w')
arquivo_d.write(decifrado)
arquivo_d.close()
