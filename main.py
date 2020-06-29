import os
import numpy as np
import configparser

from src.cfg_process_class import CFGList
from src.Mdb_process_class import MyMongoDB
from src.Mdb_process_tool import tool_TXT2Mdb_Vis, tool_TXT2Mdb_OSU
from src.data_process_class import DataProcess

MGdb_dic = {}
Remote_dit = {}

if __name__ == "__main__":
    cfg_name = "darkent_yolov4_vis2020.cfg"
    cfg_path = os.path.join("./cfg", cfg_name)
    cfg_instance = CFGList(cfg_path)
    section_list= cfg_instance.get_section_list()

    for line_loop in range(len(section_list)):
        if section_list[line_loop] == "MGdb_config":
            MGdb_dic = cfg_instance.get_cfg_dit(line_loop)
            mongo = MyMongoDB(MGdb_dic)

        elif section_list[line_loop] == "MGdb_create":
            MGdb_dic = cfg_instance.get_cfg_dit(line_loop)
            if MGdb_dic["suffix"] == ".txt":
                # mongo.delete_coll(MGdb_dic["set_name"])
                tool_TXT2Mdb_Vis(MGdb_dic["data_folder_patch"], mongo)
            elif MGdb_dic["suffix"] == ".xml":
                pass
            else:
                print("error : cann't open suffix file, see cfg file config")

        elif section_list[line_loop] == "MGdb_createOSU":
            MGdb_dic = cfg_instance.get_cfg_dit(line_loop)
            if MGdb_dic["suffix"] == ".txt":
                # mongo.delete_coll(MGdb_dic["set_name"])
                tool_TXT2Mdb_OSU(MGdb_dic["data_folder_patch"], mongo)
            elif MGdb_dic["suffix"] == ".xml":
                pass
            else:
                print("error : cann't open suffix file, see cfg file config")
            
        # elif section_list[line_loop] == "data_process":
        #     MGdb_dic = cfg_instance.get_cfg_dit(line_loop)
        #     if MGdb_dic["suffix"]  == ".jpg":
        #         DataProcess_SD = DataProcess(MGdb_dic["data_folder_patch"], MGdb_dic["suffix"], line_loop)
        #         SD_matrix = DataProcess_SD.SizeDistribution_jpg()
        #     elif MGdb_dic["suffix"]  == ".xml":
        #         pass
        #     else:
        #         print("error : cann't open suffix file, see cfg file config")

        else:
            print("cfg config is error:", line_loop, "line", section_list[line_loop], "Undefined")

    print(section_list)