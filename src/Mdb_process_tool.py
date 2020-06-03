import os
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

def tool_TXT2Mdb(file_dir, mongo):  
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
    
    print("tool_TXT2Mdb is running completed")
