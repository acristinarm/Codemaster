print("\n\n")

exemplo_teste = "CodeMaster"
exemplo_maiusculo = exemplo_teste.upper()
exemplo_minusculo = exemplo_teste.lower()
exemplo_capitalize = exemplo_teste.capitalize()
exemplo_count = exemplo_teste.count("e")
exemplo_lenf = len(exemplo_teste)
exemplo_lenm = exemplo_teste.__len__()
exemplo_substitui = exemplo_teste.replace("e", "x")

print("=== Métodos e Funções das Strings ===")

print()

print("String 'original': (", exemplo_teste, ")")

print()

print("String 'capitalizada': (", exemplo_teste.capitalize(), ")") #outra forma de fazer é chamar o original e nele aplicar a alteração
print("String 'minúsculas': (", exemplo_minusculo, ")")
print("String 'maiúsculas': (", exemplo_maiusculo, ")")

print()

print("String 'total de letras e': (", exemplo_count, ")")
print("String 'tamanho total com método': (", exemplo_lenm, ")")
print("String 'tamanho total com função': (", exemplo_lenf, ")")

print()

print("String 'substitui todo (e) por (x)': (", exemplo_substitui, ")")

print("\n\n")