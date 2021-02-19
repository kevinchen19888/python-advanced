# mysql数据库访问dmeo

# 导入mysql驱动
import mysql.connector

# 注意把psd设为root口令
conn = mysql.connector.connect(host='localhost',
                               port='3306',
                               user='root',
                               password='root',
                               database='python_test')
cursor = conn.cursor()


def create_table():
    # 创建表
    cursor.execute(
        'create table python_temp(id bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,'
        'name varchar(20),PRIMARY KEY (`id`) USING BTREE)')
    # 插入一行记录,注意mysql的占位符为%s
    cursor.execute('insert into python_temp(name) values (%s)', ['kevin'])
    # cursor.rowcount
    # 提交事务
    conn.commit()
    # cursor.close()


# create_table()


# 执行查询
cursor.execute('select * from python_temp where id = %s', ('1',))
value = cursor.fetchall()
cursor.close()
conn.close
print('查询结果:', value)
