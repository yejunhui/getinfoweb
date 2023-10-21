from flask import Flask, request, render_template,redirect,url_for,Response
import pandas as pd
import operationtext
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template('loadup.html')
    
@app.route('/resdata',methods=['GET','POST'])
def res_data():
    try:
        file = request.files['file']
        # 使用 Pandas 读取 Excel 文件内容
        df = pd.read_excel(file)
        text = df.iloc[:, 0]
        table_list = []

        num = 1
        for item in text:
            res = operationtext.getuserinfo(item)

            res['oldtext'] = item

            res['num'] = num
            num += 1

            print(res)
            table_list.append(res)

        # 将 DataFrame 转换成 HTML 表格字符串
        table_title = df.iloc[0]
        df.drop(0,inplace=True)
        table_html = df.to_html(index=True,header=False,classes='td')

        new_title = ['序号','原数据','名称','电话','省份','城市','详细地址']
        
        # 渲染带有表格的 HTML 页面
        
        return render_template('resdata.html', table_title=new_title, new_table_list=table_list)
    except:
        return redirect(url_for('upload_file'))
    
@app.route('/getinfo')
def getinfo():
    try:
        text  = request.args.get('text')
        res = operationtext.getuserinfo(text=text)
        response = Response(json.dumps(res, ensure_ascii=False), content_type='application/json; charset=utf-8')
        return response
    except:
        return {'code':'error','text':'出现了错误，请已get类型访问，并携带一个text作为参数！'}

if __name__ == '__main__':
    app.run(debug=True)
