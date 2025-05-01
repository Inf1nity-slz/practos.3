import os
from autoservice import AutoService
from user import Admin, Mechanic


def authenticate(username, password):
    if username == "admin" and password == "admin":
        return Admin(username, password)
    elif username == "mechanic" and password == "mechanic":
        return Mechanic(username, password)
    else:
        return None


def main_menu(user, service):  
    while True:
        print("\nВыберите действие:")
        if user.has_permission("view"): 
            print("1. Просмотреть все записи")
        if user.has_permission("add"):
            print("2. Добавить запись")
        if user.has_permission("delete"): 
            print("3. Удалить запись")
        if user.has_permission("sort"): 
            print("4. Сортировать записи")
        if user.has_permission("filter"):
            print("5. Фильтровать записи")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1" and user.has_permission("view"):  
            service.view_records(user)
        elif choice == "2" and user.has_permission("add"):  
            car_model = input("Введите модель автомобиля: ")
            service_type = input("Введите тип услуги: ")
            owner_name = input("Введите имя владельца автомобиля: ")
            service.add_record(user, car_model, service_type, owner_name)
        elif choice == "3" and user.has_permission("delete"):  
            record_id = int(input("Введите ID записи для удаления: "))
            service.delete_record(user, record_id)
        elif choice == "4" and user.has_permission("sort"): 
            key = input("Введите ключ для сортировки (car_model/service_type/owner_name): ")
            service.sort_records(user, key)
        elif choice == "5" and user.has_permission("filter"):  
            filter_key = input("Введите ключ для фильтрации (car_model/service_type/owner_name): ")
            filter_value = input("Введите значение для фильтрации: ")
            service.filter_records(user, filter_key, filter_value)
        elif choice == "6":
            break
        else:
            print("Неверный выбор или недостаточно прав. Попробуйте снова.")


def main():
    try:
        service = AutoService()
    except Exception as e:
        print(f"Ошибка при создании AutoService: {e}")
        print("Возможно, проблема с файлом autoservice.py или путями к файлам.")
        return

    while True:
        username = input("Введите имя пользователя (admin/mechanic) или 'exit' для выхода: ")
        if username.lower() == 'exit':
            print("Выход из программы.")
            break

        password = input("Введите пароль: ")

        user = authenticate(username, password)
        if user:
            main_menu(user, service)
        else:
            print("Неверные учетные данные. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()