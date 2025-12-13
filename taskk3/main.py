import json

# Функции
def show_menu():
    print("\n" + "="*50)
    print("МЕНЮ:")
    print("1. Показать все города")
    print("2. Найти город")
    print("3. Добавить город")
    print("4. Удалить город")
    print("5. Выход")
    print("="*50)

def add_city(cities, filename):
    try:
        city_id = int(input("Введите ID города: "))
        name = input("Введите название города: ").strip()
        population = int(input("Введите население города: "))
        region = input("Введите регион: ").strip()
        
        # Проверка ID
        for city in cities:
            if city["id"] == city_id:
                print(f" Ошибка: город с ID {city_id} уже есть!")
                return cities, False
        
        # Добавляем город
        new_city = {
            "id": city_id,
            "name": name,
            "population": population,
            "region": region
        }
        cities.append(new_city)
        
        # Сохраняем
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(cities, file, ensure_ascii=False, indent=2)
        
        print(f" Город {name} добавлен!")
        return cities, True
        
    except ValueError:
        print(" Ошибка: ID и население должны быть числами!")
        return cities, False

def delete_city(cities, filename):
    try:
        delete_id = int(input("Введите ID города для удаления: "))
        
        for i, city in enumerate(cities):
            if city["id"] == delete_id:
                deleted_city = cities.pop(i)
                
                with open(filename, 'w', encoding='utf-8') as file:
                    json.dump(cities, file, ensure_ascii=False, indent=2)
                
                print(f" Город {deleted_city['name']} удален!")
                return cities, True
        
        print(" Город с таким ID не найден!")
        return cities, False
            
    except ValueError:
        print(" Ошибка: ID должен быть числом!")
        return cities, False

def show_all(cities):
    if not cities:
        print(" Список пуст!")
    else:
        for city in cities:
            print(f"ID: {city['id']}, Город: {city['name']}, "
                  f"Население: {city['population']}, Регион: {city['region']}")

def find_city(cities):
    name = input("Введите название города: ").strip().lower()
    found = []
    
    for city in cities:
        if name in city["name"].lower():
            found.append(city)
    
    if found:
        for city in found:
            print(f"ID: {city['id']}, Город: {city['name']}")
    else:
        print(" Город не найден!")

def exit_prog(operations_count):
    print("\n" + "="*50)
    print(f"Всего операций: {operations_count}")
    print("Выход")
    print("="*50)

# Основная программа
def main():
    filename = "cities.json"
    operations_count = 0
    cities = []
    
    # Загрузка данных
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            cities = json.load(file)
    except:
        print(" Файл не найден, начинаем с пустого списка")
    
    # Главный цикл
    while True:
        show_menu()
        choice = input("Выберите: ")
        
        if choice == "1":
            show_all(cities)
        elif choice == "2":
            find_city(cities)
        elif choice == "3":
            cities, success = add_city(cities, filename)
            if success:
                operations_count += 1
        elif choice == "4":
            cities, success = delete_city(cities, filename)
            if success:
                operations_count += 1
        elif choice == "5":
            exit_prog(operations_count)
            break
        else:
            print(" Ошибка: выберите 1-5!")

# Запуск
if name == "main":
    main()
