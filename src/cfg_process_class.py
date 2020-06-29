import os
import configparser
import numpy as np

process_flag = ["MGdb_create", "data_process", "MGdb_createOSU"]

CFG_Dit = {"data_folder_patch":"XXX", "suffix":"XXX", "Remote_flag":0,
    "ip":"000.000.000.000", "port":00000, "db_name":"XXX", "set_name":"XXX",
    "Remote_IP":"000.000.000.000", "Remote_port":00000, "Remote_user":"XXX", "Remote_password":"XXX",
}

class CFGList:
    def __init__(self, cfg_path):
        self.output_list = []
        self.sections = []

        self.Dit_output = CFG_Dit.copy()
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfg_path)
        self.sections = self.cfg.sections()

    def get_section_list(self):
        # 获取所有节点名称   1、section节； 2、key键； 3、comment注释；
        for model in self.sections:
            model_delta = model.split("_")
            line_model = model_delta[0]
            for i_line in range(len(model_delta) - 2):
                line_model = line_model + "_" + model_delta[i_line + 1]
            self.output_list.append(line_model)
    
        return self.output_list

    def get_cfg_dit(self, line_loop):
        if self.output_list[line_loop] == "MGdb_config":
            self.Dit_output["ip"] = (self.cfg.get(self.sections[line_loop], "ip")).split(" ")[0]
            self.Dit_output["port"] = int((self.cfg.get(self.sections[line_loop], "port")).split(" ")[0])
            self.Dit_output["db_name"] = (self.cfg.get(self.sections[line_loop], "db_name")).split(" ")[0]
            self.Dit_output["set_name"] = (self.cfg.get(self.sections[line_loop], "set_name")).split(" ")[0]

        elif self.output_list[line_loop] in process_flag:
            self.Dit_output["data_folder_patch"] = self.cfg.get(self.sections[line_loop], "data_folder_patch")
            self.Dit_output["Remote_flag"] = int((self.cfg.get(self.sections[line_loop], "Remote_flag")).split(" ")[0])
            self.Dit_output["suffix"]  = (self.cfg.get(self.sections[line_loop], "suffix")).split(" ")[0]
            
            if self.Dit_output["Remote_flag"] == 1:
                self.Dit_output["Remote_IP"] = (self.cfg.get(self.sections[line_loop], "Remote_IP")).split(" ")[0]
                self.Dit_output["Remote_port"] = int((self.cfg.get(self.sections[line_loop], "Remote_port")).split(" ")[0])
                self.Dit_output["Remote_user"] = (self.cfg.get(self.sections[line_loop], "Remote_user")).split(" ")[0]
                self.Dit_output["Remote_password"] = (self.cfg.get(self.sections[line_loop], "Remote_password")).split(" ")[0]

        return self.Dit_output

    def clean_dit(self):
        self.Dit_output = {}

