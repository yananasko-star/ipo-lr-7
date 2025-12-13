import json

def show_menu():
    print("\n=== МЕНЮ ===")
    print("1. Показать города")
    print("2. Найти город")
    print("3. Добавить город")
    print("4. Удалить город")
    print("5. Выход")
    print("=============")

def get_choice():
    while True:
        choice = input("Выберите (1-5): ")
        if choice in ['1','2','3','4','5']:
            return choice
        print("Ошибка! Выберите 1-5")

def load_data():
    try:
        with open('cities.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_data(cities):
    try:
        with open('cities.json', 'w', encoding='utf-8') as f:
            json.dump(cities, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False

def show_cities(cities):
    if not cities:
        print("Нет городов")
        return
    for c in cities:
        print(f"ID:{c['id']} Город:{c['name']} Население:{c['population']}")

def find_city(cities):
    name = input("Название: ").lower()
    found = [c for c in cities if name in c['name'].lower()]
    if found:
        for c in found:
            print(f"ID:{c['id']} Город:{c['name']}")
    else:
        print("Не найдено")

def add_city(cities):
    try:
        cid = int(input("ID: "))
        if any(c['id'] == cid for c in cities):
            print("ID уже есть!")
            return cities, False
            
        name = input("Название: ").strip()
        pop = int(input("Население: "))
        reg = input("Регион: ").strip()
        
        cities.append({
            'id': cid,
            'name': name,
            'population': pop,
            'region': reg
        })
        
        if save_data(cities):
            print("Город добавлен!")
            return cities, True
        return cities, False
    except:
        print("Ошибка ввода!")
        return cities, False

def delete_city(cities):
    try:
        cid = int(input("ID для удаления: "))
        for i, c in enumerate(cities):
            if c['id'] == cid:
                if input(f"Удалить {c['name']}? (да/нет): ").lower() == 'да':
                    cities.pop(i)
                    save_data(cities)
                    print("Удалено!")
                    return cities, True
                return cities, False
        print("ID не найден!")
        return cities, False
    except:
        print("Ошибка!")
        return cities, False

def main():
    cities = load_data()
    operations = 0
    
    while True:
        show_menu()
        choice = get_choice()
        
        if choice == '1':
            show_cities(cities)
        elif choice == '2':
            find_city(cities)
        elif choice == '3':
            cities, ok = add_city(cities)
            if ok: operations += 1
        elif choice == '4':
            cities, ok = delete_city(cities)
            if ok: operations += 1
        elif choice == '5':
            print(f"\nОпераций: {operations}\nВыход")
            break

if name == "main":
    main()
