def VerNIF(NIF):
    if NIF.find("-") == 8:
        if len(NIF) == 12:
            print("Se ha registrado correctamente")
        else:
            print("Ingrese un NIF correcto (Recuerda este tiene que llevar 8 digitos, guion y 3 caracteres)")
            repetirb = True
            NIF = input("Ingrese NIF:\n")
            if len(NIF) == 12:
                print("Se ha registrado correctamente")
                repetirb = False
            else:
                print("Ingrese un NIF correcto (Recuerda este tiene que llevar 8 digitos, guion y 3 caracteres)")
    else:
        repetira = True
        print("Ingrese un NIF correcto (Recuerda este tiene que llevar 8 digitos, guion y 3 caracteres)")
        while repetira:
            NIF = input("Ingrese NIF:\n")
            if NIF.find("-") == 8:
                if len(NIF) == 12:
                    print("Se ha registrado correctamente")
                    repetira = False
                else:
                    print("Ingrese un NIF correcto (Recuerda este tiene que llevar 8 digitos, guion y 3 caracteres)")
                    repetirc = True
                    NIF = input("Ingrese NIF:\n")
                    if len(NIF) == 12:
                        print("Se ha registrado correctamente")
                        repetirc = False
                    else:
                        print("Ingrese un NIF correcto (Recuerda este tiene que llevar 8 digitos, guion y 3 caracteres)")
            else:
                print("Ingrese un NIF correcto (Recuerda este tiene que llevar 8 digitos, guion y 3 caracteres)")
            
            
            
    

#------------------------------------------------------------
def VerNomb(nombre):
    if len(nombre) >= 8 :
        print("pasaste")
    else:
        print("El nombre tiene que incluir 8 caracteres como mínimo")
        repetir2 = True
        while repetir2:
            nombre = input("Ingrese su nombre\n")
            if len(nombre) >= 8:
                print("Pasaste")    
                repetir2 = False
            else:
                print("El nombre tiene que incluir 8 caracteres como mínimo")
            
    return nombre

#------------------------------------------------------------
def ImpCert(rpta,edad,NIF,nombre):
    if rpta == 1:
        print(f"Imprimiendo Certificado de Nacimiento \n{NIF} \n{nombre} \n{edad} ")
        
    elif rpta == 2:
        print(f"Certificado de Estado Conyugal\n{NIF} \n{nombre} \n{edad}")
    elif rpta == 3:
        print(f"Certificado de pertenecia a la Unión Europea\n{NIF} \n{nombre} \n{edad}")
    else:
        print(f"Ingrese una opción válida")
    
    
        
    
#------------------------------------------------------------


        
    
        
    
    
        
        
        
    
    