import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='10.202.24.5:9094')

topic='GIS_TEST'

msg_dict = {
	"ac": 10,
	"ad": "112",
	"ak": 7,
	"be": "1111",
	"bn": "755AQ",
	"bt": 0,
	"cr": "gcj",
	"dx": -1.0,
	"dy": -1.0,
	"id": "1111",
	"pc": 0,
	"sc": "car",
	"sl": 11,
	"sp": 10.0,
	"state": -1,
	"tm": 1568104931,
	"tp": 1,
	"un": "车牌3号",
	"v": "",
	"xh": "1568104447911",
	"zx": 112.18456,
	"zy": 22.59468
}
msg = json.dumps(msg_dict)
producer.send(topic,msg.encode(), partition=0)
producer.close()