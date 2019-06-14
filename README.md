title:   一体化大数据平台 mock server

目录结构:
appbox:应用名称
---blueprints   蓝图目录     <br>
---modules      模型目录     <br>
---static       静态资源文件  <br>
---template     模板目录     <br>
---views        试图目录     <br>
--------data_body.py  mock 服务的请求和响应body配置 <br>
--------data_md5person.py    已停止使用的人员和照片映射 <br>
--------data_picturemap.csv  未开始使用的人员和照片映射 <br>
--------datacode_robert.csv  户籍地址的映射    <br>
test:  测试代码目录           <br>
tmp:   临时目录              <br>
appbox.py   工程入口启动目录  <br>
config.py   本工程配置文件入口(例如server name) <br>
README.md   <br>
requirements.txt  工程依赖文件 <br>


数据初始化：
1  [修改HOSTNAME  修改config.py文件中的 HOST_NAME=本机IP]   <br>
2  [修改data_body.py中的  SanHuiBigDB_connect mysql数据库连接]   <br>

常用命令：
1  [导出依赖命令  pip freeze > requirements.txt ] <br>
   [导入依赖命令  pip install -r requirements.txt ] <br>
2  [运行命令  python appbox.py]   <br>
3  [gitlab 仓库  http://gitlab.yitu-inc.com/test-garden/box-xj-mockserver] <br>

