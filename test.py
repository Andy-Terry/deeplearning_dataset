import os
import configparser
import numpy as np

MDTB_flag = ["MGdb_config", "model_config"]

CFG_Dit = {"data_folder_patch":"XXX", "Remote_flag":0,
    "ip":'000.000.000.000', "port":00000,
    "db_name":"XXX", "set_name":"XXX",
    "suffix":"XXX"
}

B = {}

B = CFG_Dit.copy()

B["data_folder_patch"] = "MiMi"

print(B)

print(CFG_Dit)

B = CFG_Dit.copy()

print(CFG_Dit)



