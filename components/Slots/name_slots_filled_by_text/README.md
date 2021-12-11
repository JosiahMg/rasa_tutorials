# 功能
使用slot的by_text实现询问对方名字(first_name + last_name)

# 知识点

- from_text: 直接从对话中提取
```shell
domain
------------------------------------
slots:
  first_name:
    type: text
    influence_conversation: true
    mappings:
      - type: from_text
        conditions:
          - active_loop: name_form
            requested_slot: first_name
  last_name:
    type: text
    influence_conversation: true
    mappings:
      - type: from_text
        conditions:
          - active_loop: name_form
            requested_slot: last_name
```
- from_entity: 从实体中抽取
```shell
domain
------------------------------------
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