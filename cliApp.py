import functions
while True:
    user_input = input("Type add, show, edit, complete or exit:  ")
    user_input = user_input.strip()

    match user_input:
        case user_input if user_input.startswith("add"):
            todo = user_input[4:]
            todos = functions.get_todos()
            todos.append(todo + '\n')
            functions.write_todos(todos)
        case user_input if user_input.startswith("show"):
            todos = functions.get_todos()
            todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                row = f"{index + 1} - {item}"
                print(row)
        case user_input if user_input.startswith("edit"):
            try:
                num = int(user_input[5:])
                num -= 1
                todos = functions.get_todos()
                new_todo = input("Enter new todo: ")
                todos[num] = f"{new_todo}\n"
                functions.write_todos(todos)
            except ValueError:
                print("your command is not valid!")
                continue
        case user_input if user_input.startswith("complete"):
            try:
                num = int(user_input[9:])
                num -= 1
                todos = functions.get_todos()
                todo = todos.pop(num)
                functions.write_todos(todos)
                print(todo + " was marked as completed and removed from todo list")
            except ValueError:
                print("your command is not valid!")
                continue
        case user_input if user_input.startswith("exit"):
            break