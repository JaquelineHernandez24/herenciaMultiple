from clases import Persona, Empleado, Responsable, Departamento, Area, Director, Gerente, JefeArea

def main():
    # Crear Departamento y Área
    depto_it = Departamento("Sistemas Computacionales")
    area_desarrollo = Area("Desarrollo", depto_it)

    # Crear empleados de diferentes roles
    director = Director("Ana Pérez", 45, "Av. Siempre Viva 123", "Director", 150000)
    gerente = Gerente("Luis García", 40, "Calle Falsa 456", "Gerente", 120000)
    jefe_area = JefeArea("Laura Torres", 38, "Calle Central 789", "Jefe de Área", 100000)

    # Asignación de Área (demostrativo)
    print(f"Departamento: {area_desarrollo.departamento.nombre}")
    print(f"Área: {area_desarrollo.nombre}")

    # Mostrar información de los empleados
    print(f"Director: {director.nombre}, Puesto: {director.puesto}, Salario: {director.salario}")
    print(f"Gerente: {gerente.nombre}, Puesto: {gerente.puesto}, Salario: {gerente.salario}")
    print(f"Jefe de Área: {jefe_area.nombre}, Puesto: {jefe_area.puesto}, Salario: {jefe_area.salario}")

if __name__ == "__main__":
    main()
