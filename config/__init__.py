#! -*- coding:utf8 -*-

from settings import db_setting

class BaseDBSetting(object):
    def __init__(self, database):

        self.database = database
        self.db_user = db_setting[self.database]["DB_USER"]
        self.db_pass = db_setting[self.database]["DB_PASS"]
        self.db_host = db_setting[self.database]["DB_HOST"]
        self.db_port = db_setting[self.database]["DB_PORT"]
        self.db_name = db_setting[self.database]["DB_NAME"]
        self.db_driver = db_setting[self.database]["DB_DRIVER"]
        self.db_type = db_setting[self.database]["DB_TYPE"]

    '''
    return db_url like 'db_type+db_driver://user:pass@host:port/db_name'
    '''

    def get_db_url(self):
        db_url = r'%s+%s://%s:%s@%s:%s/%s' % (
            self.db_type, self.db_driver, self.db_user, self.db_pass, self.db_host, self.db_port, self.db_name)
        print '获取DB连接[%s].....' % db_url
        return db_url


class DomTestSetting(BaseDBSetting):
    def __init__(self):
        super(DomTestSetting, self).__init__("dom_test")

class LocalDomSetting(BaseDBSetting):
    def __init__(self):
        super(LocalDomSetting, self).__init__("local_dom")


if __name__ == '__main__':
    domTestSetting = DomTestSetting()
    localDomSetting = LocalDomSetting()
    print domTestSetting.get_db_url()
    print localDomSetting.get_db_url()
