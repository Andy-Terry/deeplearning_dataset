import os
import configparser
import numpy as np

MDTB_flag = ["MGdb_config", "model_config"]

CFG_Dit = {"data_folder_patch":"XXX", "Remote_flag":0,
    "ip":'000.000.000.000', "port":00000,
    "db_name":"XXX", "set_name":"XXX",
    "suffix":"XXX"
}

class CFGList:
    def __init__(self, cfg_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfg_path)
        self.sections = self.cfg.sections()
        self.output_list = []
        self.sections = []
        self.Dit_output = {}

    def get_section_list(self):
        # 获取所有节点名称   1、section节； 2、key键； 3、comment注释；
        for model in self.sections:
            if model in MDTB_flag:
                self.output_list.append(model)
            else:
                model_delta = model.split("_")
                line_model = model_delta[0]
                for i_line in range(len(model_delta) - 2):
                    line_model = line_model + "_" + model_delta[i_line + 1]
                self.output_list.append(line_model)
    
        return self.output_list, self.sections, self.cfg

    def get_cfg_dit(self, line_loop):
        self.Dit_output = CFG_Dit.copy()
        self.Dit_output["data_folder_patch"] = self.cfg.get(self.sections[line_loop], "data_folder_patch")
        self.Dit_output["Remote_flag"] = int((self.cfg.get(self.sections[line_loop], "Remote_flag")).split(" ")[0])
        self.Dit_output["ip"] = (self.cfg.get(self.sections[line_loop], "ip")).split(" ")[0]
        self.Dit_output["port"] = int((self.cfg.get(self.sections[line_loop], "port")).split(" ")[0])
        self.Dit_output["db_name"] = (self.cfg.get(self.sections[line_loop], "db_name")).split(" ")[0]
        self.Dit_output["set_name"] = (self.cfg.get(self.sections[line_loop], "set_name")).split(" ")[0]

        if self.Dit_output["Remote_flag"] == 1:
            pass

        return self.Dit_output

    def clean_dit(self):
        self.Dit_output = {}

