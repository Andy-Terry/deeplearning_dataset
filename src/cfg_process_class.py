import os
import configparser
import numpy as np

MDTB_flag = ["MGdb_config", "model_config"]

class CFGList:
    def __init__(self, cfg_path):
        self.cfg_path = cfg_path

    def section_list_function(self):
        output_list = []
        cfg = configparser.ConfigParser()
        cfg.read(self.cfg_path)
        # 获取所有节点名称   1、section节； 2、key键； 3、comment注释；
        section_list = cfg.sections() 
        self.cfg_data = section_list
        output_cfg_data = section_list

        for model in section_list:
            if model in MDTB_flag:
                output_list.append(model)
            else:
                model_delta = model.split("_")
                line_model = model_delta[0]
                for i_line in range(len(model_delta) - 2):
                    line_model = line_model + "_" + model_delta[i_line + 1]
                output_list.append(line_model)
    
        return output_list, output_cfg_data, cfg