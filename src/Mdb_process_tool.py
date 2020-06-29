import os
import re
import numpy as np

from tqdm import tqdm
from pymongo import MongoClient
from src.Mdb_process_class import MyMongoDB
from src.cfg_process_class import CFGList
from src.data_process_class import DataProcess

dic_delta = {"file_name":"XXX",
    "bbox_left":0, "bbox_top":0, "bbox_width":0, "bbox_height":0,
    "score":0, "object_category":0, "truncation":0, "occlusion":0
}

def tool_TXT2Mdb_Vis(file_dir, mongo):  
    for root, dirs, files in os.walk(file_dir):  
        for file_line in tqdm(files):
            file_line_name = file_line
            file_line=os.path.join(root, file_line)
            for line_list in open(file_line, "r"):
                line_data=line_list.split()
                line_data=line_data[0].split(",")
                dic_delta = {"file_name":file_line_name,
                    "bbox_left":int(line_data[0]), "bbox_top":int(line_data[1]), "bbox_width":int(line_data[2]), "bbox_height":int(line_data[3]),
                    "score":int(line_data[4]), "object_category":int(line_data[5]), "truncation":int(line_data[6]), "occlusion":int(line_data[7])}
                mongo.insert_one(dic_delta)
    
    print("tool_TXT2Mdb_Vis is running completed")

def tool_TXT2Mdb_OSU(file_dir, mongo):  
    for root, dirs, files in os.walk(file_dir):  
        for folder in tqdm(dirs):
            file_name = os.path.join(root, folder, "groundTruth.txt")
            file_line_name = folder + "_"
            for line_list in open(file_name, "r"):
                line_data=line_list.split(" ")
                if re.match("img_", line_data[0]):  # 在起始位置匹配
                    file_line_DN = file_line_name + line_data[0]
                    for i in range(int(line_data[1])):
                        bbox_left_data = int((line_data[i*4 + 2])[1:])
                        bbox_top_data = int(line_data[i*4 + 3])
                        bbox_width_data = int(line_data[i*4 + 4]) - bbox_left_data
                        bbox_height_data = int((line_data[i*4 + 5])[:-1]) - bbox_top_data
                        dic_delta = {"file_name":file_line_DN,
                            "bbox_left":bbox_left_data, "bbox_top":bbox_top_data, "bbox_width":bbox_width_data, "bbox_height":bbox_height_data,
                            "score":1, "object_category":"person", "truncation":0, "occlusion":0}
                        mongo.insert_one(dic_delta)
        break

    print("tool_TXT2Mdb_OSU is running completed")
