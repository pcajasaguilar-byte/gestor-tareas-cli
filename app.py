tareas = []

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS CLI ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def completar_tarea():
    indice = int(input("Número de tarea a completar: ")) - 1
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Número inválido.")

def eliminar_tarea():
    indice = int(input("Número de tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        eliminada = tareas.pop(indice)
        print(f"Tarea '{eliminada['titulo']}' eliminada.")
    else:
        print("Número inválido.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción aún no implementada.")

if __name__ == "__main__":
    main()
