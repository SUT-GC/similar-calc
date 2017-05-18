#! -*- coding:utf8-*-

import sys
import json
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    func,
    text,
    BigInteger,
    Binary,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    SmallInteger,
    String,
    Text,
    VARCHAR,
    Time
)

sys.path.append("..")

from config import (
    DomTestSetting,
    LocalDomSetting,
)

dom_test_setting = DomTestSetting()
local_dom_setting = LocalDomSetting()

dom_test_engine = create_engine(dom_test_setting.get_db_url())
local_dom_setting = create_engine(local_dom_setting.get_db_url())

DomTestSession = sessionmaker(bind=dom_test_engine)
LocalDomSession = sessionmaker(bind=local_dom_setting)

Base = declarative_base()
metadata = Base.metadata


class DomBaiduRestairamtInfo(Base):
    __tablename__ = 'dom_baidu_restairamt_info'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('dom_baidu_restairamt_info_seq'::regclass)"))
    baidu_id = Column(String(255), nullable=False, server_default=text("0"))
    baidu_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    baidu_branch_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    baidu_address = Column(String(255), nullable=False, server_default=text("''::character varying"))
    baidu_phone = Column(String(255), nullable=False, server_default=text("''::character varying"))
    baidu_latitude = Column(Numeric, nullable=False, server_default=text("0.0"))
    baidu_longitude = Column(Numeric, nullable=False, server_default=text("0.0"))
    baidu_logo_hash = Column(String(512), nullable=False, server_default=text("''::character varying"))
    baidu_is_value = Column(SmallInteger, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))


class DomDianpingRestairamtInfo(Base):
    __tablename__ = 'dom_dianping_restairamt_info'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('dom_dianping_restairamt_info_seq'::regclass)"))
    dianping_id = Column(String(255), nullable=False, server_default=text("0"))
    dianping_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    dianping_branch_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    dianping_address = Column(String(255), nullable=False, server_default=text("''::character varying"))
    dianping_phone = Column(String(255), nullable=False, server_default=text("''::character varying"))
    dianping_latitude = Column(Numeric, nullable=False, server_default=text("0.0"))
    dianping_longitude = Column(Numeric, nullable=False, server_default=text("0.0"))
    dianping_logo_hash = Column(String(512), nullable=False, server_default=text("''::character varying"))
    dianping_is_value = Column(SmallInteger, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))


class DomElemeRestaurantInfo(Base):
    __tablename__ = 'dom_eleme_restaurant_info'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('dom_eleme_restaurant_info_seq'::regclass)"))
    eleme_id = Column(BigInteger, nullable=False, server_default=text("0"))
    eleme_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    eleme_branch_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    eleme_address = Column(String(255), nullable=False, server_default=text("''::character varying"))
    eleme_phone = Column(String(255), nullable=False, server_default=text("''::character varying"))
    eleme_latitude = Column(Numeric, nullable=False, server_default=text("0.0"))
    eleme_longitude = Column(Numeric, nullable=False, server_default=text("0.0"))
    eleme_logo_hash = Column(String(512), nullable=False, server_default=text("''::character varying"))
    eleme_is_value = Column(SmallInteger, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))


class DomMeituanRestairamtInfo(Base):
    __tablename__ = 'dom_meituan_restairamt_info'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('dom_meituan_restairamt_info_seq'::regclass)"))
    meituan_id = Column(String(255), nullable=False, server_default=text("0"))
    meituan_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    meituan_branch_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    meituan_address = Column(String(255), nullable=False, server_default=text("''::character varying"))
    meituan_phone = Column(String(255), nullable=False, server_default=text("''::character varying"))
    meituan_latitude = Column(Numeric, nullable=False, server_default=text("0.0"))
    meituan_longitude = Column(Numeric, nullable=False, server_default=text("0.0"))
    meituan_logo_hash = Column(String(512), nullable=False, server_default=text("''::character varying"))
    meituan_is_value = Column(SmallInteger, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))


class DomRestaurantRelation(Base):
    __tablename__ = 'dom_restaurant_relation'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('dom_restaurant_relation_seq'::regclass)"))
    eleme_poi_id = Column(BigInteger, nullable=False, server_default=text("0"))
    other_poi_id = Column(String(255), nullable=False, server_default=text("0"))
    source = Column(SmallInteger, nullable=False, server_default=text("0"))
    is_valid = Column(SmallInteger, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))


class DomRestaurantNotRelation(Base):
    __tablename__ = 'dom_restaurant_not_relation'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('dom_restaurant_not_relation_seq'::regclass)"))
    eleme_poi_id = Column(BigInteger, nullable=False, server_default=text("0"))
    other_poi_id = Column(String(255), nullable=False, server_default=text("0"))
    source = Column(SmallInteger, nullable=False, server_default=text("0"))
    is_valid = Column(SmallInteger, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))


class DomPoi(Base):
    __tablename__ = 'dom_poi'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('dom_poi_id_seq'::regclass)"))
    shop_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    branch_shop_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    shop_show_name = Column(String(255), nullable=False, server_default=text("''::character varying"))
    province_id = Column(Integer, nullable=False, server_default=text("0"))
    city_id = Column(Integer, nullable=False, server_default=text("0"))
    district_id = Column(Integer, nullable=False, server_default=text("0"))
    address = Column(String(255), nullable=False, server_default=text("''::character varying"))
    address_show = Column(String(255), nullable=False, server_default=text("''::character varying"))
    longitude = Column(Numeric(16, 13), nullable=False)
    latitude = Column(Numeric(16, 13), nullable=False)
    phone = Column(String(255), nullable=False, server_default=text("''::character varying"))
    main_category_id = Column(BigInteger, nullable=False, server_default=text("0"))
    minor_category_id = Column(BigInteger, nullable=False, server_default=text("0"))
    shop_status = Column(SmallInteger, nullable=False, server_default=text("0"))
    business_time = Column(String(2000), nullable=False, server_default=text("''::character varying"))
    business_day = Column(String(2000), nullable=False, server_default=text("''::character varying"))
    description = Column(String(2000), nullable=False, server_default=text("''::character varying"))
    head_pic = Column(String(255), nullable=False, server_default=text("''::character varying"))
    logo_pic = Column(String(255), nullable=False, server_default=text("''::character varying"))
    brand_id = Column(BigInteger, nullable=False, server_default=text("0"))
    mall_id = Column(BigInteger, nullable=False, server_default=text("0"))
    shopping_district_id = Column(BigInteger, nullable=False, server_default=text("0"))
    source = Column(SmallInteger, nullable=False, server_default=text("0"))
    data_status = Column(SmallInteger, nullable=False, server_default=text("1"))
    baidu_poi_id = Column(String(80), nullable=False, server_default=text("''::character varying"))
    meituan_poi_id = Column(String(80), nullable=False, server_default=text("''::character varying"))
    dianping_poi_id = Column(String(80), nullable=False, server_default=text("''::character varying"))
    koubei_poi_id = Column(String(80), nullable=False, server_default=text("''::character varying"))
    ers_poi_id = Column(BigInteger, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))

class DomExtBaiduRestaurant(Base):
    __tablename__ = 'dom_ext_baidu_restaurant'

    id = Column(Integer, primary_key=True, server_default=text("nextval('dom_ext_baidu_restaurant_id_seq'::regclass)"))
    shop_id = Column(String(30), nullable=False, server_default=text("''::character varying"))
    shop_name = Column(String(50), server_default=text("''::character varying"))
    takeout_price = Column(Numeric(12, 2), nullable=False, server_default=text("0.00"))
    takeout_cost = Column(Numeric(12, 2), nullable=False, server_default=text("0.00"))
    shop_announcement = Column(String(300), nullable=False, server_default=text("''::character varying"))
    saled_month = Column(String(50), nullable=False, server_default=text("''::character varying"))
    bussiness_time = Column(String(50), nullable=False, server_default=text("''::character varying"))
    address = Column(String(120), nullable=False, server_default=text("''::character varying"))
    shop_phone = Column(String(30), nullable=False, server_default=text("''::character varying"))
    front_logistics_text = Column(String(30), nullable=False, server_default=text("''::character varying"))
    shop_photo = Column(String(700), nullable=False, server_default=text("''::character varying"))
    ceritification = Column(String(700), nullable=False, server_default=text("''::character varying"))
    logo = Column(String(100), nullable=False, server_default=text("''::character varying"))
    category = Column(String(1000), nullable=False, server_default=text("''::character varying"))
    average_score = Column(Numeric(10, 2), nullable=False, server_default=text("0.00"))
    comment_num = Column(Integer, nullable=False, server_default=text("0"))
    menu_count = Column(Integer, nullable=False, server_default=text("0"))
    bizcurrentmonthbussiness = Column(Numeric(12, 2), nullable=False, server_default=text("0.00"))
    eleme_lat = Column(Numeric(16, 13), nullable=False, server_default=text("0.0000000"))
    eleme_lng = Column(Numeric(16, 13), nullable=False, server_default=text("0.0000000"))
    sheng = Column(String(20), nullable=False, server_default=text("''::character varying"))
    shiqu = Column(String(20), nullable=False, server_default=text("''::character varying"))
    xian = Column(String(20), nullable=False, server_default=text("''::character varying"))
    restaurant_status = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))
    fendian_name = Column(String(100), nullable=False, server_default=text("''::character varying"))
    fuss_url = Column(String(150), nullable=False, server_default=text("''::character varying"))
    crawler_flag = Column(Integer, nullable=False, server_default=text("0"))


class DomExtDianpingRestaurant(Base):
    __tablename__ = 'dom_ext_dianping_restaurant'

    id = Column(Integer, primary_key=True, server_default=text("nextval('dom_ext_dianping_restaurant_id_seq'::regclass)"))
    restaurant_id = Column(Integer, nullable=False, server_default=text("0"))
    restaurant_name = Column(String(70), nullable=False, server_default=text("''::character varying"))
    cityname = Column(String(30), nullable=False, server_default=text("''::character varying"))
    cityid = Column(Integer, nullable=False, server_default=text("0"))
    nav = Column(String(50), nullable=False, server_default=text("''::character varying"))
    category = Column(String(30), nullable=False, server_default=text("''::character varying"))
    address = Column(String(300), nullable=False, server_default=text("''::character varying"))
    telphone = Column(String(50), nullable=False, server_default=text("''::character varying"))
    star_text = Column(String(20), nullable=False, server_default=text("''::character varying"))
    star = Column(String(20), nullable=False, server_default=text("''::character varying"))
    average = Column(Numeric(10, 2), nullable=False, server_default=text("0.00"))
    taste = Column(Numeric(10, 2), nullable=False, server_default=text("0.00"))
    environ = Column(Numeric(10, 2), nullable=False, server_default=text("0.00"))
    service = Column(Numeric(10, 2), nullable=False, server_default=text("0.00"))
    lng = Column(Numeric(16, 13), nullable=False, server_default=text("0.0000000"))
    lat = Column(Numeric(16, 13), nullable=False, server_default=text("0.0000000"))
    waimai = Column(Integer, nullable=False, server_default=text("0"))
    month_sale = Column(Integer, nullable=False, server_default=text("0"))
    activitylist = Column(String(50), nullable=False, server_default=text("''::character varying"))
    deliver_type = Column(Integer, nullable=False, server_default=text("0"))
    flag_new = Column(Integer, nullable=False, server_default=text("0"))
    flag_fendian = Column(Integer, nullable=False, server_default=text("0"))
    flag_brand = Column(Integer, nullable=False, server_default=text("0"))
    flag_waimai = Column(Integer, nullable=False, server_default=text("0"))
    fendian_count = Column(Integer, nullable=False, server_default=text("0"))
    comment1 = Column(Integer, nullable=False, server_default=text("0"))
    tuan = Column(Integer, nullable=False, server_default=text("0"))
    shan = Column(Integer, nullable=False, server_default=text("0"))
    fendian_name = Column(String(50), nullable=False, server_default=text("''::character varying"))
    flag_tuan = Column(Integer, nullable=False, server_default=text("0"))
    flag_cu = Column(Integer, nullable=False, server_default=text("0"))
    flag_ding = Column(Integer, nullable=False, server_default=text("0"))
    zhizhao = Column(Integer, nullable=False, server_default=text("0"))
    xukezheng = Column(Integer, nullable=False, server_default=text("0"))
    open_close = Column(String(500), nullable=False, server_default=text("''::character varying"))
    flag_offline = Column(Integer, nullable=False, server_default=text("0"))
    comment_all = Column(Integer, nullable=False, server_default=text("0"))
    sheng = Column(String(20), nullable=False, server_default=text("''::character varying"))
    shiqu = Column(String(20), nullable=False, server_default=text("''::character varying"))
    xian = Column(String(20), nullable=False, server_default=text("''::character varying"))
    shop_area = Column(String(30), nullable=False, server_default=text("''::character varying"))
    logurl = Column(String(300), nullable=False, server_default=text("''::character varying"))
    imgnum = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))
    crawler_flag = Column(Integer, nullable=False, server_default=text("0"))


class DomExtMeituanRestaurant(Base):
    __tablename__ = 'dom_ext_meituan_restaurant'

    id = Column(Integer, primary_key=True, server_default=text("nextval('dom_ext_meituan_restaurant_id_seq'::regclass)"))
    shop_id = Column(Integer, nullable=False, server_default=text("0"))
    shop_name = Column(String(60), nullable=False, server_default=text("''::character varying"))
    fendian_name = Column(String(50), nullable=False, server_default=text("''::character varying"))
    bulletin = Column(String(1000), nullable=False, server_default=text("''::character varying"))
    call_center = Column(String(150), nullable=False, server_default=text("''::character varying"))
    address = Column(String(150), nullable=False, server_default=text("''::character varying"))
    thumbnails_url = Column(String(150), nullable=False, server_default=text("''::character varying"))
    shipping_time = Column(String(60), nullable=False, server_default=text("''::character varying"))
    delivery_type = Column(Integer, nullable=False, server_default=text("0"))
    pic_url = Column(String(100), nullable=False, server_default=text("''::character varying"))
    yyzz = Column(String(100), nullable=False, server_default=text("''::character varying"))
    wsxkz = Column(String(100), nullable=False, server_default=text("''::character varying"))
    totalscore = Column(Numeric(10, 2), nullable=False, server_default=text("0.00"))
    comment1 = Column(Integer, nullable=False, server_default=text("0"))
    month_sale_num = Column(Integer, nullable=False, server_default=text("0"))
    min_price = Column(Numeric(10, 2), nullable=False, server_default=text("0.00"))
    shipping_fee = Column(Numeric(10, 2), nullable=False, server_default=text("0.00"))
    category_name = Column(String(30), nullable=False, server_default=text("''::character varying"))
    menu_count = Column(Integer, nullable=False, server_default=text("0"))
    shop_amt = Column(Numeric(12, 2), nullable=False, server_default=text("0.00"))
    eleme_lat = Column(Numeric(16, 13), nullable=False, server_default=text("0.0000000"))
    eleme_lng = Column(Numeric(16, 13), nullable=False, server_default=text("0.0000000"))
    sheng = Column(String(20), nullable=False, server_default=text("''::character varying"))
    shiqu = Column(String(20), nullable=False, server_default=text("''::character varying"))
    xian = Column(String(20), nullable=False, server_default=text("''::character varying"))
    restaurant_status = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_at = Column(DateTime, nullable=False, server_default=text("now()"))
    fuss_url = Column(String(150), nullable=False, server_default=text("''::character varying"))
    crawler_flag = Column(Integer, nullable=False, server_default=text("0"))