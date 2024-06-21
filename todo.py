import sys
import os

# A simple to-do list class
class ToDoList:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.isfile(self.filename):
            return []
        with open(self.filename, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task added: {task}')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the list.')
        else:
            print('To-Do List:')
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

    def remove_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f'Task removed: {task}')
        except IndexError:
            print('Invalid task number.')

def print_help():
    print('TaskMaster-X')
    print('Usage:')
    print('  add [task] - Add a task to the list')
    print('  view - View all tasks')
    print('  remove [task number] - Remove a task by its number')
    print('  help - Show this help message')

def main():
    todo_list = ToDoList()

    if len(sys.argv) == 1:
        print_help()
        return

    command = sys.argv[1]

    if command == 'add':
        task = ' '.join(sys.argv[2:])
        if task:
            todo_list.add_task(task)
        else:
            print('Please provide a task to add.')
    elif command == 'view':
        todo_list.view_tasks()
    elif command == 'remove':
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            print('Please provide a valid task number to remove.')
        else:
            task_number = int(sys.argv[2])
            todo_list.remove_task(task_number)
    elif command == 'help':
        print_help()
    else:
        print('Unknown command. Use "help" to see the list of commands.')

if __name__ == '__main__':
    main()
