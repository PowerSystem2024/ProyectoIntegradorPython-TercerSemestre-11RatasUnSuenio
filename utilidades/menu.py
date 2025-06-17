def menu():
  print("1. Nuestros servicios")
  print("2. Reserva Online")
  print("3. Contacto")
  print("4. Salir")
    
  opcion = input("\nSelecciona una opción (1-4): ")
  
  if opcion == '1':
      print("Reservando habitación...")
  elif opcion == '2':
      print("Consultando disponibilidad...")
  elif opcion == '3':
      print("Cancelando reserva...")
  elif opcion == '4':
      print("Saliendo del sistema...")
  else:
      print("Opción no válida, por favor intenta de nuevo.")