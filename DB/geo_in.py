#!/usr/bin/env python
#coding=utf-8

geo_map=({"GL_COUNTRY":("国家",0),
				"GL_PROVINCE":("省",1),
				"GL_CITY":("城市",2),
				"GL_COUNTY":("区县",3),
				"GL_DEV_ZONE":("开发区",5),
				"GL_TOWN":("乡镇/街道",4),
				"GL_VILLAGE":("村/社区",5),
				"GL_GROUP":("组/队",5),
				"GL_BZONE":("商圈",5),
				"GL_LINE":("道路",6),
				"GL_ROAD":("道路",6),
				"GL_ROAD_BRANCH":("道路",6),
				"GL_STREETNO":("门牌",8),
				"GL_STREETNO_SUB":("支门牌",8),
				"GL_POI":("POI",9),
				"GL_ROADINTER":("道路交叉口",9),
				"GL_BUILDINGNO":("楼栋号",10),
				"GL_BUILDING_UNIT"	:("单元房间",11),
				"GL_BUILDING_FLOOR" :("单元房间",11),
				"GL_BUILDING_ROOM"  :("单元房间",11),
				"GL_OTHER":("other",-1),
				"GL_INTER":("门牌插值",-1),
				"GL_NEARBY":("附近",-1)}
	)

geo_precision_level_set = set(["GL_BUILDINGNO","GL_POI","GL_STREETNO","GL_STREETNO_SUB"])
geo_precision_filter_set = set(["1","2","8"])

def get_geolevel(geo_level):
	global geo_map
	rtn = ("",-1)
	if geo_map.has_key(geo_level) : 
		rtn = geo_map[geo_level]
	return rtn

def get_geoprecision(geo_level, geo_filter):
	global geo_precision_level_set,geo_precision_filter_set
	rtn = 0
	if geo_level in geo_precision_level_set and geo_filter in geo_precision_filter_set :
		rtn = 2
	return rtn