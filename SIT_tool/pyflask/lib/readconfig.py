import configparser
import os


dir_path=os.path.dirname(os.path.abspath('.')).replace("\\","/")+'/config/'
conf_sql=dir_path+"sql.conf"
conf_db=dir_path+"db .conf"
conf_redis=dir_path+"redis.conf"

def getdb(config):
    db=[]
    #print (config)
    conf = configparser.ConfigParser()
    conf.read(conf_db,encoding="utf-8-sig")
    print(conf.sections())
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
getdb("jira_sit")

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
    redis = {}
    conf = configparser.ConfigParser()
    conf.read(conf_redis,encoding="utf-8-sig")
    boolean = conf.has_section(config)
    if boolean:
        if "redis_type" in conf.options(config):
            redis_type='cluster'
            l=['host','port']
            redis_nodes=[]
            r=conf[config]['redis_nodes']
            lr=r.split(',')
            for i in lr:
                temp=i.split(':')
                temp[1]=int(temp[1])
                dr=dict(zip(l,temp))
                redis_nodes.append(dr)

            password = conf[config]['password']
            conn = {"startup_nodes": redis_nodes, 'password': password, 'decode_responses': 'True'}
   
        else:
            host=conf[config]['host']
            password = conf[config]['password']
            port = conf[config]['port']
            port=int(port)
            db = conf[config]['db']
            conn= {'host': host, 'port': port, 'password': password, 'db': db}
            redis_type=0
            
    return conn,redis_type

#print(getredis('ak_sit')[0])