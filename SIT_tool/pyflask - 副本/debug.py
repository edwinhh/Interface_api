from flask import Flask
from flask import render_template
from flask import request
from SIT_tool.pyflask.lib.jira_lib import jira
from SIT_tool.pyflask.lib.readconfig import getdb
# 实例化，可视为固定格式

app = Flask(__name__)

jira = jira(getdb('jira'))
# route()方法用于设定路由；类似spring路由配置
#等价于在方法后写：app.add_url_rule('/', 'helloworld', hello_world)
@app.route('/')
def hello_world():
    return 'Hello'

# 配置路由，当请求get.html时交由get_html()处理
@app.route('/get')
def get():
    k = jira.rds('GIS_ASS_RDS', 'V3.9')
    return "k"

if __name__ == '__main__':
	
    # app.run(host, port, debug, options)
    # 默认值：host=127.0.0.1, port=5000, debug=false
    app.run(debug=True)