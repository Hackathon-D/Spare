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

UPLOAD_FOLDER = '/Users/hiroki/Desktop/hackathon/hackathon-sample-replaced/Spare/static/img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)

app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)

#app.config['MAX_CONTENT_LENGTH'] = 70 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/todo') 
def todo():
    return render_template('/todo.html')

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


@app.route('/templete', methods=['GET', 'POST'])
def templete():
    return render_template('/templete.html')

@app.route('/')
def index():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channels = dbConnect.getChannelAll()
    return render_template('index.html', channels=channels, uid=uid)


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
            return render_template('index.html', channels=channels, uid=uid)


#message打つURLはここ！

@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
#    uname = dbConnect.getUsername(uid)
    print(uid)
#    print(uname)  

    # dbConnect.createKidokulist(uid)

#    kidoku = dbConnect.getKidokulist()
#    print(kidoku)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)#, uname=uname)


#大改造
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



    return render_template('detail.html', messages=messages, channel=channel, uid=uid, tim=tim, uname=uname)



@app.route('/teikei', methods=['POST'])
def add_teikei():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

#    message_teikei = request.form.get('message')
    cid_teikei = request.form.get('cid')
    print(cid_teikei)

#    teikei = request.form.get('register')

#    if teikei:
#        dbConnect.createTeikeibun(uid, cid, teikei)

#    channel = dbConnect.getChannelById(channel_id)
#    messages = dbConnect.getMessageAll(channel_id)

#    teikei = dbConnect.getTeikeibun(uid)

    return render_template('detail.html')#, channel=channel), teikei=teikei) uid=uid,messages=messages)




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

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)





@app.route('/setting')
def setting():

    imgPath={'path': 'ここに画像パス表示'}

    return render_template('/setting.html',imgPath=imgPath)


@app.route('/setting', methods=['POST'])
def setting_img():
#    if request.method == "GET":
#        return "This is a GET request."
#    elif request.method == "POST":

    uid = session.get("uid")
    if uid is None:
        return redirect('/setting')

    image = request.files['image']
    print(image)
    if image:
        # Save the image file.
        filename = secure_filename(image.filename)
        print(filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        print("bbbbbbb")

        path = UPLOAD_FOLDER + filename 

        print(path)
        dbConnect.createImag(uid,path)

        imgPath = dbConnect.getImag(path)
        print(imgPath)
    return render_template('setting.html',imgPath=imgPath)





@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')


@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)