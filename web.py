import streamlit as st

import functions2

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions2.write_todos(todos)
    print(todo)

st.title("My to do ap")

st.subheader("This is my header")
todos = functions2.get_todos()
st.write("cos cos")

for index,todo in enumerate(todos):

    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions2.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a to do", placeholder = "Add new to do",
              on_change = add_todo, key='new_todo')


st.session_state