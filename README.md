# TaskMaster-X
TaskMaster-X is a simple command-line / GUI to-do list application that allows you to manage your tasks easily. You can add, view, and remove tasks, with all tasks being saved to a file for persistence.

## Features

- Add tasks to your to-do list.
- View all tasks in your to-do list.
- Remove tasks from your to-do list.
- Tasks are saved to a file for persistence.

## Usage (CLI)
Scroll down for GUI.
### Add a Task

To add a task to your to-do list, use the `add` command followed by the task description.

```sh
python todo.py add "Buy groceries"
```
### View Tasks
To view all tasks in your to-do list, use the view command.

```sh
python todo.py view
```

### Remove a Task
To remove a task from your to-do list, use the remove command followed by the task number.

```sh
python todo.py remove [listnum]
```

### Help
To see the help message with all available commands, use the help command.

```sh
python todo.py help
```

## Example

Here's an example on how to use TaskMaster-X:
```
$ python todo.py add "Buy groceries"
Task added: Buy groceries

$ python todo_list.py add "Finish homework"
Task added: Finish homework

$ python todo.py view
To-Do List:
1. Buy groceries
2. Finish homework

$ python todo.py remove 1
Task removed: Buy groceries

$ python todo.py view
To-Do List:
1. Finish homework
```

## GUI
Alright you "non CLI-obsessed" people, GUI is pretty straight forward, however, you'll need to install a requirement: PyQt5. Installing that is as simple as executing this command:
```sh
pip install pyqt5
```
After it's done installing, just execute the todogui.py file and you'll be ready to manage your tasks like a pro!

## Usage (GUI)
### Add a Task
You just press the "Add Task" button, type the name of the task and confirm!

### Remove a Task
Select the task you want to remove, and press "Remove task".




