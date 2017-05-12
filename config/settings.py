#! -*- coding:utf8 -*-

"""
数据库配置
"""
db_setting = {
    "dom_test" : {
        "DB_TYPE": "postgresql",
        "DB_DRIVER": "psycopg2",
        "DB_NAME": "dom_test",
        "DB_USER": "dom_test_dev",
        "DB_PASS": "dom_test_dev@123",
        "DB_HOST": "192.168.104.220",
        "DB_PORT": "5432",
    },

    "local_dom" : {
        "DB_TYPE": "postgresql",
        "DB_DRIVER": "psycopg2",
        "DB_NAME": "postgres",
        "DB_USER": "postgres",
        "DB_PASS": "gc",
        "DB_HOST": "127.0.0.1",
        "DB_PORT": "5432",
    }
}

