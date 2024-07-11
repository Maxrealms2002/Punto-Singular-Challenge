from logica import BancoPatitoDB
from logica import validacionDatos
import asciiArt

# Esta variable se encarga de cerrar el programa cuando
# es verdadera (True)
salir = False

# Instancias de objetos
banco = BancoPatitoDB()
val = validacionDatos()

# Interfaz principal que ejecuta el programa
print(asciiArt.patito)
print(asciiArt.nombreBanco)

while salir is False:

    print("Bienvenido a la app de PatitoBank\n¿Que desea hacer el dia de hoy?")
    print(asciiArt.opciones)

    # Este bloque de codigo permite no que el usuario no ingrese opciones invalida
    # que rompan la ejecucion del programa
    opcion = input("Seleccione el numero de la opcion\n> ")

    # Crear una cuenta
    if opcion == "1":

        # Varible booleana para volver a ingresar CURP en caso
        # de ingresar un valor no permitido
        curpValidada = False
        curp = ""
        nombretitular = input("Ingrese nombre de titular\n> ")

        while curpValidada is False:
            validacion = val.validarCurp(curp)

            if validacion:
                # Asegura que la CURP solo contenga 16 caracteres
                curp = curp[0:16]
                curpValidada = True
            else:
                curp = input("Ingrese una CURP valida\n> ")

        banco.crearCuenta(titular=nombretitular, curp=curp)
        print("\nLa cuenta ha sido creada con exito!!!\n")
        input("\nPrescione Enter para continuar\n")

    # Mostrar saldo de una cuenta
    elif opcion == "2":
        numeroCuenta = input("Ingrese un numero de cuenta valido\n> ")
        validacion = val.validarNumeroCuenta(numeroCuenta)

        # Verifica que el usuario no ingrese texto o un numero que
        # no sea igual a 10 digitos
        if validacion:
            listaCuentas = banco.obtenerCuentas()
            numeroCuenta = int(numeroCuenta)
            cuentaExiste = banco.existeCuenta(numeroCuenta, listaCuentas)

            if cuentaExiste:
                # Recuperamos el balance actual en la cuenta del usuario
                saldo = banco.obtenerSaldo(numeroCuenta)
                print(f"El saldo de la cuenta {numeroCuenta} es:\n${saldo} MXN")

                # Recuperamos el valor del premio que el usuario puede solicitar
                premio = banco.obtenerPremio(numeroCuenta)

                # Con esto vaidamos si el premio se ha cobrado con anterioridad
                if premio == 0.0:
                    input("\nPrescione Enter para continuar\n")

                # Si el premio no ha sido cobrado, le preguntamos al usuario si desea
                # cobrarlo
                else:
                    respuesta = input("Te gustaria solicitar el premio: Y o N\n> ").upper()

                    if respuesta == "Y":
                        banco.cobrarPremio(numeroCuenta, premio)
                        print("\n El premio ha sido cobrado con exito!!!")

                        while respuesta == "Y":
                            respuesta = input("¿Te gustaria simular otra fecha para ganar premio? Y o N\n> ").upper()
                            if respuesta == "Y":
                                print(asciiArt.premios)
                                print(f"\nFecha de creacion de esta cuenta:\n{banco.obtenerFecha(numeroCuenta)}\n")

                                # Evalua que el usuario unicamente ingrese numeros en
                                # formato decimal (0.0)
                                montoValidado = False
                                monto = ""
                                while montoValidado is False:
                                    validacion = val.validarDinero(monto)

                                    if validacion:
                                        montoValidado = True
                                    else:
                                        monto = input("Ingresa el monto a depositar en formato decimal\n> ")

                                monto = float(monto)

                                # Evalua que el usuario unicamente ingrese numeros en
                                # formato entero

                                anioValidado = False
                                anio = ""
                                while anioValidado is False:
                                    validacion = val.validarInt(anio)

                                    if validacion:
                                        anioValidado = True
                                    else:
                                        anio = input("Ingrese la cantidad de años que desea que tenga su cuenta\n> ")

                                anio = int(anio)
                                banco.simularPremios(monto, anio)

                            else:
                                input("\nPrescione Enter para continuar\n")
                    else:
                        input("\nPrescione Enter para continuar\n")
            else:
                print("Ha introducido un numero de cuanta que no existe")
                input("\nPrescione Enter para continuar\n")
        else:
            print("Ha introducido un numero de cuenta no valido")
            input("\nPrescione Enter para continuar\n")

    # Depositar dinero a cuenta
    elif opcion == "3":
        numeroCuenta = input("Ingrese un numero de cuenta valido\n> ")
        validacion = val.validarNumeroCuenta(numeroCuenta)

        # Verifica que el usuario no ingrese texto o un numero que
        # no sea igual a 10 digitos
        if validacion:

            listaCuentas = banco.obtenerCuentas()
            numeroCuenta = int(numeroCuenta)
            cuentaExiste = banco.existeCuenta(numeroCuenta, listaCuentas)

            if cuentaExiste:
                # Evalua que el usuario unicamente ingrese numeros en
                # formato decimal (0.0)
                montoValidado = False
                monto = ""
                while montoValidado is False:
                    validacion = val.validarDinero(monto)

                    if validacion:
                        montoValidado = True
                    else:
                        monto = input("Ingresa el monto a depositar en formato decimal\n> ")

                monto = float(monto)

                concepto = input("Ingrese el concepto del movimiento (Opcional)\n> ")

                # Crea y registra la operacion de transaccion en la cuenta especificada
                numeroTransaccion = banco.crearTransaccion(numeroCuenta=numeroCuenta, monto=monto, concepto=concepto)
                # Deposita el dinero al balance de la cuenta
                banco.depositarDinero(numeroCuenta=numeroCuenta, numerotransaccion=numeroTransaccion)
                print("\nDeposito realizado con exito!!!\n")
                input("\nPrescione Enter para continuar\n")
            else:
                print("Ha introducido un numero de cuanta que no existe")
                input("\nPrescione Enter para continuar\n")
        else:
            print("Ha introducido un numero de cuenta no valido")
            input("\nPrescione Enter para continuar\n")

    # Retirar dinero de cuenta
    elif opcion == "4":
        numeroCuenta = input("Ingrese un numero de cuenta valido\n> ")
        validacion = val.validarNumeroCuenta(numeroCuenta)

        # Verifica que el usuario no ingrese texto o un numero que
        # no sea igual a 10 digitos
        if validacion:

            listaCuentas = banco.obtenerCuentas()
            numeroCuenta = int(numeroCuenta)
            cuentaExiste = banco.existeCuenta(numeroCuenta, listaCuentas)

            if cuentaExiste:
                # Evalua que el usuario unicamente ingrese numeros en
                # formato decimal (0.0)
                montoValidado = False
                monto = ""
                while montoValidado is False:
                    validacion = val.validarDinero(monto)

                    if validacion:
                        montoValidado = True
                    else:
                        monto = input("Ingresa el monto a retirar en formato decimal\n> ")

                monto = float(monto)
                # Recuperamos el valor de nuestro saldo actual
                balanceCuenta = banco.obtenerSaldo(numeroCuenta)

                # Este bloque de codigo asegura que el usuario no intente
                # retirar mas dinero del que tiene en su cuenta
                if monto < balanceCuenta:
                    concepto = input("Ingrese el concepto del movimiento (Opcional)\n> ")

                    # Crea y registra la operacion de transaccion en la cuenta especificada
                    numeroTransaccion = banco.crearTransaccion(numeroCuenta=numeroCuenta, monto=monto,
                                                               concepto=concepto)
                    # Deposita el dinero al balance de la cuenta
                    banco.retitarDinero(numeroCuenta=numeroCuenta, numerotransaccion=numeroTransaccion)
                    print("\nRetiro realizado con exito!!!\n")
                    input("\nPrescione Enter para continuar\n")
                else:
                    print("\nError: Ha intendado retirar mas dinero del que tiene en su cuenta\n")
                    input("\nPrescione Enter para continuar\n")
            else:
                print("Ha introducido un numero de cuanta que no existe")
                input("\nPrescione Enter para continuar\n")
        else:
            print("Ha introducido un numero de cuenta no valido")
            input("\nPrescione Enter para continuar\n")

    # Mostrar todas las cuentas
    elif opcion == "5":

        # Valida si el usuario ha creado una contraseña
        # previamente

        contrasenaExiste = val.contrasenaExiste()

        if contrasenaExiste:
            contrasena = input("Introduzca la contraseña\n> ")
            contrasenaValidada = val.validarContrasena(contrasena)

            # Solo cuando el usuario ingresa una contraseña valida
            # el sistema imprimira todas las cuentas del banco
            if contrasenaValidada:
                banco.mostrarCuentas()
                input("\nPrescione Enter para continuar\n")

            # De lo contrario, cancelara la operacion
            else:
                print("\nError: Las contraseñas no coinciden\n")
                input("\nPrescione Enter para continuar\n")

        # De lo contrario, crea una nueva contraseña
        else:
            nuevaContrasena = input("Introduzca una nueva contraseña\n> ")
            val.crearContrasena(nuevaContrasena)
            print("\nSu nueva contraseña fue creada exitosamente!\n")
            input("\nPrescione Enter para continuar\n")

    # Mostrar historial de transacciones de una cuenta
    elif opcion == "6":

        # Valida si el usuario ha creado una contraseña
        # previamente

        contrasenaExiste = val.contrasenaExiste()

        if contrasenaExiste:
            contrasena = input("Introduzca la contraseña\n> ")
            contrasenaValidada = val.validarContrasena(contrasena)

            # Solo cuando el usuario ingresa una contraseña valida
            # el sistema imprimira todas las cuentas del banco
            if contrasenaValidada:
                numeroCuenta = input("Ingrese un numero de cuenta valido\n> ")
                validacion = val.validarNumeroCuenta(numeroCuenta)

                # Verifica que el usuario no ingrese texto o un numero que
                # no sea igual a 10 digitos
                if validacion:

                    listaCuentas = banco.obtenerCuentas()
                    numeroCuenta = int(numeroCuenta)
                    cuentaExiste = banco.existeCuenta(numeroCuenta, listaCuentas)

                    if cuentaExiste:
                        banco.mostrarTransferencias(numeroCuenta)
                        input("\nPrescione Enter para continuar\n")
                    else:
                        print("Ha introducido un numero de cuanta que no existe")
                        input("\nPrescione Enter para continuar\n")
                else:
                    print("Ha introducido un numero de cuenta no valido")
                    input("\nPrescione Enter para continuar\n")

            # De lo contrario, cancelara la operacion
            else:
                print("\nError: Las contraseñas no coinciden\n")
                input("\nPrescione Enter para continuar\n")

        # De lo contrario, crea una nueva contraseña
        else:
            nuevaContrasena = input("Introduzca una nueva contraseña\n> ")
            val.crearContrasena(nuevaContrasena)
            print("\nSu nueva contraseña fue creada exitosamente!\n")
            input("\nPrescione Enter para continuar\n")

    # Permite cerrar el programa
    elif opcion == "7":
        salir = True

    # En caso de un valor no permitido
    else:
        print("\nOpcion no valida")
        input("\nPrescione Enter para continuar\n")

print("\nGracias por usar la app, que tenga un excelente dia")
