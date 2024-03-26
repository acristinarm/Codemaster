print("\n\n")

nome = "Ana"
idade = 21
morada = "Gondomar"

print("O (a) paciente '", nome, "', que tem '", idade, "' anos, mora em '", morada, "'", sep="")
#esta primeira forma é muito trabalhosa e pode dar errado
print()

#1º método com o format
print("O (a) paciente '{}', que tem '{}' anos, mora em '{}'".format(nome, idade, morada))

#2º método com o format, lembrar que começa no 0. Aqui especifico a ordem que quero
print("O (a) paciente '{1}', que tem '{2}' anos, mora em '{0}'".format(nome, idade, morada))

#3º método do format, não é tão utilizado
print("O (a) paciente '{valor_2}', que tem '{valor_3}' anos, mora em '{valor_1}'".format(valor_1="teste 1", valor_2="teste 2", valor_3="teste 3"))

#4º método, posso escrever diretamente dentro da chaveta
print(f"O (a) paciente '{nome}', que tem '{round(idade)}' anos, mora em '{morada}'")

print()

print("Nome: {:>10}".format(nome))#isto permite dar espaço de 10 caracteres entre o nome e o ana, ana incluído
print("Nome: {:<10}".format(nome))#isto permite dar espaço de 10 caracteres depois do ana, ana incluido
print("Nome: {:^10}".format(nome))#isto permite alinhar ao centro
print("Nome: {:*^11}".format(nome))#isto permite alinhar ao centro e colocar * em vez dos espaços em branco


print("\n\n")