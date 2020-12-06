import sqlite3
import os
from enum import Enum

# config
default_where = '1=1'
show_sql = True


# sql 操作类型
class Type(Enum):
    CREATE = 1
    INSERT = 2
    QUERY = 3
    UPDATE = 4
    DELETE = 5


class Sqllite_Util:
    con = None

    def __init__(self):
        self.con = self.get_connect()

    # 获取数据库连接
    def get_connect(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cdb = current_dir + '/test_data.db'
        return sqlite3.connect(cdb)

    def __execute(self, sql, type):
        cur = self.con.cursor()
        self.show_sql(sql)
        cur.execute(sql)
        if Type.QUERY == type:
            return cur.fetchall()
        else:
            self.con.commit()

    #  查询表
    def select(self, field, tablename, where):
        sql = "select %s from %s where %s" % (field, tablename, where)
        return self.__execute(sql, Type.QUERY)

    # 创建表 field 多字段逗号分隔
    def create(self, tablename, fields):
        sql = "CREATE TABLE IF NOT EXISTS %s(%s)" % (tablename, fields)
        self.__execute(sql, Type.CREATE)
        print("表 %s 创建成功！" % tablename)

    #  数据库 插入数据
    def insert(self, tablename, field, values):
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (tablename, field, values)
        self.__execute(sql, Type.INSERT)
        print("表 %s 新增数据成功！" % tablename)

    #  修改数据
    def update(self, sql):
        self.__execute(sql, Type.UPDATE)

    #  删除数据
    def delete(self, tablename, where):
        sql = "DELETE from %s where %s;" % (tablename, where)
        self.__execute(sql, Type.DELETE)

    # 打印sql
    def show_sql(self, sql):
        if show_sql:
            print("执行sql ->  " + sql)


if __name__ == "__main__":
    obj = Sqllite_Util()
    res = obj.select('user_name', 'data_user', default_where)
    print(res)
    obj.insert('data_user', 'user_name,age,password', "'嬴政',45,'123456'")
    # obj.create('unit','id,unit,creator')
    # obj.update('update data_user set user_name = "enzo" where id = 1')
