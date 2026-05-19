"""
============================================================
 Dictionary-Based Database Management System
 Language   : Python
 Author     : Esiri Angel Ediri
 University : Prairie View A&M University
============================================================
"""


# ── Helpers ────────────────────────────────────────────────

def print_header(title: str) -> None:
    line = "=" * 44
    print(f"\n{line}")
    print(f"  {title}")
    print(f"{line}")


def print_separator() -> None:
    print("-" * 44)


# ── Core Database Functions ─────────────────────────────────

def add_record(db: dict) -> None:
    """Add a new key-value record to the database."""
    print_header("ADD RECORD")
    key   = input("  Enter key   : ").strip()
    value = input("  Enter value : ").strip()

    if not key:
        print("  [!] Key cannot be empty.")
        return

    if key in db:
        print(f"  [!] Key '{key}' already exists  →  current value: '{db[key]}'")
        choice = input("  Overwrite? (y/n): ").strip().lower()
        if choice != 'y':
            print("  Operation cancelled.")
            return

    db[key] = value
    print(f"  [✓] Record added  →  '{key}' : '{value}'")


def view_records(db: dict) -> None:
    """Display all records, sorted by key or value."""
    print_header("VIEW ALL RECORDS")

    if not db:
        print("  Database is empty.")
        return

    print("  Sort by: (1) Key   (2) Value")
    sort_choice = input("  Choose: ").strip()

    if sort_choice == '2':
        sorted_items = sorted(db.items(), key=lambda x: x[1])
        print("  (sorted by value)")
    else:
        sorted_items = sorted(db.items(), key=lambda x: x[0])
        print("  (sorted by key)")

    print_separator()
    print(f"  {'KEY':<20} {'VALUE'}")
    print_separator()
    for k, v in sorted_items:
        print(f"  {k:<20} {v}")
    print_separator()
    print(f"  Total records: {len(db)}")


def search_record(db: dict) -> None:
    """Search for a record by key."""
    print_header("SEARCH RECORD")
    key = input("  Enter key to search: ").strip()

    if key in db:
        print(f"  [✓] Found  →  '{key}' : '{db[key]}'")
    else:
        print(f"  [!] Key '{key}' not found in database.")


def update_or_delete(db: dict) -> None:
    """Update a record's value or delete a record by key."""
    print_header("UPDATE / DELETE RECORD")
    key = input("  Enter key to update or delete: ").strip()

    if key not in db:
        print(f"  [!] Key '{key}' not found.")
        retry = input("  Try again? (y/n): ").strip().lower()
        if retry == 'y':
            update_or_delete(db)
        return

    print(f"  Current  →  '{key}' : '{db[key]}'")
    print("  (1) Update value")
    print("  (2) Delete record")
    action = input("  Choose: ").strip()

    if action == '1':
        new_value = input("  Enter new value: ").strip()
        db[key] = new_value
        print(f"  [✓] Updated  →  '{key}' : '{db[key]}'")
    elif action == '2':
        del db[key]
        print(f"  [✓] Record '{key}' deleted.")
    else:
        print("  [!] Invalid choice. Operation cancelled.")


# ── Main Menu ───────────────────────────────────────────────

def show_menu() -> None:
    print_header("DATABASE MANAGEMENT SYSTEM")
    print("  1.  Add record")
    print("  2.  View all records")
    print("  3.  Search by key")
    print("  4.  Update / Delete record")
    print("  0.  Exit")
    print_separator()


def main() -> None:
    database: dict = {}

    while True:
        show_menu()
        choice = input("  Select option: ").strip()

        if   choice == '1': add_record(database)
        elif choice == '2': view_records(database)
        elif choice == '3': search_record(database)
        elif choice == '4': update_or_delete(database)
        elif choice == '0':
            print("\n  Goodbye!\n")
            break
        else:
            print("  [!] Invalid option. Please choose 0–4.")


if __name__ == "__main__":
    main()
