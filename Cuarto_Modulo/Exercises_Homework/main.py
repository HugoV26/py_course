
my_d = {}

with open("./test.txt", "r") as file:
    lines = file.readlines()

    lines.isnan()

    print(lines)
    
    
    one = lines[0]
    print(one)

    valor = one.replace('*', '').replace(' ', '')
    a, b = valor.split(':')
    print(a, b)
    my_d[a] = b.strip('\n')
    print(my_d)

    one = lines[2]
    print(one)
    #print(line.rfind('E'))
    position = one.rfind('E')
    valor = one[(position+1):].replace(' ', '')
    print(valor)
    my_d["tiempo_de_arranque"] = valor.replace('\n', '')
    print(my_d)

    """
    for line in lines:
        
        if "Producto" in line:
            valor = line.replace('*', '').replace(' ', '')
            a, b = valor.split(':')
            print(a, b)
            my_d[a] = b.strip('\n')
            print(my_d)
        
        elif "TIEMPO DE ARRANQUE" in line:
            #print(line.rfind('E'))
            position = line.rfind('E')
            valor = line[(position+1):].replace(' ', '')
            print(valor)
            my_d["tiempo_de_arranque"] = valor.replace('\n', '')
            print(my_d)

        elif "TOTAL PES" in line:
            position = line.rfind('S')
            #print(position)
            valor = line[(position+1):].replace(' ', '')
            #print(valor)
            my_d["total_peso"] = valor.strip()
            print(my_d)
        """