import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QInputDialog, QMessageBox

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

    def remove_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            return task
        except IndexError:
            return None

# GUI for the to-do list
class ToDoApp(QWidget):
    def __init__(self, todo_list):
        super().__init__()
        self.todo_list = todo_list

        self.initUI()

    def initUI(self):
        self.setWindowTitle('TaskMaster-X')

        self.layout = QVBoxLayout()

        self.task_listbox = QListWidget()
        self.layout.addWidget(self.task_listbox)

        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton('Remove Task')
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        self.setLayout(self.layout)

        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.clear()
        for task in self.todo_list.tasks:
            self.task_listbox.addItem(task)

    def add_task(self):
        task, ok = QInputDialog.getText(self, 'Add Task', 'Enter the task:')
        if ok and task:
            self.todo_list.add_task(task)
            self.task_listbox.addItem(task)

    def remove_task(self):
        selected_task_index = self.task_listbox.currentRow()
        if selected_task_index == -1:
            QMessageBox.warning(self, 'Remove Task', 'No task selected.')
            return

        task_number = selected_task_index + 1
        removed_task = self.todo_list.remove_task(task_number)
        if removed_task:
            self.task_listbox.takeItem(selected_task_index)
            QMessageBox.information(self, 'Remove Task', f'Task removed: {removed_task}')
        else:
            QMessageBox.warning(self, 'Remove Task', 'Failed to remove task.')

def main():
    todo_list = ToDoList()
    
    app = QApplication(sys.argv)
    window = ToDoApp(todo_list)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
