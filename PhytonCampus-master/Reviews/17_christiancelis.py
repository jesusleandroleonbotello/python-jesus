import json

def menu():
    while True:
        print("*"*4+ "Libreria Libros.com" + "*"*4)
        print("1. Agregar o insertar")
        print("2. Consultar")
        print("3. Editar Libro")
        print("4. Borrar Libro")
        print("5. Listar Libro")
        try:
            opcion = int(input("Digite opcion: "))
            if(opcion<1 or opcion>5):
                print("opcion no valida, digite nuevamente: ")
                continue
            break
        except Exception as e:
            print("No valido",e)
    return opcion


def leerTitulo(msg):
    while True:
        try:
            n = input(msg)
            n.strip()
            if(n==""):
                print("\nTitulo no valido\n")
                continue
            return n
        except Exception as e:
            print("\nError al ingresar el titulo\n", e)

def leerAutor(msg):
    while True:
        try:
            n = input(msg)
            n.strip()
            if(n==""):
                print("\nAutor no valido\n")
                continue
            return n
        except Exception as e:
            print("\nError al ingresar el Autor\n", e)

def leerPrecio(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<0):
                print("\nValor invalido, debe ser mayor a cero\n")
                continue
            return n
        except Exception as e:
            print("\nError\n",e)


def leercodigo(msg):
    while True:
        try:
            codigo = str(input(msg))
            codigo = codigo.lower()
            if(codigo == "" or not codigo.isalnum()):
                print("\nValor invalido, no debe ser vacio\n")
                continue
            return codigo
        except Exception as e:
            print("\nError\n",e)





def existecodigo(codigo,lstlibro):
    variable = False
    for datos in lstlibro:
        K = (list(datos.keys())[0])
        if( K == codigo):
            variable = True
            return variable
        else:
            variable = False
    return variable
        
def cargarinfo(rutaFile):
    lstlibro = []
    try:
        fd = open(rutaFile,"r")
    except Exception as e:
        try:
            fd = open(rutaFile,"w")
        except Exception as d:
            print("Error al intentar abrir el archivo",d)
            fd.close()
            return lstlibro
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstlibro = json.load(fd)
        else:
            lstlibro = []
    except Exception as e:
        print("Error al cargar la informacion",e)
        return lstlibro
    
    fd.close()
    return lstlibro

def guardarLibro(lst,rutaFile):
    try:
        fd = open(rutaFile,"w")
    except Exception as e:
        print("error",e) 
        return None
    
    try:
        json.dump(lst,fd)
    except Exception as e:
        print("Error al guardar la información del libro",e)

    fd.close
    return True


def insertarlibro(lstlibro,rutaFile):
    print("\n1. Agregar libro")
    codigo = str(leercodigo("ingrese el codigo: "))
    while existecodigo(codigo,lstlibro):
        print("libro existe en codigo")
        input()
        codigo = str(input("ingresea el codigo: "))

    Titulo = leerTitulo("titulo =?: ")
    Autor = leerAutor("Autor =?: ")
    Precio = leerPrecio("Precio =?: ")
    DictLibros = {}
    DictLibros[codigo] = {"titulo":Titulo, "autor": Autor,"precio":Precio}
    lstlibro.append(DictLibros)

    if guardarLibro(lstlibro,rutaFile) == True:
        print("libro guardado con exito")
    else:
        print("Ocurrio un error al guardar el libro")



def consultarlibro(lstlibro,codigo):
    if existecodigo(codigo,lstlibro) == True:
        print()
        print("libro encontrado")
        for datos in lstlibro:
            K = (list(datos.keys())[0])
            if( K == codigo):
                print(f"Libro: {list(datos.values())[0]['titulo']}")
                print(f"Autor: {list(datos.values())[0]['autor']}")
                print(f"Precio: {list(datos.values())[0]['precio']}")
                print()
                return   
    else:
        print()
        print("Libro no encontrado")
        print()
        return
    
def EditarLibro(lstlibro,rutafile):
    codigo = str(leercodigo("Digite codigo del libro a consultar"))
    if existecodigo(codigo,lstlibro) == True:
          for datos in lstlibro:
            K = (list(datos.keys())[0])
            if( K == codigo):
                indice = lstlibro.index(datos)
                consultarlibro(lstlibro,codigo)
                while True:
                    try:
                        print("\nOPCIONES A MODIFICAR")
                        print("1. Nombre del libro")
                        print("2. Autor")
                        print("3. Precio\n")
                
                        select = int(input("\nDigite la opcion del libro que quiere modificar: "))
                        if(select<1 or select>3):
                            print("Error numero fuera de rango")
                            continue
                        break
                    except Exception as e:
                        print("Error", e)
                            
                if(select == 1):
                    Titulo = leerTitulo("titulo =?: ")
                    lstlibro[indice][codigo]["titulo"] = Titulo
                elif(select ==2):
                    Autor = leerAutor("Autor =?: ") 
                    lstlibro[indice][codigo]["autor"] = Autor
                elif(select == 3):
                    Precio = leerPrecio("Precio =?: ")
                    lstlibro[indice][codigo]["precio"] = Precio
                
                
                if guardarLibro(lstlibro,rutafile) == True:
                    print("libro editado con exito")
                else:
                    print("Ocurrio un error al editar el libro")
                return
                            
    else:
        print()
        print("Libro no encontrado")
        print()
        return
    
def BorrarLibro(lstlibro,rutafile):
    codigo = str(leercodigo("Digite codigo del libro a borrar"))
    if existecodigo(codigo,lstlibro) == True:
        for datos in lstlibro:
            indice = lstlibro.index(datos)
            K = (list(datos.keys())[0])
            if( K == codigo):
                lstlibro.remove(lstlibro[indice])
                if guardarLibro(lstlibro,rutafile) == True:
                    print("libro borrado con exito")
                else:
                    print("Ocurrio un error al borrar el libro")
                return
                            
    else:
        print()
        print("Libro no encontrado")
        print()
        return
    
def OrdenarLibros(lstlibros,rutafile,categoria):
    for i in range(len(lstlibros)-1):
        for j in range(i+1,len(lstlibros)):
            K = (list(lstlibros[i].keys())[0])
            Kj = (list(lstlibros[j].keys())[0])
            if(lstlibros[i][str(K)][categoria]>lstlibros[j][str(Kj)][categoria]):
                t= lstlibros[i]
                lstlibros[i] = lstlibros[j]
                lstlibros[j] = t
    return  lstlibros
    
def listarLibro(lstLibro,rutafile):
    while True:
        try:
            print("\nOPCIONES A listar")
            print("1. Por Nombre")
            print("2. Por Autor")
            print("3. Por Precio\n")
            select = int(input("\nDigite la opcion por la que quiere listar los libros: "))
            if(select<1 or select>3):
                print("Error numero fuera de rango")
                continue
        except Exception as e:
            print("Error", e)
        
        print()
        if(select==1):
            Categoria = "titulo"
            listanueva = OrdenarLibros(lstLibro,rutafile,Categoria)
        elif(select==2):
            Categoria = "autor"
            listanueva = OrdenarLibros(lstLibro,rutafile,Categoria)
        elif(select==3):
            Categoria = "precio"
            listanueva = OrdenarLibros(lstLibro,rutafile,Categoria)
        cont = 1
        for i in range(len(listanueva)):
            K = (list(listanueva[i].keys())[0])
            print(" ", listanueva[i][K]["titulo"],listanueva[i][K]["autor"],listanueva[i][K]["precio"])
            print()
            
            if(cont==3):
                cont=0
                op = input(">> desea continuar? si: cualquier letra no: n: ")
                print()
                if(op == "n"):
                    return
            cont+=1
            
        print("No hay mas libros para mostrar..")
        print()
        return
                         
                   
             
        
    




def main():
    
    rutafile = "Reviews\\libros.json"
    lstlibro = cargarinfo(rutafile)        
    while True:
        opcion = menu()
        if(opcion==1):
            insertarlibro(lstlibro,rutafile)
        elif(opcion==2):
            codigo = str(leercodigo(">> Digite codigo del libro a consultar"))
            consultarlibro(lstlibro,codigo)
        elif(opcion==3):
            EditarLibro(lstlibro,rutafile)
        elif(opcion==4):
            BorrarLibro(lstlibro,rutafile)
        elif(opcion==5):
            listarLibro(lstlibro,rutafile)
            
        op = str(input(">> Volver al Menu? si: cualquier caracter / no: n: "))
        print()
                 
        if op.lower() == "n":
            return
                
        
main()
