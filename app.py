tareas = []

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS CLI ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea():
    titulo = input("Ingresa el título de la tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada con éxito.")

def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for i, t in enumerate(tareas, 1):
        estado = "✔" if t["completada"] else "✘"
        print(f"{i}. [{estado}] {t['titulo']}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "5":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción aún no implementada.")

if __name__ == "__main__":
    main()
