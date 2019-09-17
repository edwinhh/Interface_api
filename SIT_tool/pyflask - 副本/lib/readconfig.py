import configparser

conf_sql="e:/project/Interface_api-master/SIT_tool/pyflask/config/sql.conf"
conf_db="e:/project/Interface_api-master/SIT_tool/pyflask/config/db.conf"
conf_redis="e:/project/Interface_api-master/SIT_tool/pyflask/config/redis.conf"
def getdb(config):
    db=[]
    #print (config)
    conf = configparser.ConfigParser()
    conf.read(conf_db,encoding="utf-8-sig")
    boolean = conf.has_section(config)
    if boolean:
        host=conf[config]['host']
        username = conf[config]['username']
        password = conf[config]['password']
        port = conf[config]['port']
        database = conf[config]['database']
        db.append(host)
        db.append(username)
        db.append(password)
        db.append(port)
        db.append(database)
    return db

def getsql(config,sql):
    config=config
    #print (config)
    conf = configparser.RawConfigParser()
    conf.read(conf_sql,encoding="utf-8-sig")
    # lists_header = conf.sections()
    # print(lists_header)
    boolean = conf.has_section(config)
    # print(config,"is",boolean)
    if boolean:
        sql=conf[config][sql]
        return sql

# v=getsql('rds','sql1')
# print(v)

def getredis(config):
    redis=[]
    #print (config)
    conf = configparser.ConfigParser()
    conf.read(conf_redis,encoding="utf-8-sig")
    boolean = conf.has_section(config)
    if boolean:
        host=conf[config]['host']
        password = conf[config]['password']
        port = conf[config]['port']
        db = conf[config]['db']
        redis.append(host)
        redis.append(password)
        redis.append(port)
        redis.append(db)
    return redis