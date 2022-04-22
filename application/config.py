

# mysql 配置
class MysqlDataBase:
    Host = ""
    Port = ""
    Name = ""
    Password = ""
    DB = ""


# redis 配置
class RedisDataBase:
    Host = ""
    Port = ""
    Name = ""
    Password = ""
    DB = 0


# 配置
class Config(object, MysqlDataBase, RedisDataBase):
    """配置"""
    Debug = True
    Testing = True
    Host = "127.0.0.1"
    Port = "5050"

