import functions
import streamlit as st

todos = functions.get_todos("/Users/nasya/Python/Udemy/web1/todos.txt")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos, filepath="/Users/nasya/Python/Udemy/web1/todos.txt")


st.title("My Todo App")
st.subheader("This is my todo app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, filepath="/Users/nasya/Python/Udemy/web1/todos.txt")
        del st.session_state[todo]
        st.rerun()
st.text_input(label=" ", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
