productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def validacion_texto(mensaje:str):
    while True:
        texto = input(mensaje)
        if len(texto) == 0:
            print("El texto debe contener caracteres.")
            continue
        return False



def stock_marca(marca:str):
    marca =input("Ingresa la marca a buscar")
    for i in stock:
        if stock [1][0] == marca:
            print("Hay stock")
            marca_encontradaa =[1]
            marca_encontradaa.insert[0,1]
            return marca_encontradaa
    for i in stock[productos]:
        print ("NOMBRE:"+i["NOMBRE"]+stock)       


def busqueda_precio(p_min:int,p_max:int):
    for i in productos:
        if i == stock:
            print(f"producto",productos)
    print("Producto no encontrado.")
def actualizar_precio(modelo,p):
    stock_disponible = stock_marca(modelo)
    if stock_disponible>= 0:
        stock[modelo][1] =+0
        print("Precio actualizado")
        return True
    else:
        print("Modelo no encontrado!")
    while True:
        try:
            actualizar = (input("Ingresa el modelo a actualizar : "))
            if actualizar <=0:
                print("Porfavor ingresa un valor mayor a 0")
                continue
            break
        except ValueError:
            print("Porfavor ingresa un valor valido")
    

def validar_numero_entero_positivo():
        while True:
            try:
                actualizar = (input("Ingresa el modelo a actualizar : "))
                if actualizar <=0:
                    print("Porfavor ingresa un valor mayor a 0")
                    continue
                break
            except ValueError:
                print("Porfavor ingresa un valor valido")



while True:
        print("*** MENU PRINCIPAL ***")
        print("[1]Stock marca")
        print("[2]Busqueda por precio")
        print("[3]Actualizar precio")
        print("[4] Salir")
        try:
            opc = int(input("Ingresa un valor (1-4): "))
        except ValueError:
            print("Ingresa un valor valido!")
        if opc == 1:
            print(stock_marca)
        elif opc == 2:
            input("Ingresa el numero menor: ")
            p_min=(validar_numero_entero_positivo)
            input("Ingresa el numero mayor: ")
            p_max=(validar_numero_entero_positivo)
            busqueda_precio()
        elif opc == 3:
            print(actualizar_precio)
        elif opc == 4:
            break