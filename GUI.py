import PySimpleGUI as Sg
import time
import functions

clock = Sg.Text(time.strftime("%b %d, %Y %H:%M:%S"), key='clock')
label_todo = Sg.Text("Todo:")
input_todo = Sg.InputText(tooltip="Enter Todo", key="todo")
add_button = Sg.Button("Add")
todo_list = Sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")
window = Sg.Window("MY TO-DO App",
                   layout=[[clock],
                           [label_todo],
                           [input_todo, add_button],
                           [todo_list, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todo = values['todo']
            todos = functions.get_todos()
            todos.append(todo + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo)
                new_todo = values['todo']
                todos[index] = f"{new_todo}\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup("Please select a todo first", font=('Helvetica', 20))
        case 'Complete':
            try:
                todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup("Please select a todo first", font=('Helvetica', 20))
        case 'todos':
            todos = values['todos'][0].strip('\n')
            window['todo'].update(value=todos)
        case 'Exit':
            break
        case Sg.WIN_CLOSED:
            break
window.close()
