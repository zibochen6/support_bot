# 在 reComputer 上使用 SQLite

## 简介

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/sqlite/sqlite.jpg)

本 wiki 介绍如何在 reComputer 盒子上使用 [SQlite](https://sqlite.org/)。SQLite 是一个轻量级的嵌入式关系数据库管理系统，广泛应用于移动设备、桌面应用程序和嵌入式系统中。它不需要单独的服务器进程；数据库直接存储在一个普通的磁盘文件中。SQLite 使用简单，性能优异。它支持标准的 SQL 语法，适用于中小型数据存储需求。由于其零配置和易于部署的特性，SQLite 已成为许多项目的首选数据库引擎。

## 准备硬件

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html) | | | | | | | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

## 准备软件

### 更新系统

```
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"  
sudo apt update  
sudo apt full-upgrade
```

### 安装 SQlite

```
sudo apt-get install sqlite3
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/sqlite/sqlite_install.png)

### 创建数据库

```
sqlite3 sensordata.db
```

使用 `.help` 命令可以快速查看所有支持的命令及其用法。

```
sqlite> .help
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/sqlite/sqlite_help.png)

然后使用 `.quit` 退出 SQlite shell。

```
sqlite> .quit
```

## 使用 SQL

### SQL 创建表

```
sqlite3 sensordata.db
```

然后使用如下命令创建一个新表。

```
ain@raspberrypi:~ $ sqlite3 sensordata.db  
SQLite version 3.40.1 2022-12-28 14:03:47  
Enter ".help" for usage hints.  
sqlite> BEGIN;  
sqlite> CREATE TABLE dhtreadings (  
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,  
   ...> temperature NUMERIC,  
   ...> humidity NUMERIC,  
   ...> currentdate DATE,  
   ...> currenttime TIME,  
   ...> device TEXT  
   ...> );  
sqlite> COMMIT;
```

### 检查表

您可以使用以下命令查看创建的表。

```
sqlite> .tables  
dhtreadings  
sqlite> .fullschema  
CREATE TABLE dhtreadings (  
id INTEGER PRIMARY KEY AUTOINCREMENT,  
  
temperature NUMERIC,  
humidity NUMERIC,  
currentdate DATE,  
currenttime TIME,  
device TEXT  
);  
/* No STAT tables available */
```

### SQL 插入

要在数据库中插入新的温度和湿度读数，您可以这样做：

```
sqlite> BEGIN;  
sqlite> INSERT INTO dhtreadings(temperature, humidity, currentdate, currenttime, device) values(22.4, 48, date('now'), time('now'), "manual");  
sqlite> COMMIT;
```

### SQL 查询

要访问数据库中存储的数据，您可以使用 SELECT SQL 语句：

```
sqlite> SELECT * FROM dhtreadings;  
1|22.4|48|2025-09-26|01:23:37|manual
```

到目前为止，您只在数据库中插入了 1 条读数。您可以按如下方式插入新的读数：

```
sqlite> BEGIN;  
sqlite> INSERT INTO dhtreadings(temperature, humidity, currentdate, currenttime, device) values(22.5, 48.7, date('now'), time('now'), "manual");  
sqlite> COMMIT;
```

当您 SELECT 表中存储的数据时，它返回 2 条读数：

```
sqlite> SELECT * FROM dhtreadings;  
1|22.4|48|2025-09-26|01:23:37|manual  
2|22.5|48.7|2025-09-26|02:06:35|manual
```

### SQL 删除

如果您想从数据库中完全删除表，可以使用 DROP TABLE 命令。

> 注意：下一个命令将完全删除 dhtreadings 表：

```
sqlite> DROP TABLE dhtreadings;
```

现在，如果您输入 '.tables' 命令：

```
sqlite> .tables
```

它不会返回任何内容，因为您的表已被完全删除。

### 使用 Python 与 SQLite

使用 Python 与 SQLite 交互如下：

test\_sqlite.py

```
import sqlite3  
from datetime import datetime  
import os  
  
def create_connection(db_file="dht_readings.db"):  
    """Create a database connection to the SQLite database"""  
    conn = None  
    try:  
        conn = sqlite3.connect(db_file)  
        print(f"Connected to SQLite database: {db_file}")  
    except sqlite3.Error as e:  
        print(f"Error connecting to database: {e}")  
    return conn  
  
def create_table(conn):  
    """Create the dhtreadings table if it doesn't exist"""  
    try:  
        sql_create_dhtreadings_table = """  
        CREATE TABLE IF NOT EXISTS dhtreadings (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            temperature REAL NOT NULL,  
            humidity REAL NOT NULL,  
            currentdate TEXT NOT NULL,  
            currenttime TEXT NOT NULL,  
            device TEXT NOT NULL  
        );  
        """  
        conn.cursor().execute(sql_create_dhtreadings_table)  
        conn.commit()  
        print("DHT readings table created successfully")  
    except sqlite3.Error as e:  
        print(f"Error creating table: {e}")  
  
def insert_dht_reading(conn, temperature, humidity, device):  
    """Insert a new DHT reading into the dhtreadings table"""  
    sql_insert = """INSERT INTO dhtreadings(temperature, humidity, currentdate, currenttime, device)   
                    VALUES(?, ?, date('now'), time('now'), ?);"""  
    try:  
        cursor = conn.cursor()  
        cursor.execute(sql_insert, (temperature, humidity, device))  
        conn.commit()  
        print(f"New record created successfully with ID: {cursor.lastrowid}")  
        return cursor.lastrowid  
    except sqlite3.Error as e:  
        print(f"Error inserting data: {e}")  
        return None  
  
def select_all_readings(conn):  
    """Query all DHT readings in the dhtreadings table"""  
    try:  
        cursor = conn.cursor()  
        cursor.execute("SELECT * FROM dhtreadings ORDER BY currentdate DESC, currenttime DESC")  
  
        rows = cursor.fetchall()  
        print("\nAll DHT readings:")  
        print("ID | Temperature | Humidity | Date | Time | Device")  
        print("-" * 60)  
        for row in rows:  
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")  
    except sqlite3.Error as e:  
        print(f"Error fetching data: {e}")  
  
def main():  
    # Create a database connection  
    database = "dht_readings.db"  
    conn = create_connection(database)  
  
    # Create table  
    if conn is not None:  
        create_table(conn)  
  
        # Insert a sample reading as specified in your requirement  
        insert_dht_reading(conn, 22.5, 48.7, "manual")  
  
        # Insert some additional sample data for testing  
        insert_dht_reading(conn, 23.1, 45.2, "sensor1")  
        insert_dht_reading(conn, 21.8, 50.3, "sensor2")  
  
        # Display all readings  
        select_all_readings(conn)  
  
        # Close the connection  
        conn.close()  
        print("\nDatabase connection closed.")  
    else:  
        print("Error! Cannot create database connection.")  
  
if __name__ == '__main__':  
    main()
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/sqlite/sqlite_python.png)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在此为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。