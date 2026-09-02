import json
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("任务文件内容损坏，将使用空任务列表。")
        return []

tasks =load_tasks()

def add_task(name=None, deadline=None):
    if name is None:
        name = input("请输入任务名称：").strip()
    if deadline is None:
        deadline = input("请输入截止日期：")
    if not name:
        print("任务名称不能为空。")
        return
    task = {
        "name": name,
        "deadline": deadline,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("任务添加成功！")

def show_tasks():
    if len(tasks) != 0:
        for index, task in enumerate(tasks, start=1):
            status = "已完成" if task["done"] else "未完成"
            print(
                f"{index}. {task['name']} | "
                f"截止：{task['deadline']} | {status}"
            )
    else:
        print("当前没有学习任务。")

def delete_task(task_number=None):
    if task_number is None:
        try:
            task_number = int(input("请输入要删除的任务编号："))
        except ValueError:
            print("请输入有效的数字。")
            return
    if 1 <= task_number <= len(tasks):
        del (tasks[task_number - 1])
        save_tasks(tasks)
        print("删除任务成功！")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} | 截止：{task['deadline']}")
    else:
        print("没有这个任务。")

def complete_task(task_number=None):
    if task_number is None:
        try:
            task_number = int(input("请输入已完成任务的编号"))
        except ValueError:
            print("请输入有效的数字。")
            return
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print("任务已标记为完成。")
        for index, task in enumerate(tasks, start=1):
            status = "已完成" if task["done"] else "未完成"
            print(
                f"{index}. {task['name']} | "
                f"截止：{task['deadline']} | {status}"
            )
def main():
    while True:
        print("1. 添加学习任务")
        print("2. 查看所有任务")
        print("3. 标记任务完成")
        print("4. 删除任务")
        print("5. 退出程序")
        try:
            choice = int(input("请输入任务编号："))
        except ValueError:
            print("请输入有效的数字。")
            continue
        else:
            if choice == 1:
                add_task()
            elif choice == 2:
               show_tasks()
            elif choice == 3:
                complete_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("程序已退出。")
                break
            else:
                print("输入提示无效。")

if __name__ == "__main__":
    main()

