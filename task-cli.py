#!/usr/bin/env python3.10
import argparse
from libraries.constants import Status
from libraries.helper import (
    add_task,
    delete_task,
    help,
    mark_task,
    list_tasks,
    update_task,
    valid_command,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    parser.add_argument("command", type=str, help="Command to execute")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments for the command")

    args = parser.parse_args()

    if not valid_command(args.command):
        print(f"Invalid command: {args.command}")
        help()
        return

    if args.command == "add":
        add_task(args.args[0])
    elif args.command == "delete":
        delete_task(int(args.args[0]))
    elif args.command == "mark-in-progress":
        mark_task(int(args.args[0]), Status.IN_PROGRESS)
    elif args.command == "mark-done":
        mark_task(int(args.args[0]), Status.DONE)
    elif args.command == "list":
        if args.args == []:
            list_tasks()
        elif args.args[0] == "done":
            list_tasks(Status.DONE)
        elif args.args[0] == "in-progress":
            list_tasks(Status.IN_PROGRESS)
        elif args.args[0] == "todo":
            list_tasks(Status.TODO)
    elif args.command == "update":
        update_task(int(args.args[0]), " ".join(args.args[1:]))
    else:
        help()


if __name__ == "__main__":
    main()
