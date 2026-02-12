Hola hola espero estes bien, te adjunto la documentación de lo que hice y el por que lo hice.
Primero defini variables: "usuario_correcto" y "password_correcto" para comparar los datos ingresados.
Segundo Bucle de Intentos: Use un while que se repite mientras intento_actual sea menor a 3.
Tercero lógica anidad: Primero validamos si el nombre_usuario coincide. Si coincide, entramos a un segundo if para validar la password_usuario. Esto cumple con el requisito de "condiciones anidadas".
Cuarto utilización de "Break": Si las credenciales son correctas, el break rompe el ciclo de intentos inmediatamente.
Quinto y final Reinicio del programa: Al finalizar los 3 intentos sin éxito, el programa lanza un input(). Si el usuario escribe algo distinto a "si", el bucle principal se rompe con otro break y el programa termina.
<img width="1026" height="516" alt="image" src="https://github.com/user-attachments/assets/afe3b5bf-1827-4b69-9615-d9cfd8b46581" />

