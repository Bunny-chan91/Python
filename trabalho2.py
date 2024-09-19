#a linha abaixo esta inciando um loop infinito utilizando a estrutura while e dentro do loop ele esta utilizando 3 variaveis
while True:
 cont = 1
 maior = -0
 menor = +0
#aqui eu estou criando outro loop que irá executar o programa se a variavel cont for maior ou igual a variavel a 10 
 while cont <= 10:
  #aqui acontece a entrada de dados digitado pelo usuaria correspondente ao que foi pedido
    num = int(input("Digite um número ou digite o numero '0' para sair: "))
    num2 = int(input("Digite outro número: "))
  #aqui eu uso uma condiçao para determinar se o programa será encerrado se o usuario digitar "0"
    if num == 0:
        print("Encerrando o programa.")

        exit()
    #aqui continua a condiçao que irá continuar com o programa normalmente se o usuario nao digitar "0"    
    else:
        print("Você digitou o número.", num)
#as proximas condicionais estao criando variaveis que vão fazer os calculos para determinar qual numero será maior e qual será menor
#a variavel cont iráiniciar as variaveis maior e menor se ele for igual a 1 que é o numero digitado pelo usuario
        print ("O maior numero é ", num, "e o número menor é", num2)
    if cont == 1:
        maior = num
        menor = num
#aqui determina se a varivel num for maior que a varivel maior irá ser armazenado o maior valor digitado na variavel maior
    if num > maior:
        maior = num
#aqui acontece o contrario, se a varivel num for menor que a varivel menor irá ser armazenado o menor valor digitado na variavel menor
    if num < menor:
        menor = num
#aqui e incrementado 1 na variavel cont para que o loop continue ate o valor determinado
    cont += 1
#aqui é impresso na tela o resultado das variaves maior e menor
 
 #aqui é encerrado o loop do começo
 break
