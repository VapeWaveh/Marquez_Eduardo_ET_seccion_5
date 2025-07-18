
productos = {'C-123': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 'C-111': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'C-234': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'C-456': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'C-1222': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 'C-477': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 'C-334': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'C-2906': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}
stock = {'C-123': [387990,10],
 'C-111': [327990,4],
 'C-234': [424990,1],
 'C-456': [664990,21],
 'C-477': [290890,32],
 'C-334': [444990,7],
 'C-1222': [749990,2],
 'C-2906': [349990,1]}

def actualizar_precio(lst_stock:dict,codigo:str,nuevo_precio:int)->bool:
 if codigo not in lst_stock:
    print("El codigo no existe")
    return False
 else:
    lst_stock[codigo[1]]+=nuevo_precio
 return True
def busqueda_precio (lst_productos:dict,lst_stock:dict,p_min:int,p_max:int)->None:
 if codigo in lst_productos or stock:
    return True
 for p_min,p_max in stock:
    lst_stock[stock[p_min,p_max]]
    print(f"Codigo:{codigo}, Marca: {marca_buscada},Rango de precio: {p_min}-{p_max}")
    continue
def stock_marca(lst_productos:dict,lst_stock:dict,marca_buscada:str)->int:
 total=0
 for codigo,datos in lst_productos.items():
    marca=datos[0]
 if marca.lower() == marca_buscada.lower():
    if codigo in lst_stock:
        total+= lst_stock[codigo[1]]

buscar=[]
lst_productos={}
lst_stock={}


while True:
        print("1.Consultar Stock ")
        print("2.Buscar Producto por rango de precio")
        print("3.Actualizar Precio ")
        print("4.Salir")

        opcion=input("Seleccione una opcion: ")

        if opcion =="1":
                marca_buscada=input("Ingrese la marca: ")
                if stock_marca (lst_productos,lst_stock,marca_buscada):
                    print("El producto se encuentra en stock ")
                else:
                    print("El producto ingresado no existe o no tiene stock ")

        elif opcion =="2":
            try:
                p_min=int(input("Ingrese el precio minimo: "))
                p_max=int(input("Ingrese el precio maximo: "))

            except ValueError:
                print("El precio debe ser un numero entero.")




        elif opcion =="3":
            codigo=input("Ingrese el codigo: ")
            try:
                if actualizar_precio(codigo,nuevo_precio):

                    nuevo_precio=int("Ingrese el nuevo precio: ")

            except ValueError:
                print("Ingrese solo numeros enteros")
            else:
                print("El producto no fue encontrado")

        elif opcion =="4":
            print("Saliendo")
            break

        else:
            print("Opcion ingresada no valida")

