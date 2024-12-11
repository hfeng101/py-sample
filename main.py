# 这是一个示例 Python 脚本。
import argparse
import http.server
import logging
import os
import socket
import sqlite3
import mysql.connector
import psycopg2
from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer

import FastAPI as FastAPI
import Flask as Flask
import mysql as mysql
import unicron as unicron

from aiohttp import web


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

# 命令行参数解析
class flag_parser:
    def __init__(self):
        # super.__init__(self)
        self.name="flag parser"
        self.age=28
        print("test flag parser!"+"test")
    def parse(self, name, age):
        print("name is "+name,"value is %d",age)
        parser = argparse.ArgumentParser(description="命令行参数解析测试")
        parser.add_argument("--param", type=int, help="参数1")
        parser.add_argument("-v", "--verbose", action="store_true", help="启动详细模式")

        args = parser.parse_args()
        print(args.param)
        print(args.verbose)

# 设置日志打印级别，并打印日志
class log_print:
    def __init__(self):
        logging.config(self)
        logging.info("this is info log")
        logging.debug("this is debug log")
        logging.warning("this is warn log")
        logging.error("this is err log")
        logging.log(logging.INFO)
    def Print(self, content):
        logging.info(content)

# 网络连接
class net_session:
    def __init__(self):
        print("test net session!")
        log_print.Print("test answer")

    def server(self, host, port):
        #with和直接赋值有什么区别
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(host,port)
        print(f"starting server, address is host:{host}, port:{port}")
        serverSocket.listen(1)

        while True:
            print("waiting for conn")
            conn, addr = serverSocket.accept()
            with conn:
                print(f"already connection: {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print("connection stopped!")
                        break
                    print(f"receive msg: {data}")
                    conn.sendall(data)


    def client(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketClient:
            socketClient.connect(host,port)
            print(f"already connect to {host}:{port}")

            while True:
                # data="test tcp session"
                # socketClient.send(data)
                message = input("test tcp session")
                if message.lower() == 'exit':
                    print("stop connection")
                    break

                socketClient.send(message.encode())
                data = socketClient.recv(1024)
                print(f"receive message is {data}")



        





    def connet(self):
        net_session.connet()

class file_IO:
    def __init__(self, filepath):
        if os.path.exists(filepath):
            print(f"Open file {filepath}")
        print("Start file_IO operations")
        fd = os.open(filepath)
        data=os.read(fd,1024)
        print(f"open file {filepath}, read data is {data[:100]}")

        os.write(fd, "hahah")


    def test(self, filepath):
        if os.path.exists(filepath):
            print(f"test file io for {filepath}")

        try:
            with open(filepath, "w") as fd:
                fd.write("test file write!")

                content=fd.read(1024)
                print(f"read content is {content}")

                print(f"Current Position",fd.tell())
                fd.seek(0) #移动到文件开头的位置
                print(f"New Position", fd.tell())
        except FileExistsError as e0:
            print(f"Error: file {filepath} is not exist!")
        except FileNotFoundError as e1:
            print(f"Error: file {filepath} is no found!")

    def raw_io(self, filepath):
        try:
            with open(filepath, "wb") as fd:
                data=b"test binary write & read!"
                fd.write(data)
                print("Finish write raw data!")
        except FileNotFoundError:
            print(f"Error: file {filepath} is not found!")
        except FileExistsError:
            print(f"Error: file {filepath} is not exist!")


# http service，使用标准库http.server模块，或使用第三方框架如：Flask、FastAPI等
# 或使用异步框架asyncio 和 aiohttp
class http_service:
    def __init__(self, host, port):
        print("start http service!")
        #with http.server.HTTPServer((host,port), SimpleHTTPRequestHandler) as server:
        with http.server.HTTPServer((host, port), Http_process_handler) as server:
            server.serve_forever()
            print(f"http server running on {host}:{port}")

    def server(self):
        print("starting server!")

    def client(self):
        print("starting client!")

    def flask_server(self, host, port):
        app = Flask(__name__)
        app.run(host, port)

    @app.route("/")
    def flask_home():
        return "hello world"

    @app.route("/hello/<name>")
    def flask_hello(self, name):
        return f"hello, {name}"


    def FastAPI_Server(self, host, port):
        app = FastAPI()
        unicron.run(app, host, port)

    def FastAPI_Read_Root(self):
        print("Read Root")
        return {"message": "hello world!"}

    def FastAPI_Read_Item(self, item_id: int, q: str=None):
        print("Read Item")
        return {"item_id": item_id, "q": q}


    def Async_Http_Server(self, host, port):
        app = web.Application()
        app.router.add_get("/", handle)
        app.router.add_get("/{name}", handle)
        web.run_app(app, host, port)

    async def handle(self, request):
        name = request.match_info.get("name", "Anonymous")
        text = f"hello {name}"
        return web.Response(text)

class Http_process_handler(BaseHTTPRequestHandler):
    def do_Get(self):
        # 设置响应头
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # 设置响应体
        response=f"<html><body><h1>hello, {self.path}</h1></body></html>"
        self.wfile.write(response.encode("utf-8"))


#Python 可以通过多种库与数据库交互，如 SQLite（内置库）、MySQL、PostgreSQL
class database_operation:
    def __init__(self):
        print("starting database operation")

    def sqlite_database_operation(self, host, port):
        dsn = host+port
        #conn = sqlite3.connect("example.db")
        conn = sqlite3.connect(dsn)

        cursor = conn.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL)
                        """)

        cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", ("Alice", 25))
        cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", ("Bob", 25))

        print(f"Finish Create table & excute insert operation")
        conn.commit()

        # 查询数据
        cursor.execute("SELECT * from users")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row}")

        # 更新数据
        cursor.execute("UPDATA users SET age=? WHERE name=?",(18,"Alice"))

        # 删除数据
        cursor.execute("DELETE FROM users WHERE name=?",("Bob"))

        conn.commit()
        conn.close()

    def mysql_database_operation(self, host, port):
        dsn=host+port
        conn=mysql.connector.connect(
            host=host,
            user="root",
            password="password",
            database="testdb"
        )

        cursor=conn.cursor

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS employees (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(256) NOT NULL,
                    age INT NOT NULL,
                    salary FLOAT)
                    """)

        cursor.execute("INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)", ("Alice",25, 10000))
        cursor.execute("INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)", ("Jone", 18, 5000))

        conn.commit()

        # 查询
        cursor.execute("SELECT * FROM employees")
        rows=cursor.fetchall()
        for row in rows:
            print(row)

        # 更新数据
        cursor.execute("UPDATE employees SET salary= %s WHERE name = %s", (100000, "Alice"))

        # 删除数据
        cursor.execute("DELETE FROM employees WHERE name = %s", "Alice")

        conn.commit()
        conn.close()

    def pgsql_database_operation(self, host, port):
        conn = psycopg2.connect(
            dbname="testdb",
            user="postgres",
            password="password",
            host=host,
            port=port
        )

        cursor=conn.cursor

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS student(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(256) NOT NULL,
                    grade INTEGER)
                    """)

        cursor.execute("INSERT INOT student (name, grade) VALUES (%s, %s)", ("Alice", 3))
        cursor.execute("INSERT INTO student (name, grade) VALUES (%s,  %s)", ("john", 5))

        conn.commit()

        # 查询数据
        cursor.execute("SELECT * FROM student WHERE name=%s", "Alice")
        rows=cursor.fetchall()
        for row in rows
            print(row)

        # 更新数据
        cursor.execute("UPDATE student SET grade=%s WHERE name=%s", (1, "john"))

        #删除数据
        cursor.execute("DELETE FROM student WHERE name=%s", "Alice")

        conn.commit()
        conn.close()
    def TableOperation(self):
        print("starting TableOperation")
    def crud(self):
        print("crud demo")

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    flag_parser.parse("test", "test", 25)



