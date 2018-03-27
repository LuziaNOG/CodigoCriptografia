def monta_matriz(chave):
	alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVXYZ")
	chave=chave.upper()
	linha, coluna, posicao = 0, 0, 0
	
	matriz = []
	for i in range(5):
		matriz.append( [0] * 5 )
	
	
	for letra in chave:
		linha = int(posicao / 5)
		coluna = int(posicao % 5) 
				
		if letra in alfabeto:
			alfabeto.remove(letra)
			matriz[linha][coluna] = letra
			posicao += 1

	while alfabeto:
		linha = int(posicao / 5)
		coluna = int(posicao % 5)
		matriz[linha][coluna] = alfabeto[0]
		del alfabeto[0]
		posicao += 1
	return matriz

def cifra(frase,chave):
	frase=frase.upper()
	chave=chave.upper()
	matriz = monta_matriz(chave)
	print matriz
	posicao = 0
	texto_cifrado = ""
	
	if (len(frase) % 2) !=0:
		frase += "Z"	
	
	
	if frase[posicao] == frase[posicao + 1]:
		aux_frase=""
		indice=0
		while indice < len(frase):
			if frase[indice]==frase[indice+1]:
				if frase[indice] == 'x':
					aux_frase+=frase[indice] + 'z' + frase[indice+1]
				else:
					aux_frase+=frase[indice] + 'x' + frase[indice+1]
			else:
				aux_frase+=frase[indice]+frase[indice+1]
			indice = indice + 2
		if aux_frase[len(aux_frase)-1] != 'x':
			aux_frase+='x'
		else:
			aux_frase+='z'
		frase=aux_frase
	    
		
	if (frase[posicao] == frase[posicao + 1]) and (frase[posicao] == "Z"):
		frase[posicao+1] = "X"
	
	while posicao < len(frase):
		posicao_m = 0
		for linha in matriz:
			for coluna in linha:
				if coluna == frase[posicao]:
					letra_1_l = posicao_m // 5
					letra_1_c = posicao_m % 5
				posicao_m +=1
				
		posicao_m=0
		for linha in matriz:
			for coluna in linha:
				if coluna == frase[posicao + 1]:
					letra_2_l = posicao_m // 5
					letra_2_c = posicao_m % 5
				posicao_m += 1

        
		if letra_1_l == letra_2_l:
			letra_1_c = (letra_1_c + 1) % 5
			letra_2_c = (letra_2_c + 1) % 5
			texto_cifrado += \
				matriz[letra_1_l][letra_1_c]+matriz[letra_2_l][letra_2_c]

        
		elif letra_1_c == letra_2_c:
			letra_1_l = (letra_1_l + 1) % 5
			letra_2_l = (letra_2_l + 1) % 5
			texto_cifrado += \
				matriz[letra_1_l][letra_1_c] + matriz[letra_2_l][letra_2_c]

        
		elif (letra_1_l != letra_2_l) and (letra_1_c != letra_2_c):
			letra_2_c_r = letra_1_c
			letra_1_c_r = letra_2_c
			texto_cifrado += \
				matriz[letra_1_l][letra_1_c_r]+matriz[letra_2_l][letra_2_c_r]
			
		posicao += 2
		
		
	return texto_cifrado
    
def decifra(frase,chave):
	frase=frase.upper()
	chave=chave.upper()
	matriz = monta_matriz(chave)
	print matriz
	posicao = 0
	decifra_result = ""
    
    
	if (len(frase) % 2) != 0:
		frase += "w"
	
	if frase[posicao] == frase[posicao + 1]:
		frase[posicao] = "w"
	
	if (frase[posicao] == frase[posicao + 1]) and (frase[posicao] == "w"):
		frase[posicao] = "x"
    
	while posicao < len(frase):
		posicao_m = 0
        
		for linha in matriz:
			for coluna in linha:
				if coluna == frase[posicao]:
					letra_1_l = posicao_m // 5
					letra_1_c = posicao_m % 5
				posicao_m +=1
				
		posicao_m=0
		for linha in matriz:
			for coluna in linha:
				if coluna == frase[posicao + 1]:
					letra_2_l = posicao_m // 5
					letra_2_c = posicao_m % 5
				posicao_m += 1
		
		if letra_1_l == letra_2_l:
			letra_1_c = (letra_1_c - 1) % 5
			letra_2_c = (letra_2_c - 1) % 5
			decifra_result += \
				matriz[letra_1_l][letra_1_c]+matriz[letra_2_l][letra_2_c]

        
		elif letra_1_c == letra_2_c:
			letra_1_l = (letra_1_l - 1) % 5
			letra_2_l = (letra_2_l - 1) % 5
			decifra_result += \
				matriz[letra_1_l][letra_1_c] + matriz[letra_2_l][letra_2_c]

        
		elif (letra_1_l != letra_2_l) and (letra_1_c != letra_2_c):
			letra_2_c_r = letra_1_c
			letra_1_c_r = letra_2_c
			decifra_result += \
				matriz[letra_1_l][letra_1_c_r]+matriz[letra_2_l][letra_2_c_r]
				
		posicao += 2
	return decifra_result

op=0
while (op!=3):
	op=input('1-cifra, 2- decifrar,3-sair \n')
	if(op==1):
		ch=raw_input('digite uma palavra-chave \n')
		palavra=raw_input('digite a palavra ou frase para ser cifrada\n').replace(" ","")
		palavra_cifrada = cifra(palavra,ch)
		print ('palavra cifrada:',palavra_cifrada)
		
	if(op==2):
		ch=raw_input('digite uma palavra-chave \n')
		palavra=raw_input('digite a palavra ou frase para ser decifrada \n').replace(" ","")
		palavra_decifrada=decifra(palavra,ch)
		print('palavra decifrada:',palavra_decifrada)
		





