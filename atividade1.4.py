Segundos_ent =int (input("Digite os segundo para conversão: "))

dias = Segundos_ent // 86400
seg_sobra = Segundos_ent % 86400

horas = seg_sobra // 3600
seg_sobra1 =  seg_sobra % 3600

minutos = seg_sobra1 // 60
seg_sobra2 = seg_sobra1 % 60

segundos = seg_sobra2 % 60


print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
