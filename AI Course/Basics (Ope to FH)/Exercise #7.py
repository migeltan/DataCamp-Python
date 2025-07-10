#Example 1: Command-Line Task Manager

import os 

#File to store tasks
File="tasks.txt"

#Loads tasks from file
def loadtasks():
    tasks = {}
    if os.path.exists(File):
        with open(File, "r") as file:
            for line in file:
                taskid, title, status = line.strip(). split(" | ")
                tasks[int(taskid)] = {"title": title, "status": status}
    return tasks

#save task to file
def savetask (tasks):
    with open(File, "w") as file:
        for taskid, task in tasks.items():
            file.write(f"{taskid} | {task['title']} | {task['status']}\n")
            
#Add new task
def addtask(tasks):
    title = input("Enter task title: ")
    taskid = max(tasks.keys(), default = 0) +1
    tasks[taskid] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")
    
#view
def viewtasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for taskid, tasks in tasks.items():
            print(f"[{taskid}] {tasks['title']} - {tasks['status']}")
            
#Mark task as complete
def marktask(tasks):
    taskid = int(input("Enter task ID to mark as complete: "))
    if taskid in tasks:
        tasks[taskid]["status"] = "Complete"
        print(f"Task '{tasks[taskid]['title']}' marked as complete.")
    else:
        print("Task ID not found.")
        
#Delete a task
def deletetask(tasks):
    taskid = int(input("Enter task ID to delete: "))
    if taskid in tasks:
        deletedtask = tasks.pop(taskid)
        print(f"Task '{deletedtask['title']}' deleted.")
    else:
        print("Task ID not found.")
        
#main menu
def main():
    tasks = loadtasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add a Task")
        print("2. View a Task")
        print("3. Mark as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            addtask(tasks)
        elif choice == "2":
            viewtasks(tasks)
        elif choice == "3":
            marktask (tasks)
        elif choice == "4":
            deletetask(tasks)
        elif choice == "5":
            savetask(tasks)
            print("Goodbye!")
            break
        else: 
            print ("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()
