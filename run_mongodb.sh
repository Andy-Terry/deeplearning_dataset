echo "welcome to run_mongodb"

cd /usr/local/mongodb/bin/

pwd

db_path="/media/zhizhoukeji/EE68A7C268A787C3/mongodb_data/db"
log_path="/media/zhizhoukeji/EE68A7C268A787C3/mongodb_data/log.log"
IP=0.0.0.0
PN=27017
#fork=true #以守护程序的方式启用，即在后台运行

./mongod --dbpath=$db_path --logpath=$log_path --bind_ip=$IP --port=$PN --fork

# close mongodb 
# ps -ef | grep mongo   # find mongo
# sudo kill 74316(pid) # close mongo
