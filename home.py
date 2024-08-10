from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
        super().__init__(value)
        if not value:
            raise ValueError("Ім'я не може бути порожнім")
        pass

class Phone(Field):
        super().__init__(value)
        if not re.match(r"^\d{10}$", value):
            raise ValueError("Невірний формат номера телефону")
        pass




class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
             self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for
        
    p in self.phones:
    if p.value == phone:
        self.phones.remove(p)
        return 
    raise ValueError("Телефон не знайдено")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
            raise ValueError("Телефон _ не знайдено")
        def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def find_record(self, name):
        for record in self.records:
            if record.name.value == name:
                return record
        return None

    def delete_record(self, name):
        record = self.find_record(name)
        if record:
            self.records.remove(record)
        else:
            raise ValueError("Запис не знайдено")
        pass
