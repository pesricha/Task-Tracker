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

3. Install requirements.txt
    ```sh
    pip install -r requirements.txt
    ```
## Usage

To use Task-Tracker, follow these steps:

1. Adding a new task:
    ```sh
    ./task_cli add "Buy groceries"
    # Output: Task added successfully (ID: 1)
    ```

2. Updating a task:
    ```sh
    ./task-cli update 1 "Buy groceries and cook dinner"
    ```

3. Deleting a task:
    ```sh
    ./task-cli delete 1
    ```

4. Marking a task as in progress:
    ```sh
    ./task-cli mark-in-progress 1
    ```

5. Marking a task as done:
    ```sh
    ./task-cli mark-done 1
    ```

6. Listing all tasks:
    ```sh
    ./task-cli list
    ```

7. Listing tasks by status:
    ```sh
    ./task-cli list done
    ./task_cli list todo
    ./task_cli list in-progress
    ```

Sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).