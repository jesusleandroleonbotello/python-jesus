while True:
    try:
        cat =  int(input("Digite una categoria: "))
        if cat <1 or cat > 3:
            print("Categoria invalida: Ingrese (1,2,3)")
            continue
        break
    except Exception as e:
        print("Error, Categoria invalida", e)
