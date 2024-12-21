import json
from libraries.constants import HELPER_CMDS, VALID_CMDS, FILE_PATH, Status
from datetime import datetime
from tabulate import tabulate

def add_task(description: str, status: Status = Status.TODO) -> None:
    try:
        with open(FILE_PATH, "r+") as file:
            data = json.load(file)
            task = {
                "task_id": data["counter"] + 1,
                "description": description,
                "status": status.value,
                "created_at": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                "updated_at": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            }
            data["tasks"].append(task)
            data["counter"] += 1
            file.seek(0)
            json.dump(data, file, indent=4)
            print(f"Task added successfully (ID: {task['task_id']})")
    except FileNotFoundError:
        with open(FILE_PATH, "w") as file:
            data = {
                "counter": 1,
                "tasks": [
                    {
                        "task_id": 1,
                        "description": description,
                        "status": status.value,
                        "created_at": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                        "updated_at": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                    }
                ],
            }
            json.dump(data, file, indent=4)
            print(f"Task added successfully (ID: {data['counter']})")


def delete_task(task_id: int) -> None:
    try:
        with open(FILE_PATH, "r+") as file:
            data = json.load(file)
            tasks = data["tasks"]
            task_index = next(
                (index for (index, d) in enumerate(tasks) if d["task_id"] == task_id),
                None,
            )
            if task_index is not None:
                del tasks[task_index]
                data["tasks"] = tasks
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
            else:
                print(f"Task with ID {task_id} not found.")
    except FileNotFoundError:
        print("Task database not found.")


def update_task(task_id: int, description: str) -> None:
    try:
        with open(FILE_PATH, "r+") as file:
            data = json.load(file)
            tasks = data["tasks"]
            task = next((d for d in tasks if d["task_id"] == task_id), None)
            if task is not None:
                task["description"] = description
                task["updated_at"] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
            else:
                print(f"Task with ID {task_id} not found.")
    except FileNotFoundError:
        print("Task database not found.")


def mark_task(task_id: int, status: Status) -> None:
    try:
        with open(FILE_PATH, "r+") as file:
            data = json.load(file)
            tasks = data["tasks"]
            task = next((d for d in tasks if d["task_id"] == task_id), None)
            if task is not None:
                task["status"] = status.value
                task["updated_at"] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
            else:
                print(f"Task with ID {task_id} not found.")
    except FileNotFoundError:
        print("Task database not found.")


def list_tasks(status: Status = None) -> None:
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            tasks = data["tasks"]
            if status:
                tasks = [task for task in tasks if task["status"] == status.value]
            if tasks:
                print(tabulate(tasks, headers="keys", tablefmt="grid"))
            else:
                print("No tasks found.")
    except FileNotFoundError:
        print("Task database not found.")

def help() -> None:
    print(HELPER_CMDS)


def valid_command(cmd: str) -> bool:
    if cmd in VALID_CMDS:
        return True
    else:
        print(
            "Invalid Command. \n Look at the following examples to see how to use the tool."
        )
        help()