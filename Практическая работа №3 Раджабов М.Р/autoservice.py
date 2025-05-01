import json
import os
from record import Record


class AutoService: 
    def __init__(self, data_file="C:\Users\Max\Desktop\Новая папка (2)\Учёба\Практическая работа №3 Раджабов М.Р/service_data.json"):
        self._records = {}
        self._next_record_id = 1
        self._data_file = data_file
        self.load_data()

    def view_records(self, user):  
        if not user.has_permission("view"):
            print("У вас нет прав для просмотра записей.")
            return
        if not self._records:
            print("Нет записей об обслуживании.")
            return

        for record_id, record in self._records.items():
            print(record)

    def add_record(self, user, car_model, service_type, owner_name): 
        if not user.has_permission("add"):
            print("У вас нет прав для добавления записей.")
            return
        record = Record(self._next_record_id, car_model, service_type, owner_name)
        self._records[self._next_record_id] = record
        self._next_record_id += 1
        print(f"Запись добавлена с ID: {record.record_id}")
        self.save_data()

    def delete_record(self, user, record_id): 
        if not user.has_permission("delete"):
            print("У вас нет прав для удаления записей.")
            return
        if record_id in self._records:
            del self._records[record_id]
            print(f"Запись с ID {record_id} удалена.")
            self.save_data()
        else:
            print(f"Запись с ID {record_id} не найдена.")

    def sort_records(self, user, key):  
        if not user.has_permission("sort"):
            print("У вас нет прав для сортировки записей.")
            return
        valid_keys = ["car_model", "service_type", "owner_name"]
        if key not in valid_keys:
            print("Недопустимый ключ для сортировки.")
            return

        sorted_records = sorted(self._records.values(), key=lambda record: getattr(record, key))
        for record in sorted_records:
            print(record)

    def filter_records(self, user, filter_key, filter_value): 
        if not user.has_permission("filter"):
            print("У вас нет прав для фильтрации записей.")
            return
        valid_keys = ["car_model", "service_type", "owner_name"]
        if filter_key not in valid_keys:
            print("Недопустимый ключ для фильтрации.")
            return

        filtered_records = [record for record in self._records.values() if
                            getattr(record, filter_key).lower() == filter_value.lower()]

        if not filtered_records:
            print("Нет записей, соответствующих критериям фильтрации.")
            return

        for record in filtered_records:
            print(record)

    def save_data(self):
            data = {
                "next_record_id": self._next_record_id,
                "records": {
                    record_id: {
                        "car_model": record.car_model,
                        "service_type": record.service_type,
                        "owner_name": record.owner_name
                    }
                    for record_id, record in self._records.items()
                }
            }
            try:
                with open(self._data_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
            except IOError as e:
                print(f"Ошибка при сохранении данных: {e}")

    def load_data(self):
            try:
                with open(self._data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._next_record_id = data.get("next_record_id", 1)
                    records_data = data.get("records", {})

                    self._records = {}
                    for record_id, record_data in records_data.items():
                        record = Record(int(record_id), record_data['car_model'], record_data['service_type'],
                                        record_data['owner_name'])
                        self._records[int(record_id)] = record

            except FileNotFoundError:
                print("Файл данных не найден. Начинаем с пустой базы данных.")
            except json.JSONDecodeError:
                print("Ошибка при чтении файла данных. Начинаем с пустой базы данных.")
            except IOError as e:
                print(f"Ошибка при загрузке данных: {e}")
