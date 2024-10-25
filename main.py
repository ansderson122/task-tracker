import json 
import os
from datetime import datetime

def add_task(task:str):  
    with open("data.json","r+") as file:
        data = json.load(file)
        newTask = {
            # o id sera o id do ultimo elemento mais 1 
            "id" : data["task"][-1]['id'] + 1 if len(data["task"]) >= 1 else 1,
            "content":task,
            "status" :"todo",
            "createdAt" : f"{datetime.now().date()} {datetime.now().time()}",
            "updatedAt" : ""
        }
        data["task"].append(newTask)
        file.seek(0)  # Move para o início do arquivo para sobrescrever
        json.dump(data, file, indent=4)
        file.truncate() 
        print(f"Task added successfully (ID: {newTask['id']})")

def update_status(status:str,id:str):
    with open("data.json","r+") as file:
        data = json.load(file)

        for task in data["task"]:
            if str(task["id"]) == id:
                task['status'] = status
                task['updatedAt'] = f"{datetime.now().date()} {datetime.now().time()}"

                file.seek(0)  # Move para o início do arquivo para sobrescrever
                json.dump(data, file, indent=4)
                file.truncate() 

                print(f"Status changed successfully")
                return
        print(f"Task with ID {task["id"]} not found")

def update_task(id:str,newContent:str):
    if len(newContent) == 0:
        print("Please provide content to update the task")
        return
    
    with open("data.json","r+") as file:
        data = json.load(file)
        for task in data["task"]:
            if str(task["id"]) == id:
                task['content'] = newContent
                task['updatedAt'] = f"{datetime.now().date()} {datetime.now().time()}"

                file.seek(0)  # Move para o início do arquivo para sobrescrever
                json.dump(data, file, indent=4)
                file.truncate() 
                print("The update was a success")
                return
        print(f"Task with ID {task["id"]} not found")

def delete_task(id:str):
    with open("data.json","r+") as file:
        data = json.load(file)
        for task in data["task"]:
            if str(task["id"]) == id:
                data["task"].remove(task)

                file.seek(0)  # Move para o início do arquivo para sobrescrever
                json.dump(data, file, indent=4)
                file.truncate() 
                print("Task deleted successfully")
                return
        print(f"Task with ID {task["id"]} not found")

def list_tasks(selet = "all"):
    with open("data.json","r+") as file:
        data = json.load(file)
        for task in data["task"]:
            if selet == "all" or task["status"] == selet:
                print(f"--------- (ID: {task["id"]}) ----------")
                print(f"Content: {task["content"]}")
                print(f"Status: {task["status"]} ")
                print(f"createdAt: {task["createdAt"]} ")
                print(f"updatedAt: {task["updatedAt"]} ")
                print()

def list_commands():
    print("Available commands:")
    print("1. add <task> - Add a new task.")
    print("2. mark-in-progress <id> - Mark a task as in-progress.")
    print("3. mark-done <id> - Mark a task as done.")
    print("4. update <id> <new_content> - Update the content of a task.")
    print("5. delete <id> - Delete a task.")
    print("6. list [status] - List all tasks or tasks with a specific status (todo, in-progress, done).")
    print("7. exit - Exit the program.")



if __name__ == '__main__':
    if not os.path.exists("data.json"): # caso o arquivo data não exitar, entao crie um data.json
        with open("data.json", "w") as file:
            data = {
                "task":[]
            }
            json.dump(data, file, indent=4)

    isContinue = True
    while isContinue:
        command = input(str("task-cli "))

        match  command.split(" ")[0]: # primeiro argumento do comando 
            case "add":
                if len(command.split(" ")) == 1:
                    print("Please provide content to create the task")
                    continue

                add_task(command.split(" ")[1])

            case "mark-in-progress":
                if len(command.split(" ")) == 1:
                    print("Please provide an ID to update the task status.")
                    continue
                update_status("in-progress",command.split(" ")[1])

            case "mark-done":
                if len(command.split(" ")) == 1:
                    print("Please provide an ID to update the task status.")
                    continue
                update_status("done",command.split(" ")[1])
            
            case "update":
                if len(command.split(" ")) >= 3:
                    print("Please provide an ID and content to update the task")
                update_task(command.split(" ")[1],command.split(" ")[2])
            
            case "delete":
                if len(command.split(" ")) == 1:
                    print("Please provide an ID to delete the task.")
                    continue
                delete_task(command.split(" ")[1])
            


            case "list":
                if len(command.split(" ")) > 1: 
                    match  command.split(" ")[1]: # segundo argumento do comando 
                        case "done":
                            list_tasks("done")
                        case "todo":
                            list_tasks("todo")
                        case "in-progress":
                            list_tasks("in-progress")
                        case _:
                            print("Invalid argument")
                else:
                    list_tasks()

            case "help":  
                list_commands()
            case "exit":
                isContinue = False
            case _:
                 print("Invalid argument")