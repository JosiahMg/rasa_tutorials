# rasa_tutorials



# 相关命令

## 启动rasa server
```shell
rasa run -m models --enable-api --cors "*" --debug
```
## web访问url：
```shell
http://localhost:5005/model/parse
```

## flask code demo
```shell
from flask import Flask, render_template, url_for, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chat',methods=["POST"])
def chat():
    user_message = request.get_json()['text']
    response = requests.post("http://localhost:5005/model/parse", params={"message": user_message} )
    return jsonify({"status": "success", "response": response.text})


if __name__ == "__main__":
    app.run(debug = True, port = 5000)
```

