import pymysql
from flask import Flask , request, jsonify
from flask_cors import CORS

db = pymysql.connect(host="127.0.0.1",user="root",password="xochitlqx77",database="Arknights",charset="utf8")
cursor = db.cursor()
# 连接本机数据库 cursor是获取一个光标

app = Flask(__name__)
CORS(app,resources=r'/*')
# 后端服务启动

# url是这个接口的地址   POST：向服务器提交信息 GET：从服务器接受信息
# 接口都是按照这个模板 print里都是后端干的事
# 后面get的username一定要和前端发送的参数一致

#用于用户注册
@app.route('/login/add',methods=['POST'])
def login_add():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        sql="insert into login(username,password) values (\"" +str(username)+"\",\""+str(password)+"\")"
#双引号转义符: 如果是一个变量是str类型 语句字符串里这个变量要有引号 可以用双引号转义符来实现
        try:
            cursor.execute(sql)
            db.commit() #提交，使操作生效
            print("add a new user successfully!")
            return "1"
        except Exception as e:
            print("add a new user failed:",e)
            db.rollback() #发生错误就回滚
            return "-1"

#用于用户登录
@app.route('/login/login', methods=['POST'])
def login_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cursor.execute("select id,username,role,ctime from login where username=\""
                       +str(username)+"\" and password=\""+str(password)+"\"")
        data = cursor.fetchone()
        if(data!=None):
            print("result:",data)
            jsondata = {"id":str(data[0]),"username":str(data[1]),
                        "role":str(data[2]),"ctime":str(data[3])}
            return jsonify(jsondata)
        else:
            print("result: NULL")
            jsondata = {}
            return jsonify(jsondata)

#用于查询指定素材不同地图掉率 获取的item_num格式应如"1"，"2"...."13"
@app.route('/Total_map/listmaps', methods=['POST'])
def maps_list():
    if request.method == "POST":
        item_num = request.form.get("item_num")

        cursor.execute("SELECT map_name,prob_item"+str(item_num)+",Count "
       "FROM total_map WHERE prob_item"+str(item_num)+" is not Null "
       "ORDER BY prob_item"+str(item_num)+" DESC")

        data = cursor.fetchall()
        temp={}
        result=[]
        if(data!=None):
            for i in data:
                temp["map_name"]=i[0]
                temp["prob_item"]=i[1]
                temp["Count"]=i[2]
                result.append(temp.copy()) #特别注意要用copy，否则只是内存的引用
            print("result:",len(data))
            return jsonify(result)
        else:
            print("result: NULL wrong")
            return jsonify([])

#用于查询地图不同素材掉率 获取的map_num格式应如"1"，"2"...."9"
@app.route('/Total_map/listItems', methods=['POST'])
def items_list():
    if request.method == "POST":
        map_num = request.form.get("map_num")
        cursor.execute("SELECT * FROM total_map "
                       "WHERE map_name='1_"+str(map_num)+"'")

        data = cursor.fetchall()
        temp={}
        result=[]
        if(data!=None):
            for i in data:
                temp["map_name"]=i[0]
                temp["prob_item1"]=i[1]
                temp["prob_item2"] = i[2]
                temp["prob_item3"] = i[3]
                temp["prob_item4"] = i[4]
                temp["prob_item5"] = i[5]
                temp["prob_item6"] = i[6]
                temp["prob_item7"] = i[7]
                temp["prob_item8"] = i[8]
                temp["prob_item9"] = i[9]
                temp["prob_item10"] = i[10]
                temp["prob_item11"] = i[11]
                temp["prob_item12"] = i[12]
                temp["prob_item13"] = i[13]
                temp["Count"]=i[14]
                result.append(temp.copy()) #特别注意要用copy，否则只是内存的引用
            print("result:",len(data))
            return jsonify(result)
        else:
            print("result: NULL wrong")
            return jsonify([])

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8879)
    db.close()
    print("Good Bye!")