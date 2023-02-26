import pymysql
from util.DB import DB

class dbConnect:
    def createUser(user):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (user.uid, user.name, user.email, user.password))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getUserId(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT uid FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            id = cur.fetchone()
            return id
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def addChannel(uid, newChannelName, newChannelDescription):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (uid, name, abstract) VALUES (%s, %s, %s);"
            cur.execute(sql, (uid, newChannelName, newChannelDescription))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
        except Exception as e:
            print(e + 'が発生しました')
            return None
        finally:
            cur.close()
            return channel


    def updateChannel(uid, newChannelName, newChannelDescription, cid):
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
        cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
        conn.commit()
        cur.close()


    #deleteチャンネル関数
    def deleteChannel(cid):
        try: 
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT id,u.uid, user_name, message,created_at FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def deleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM messages WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
    

#以下追加機能
    def getSitagakiAll(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM sitagaki WHERE uid = %s;"
            cur.execute(sql, (uid))
            sitagaki = cur.fetchall()
            return sitagaki
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def createSitagaki(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO sitagaki(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def deleteSitagaki(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM sitagaki WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getTimeMessage(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT created_at FROM messages WHERE cid=%s;"
            cur.execute(sql, (cid))
            conn.commit()
            time = cur.fetchall()
            return time
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()




    def getUsername(uid):

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT user_name FROM users WHERE uid=%s;"
            cur.execute(sql, (uid))
            conn.commit()
            uname = cur.fetchone()
            return uname

        except Exception as e:
            print(e + 'が発生しています')
            return None

        finally:
            cur.close()

    def gerKidokulist():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM kidoku;"
            cur.execute(sql)
            conn.commit()
            kidoku = cur.fetchall()
            return kidoku 
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def createKidokulist(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO kidoku(uid) VALUES(%s)"
            cur.execute(sql, (uid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def createTeikeibun(uid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO teikeibun(uid, message) VALUES(%s, %s)"
            cur.execute(sql, (uid, message))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getTeikeibun(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM teikeibun WHERE uid=%s;"
            cur.execute(sql, (uid))
            teikeibun = cur.fetchall()
            return teikeibun
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def deleteTeikeibun(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM teikeibun WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()




    def createImag(uid, path):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO imag(uid, path) VALUES(%s, %s)"
            cur.execute(sql, (uid, path))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getImag(path):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT path FROM imag WHERE path = %s;"
            cur.execute(sql, (path))
            imags = cur.fetchone()
            return imags 
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()



    def deleteImag(id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM imag WHERE id=%s;"
            cur.execute(sql, (id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()




    def createTodolist(uid, prio, tkname, expr):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO todolist(uid, proity, tkname, expr) VALUES(%s, %s, %s, %s)"
            cur.execute(sql, (uid, prio, tkname, expr))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getTodoAll(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM todolist WHERE uid=%s;"
            cur.execute(sql, (uid))
            todolist = cur.fetchall()
            return todolist
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def deleteTodolist(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM todolist WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def updateUserName(user_name, uid):
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "UPDATE users SET user_name=%s WHERE uid=%s;"
        cur.execute(sql, (user_name, uid))
        conn.commit()
        cur.close()



    def updateUserEmail(email, uid):
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "UPDATE users SET email=%s WHERE uid=%s;"
        cur.execute(sql, (email, uid))
        conn.commit()
        cur.close()


    def updatePassword(password, uid):
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "UPDATE users SET password=%s WHERE uid=%s;"
        cur.execute(sql, (password, uid))
        conn.commit()
        cur.close()

    def getReaction():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT path FROM riaction;"
            cur.execute(sql)
            reaction = cur.fetchall()
            return reaction
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()