#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d %Y %H: %M: %S")
print('It is ', now)

while True:
    # get user input and strip space char from it
    user_action = input("enter add,show,edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todo = [item.strip('\n) for item in todos]--

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('enter a new todo:')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Your command is note valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from list."
            print(message)
        except IndexError:
            print('There is not item with this number.')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid!')

print('bye!')
