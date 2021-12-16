# 功能
使用custom_action和lookup实现询问地区时间

# 知识点
- custom action的定义方法
- lookup定义方法  

```shell
- lookup: place  # place为entity
  examples: |
    - brussels
    - zagreb
    - london
    - lisbon
    - amsterdam
    - seattle
```

- entity的获取
```shell
actions.py
--------------------------------------------------------------------
current_place = next(tracker.get_latest_entity_values("place"), None)
```

- slot定义
```shell
domain
---------------------------------
entities:
  - place

slots:
  location:
    type: text
    influence_conversation: true
    mappings:
      - type: from_entity
        entity: place
```

- story中entity和slot的设置
```shell
  - intent: where_i_live
    entities:
    - place: london
  - action: action_remember_where
  - slot_was_set:
    - location: london
  - intent: inquire_time_difference
    entities:
    - place: amsterdam
```

