import os
import configparser
import numpy as np

MDTB_flag = ["MGdb_config", "model_config"]
CFG_Dit = {
    
}

class CFGList:
    def __init__(self, cfg_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfg_path)
        self.output_list = []

    def section_list_function(self):
        # 获取所有节点名称   1、section节； 2、key键； 3、comment注释；
        for model in self.cfg.sections():
            if model in MDTB_flag:
                self.output_list.append(model)
            else:
                model_delta = model.split("_")
                line_model = model_delta[0]
                for i_line in range(len(model_delta) - 2):
                    line_model = line_model + "_" + model_delta[i_line + 1]
                self.output_list.append(line_model)
    
        return self.output_list, self.cfg.sections(), self.cfg