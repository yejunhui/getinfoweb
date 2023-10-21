# Flask应用示例 - Excel文件处理和数据展示

这个Flask应用允许用户上传Excel文件，并对文件中的数据进行处理和展示。

## 安装依赖

在运行该应用之前，请确保已安装以下依赖库：
- Flask
- pandas

可以使用以下命令来安装所需依赖：
```
pip install flask pandas
```

## 文件结构

本示例应用的文件结构如下：
- `main.py`：Flask应用主要代码
- `templates/` 目录：包含HTML模板文件
  - `loadup.html`：文件上传页面的模板
  - `resdata.html`：处理结果展示页面的模板

## 使用方法

1. 将需要处理的Excel文件上传。
2. 在终端中，进入应用所在的目录，并运行以下命令启动web服务，当然，架设服务需要同时开放端口，默认5000，默认打开debug：
   ```
   python main.py
   ```
3. 打开浏览器，在本机访问 `http://localhost:5000` 来上传文件并查看处理结果。

## 注意事项

- 应用仅支持上传Excel文件（`.xlsx` 格式）。
- Excel文件需要包含一个名为“文本”的列。
- 应用使用 `operationtext.getuserinfo()` 方法对每个文本数据进行处理。请根据实际需求编写该方法的实现。
- 处理结果将以表格的形式展示在页面上，包含序号、原始数据、名称、电话、省份和城市等信息。

## 其他

该示例应用仅供演示目的，为了在真实环境中保证安全性，请添加适当的验证和安全措施。

如果有其他疑问，可以参考Flask官方文档（https://flask.palletsprojects.com/）或联系开发者进行进一步指导。

##  联系
Email：arkkeji.foxmail.com