# 功能
正则表达提取实体

# 知识点
- story中记录entity
```shell
  - intent: credit_account
    entities:
      - account: "credit"
  - action: utter_balance
```

- 同义词, 应用在实体抽取之后
```shell
- synonym: credit   # "credit"为value值
  examples: |
    - credit card account
    - credit account
```

- DIETClassifier设置不进行实体识别
```shell
config
-----------------------------
  - name: DIETClassifier
    entity_recognition: False
```

- RegexEntityExtractor进行实体抽取
```shell
config
-----------------------------
  - name: RegexEntityExtractor
    case_sensitive: False
    use_lookup_tables: true
    use_regexes: true
```


- lookup & regex
```shell
- regex: account_number # "account_number"为entity值
  examples: |
    - \b\d{6,8}\b
    - ^7\d{6,8}

- lookup: object  # "object"为entity值
  examples: |
    - box
    - door
    - window
    - poster
    - key
```


