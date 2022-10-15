### Abishek - Oct 5, 2022 ###

import db.store as store
import db.retrieve as retrieve


def main():
    db_name = 'password_store'
    # Get type of task
    task = None
    while task != 3:
        task = int(input("What do you want to do: \n1 - Get password.\n2 - Store password.\n3 - Quit\n"))
        if task == 1:
            print("Powering up the database to retrieve...")
            retrieve.retrieve()
        elif task == 2:
            print("Powering up the database to store...")
            store.store(db_name)
        else:
            print("Exiting...")
            return 0


if __name__ == '__main__':
    main()
