#------------------------------------------------------------
#Escobita
import os 

os.system('cls')
#------------------------------------------------------------
from funciones import VerNIF, ImpCert, VerNomb
#------------------------------------------------------------
#Registro
Registro = []




#------------------------------------------------------------
#Repetir
Menu = True
while Menu:
    #------------------------------------------------------------
    #Ver Menu
    
    print("\t\tMenú")
    print("1:Grabar\n2:Buscar\n3:Imprimir Certificados\n4:Salir")

#------------------------------------------------------------
    #Champu anticaidas version menu
    try:
        opcion1 = int(input('Elija una opción:\n'))
    except:
        opcion1 = 0
#------------------------------------------------------------
    #Menu de opciones
    
    
    if opcion1 == 4:
        #Opcion Salir
        print("Hasta pronto", nombre)
        print("Version 1.0")
        
        Menu = False
    #------------------------------------------------------------
    
    elif opcion1 == 3:
         #opcion Certificado
        print("Imprimir certificados")
        print("1:Certificado de Nacimiento\n2:Certificado de Estado Conyugal\n3:Certificado de pertenecia a la UE")
        try:
            rpta = int(input("Ingrese opción a imprimir:\n"))
        except:
            rpta = 0 
        #Funcion Imprimir Certificado
        ImpCert (rpta,edad,NIF,nombre)
        
    #------------------------------------------------------------
    elif opcion1 == 2:
        #Opcion Buscar
        print("Buscar")
        busqueda = input("Ingrese el NIM a buscar:\n")
        if busqueda.find("SP") == 10:
            print("La persona pertenece a españa")
        else:
            print("La persona pertenece a la Union Europea")
        print(Registro)
        
        
        
    #------------------------------------------------------------
  
    elif opcion1 == 1:
        #Opcion Datos
    
        NIF = input("Ingrese NIF:\n")
        VerNIF(NIF)#Verifica el NIF 
        
        nombre = input("Ingrese su nombre\n")
        VerNomb(nombre) #Ingresa y Verifica el nombre
        #------------------------------------------------------------
        repetiredad = True
        while repetiredad:
            try:
                edad = int(input("Ingrese su edad:\n"))
            except:
                print("La edad tiene que ser un número")
                edad = -1
            
            if edad > 0:
                print("Pasaste")
                repetiredad = False
            else:
                print("La edad no puede ser menor a 0")
        #------------------------------------------------------------


        
        lista = {
            "NIF"  : NIF,
            "Nombre" : nombre,
            "Edad" : edad
            }

        Registro.append(lista)

        
        
        
    else:
     print("Opcion invalida")
     
     
     
     
#------------------------------------------------------------    

    