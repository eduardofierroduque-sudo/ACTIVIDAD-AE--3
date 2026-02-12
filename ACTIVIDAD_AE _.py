def ejecutar_login():
    # Credenciales predefinidas
    usuario_correcto = "admin"
    password_correcto = "123456"
    
    while True:  # Bucle para permitir reiniciar todo el proceso
        intentos_maximos = 3
        intento_actual = 0
        acceso_concedido = False

        print("\n--- Sistema de Acceso ---")

        while intento_actual < intentos_maximos:
            # Pedir datos al usuario
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            password_usuario = input("Ingrese su contraseña: ")

            # Condiciones anidadas para verificar credenciales
            if nombre_usuario == usuario_correcto:
                if password_usuario == password_correcto:
                    print("¡Acceso concedido! Bienvenido al sistema.")
                    acceso_concedido = True
                    break  # Sale del bucle de intentos por éxito
                else:
                    print("Contraseña incorrecta.")
            else:
                print("El usuario no existe.")

            intento_actual += 1
            intentos_restantes = intentos_maximos - intento_actual
            
            if intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intentos.")
            else:
                print("Acceso bloqueado. Has superado el límite de intentos.")

        # Si el acceso fue exitoso, terminamos el programa por completo
        if acceso_concedido:
            break
        
        # Pregunta final si se agotaron los intentos
        reiniciar = input("\nNo se reconoce Admin y contraseña, ¿quieres volver al inicio? (si/no): ").lower()
        
        if reiniciar != "si":
            print("Programa finalizado. Gracias.")
            break

# Ejecución de la función
if __name__ == "__main__":
    ejecutar_login()