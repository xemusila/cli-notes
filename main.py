from notes import Note

def main():
    print("Чтобы выйти, нажмите 0. Доступные команды:")
    print('"add" - добавить заметку')
    print('"remove" - удалить заметку')
    print('"edit" - отредактировать заметку')
    print('"show" - показать существующие заметки')
    my_note = Note()
    inp = input()
    while inp != '0':
        if len(inp.split()) < 2:
            print("Недостаточно параметров")
            inp = input()
            continue
        if inp.split()[0] == 'add':
            my_note.add(' '.join(inp.split()[1:]))
        elif inp.split()[0] == 'remove':
            my_note.remove(int(' '.join(inp.split()[1:])))
        elif inp.split()[0] == 'edit':
            if len(inp.split()) < 3:
                print("Недостаточно параметров")
                inp = input()
                continue
            my_note.edit(int(' '.join(inp.split()[1])), ' '.join(inp.split()[2:]))
        elif inp.split()[0] == 'show':
            my_note.show()
        else:
            print("Нет такой команды!")
        
        inp = input()

if __name__ == "__main__":
    main()