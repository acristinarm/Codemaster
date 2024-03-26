print("\n\n")

nome = "Ana Rebelo"
nota_1 = 18
nota_2 = 13
nota_3 = 16
media = (nota_1 + nota_2 + nota_3)/ 3
media_arredondada = round(media)

print("=== Método 'format' ===")

print()

print("O(a) aluno(a) [{}] com as notas [n1: {}] [n2: {}] [nt: {}], obteve uma média de [{}].".format(nome, nota_1, nota_2, nota_3, media_arredondada))

print(f"O(a) aluno(a) [{nome}] com as notas [n1: {nota_1}] [n2: {nota_2}] [nt: {nota_3}], obteve uma média de [{media_arredondada}].")


print("\n\n")