# 学习任务 Agent

## 项目简介

这是一个基于 DeepSeek API 的学习任务管理 Agent。

用户可以通过自然语言添加、查看、完成和删除学习任务。

## 功能

- 自然语言添加任务
- 查看所有任务
- 标记任务完成
- 删除任务
- JSON 文件持久化
- 无法识别请求时给出提示

## 项目结构

```text
learning-agent
├── .venv
├── api_test.py
├── task_manager.py
├── tasks.json
└── README.md
```

## 运行方式

### 1. 安装依赖

```bash
pip install openai
```

### 2. 配置环境变量

设置环境变量：

```text
DEEPSEEK_API_KEY=你的 API Key
```

不要把真实 API Key 写入代码，也不要上传到 GitHub。

### 3. 启动程序

```bash
python api_test.py
```

## 支持的示例

```text
明天晚上复习Python函数
查看我的任务
完成第1个任务
删除第2个任务
退出
```

## Agent流程

```text
用户输入
→ DeepSeek识别意图
→ JSON解析
→ 选择任务工具
→ 执行任务操作
→ 保存任务数据
```

## 当前不足

- 日期还没有严格验证；
- 任务数据使用 JSON，暂未使用数据库；
- 模型返回格式仍需要进一步校验；
- 暂不支持多轮复杂对话；
- 当前项目主要用于学习和实践。