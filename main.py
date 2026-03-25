from db import get_connection


def show_users(cursor):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if not users:
        print("Žádní uživatelé v databázi.")
        return

    for user in users:
        print(user)


def add_user(cursor, conn):
    name = input("Zadej jméno: ").strip()

    if not name:
        print("Jméno nesmí být prázdné.")
        return

    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    print(f"Uživatel '{name}' byl přidán.")


def main():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        while True:
            print("\n1 - zobraz uživatele")
            print("2 - přidat uživatele")
            print("3 - konec")

            choice = input("Vyber: ").strip()

            if choice == "1":
                show_users(cursor)
            elif choice == "2":
                add_user(cursor, conn)
            elif choice == "3":
                print("Konec programu.")
                break
            else:
                print("Neplatná volba.")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
