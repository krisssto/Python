import sqlite3
import getpass

def search_user(name):

    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM alumnos WHERE nombre = '{name}'"
    
    rows = cursor.execute(query)
    data = rows.fetchone()

    if data == None:
        print("No se encontro el alumno!")
    else:
        print(data)

    cursor.close()
    conn.close()

def main():
    name = input("Ingrese el nombre del alumno: ")

    search_user(name);

if __name__ == '__main__':
    main()