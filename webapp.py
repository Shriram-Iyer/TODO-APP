import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['todo']
    print(new_todo)
    todos.append(new_todo + '\n')
    print(todos)
    functions.write_todos(todos)
    placeholder.text_input(label='', value='', key='todo')


def edit_onchange(i):
    edit = st.session_state['edit']
    todos[i] = edit + '\n'
    functions.write_todos(todos)


def complete_onclick(todo_rem):
    todos.remove(todo_rem)
    functions.write_todos(todos)


st.title("TO-DO Web App")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        edit_button = st.button(label='Edit', key='Edit', )
        complete_button = st.button(label='Complete', key='complete', on_click=complete_onclick, args=(todo,))
        if edit_button:
            todo = todos[index].strip('\n')
            edit_todo = st.text_input(label="", value=todo, key="edit", on_change=edit_onchange,
                                      args=(index,))
placeholder = st.empty()
todo1 = placeholder.text_input(label="", placeholder="Add new todos.", on_change=add_todo, key='todo')
