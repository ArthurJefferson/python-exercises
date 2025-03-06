hora_do_dia = int(input("Qual é a Hora: "))  # Convertendo para inteiro

match hora_do_dia:
    case hora if hora > 12 and hora < 18:
        print("Boa Tarde")
        
    case hora if hora < 12 and hora > 6:
        print("Boa Manhã")
    
    case hora if hora == 12:
        print("Bom Almoço")
    
    case hora if hora >= 18:
        print("Boa Noite")
    
    case hora if hora < 6:
        print("Boa Madrugada")