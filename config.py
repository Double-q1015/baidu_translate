# -*- coding: UTF-8 -*-

import os
import sys
import yaml
import threading

class Global_config(object):
    """
    配置文件对象， global_config属性保存了全局配置文件
    """
    _instance_lock = threading.Lock()
    CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yml")

    def __init__(self):
        self.global_config = self.load_config()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Global_config, "_instance"):
            with Global_config._instance_lock:
                if not hasattr(Global_config, "_instance"):
                    Global_config._instance = object.__new__(cls)
        return Global_config._instance

    def load_config(self):
        """
        加载配置文件
        """
        try:
            with open(self.CONFIG_PATH) as f:
                yaml_con = yaml.load(f, Loader=yaml.FullLoader)
                return yaml_con
        except Exception as e:
            raise e

if __name__ == '__main__':
    conf = Global_config()
    print(conf.global_config)