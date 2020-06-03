import os
import numpy as np
import configparser

from src.cfg_process_class import CFGList
from src.Mdb_process_class import MyMongoDB
from src.Mdb_process_tool import tool_TXT2Mdb
from src.data_process_class import DataProcess

settings = {
    "ip":'000.000.000.000',   #ip
    "port":00000,           #端口
    "db_name":"YYY",    #数据库名字
    "set_name":"XXX"   #集合名字
}

if __name__ == "__main__":
    cfg_name = "darkent_yolov4_vis2020.cfg"
    cfg_folder_path = "./cfg"

    cfg_path = os.path.join(cfg_folder_path, cfg_name)
    cfg_instance = CFGList(cfg_path)
    section_list, cfg_section, cfg_data= cfg_instance.section_list_function()

    for line_loop in range(len(section_list)):
        if section_list[line_loop] == "MGdb_config":
            settings["ip"] = (cfg_data.get(cfg_section[line_loop], "ip")).split(" ")[0]
            settings["port"] = int((cfg_data.get(cfg_section[line_loop], "port")).split(" ")[0])
            settings["db_name"] = (cfg_data.get(cfg_section[line_loop], "db_name")).split(" ")[0]
            settings["set_name"] = (cfg_data.get(cfg_section[line_loop], "set_name")).split(" ")[0]
            mongo = MyMongoDB(settings)

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