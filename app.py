tareas = []

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS CLI (AYUDA: Elige un número del 1 al 5) ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea():
    titulo = input("Ingresa el título de la tarea: ").strip()
    if not titulo:
        print("Error: El título de la tarea no puede estar vacío.")
        return
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada con éxito.")

def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for i, t in enumerate(tareas, 1):
        estado = "✔" if t["completada"] else "✘"
        print(f"{i}. [{estado}] {t['titulo']}")

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
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
