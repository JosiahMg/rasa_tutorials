# 功能
使用rasa构建FAQs类型的对话系统，FAQs是不考虑上下文的对话系统

# 知识点
- 配置方法
```shell
config
----------------------------------------------------------------
pipeline:
  - name: ResponseSelector
    epochs: 100

policies:
  - name: RulePolicy

rules:
  - rule: respond to FAQs
    steps:
    - intent: faq
    - action: utter_faq
```

# 疑问
