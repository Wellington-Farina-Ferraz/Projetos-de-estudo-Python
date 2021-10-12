print("Digite zero para finalizar o Programa .")

soma = 0 #variaveu par guarda a soma 
cont = 0 # variavel par contar quanta vez passou no laco
result = 0 # variavel para guarda o resultado
valor = 1 # variavel para guarda o valor digitado pelo usuario 

while valor!= 0:
	cont = cont + 1
	valor = int(input("digite o valor: "))
	soma = soma + valor # soma os valors digitado // Digitado 0 ele sai do laco
	
cont = cont -1	# retira 1 para deixar a divisao exata 
result = soma / cont # calcula o resultado 

print("sua conta é: ",soma," / ",cont)
print("A media aritimetica é: ",result) #imprime o resultado 