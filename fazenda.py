vacas   = int(input("Vacas: "))
cavalos = int(input("Cavalos: "))
ovelhas = int(input("Ovelhas: "))

leite_dia = vacas * 3.2
la_tosquia = ovelhas * 2.3
ferraduras = cavalos * 4

leite_semana = leite_dia * 7
leite_mes = leite_dia * 30
print("Produção diária: " , leite_dia)
print("Produção semanal: " , leite_semana)
print("Produção mensal: " , leite_mes)