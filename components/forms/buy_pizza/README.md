# 功能
使用form表单功能构建购买PIZZA的问题


# 知识点

## 激活表单
在story或rules中需要激活和提交表单
```shell
rules
----------------------------------
- rule: Activate Pizza Form
  steps:
  - intent: buy_pizza
  - action: simple_pizza_form
  - active_loop: simple_pizza_form
```

## 提交表单
```shell
rules
----------------------------------
- rule: Submit Pizza Form
  condition:
  - active_loop: simple_pizza_form
  steps:
  - action: simple_pizza_form
  - active_loop: null
  - slot_was_set:
    - requested_slot: null
  - action: utter_submit
  - action: utter_pizza_slots
```

## slot
```shell
entities:
  - pizza_size
  - pizza_type

slots:
  pizza_size:
    type: text
    influence_conversation: true
    mappings:
    - type: from_entity
      entity: pizza_size
  pizza_type:
    type: text
    influence_conversation: true
    mappings:
    - type: from_entity
      entity: pizza_type
```

## 验证每次回答是否满足要求
```shell
domain
---------------------------
actions:
- validate_simple_pizza_form
```

## 在domain中声明表单
```shell
domain
---------------------------
forms:
  simple_pizza_form:
    required_slots:
      - pizza_size
      - pizza_type
```

# 疑问
- 一轮对话结束后，slot值没有清空
- 对话过程中主题改变了如何定义story