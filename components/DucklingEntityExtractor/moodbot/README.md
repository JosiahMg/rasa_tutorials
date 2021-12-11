# 功能
通过facebook/duckling server解析如: 
["time", "number", "amount-of-money", "distance"]

# 知识点
- 配置方法
```shell
  config
  ----------------------------------------------------------------
  - name: "DucklingEntityExtractor"
    url: "http://45.76.135.172:8000"
    dimensions: ["time"]
    # dimensions: ["time", "number", "amount-of-money", "distance"]
    # locale: "en_GB"     # 语言?
    timezone: "Asia/Shanghai"  # 时区
    timeout : 3  # 超时时间
```

# 疑问
- 中文配置是怎样的