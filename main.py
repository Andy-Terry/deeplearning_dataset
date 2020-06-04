import os
import numpy as np
import configparser

from src.cfg_process_class import CFGList
from src.Mdb_process_class import MyMongoDB
from src.Mdb_process_tool import tool_TXT2Mdb
from src.data_process_class import DataProcess

MGdb_dic = {}
Remote_dit = {}

if __name__ == "__main__":
    cfg_name = "darkent_yolov4_vis2020.cfg"
    cfg_folder_path = "./cfg"

    cfg_path = os.path.join(cfg_folder_path, cfg_name)
    cfg_instance = CFGList(cfg_path)
    section_list, cfg_section, cfg_data= cfg_instance.get_section_list()

    for line_loop in range(len(section_list)):
        if section_list[line_loop] == "MGdb_config":
            MGdb_dic = cfg_instance.get_cfg_dit(line_loop)
            mongo = MyMongoDB(MGdb_dic)
            # MGdb_dic = {}

        elif section_list[line_loop] == "MGdb_create":
            foldel_path = cfg_data.get(cfg_section[line_loop], "data_folder_patch")
            open_suffix = (cfg_data.get(cfg_section[line_loop], "suffix")).split(" ")[0]
            if open_suffix == ".txt":
                tool_TXT2Mdb(foldel_path, mongo)
            elif open_suffix == ".xml":
                pass
            else:
                print("error : cann't open suffix file, see cfg file config")
            

        elif section_list[line_loop] == "data_process":
            foldel_path = cfg_data.get(cfg_section[line_loop], "data_folder_patch")
            open_suffix = (cfg_data.get(cfg_section[line_loop], "suffix")).split(" ")[0]
            if open_suffix == ".jpg":
                DataProcess_SD = DataProcess(foldel_path, open_suffix, line_loop)
                SD_matrix = DataProcess_SD.SizeDistribution_jpg()
            elif open_suffix == ".xml":
                pass
            else:
                print("error : cann't open suffix file, see cfg file config")

        # elif section_list[line_loop] == "MGdb_process":
        #     print("welcome MGdb")

        else:
            print("cfg config is error:", line_loop, "line", section_list[line_loop], "Undefined")



    print(section_list)
    print(cfg_data)

    # print(section_list)  
    # option_list = cfg.options(section_list[3])
    # print(option_list) 
    # key_value = cfg.get(section_list[3], option_list[0])
    # print(len(key_value)) 
    # key_value = key_value.split("#")
    # print(len(key_value)) 
    # print("ok")