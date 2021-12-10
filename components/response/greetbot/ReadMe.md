# 功能

用户说出自己的名字，robot通过slot记住名字，然后机器人可以带有名字的问候语句。

# 知识点

## domain
 - slot定义方法
 
 ```shell
slots:
  name:
    type: text
    mappings:
    - type: from_entity
      entity: name
 ```
只有当slot类型为from_entity时，SlotSet(key, value)才会设置成功


- slot可以通过变量的形式定义在response中
```shell
utter_greet:
  - text: "Hey, {name}. How is your day going?" # 明白slot如果填充
```
- 发送图片给用户
```shell
  utter_cheer_up:
  - text: "Here is something to cheer you up:"
    image: "https://i.imgur.com/nGF1K8f.jpg"  # 明白可以发送图片
```

- button
```shell
  utter_did_that_help:
  - text: "Did that help you?"
    buttons:
    - title: "great"   # 按钮上的文字
      payload: "/mood_great"  # TODO 用于点击按钮后发送给rasa发送的数据，该如今如何接收并处理待研究
    - title: "super sad"
      payload: "/mood_sad"
```
## action

- 指定实体类型，提取实体值
```shell
# 提取entity为name的值
name_value = next(tracker.get_latest_entity_values("name"), None)
```
- 通过模板发消息给用户
```shell
responses:
  utter_greet:
  - text: "Hey, {name}. How is your day going?"

dispatcher.utter_message(response='utter_greet', name=name_value)
```
- 给slot赋值函数
```shell
from rasa_sdk.events import SlotSet
SlotSet(key=slot_name, value=slot_value)
```

# 疑问
- slot为text类型，如何记录在story中
```shell
- story: greet by action server
  steps:
  - intent: greet_name
    # - slot_was_set:
    # - name: true  # text类型的slot如何设置
  - action: action_greet
```

- stot的type为custom类型时如何使用
```shell
slots:
  name:
    type: text
    mappings:
    - type: custom
```

- button回复的payload如何使用
```shell
    buttons:
    - title: "great"   # 按钮上的文字
      payload: "/mood_great"  # TODO 用于点击按钮后发送给rasa发送的数据，该如今如何接收并处理待研究
    - title: "super sad"
      payload: "/mood_sad"
```
