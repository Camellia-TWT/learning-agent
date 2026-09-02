import json
import os
from openai import OpenAI
from task_manager import add_task, show_tasks,complete_task,delete_task

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("没有找到 DEEPSEEK_API_KEY")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)
system_prompt = """
你是一个学习任务管理助手。
请根据用户输入判断意图，只能返回JSON。

添加任务：
{"intent": "add_task", "name": "任务名称", "deadline": "截止日期"}

查看任务：
{"intent": "list_tasks"}

标记完成：
{"intent": "complete_task", "task_number": 任务编号}

删除任务：
{"intent": "delete_task", "task_number": 任务编号}

标记完成：
{"intent": "complete_task", "task_number": 任务编号}

删除任务：
{"intent": "delete_task", "task_number": 任务编号}

无法识别：
{"intent": "unknown"}

不要输出JSON以外的内容。
"""
def execute_intent(data):
    intent = data.get("intent")

    if intent == "add_task":
        name = data.get("name")
        deadline = data.get("deadline")
        add_task(name, deadline)

    elif intent == "list_tasks":
        show_tasks()

    elif intent == "complete_task":
        task_number = data.get("task_number")

        if not isinstance(task_number, int):
            print("没有识别出有效的任务编号。")
            return

        complete_task(task_number)

    elif intent == "delete_task":
        task_number = data.get("task_number")

        if not isinstance(task_number, int):
            print("没有识别出有效的任务编号。")
            return

        delete_task(task_number)

    elif intent == "unknown":
        print("抱歉，我暂时无法处理这个请求。")

    else:
        print("暂时还没有连接这个功能：", intent)
while True:
    user_input=input("请输入你的需求：")
    if user_input.strip() == "退出":
        print("程序已退出。")
        break
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
            "role": "system",
            "content": system_prompt
            },
            {
                "role":"user",
                "content":user_input
            }
        ],
        temperature=0
    )
    answer = response.choices[0].message.content
    try:
        data = json.loads(answer)
    except json.JSONDecodeError:
        print("模型返回的内容不是有效的JSON：")
        print(answer)
        continue
    else:
        print(data)
        execute_intent(data)