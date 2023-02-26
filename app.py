from flask import Flask, request, redirect, render_template, session, flash, make_response, jsonify
from models import dbConnect
from util.user import User
from datetime import timedelta
import hashlib
import uuid
import re

from datetime import datetime

import os
import werkzeug
from werkzeug.utils import secure_filename
from datetime import datetime

UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)

app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)

#app.config['MAX_CONTENT_LENGTH'] = 70 * 1024 * 1024
#test
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/todo')
def todo():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    todolist = dbConnect.getTodoAll(uid)
    tkname = request.form.get("tkna")
    expr = request.form.get("kizi")
    prio = request.form.get("level")

    print("toooooooo")
    print(tkname)
    return render_template('todo.html', todolist=todolist)

@app.route('/todo', methods=['POST'])
def todolist():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    tkname = request.form.get("tkna")
    expr = request.form.get("kizi")
    prio = request.form.get("level")
    print(prio)
    print(tkname)
    print(expr)

    dbConnect.createTodolist(uid, prio, tkname, expr)

    todolist = dbConnect.getTodoAll(uid)
    print(todolist)


    return render_template('todo.html',todolist=todolist)

@app.route('/todo_delete', methods=['POST'])

def todo_delete():

    uid = session.get("uid")

    if uid is None:

        return redirect('/login')



    tkname = request.form.get("tkna")

    expr = request.form.get("kizi")

    prio = request.form.get("level")





    todolist = dbConnect.getTodoAll(uid)



    todo_id = request.form.get("todo_id")

    dbConnect.deleteTodolist(todo_id)





    return render_template('todo.html',todolist=todolist)

@app.route('/signup')
def signup():
    return render_template('registration/signup.html')


@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or email =='' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('二つのパスワードの値が違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        user = User(uid, name, email, password)
        DBuser = dbConnect.getUser(email)

        if DBuser != None:
            flash('既に登録されているようです')
        else:
            dbConnect.createUser(user)
            UserId = str(uid)
            session['uid'] = UserId
            return redirect('/')
    return redirect('/signup')


@app.route('/login')
def login():
    return render_template('registration/login.html')


@app.route('/login', methods=['POST'])
def userLogin():

    print(UPLOAD_FOLDER)

    email = request.form.get('email')
    password = request.form.get('password')

        #dbConnect.createImag(uid)

    #imagPass = dbConnect.getImag(uid)

    if email =='' or password == '':
        flash('空のフォームがあるようです')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードが間違っています！')
            else:
                session['uid'] = user["uid"]
                return redirect('/')
    return redirect('/login')#,imagPass=imagPass)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/templete', methods=['POST'])
def templete():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message = request.form.get('message')
    channel_id = request.form.get('channel_id')
    #user_id = request.form.get('message_uid')

    if message:
        dbConnect.createMessage(uid, channel_id, message)

    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)

    tim = dbConnect.getTimeMessage(channel_id)

    #time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("OKうえーい"+str(tim))
    uname = dbConnect.getUsername(uid)
    #print(username)



    return render_template('/detail.html', messages=messages, channel=channel, uid=uid, tim=tim, uname=uname)


@app.route('/')
def index():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        uname = dbConnect.getUsername(uid)
        channels = dbConnect.getChannelAll()
    return render_template('index.html', channels=channels, uid=uid, uname=uname)


#index.html
@app.route('/', methods=['POST'])
def add_channel():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    channel_name = request.form.get('channel-title')
    channel = dbConnect.getChannelByName(channel_name)

    #ramen = request.form.getlist("ramen")
    #ramchk = 

    if channel == None:
        channel_description = request.form.get('channel-description')

        dbConnect.addChannel(uid, channel_name, channel_description)
        return redirect('/')
    else:
        error = '既に同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)


@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    cid = request.form.get('cid')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')

    dbConnect.updateChannel(uid, channel_name, channel_description, cid)
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid)


@app.route('/delete/<cid>')
def delete_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(cid)
        if channel["uid"] != uid:
            flash('チャンネルは作成者のみ削除可能です')
            return redirect ('/')
        else:
            dbConnect.deleteChannel(cid)
            channels = dbConnect.getChannelAll()
            uname = dbConnect.getUsername(uid)
            return render_template('index.html', channels=channels, uid=uid, uname=uname)


#message打つURLはここ！

@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    sitagaki = dbConnect.getSitagakiAll(uid)    

    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
#    uname = dbConnect.getUsername(uid)
    print(uid)
#    print(uname)  

    # dbConnect.createKidokulist(uid)

#    kidoku = dbConnect.getKidokulist()
#    print(kidoku)


    teikei = dbConnect.getTeikeibun(uid)
    reaction = dbConnect.getReaction()
    print(reaction)

    return render_template('detail.html',teikei=teikei, messages=messages, channel=channel, uid=uid, sitagaki=sitagaki)


@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message = request.form.get('message')
    channel_id = request.form.get('channel_id')
    #user_id = request.form.get('message_uid')

    if message:
        dbConnect.createMessage(uid, channel_id, message)

    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)

    tim = dbConnect.getTimeMessage(channel_id)

    #time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("OKうえーい"+str(tim))
    uname = dbConnect.getUsername(uid) 
    #print(username)


    sitagaki = dbConnect.getSitagakiAll(uid)
    teikei = dbConnect.getTeikeibun(uid)



    return render_template('detail.html',teikei=teikei,  sitagaki=sitagaki, messages=messages, channel=channel, uid=uid, tim=tim, uname=uname)



@app.route('/sitagaki', methods=['POST'])
def add_sitagaki():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message = request.form.get('message')
    channel_id = request.form.get('channel_id')
    #user_id = request.form.get('message_uid')

    if message:
        dbConnect.createSitagaki(uid, channel_id, message)

    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)

    tim = dbConnect.getTimeMessage(channel_id)

    uname = dbConnect.getUsername(uid)
    #print(username)

    sitagaki = dbConnect.getSitagakiAll(uid)
    teikei = dbConnect.getTeikeibun(uid)



    return render_template('detail.html',teikei=teikei, sitagaki=sitagaki, messages=messages, channel=channel, uid=uid, tim=tim, uname=uname)







@app.route('/teikei', methods=['POST'])
def add_teikei():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message_teikei = request.form.get('message')

    cid_teikei = request.form.get('cid')
    print(cid_teikei)

    teikei = request.form.get('register')
    print(teikei)

    if teikei:
        dbConnect.createTeikeibun(uid, teikei)

    channel = dbConnect.getChannelById(cid_teikei)
    messages = dbConnect.getMessageAll(cid_teikei)

    teikei = dbConnect.getTeikeibun(uid)

    sitagaki = dbConnect.getSitagakiAll(uid)

    return render_template('detail.html', channel=channel, sitagaki=sitagaki,uid=uid, teikei=teikei,messages=messages)

@app.route('/delete_teikei', methods=['POST'])

def delete_teikei():

    uid = session.get("uid")

    if uid is None:

        return redirect('/login')



    teikei_id = request.form.get('teikei_id')

    cid = request.form.get('channel_id')

    print(teikei_id)

    if teikei_id:

        dbConnect.deleteTeikeibun(teikei_id)

    print("aaaaa")

    channel = dbConnect.getChannelById(cid)

    messages = dbConnect.getMessageAll(cid)



    teikei = dbConnect.getTeikeibun(uid)



    sitagaki = dbConnect.getSitagakiAll(uid)





    return render_template('detail.html', messages=messages, sitagaki=sitagaki, teikei=teikei,channel=channel, uid=uid)





@app.route('/delete_sitagaki', methods=['POST'])

def delete_sitagaki():

    uid = session.get("uid")

    if uid is None:

        return redirect('/login')



    sitagaki_id = request.form.get('sitagaki_id')

    cid = request.form.get('channel_id')

    if sitagaki_id:

        dbConnect.deleteSitagaki(sitagaki_id)



    channel = dbConnect.getChannelById(cid)

    messages = dbConnect.getMessageAll(cid)



    teikei = dbConnect.getTeikeibun(uid)



    sitagaki = dbConnect.getSitagakiAll(uid)



    return render_template('detail.html', messages=messages, sitagaki=sitagaki, teikei=teikei,channel=channel, uid=uid)


@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message_id = request.form.get('message_id')
    cid = request.form.get('channel_id')
    if message_id:
        dbConnect.deleteMessage(message_id)

    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    teikei = dbConnect.getTeikeibun(uid)

    sitagaki = dbConnect.getSitagakiAll(uid)



    return render_template('detail.html', messages=messages, sitagaki=sitagaki, teikei=teikei,channel=channel, uid=uid)






@app.route('/setting')
def setting():

    uid = session.get("uid")
    if uid is None:
        return redirect('/setting')

    uname = dbConnect.getUsername(uid)

    imgPath={'path': 'ここに画像パス表示'}

    return render_template('/setting.html',imgPath=imgPath, uname=uname)


@app.route('/setting', methods=['POST'])
def setting_img():
#    if request.method == "GET":
#        return "This is a GET request."
#    elif request.method == "POST":

    uid = session.get("uid")
    if uid is None:
        return redirect('/setting')
    uname = dbConnect.getUsername(uid)

    image = request.files['image']
    print(image)
    if image:
        # Save the image file.
        file = request.files['image']
        filename = (uname["user_name"]) + '.jpg'
        file.save('./static/img/' + filename)
    return render_template('setting.html', uname=uname)

@app.route('/henkouN', methods=['POST'])
def setting_henkouN():
    uid = session.get("uid")
    if uid is None:
        return redirect('/setting')
    uname = request.form.get("uname")
    #ema = request.form.get("ema")
    #passwo = request.form.get("passw")

    imgPath={'path': 'ここに画像パス表示'}

    print(uname)

    print("bbbbbbb")


    print(uid)
    dbConnect. updateUserName(uname, uid)

#    imgPath = dbConnect.getImag(path)
#    print(imgPath)
    uname = dbConnect.getUsername(uid)
    return render_template('setting.html', imgPath=imgPath, uname=uname)



@app.route('/henkouE', methods=['POST'])
def setting_henkouE():
    uid = session.get("uid")
    if uid is None:
        return redirect('/setting')
    #uname = request.form.get("uname")
    ema = request.form.get("ema")
    #passwo = request.form.get("passw")

    imgPath={'path': 'ここに画像パス表示'}

    print(ema)

    print("bbbbbbb")


    print(uid)
    dbConnect. updateUserEmail(ema, uid)

#    imgPath = dbConnect.getImag(path)
#    print(imgPath)
    uname = dbConnect.getUsername(uid)
    return render_template('setting.html', imgPath=imgPath, uname=uname)


@app.route('/henkouP', methods=['POST'])
def setting_henkouP():
    uid = session.get("uid")
    if uid is None:
        return redirect('/setting')
    #uname = request.form.get("uname")
    #ema = request.form.get("ema")
    passwo = request.form.get("passw")

    imgPath={'path': 'ここに画像パス表示'}

    print(passwo)

    print("bbbbbbb")


    print(uid)
    dbConnect. updatePassword(passwo, uid)

#    imgPath = dbConnect.getImag(path)
#    print(imgPath)
    uname = dbConnect.getUsername(uid)
    return render_template('setting.html', imgPath=imgPath, uname=uname)



@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')


@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)