from datetime import datetime 
class Note:
    def __init__(self):
        self.notes = {}
        self.last_id = 0
    
    def add(self, string):
        try:
            self.notes[self.last_id + 1] = [datetime.now(), string]
            self.last_id += 1
            print("Заметка успешно добавлена")
        except:
            print("Возникла ошибка при добавлении заметки")

    def remove(self, id):
        try:
            del self.notes[id]
            print(f"Заметка {id} удалена")
        except KeyError:
            print("Нет такого индекса")
    
    def show(self):
        if not self.notes:
            print("У вас нет заметок")
            return
        for id, value in self.notes.items():
            print(f'{id}: {value[0]}')
            print(value[1])
    
    def edit(self, id, string):
        try:
            self.notes[id] = [datetime.now(), string]
            print("Заметка изменена!")
        except KeyError:
            print("Нет такого индекса")
    
