# <bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>
# ignored regions(0), pedestrian(1), people(2), bicycle(3), car(4), van(5), truck(6), tricycle(7), awning-tricycle(8), bus(9), motor(10), others(11)
import os 
from tqdm import tqdm
from pymongo import MongoClient
from mongodb_process_class import MyMongoDB

settings = {
    "ip":'192.168.100.118',   #ip
    "port":27017,           #端口
    "db_name" : "YYY",    #数据库名字
    "set_name" : "XXX"   #集合名字
}

def file_name(file_dir):   
    # line_data=[]
    for root, dirs, files in os.walk(file_dir):  
        for file_line in tqdm(files):
            file_line_name = file_line
            # dic_delta["file_name"]=file_line
            file_line=os.path.join(root, file_line)
            # print(file_line)
            for line_list in open(file_line, "r"):
                line_data=line_list.split()
                line_data=line_data[0].split(",")
                dic_delta = {"file_name":file_line_name,
                    "bbox_left":int(line_data[0]), "bbox_top":int(line_data[1]), "bbox_width":int(line_data[2]), "bbox_height":int(line_data[3]),
                    "score":int(line_data[4]), "object_category":int(line_data[5]), "truncation":int(line_data[6]), "occlusion":int(line_data[7])}
                mongo.insert_one(dic_delta)
                # mongo.update(dic_delta)
                # print(line_data)


if __name__ == "__main__":
    path_file = "/home/andy/baidunetdiskdownload/VisDrone2020/VisDrone2019-DET-train/annotations"
    # config settings dic
    settings["db_name"]="visdrone_2020"
    settings["set_name"]="VisDrone2019-DET-train"
    mongo = MyMongoDB(settings)
    # mongo.delete_coll("VisDrone2019-DET-train")
    file_name(path_file)

    # data_all = mongo.dbfind_all({"object_category": "4"})
    # for doc in data_all:
    #     print(doc)
    # print("type = ", type(data_all))
    # print(data_all.count)


    # conn = MongoClient(settings["ip"], settings["port"])
    # db = conn["visdrone_2020"]
    # my_set = db["VisDrone2019-DET-train"]
    # my_set.drop()

# name_dict = {'0': 'ignored regions', '1': 'pedestrian', '2': 'people',
#     '3': 'bicycle', '4': 'car', '5': 'van', '6': 'truck',
#     '7': 'tricycle', '8': 'awning-tricycle', '9': 'bus',
#     '10': 'motor', '11': 'others'}