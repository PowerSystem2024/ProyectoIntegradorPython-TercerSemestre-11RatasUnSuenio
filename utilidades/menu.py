def menu():
  print("1. Nuestros servicios")
  print("2. Reserva Online")
  print("3. Contacto")
  print("4. Salir")
    
  opcion = input("\nSelecciona una opción (1-4): ")
  
  if opcion == '1':
      print("Mostrando servicios...")
  elif opcion == '2':
      print("Reserva...")
  elif opcion == '3':
      print("Mostrando contactos...")
  elif opcion == '4':
      print("Saliendo...")
  else:
      print("Opción no válida, por favor intenta de nuevo.")