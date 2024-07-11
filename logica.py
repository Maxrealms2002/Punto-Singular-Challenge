import random
import datetime
import re


# Esta clase simula ser una base de datos que almacenara los
# datos de las cuentas bancarias, ademas de registrar cada
# transaccion realizada en la aplicación
class BancoPatitoDB:

    # Metodo constructor que fungira como una base de datos
    # para almacenar cada cuenta creada.
    def __init__(self):
        self.CuentasBancarias = {}

    # Este metodo permite alojar los datos iniciales al
    # crear una cuenta nueva, es decir: curp, nombre del
    # titular y un ID.

    def crearCuenta(self, titular: str, curp: str) -> None:
        DatosBancario = {
            "titular": titular,
            "curp": curp,
            "fecha de creacion": "",
            "balance": 0.0,
            "transacciones": {},
            "Premio cobrado": False
        }

        # Genera una fecha de creacion aleatoria para la cuenta
        DatosBancario.update({"fecha de creacion": self.generarFecha()})

        # numero de cuenta aleatorio
        id = self.generarID()

        # Corrobora que los numeros de cuenta no se repitan
        if id in self.CuentasBancarias:
            id = self.generarID()
        else:
            self.agregarCuentaDB(numeroCuenta=id, datos=DatosBancario)

    # Este metodo permite añadir una cuenta recien creada a un
    # diccionario de datos que las almacenara como un base de datos
    def agregarCuentaDB(self, numeroCuenta: int, datos: dict) -> None:
        self.CuentasBancarias.update({numeroCuenta: datos})

    # Este metodo crea una transacción, ya sea un retiro o un deposito
    def crearTransaccion(self, numeroCuenta: int, monto: float, concepto: str) -> int:
        transaccion = {"cantidad": monto,
                       "fecha y hora": datetime.datetime.now(),
                       "concepto": concepto,
                       "tipo": ""}

        # Creamos la fecha de la transaccion en formato legible
        fechaActual = datetime.datetime.now()
        fechaLegible = fechaActual.strftime("%c")
        transaccion["fecha y hora"] = fechaLegible

        # numero de transaccion aleatorio
        id = self.generarID()

        # Corrobora que los numeros de cuenta no se repitan
        if id in self.CuentasBancarias:
            id = self.generarID()
        else:
            self.agregarTransaccion(numeroCuenta, idoperacion=id, datos=transaccion)

        # Devuelve el identificador de la transaccion para
        # operaciones de retiro y deposito
        return id

    # Este metodo permite añadir una transaccion a un numero
    # de cuenta
    def agregarTransaccion(self, numeroCuenta: int, idoperacion: int, datos: dict) -> None:
        # Permite añadir muchas transacciones a una misma cuenta
        self.CuentasBancarias[numeroCuenta]["transacciones"].update({idoperacion: datos})

    # Metodo para depositar dinero a una cuenta
    def depositarDinero(self, numeroCuenta: int, numerotransaccion: int) -> None:

        # Recuperamos el valor de la transaccion
        monto = self.CuentasBancarias[numeroCuenta]["transacciones"][numerotransaccion]["cantidad"]

        # Indicamos el tipo de transaccion, en este caso es un deposito
        self.CuentasBancarias[numeroCuenta]["transacciones"][numerotransaccion]["tipo"] = "Deposito"

        # Recuperamos el valor del balance de la cuenta asociada
        balance_actual = self.CuentasBancarias[numeroCuenta]["balance"]

        # Al ser un depositso el valor se suma y se actualiza
        # el valor del balance de la cuenta.
        balance_nuevo = balance_actual + monto
        # balance_formato = f"+ ${balance_nuevo}"
        self.CuentasBancarias[numeroCuenta]["balance"] = balance_nuevo

    # Metodo para retirar dinero a una cuenta
    def retitarDinero(self, numeroCuenta: int, numerotransaccion: int):

        # Recuperamos el valor de la transaccion
        monto = self.CuentasBancarias[numeroCuenta]["transacciones"][numerotransaccion]["cantidad"]

        # Indicamos el tipo de transaccion, en este caso es un retiro
        self.CuentasBancarias[numeroCuenta]["transacciones"][numerotransaccion]["tipo"] = "Retiro"

        # Recuperamos el valor del balance de la cuenta asociada
        balance_actual = self.CuentasBancarias[numeroCuenta]["balance"]

        # Corrobora que el monto a retirar no sea mayor al que exista
        # en la cuenta
        balance_nuevo = balance_actual - monto
        self.CuentasBancarias[numeroCuenta]["balance"] = balance_nuevo

    # Este metodo se encarga de generar el ID que se
    # compone de 10 digitos aleatorios
    def generarID(self) -> int:
        id_cuenta = random.randint(1000000000, 9999999999)
        return id_cuenta

    # Este metodo genera una fecha de creacion de cada cuenta
    # de manera aleatoria contando años desde el año 2000 a
    # 2024
    def generarFecha(self) -> list:
        # primero se generan los dias, meses y años
        dia = random.randint(1, 31)
        mes = random.randint(1, 12)
        anio = random.randint(2000, 2024)

        fecha = [anio, mes, dia]
        return fecha

    # Este metodo sirve para crear y recuperar una fecha mas legible
    # en el formato dia/mes/año
    def obtenerFecha(self, numeroCuenta: int) -> str:
        fecha = self.CuentasBancarias[numeroCuenta]["fecha de creacion"]
        fechaPreFormato = datetime.datetime(fecha[0], fecha[1], fecha[2])
        fechaFormato = fechaPreFormato.strftime("%d/%m/%Y")
        return fechaFormato

    # Este metodo se encarga de mostrar el saldo de una cuenta
    def obtenerSaldo(self, numeroCuenta: int) -> float:
        saldo = self.CuentasBancarias[numeroCuenta]["balance"]
        return saldo

    # Este metodo muestra todas las cuentas creadas
    # Solo mostrando nombre del titular y el numero de la cuenta
    def mostrarCuentas(self) -> None:
        for x in self.CuentasBancarias.keys():
            print(f"{x} - {self.CuentasBancarias[x]["titular"]}")

    # Este metodo obtiene los numeros de cuentas creados
    # y los devuelve como una lista
    def obtenerCuentas(self) -> list:
        numeroCuentas = []
        for x in self.CuentasBancarias.keys():
            numeroCuentas.append(x)
        return numeroCuentas

    # Este metodo comprueba que existe una cuenta en la
    # base de datos
    def existeCuenta(self, numeroCuenta: int, listaCuentas: list) -> bool:
        valor = listaCuentas.count(numeroCuenta)
        if valor == 1:
            return True
        else:
            return False

    # Este metodo permite mostrar cada una de als transacciones
    # realizadas por una cuenta en especifico
    def mostrarTransferencias(self, numeroCuenta: int) -> None:
        transferencias = self.CuentasBancarias[numeroCuenta]["transacciones"]
        # print(self.CuentasBancarias[numeroCuenta])
        for x, y in transferencias.items():
            print(f"{x} - {y}")

    # Esta funcion determina que premio es acreedor una cuenta
    # en base al monto y fecha de creacion de la cuenta
    def obtenerPremio(self, numeroCuenta: int) -> float:
        monto = self.CuentasBancarias[numeroCuenta]["balance"]
        anioCuenta = self.CuentasBancarias[numeroCuenta]["fecha de creacion"][2]
        premio = 0.0

        # Primero verificamos que el premio no haya sido cobrado antes
        premioCobrado = self.validarPremio(numeroCuenta)
        if premioCobrado:
            print("Usted ya ha cobrado su premio")
        else:

            # Evaluador de premios
            if anioCuenta >= 15:
                if monto < 1500.0:
                    print("Necesita al menos 1500 MXN para ser acreedor de un premio")

                else:
                    premio = (monto / 100) * 25
                    print(f"Felicidades!!! puede solicitar un premio de {premio}")

            elif 15 > anioCuenta >= 10:
                if monto < 1000.0:
                    print("Necesita al menos 1000 MXN para ser acreedor de un premio")

                else:
                    premio = (monto / 100) * 20
                    print(f"Felicidades!!! puede solicitar un premio de {premio}")

            elif 10 > anioCuenta >= 5:
                if monto < 1000.0:
                    print("Necesita al menos 1000 MXN para ser acreedor de un premio")

                else:
                    premio = (monto / 100) * 15
                    print(f"Felicidades!!! puede solicitar un premio de {premio}")

            elif 5 > anioCuenta >= 3:
                if monto < 500.0:
                    print("Necesita al menos 500 MXN para ser acreedor de un premio")

                else:
                    premio = (monto / 100) * 12
                    print(f"Felicidades!!! puede solicitar un premio de {premio}")

            elif 3 > anioCuenta >= 1:
                if monto < 250.0:
                    print("Necesita al menos 250 MXN para ser acreedor de un premio")

                else:
                    premio = (monto / 100) * 10
                    print(f"Felicidades!!! puede solicitar un premio de {premio}")

            else:
                if monto < 100.0:
                    print("Necesita al menos 100 MXN para ser acreedor de un premio")

                else:
                    premio = (monto / 100) * 5
                    print(f"Felicidades!!! puede solicitar un premio de {premio}")

        return premio

        # Esta funcion determina si el usuario ya ha cobrado su premio

    def validarPremio(self, numeroCuenta: int) -> bool:
        # Primero se obtiene el valor booleano
        premioCobrado = self.CuentasBancarias[numeroCuenta]["Premio cobrado"]

        # Si ya fue cobrado, entonces devuelve verdadero
        if premioCobrado:
            return True
        # Si no ha sido cobrado, entonces devuelve falso
        else:
            return False

    # Este metodo permite cobrar el premio al que una cuenta es acreedor:
    def cobrarPremio(self, numeroCuenta: int, premio: float) -> None:

        # Creamos la transaccion necesaria para cobrar el premio
        numeroTransaccion = self.crearTransaccion(numeroCuenta=numeroCuenta, monto=premio, concepto="Premio")
        self.depositarDinero(numeroCuenta=numeroCuenta, numerotransaccion=numeroTransaccion)

        # Ahora indicamos que el premio ya fue cobrado
        self.CuentasBancarias[numeroCuenta]["Premio cobrado"] = True

    # Este metodo sirve para simular los premios que ganaria el usuario
    # con un año diferente en su cuenta y un monto diferente
    def simularPremios(self, monto: float, anioCuenta: int):
        # Evaluador de premios

        if anioCuenta >= 15:
            if monto < 1500.0:
                print("Necesita al menos 1500 MXN para ser acreedor de un premio")

            else:
                premio = (monto / 100) * 25
                print(f"Felicidades!!! puede solicitar un premio de {premio}")

        elif 15 > anioCuenta >= 10:
            if monto < 1000.0:
                print("Necesita al menos 1000 MXN para ser acreedor de un premio")

            else:
                premio = (monto / 100) * 20
                print(f"Felicidades!!! puede solicitar un premio de {premio}")

        elif 10 > anioCuenta >= 5:
            if monto < 1000.0:
                print("Necesita al menos 1000 MXN para ser acreedor de un premio")

            else:
                premio = (monto / 100) * 15
                print(f"Felicidades!!! puede solicitar un premio de {premio}")

        elif 5 > anioCuenta >= 3:
            if monto < 500.0:
                print("Necesita al menos 500 MXN para ser acreedor de un premio")

            else:
                premio = (monto / 100) * 12
                print(f"Felicidades!!! puede solicitar un premio de {premio}")

        elif 3 > anioCuenta >= 1:
            if monto < 250.0:
                print("Necesita al menos 250 MXN para ser acreedor de un premio")

            else:
                premio = (monto / 100) * 10
                print(f"Felicidades!!! puede solicitar un premio de {premio}")

        else:
            if monto < 100.0:
                print("Necesita al menos 100 MXN para ser acreedor de un premio")

            else:
                premio = (monto / 100) * 5
                print(f"Felicidades!!! puede solicitar un premio de {premio}")


# Esta clase se encarga de validar que los datos introducidos por
# el usuario sean correctos de acuerdo al tipo de dato solicitado
class validacionDatos:
    def __init__(self):
        self.contrasena = ""

    # El metodo permite corroborar que en el sistema existe
    # o no una contraseña asignada
    def contrasenaExiste(self) -> bool:
        if self.contrasena == "":
            return False
        else:
            return True

    # Con este metodo creamos una nueva contraseña para
    # las operaciones de mostrar cuentas y mostrar
    # historial de transacciones
    def crearContrasena(self, nuevacontrsena: str) -> None:
        self.contrasena = nuevacontrsena

    # Este metodo evalua si la contrasena ingresada por el usuario
    # es la misma que fue creada
    def validarContrasena(self, contrasena: str) -> bool:
        if self.contrasena == contrasena:
            return True
        else:
            return False

    # Este metodo se encarga de validar que la CURP
    # ingresada por el usuario siga una estructura
    # valida de acuerdo a los ejemplos del reto
    def validarCurp(self, curp: str) -> bool:
        # Expresion Regular
        patron = r"([A-Z]{2})(\d{6})(H|M)([A-Z]{5})(\d{2})"
        busqueda = re.search(patron, curp)
        if busqueda is None:
            return False
        else:
            return True

    # Este metodo se asegura que el usuario no
    # introduzca texto en campos donde se soliciten
    # cantidades de dinero
    def validarDinero(self, monto: str) -> bool:
        # Expresion Regular
        patron = r"(\d+)\.(\d+)"
        busqueda = re.search(patron, monto)
        if busqueda is None:
            return False
        else:
            return True

    # Este metodo se asegura que el usuario no
    # introduzca texto en campos donde se solicite
    # ingresar numeros entero
    def validarInt(self, numero: str) -> bool:
        # Expresion Regular
        patron = r"^\d+$"
        busqueda = re.search(patron, numero)
        if busqueda is None:
            return False
        else:
            return True

    # Este metodo permite validar si el numero de cuenta
    # ingresado es valido
    def validarNumeroCuenta(self, numeroCuenta: str) -> bool:
        # Expresion Regular
        patron = r"[0-9]{10}"
        busqueda = re.search(patron, numeroCuenta)

        if busqueda is None:
            return False
        else:
            return True
