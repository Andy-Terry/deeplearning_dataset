import sys
from pymongo import MongoClient

# settings = {
#     "ip":'192.168.100.118',
#     "port":27017,
#     "db_name" : "vis2020",
#     "set_name" : "train_dataset"
# }

class MyMongoDB(object):
# class MyMongoDB:
    def __init__(self, settings):
        try:
            self.conn = MongoClient(settings["ip"],settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert_one(self, dic):
        self.my_set.insert_one(dic)

    def update(self, dic, newdic):
        self.my_set.update(dic, newdic)
        print("update...")

    # delete datasets
    def delete_coll(self, coll_name):
        self.my_set = self.db[coll_name]
        self.my_set.drop()

    # delete data
    def delete_data(self, dic):
        self.my_set.remove(dic)

    # find one data
    def dbfind_one(self, dic):
        data_one = self.my_set.find_one(dic)
        return data_one

    # find all data
    def dbfind_all(self,dic):
        data_all = self.my_set.find(dic)
        return data_all

# def main():
#     dic={"name":"zhangsan","age":18}
#     mongo = MyMongoDB(settings)
#     mongo.insert_one(dic)
#     dic={"name":"zhangsan_1","age":18}
#     mongo.insert_one(dic)
#     # mongo.dbfind({"name":"zhangsan"})
#     # mongo.update({"name":"zhangsan"},{"$set":{"age":"25"}})
#     # mongo.dbfind({"name":"zhangsan"})
#     # mongo.delete({"name":"zhangsan"})
#     # mongo.dbfind({"name":"zhangsan"})

# if __name__ == "__main__":
#     main()