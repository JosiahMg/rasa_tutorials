# 功能
使用slot实现询问衬衫尺寸，尺寸保存到slot中

# 知识点

- slot的定义
```shell
domain
--------------------------------
slots:
  shirt_size:
    type: text
    influence_conversation: true
    mappings:
      - type: from_entity
        entity: shirt_size
```

- 设置slot的方法: 在story中填充
从意图give_shirt_size中提取出shirt_size实体并赋值到slot中,该赋值是非必须的
主要作用是在stroy中增加状态，有利于对话管理模块
```shell
stories
--------------------------------
- intent: give_shirt_size
  entities:
  - shirt_size: large
- slot_was_set:
  - shirt_size: large
```

- get_slot方法
```shell
actions.py
-------------------------------------------
from rasa_sdk.events import SlotSet
shirt_size = tracker.get_slot('shirt_size')
```
