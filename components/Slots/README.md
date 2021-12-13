# 知识点
- stories中的配置
```shell
stories:
- story: booking a flight ticket
  steps:
  - intent: book_a_ticket
  - or:
    - slot_was_set:
      - destination: Toronto
    - slot_was_set:
      - destination: London
```

- slot mapping
```shell
entities:
- entity_name
slots:
  slot_name:
    type: any
    mappings:
    - type: from_entity      # 类型
      entity: entity_name    # 知道哪个实体中填充slot
      role: role_name        # 在role中的才被填充
      group: group_name      # 在group中的才被填充
      intent: intent_name    # 在intent中的才被填充
      not_intent: excluded_intent  # 在not_intend中的不被填充
```
- from_entity of value
如果用户的意图在intent_name且不是excluded_intent时, 用value值(my_value)填充slot
```shell
slots:
  slot_name:
    type: text
    mappings:
    - type: from_entity
      value: my_value
      intent: intent_name
      not_intent: excluded_intent
```
- from_entity of entity
从意图在intent_name且不是excluded_intent的用户输入的句子抽取的实体值(entity_name)用于填充slot
```shell
slots:
  slot_name:
    type: text
    mappings:
    - type: from_entity
      entity: entity_name
      intent: intent_name
      not_intent: excluded_intent
```

- from_text
从意图在intent_name且不是excluded_intent的用户输入的句子用于填充slot
```shell
slots:
  slot_name:
    type: text
    mappings:
    - type: from_text
      intent: intent_name
      not_intent: excluded_intent
```

- from_trigger_intent
当form被激活时，且用户的意图是intent_name并不是excluded_intent,使用value填充slot
```shell
slots:
  slot_name:
    type: any
    mappings:
    - type: from_trigger_intent
      value: my_value
      intent: intent_name
      not_intent: excluded_intent
```

- slot type: text
存储文本类型的数据, 是否影响对话指和是否被设置有关, 与具体设置的什么无关
```shell
slots:
  destination:
    type: text
    influence_conversation: true
    mappings:
    - type: from_entity
      entity: destination
```

- slot type: boolean
true / false
```shell
slots:
  authenticated:
    type: boolean
    influence_conversation: true
    mappings:
    - type: custom
```

- slot type: categoriacal
可以设置多个value
```shell
slots:
  price_range:
    type: categorical
    influence_conversation: true
    mappings:
    - type: custom
```

- slot type: float
存储numerical values
```shell
slots:
  radius:
    type: float
    initial_value: 100
    min_value: 0
    max_value: 100
    mappings:
    - type: custom
```

- slot type: list
存储一系列值: I'd like to order some cookies, chocolate and milk
```shell
slots:
  items:
    type: list
    mappings:
    - type: from_entity
      entity: shopping_item
```

- slot type: any
可以存储任意值, 不会对对话系统有影响

```shell
slots:
  items:
    type: list
    mappings:
    - type: from_entity
      entity: shopping_item
```