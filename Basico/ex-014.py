#Horario 2.0

import datetime as data

x = data.datetime.now()
y = x.strftime('%H %M %S ')

z = y.split()[0]

hora = int(z)

if hora > 12 and hora < 18:
    print("Boa Tarde")
    
elif hora == 12:
    print("Bom Almoço")
    
elif hora < 12 and hora > 6:
    print("Boa Manhã")

elif hora < 6 and hora >= 0:
    print("Boa Madrugada")
    
else:
    print("Boa Noite")
    
print(y)