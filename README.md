# TaskMaster-X
TaskMaster CLI is a simple command-line to-do list application that allows you to manage your tasks easily. You can add, view, and remove tasks, with all tasks being saved to a file for persistence.

## Features

- Add tasks to your to-do list.
- View all tasks in your to-do list.
- Remove tasks from your to-do list.
- Tasks are saved to a file for persistence.

## Usage

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
$ python todo_list.py add "Buy groceries"
Task added: Buy groceries

$ python todo_list.py add "Finish homework"
Task added: Finish homework

$ python todo_list.py view
To-Do List:
1. Buy groceries
2. Finish homework

$ python todo_list.py remove 1
Task removed: Buy groceries

$ python todo_list.py view
To-Do List:
1. Finish homework
```
