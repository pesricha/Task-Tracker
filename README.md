# Task-Tracker

## Description

Task-Tracker is a simple command-line tool to help you manage your daily tasks efficiently. You can add, update, delete, and list tasks, as well as mark them as in progress or done.

## Installation

To install Task-Tracker, follow these steps:

1. Clone the repository:
    ```sh
    git clone git@github.com:pesricha/Task-Tracker.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Task-Tracker
    ```

## Adding a new task
```sh
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

## Updating and deleting tasks
```sh
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
```

## Marking a task as in progress or done
```sh
task-cli mark-in-progress 1
task-cli mark-done 1
```

## Listing all tasks
```sh
task-cli list
```

## Listing tasks by status
```sh
task-cli list done
task-cli list todo
task-cli list in-progress
```

Sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).