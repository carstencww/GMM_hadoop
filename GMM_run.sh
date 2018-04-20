#!/bin/bash

OUT_FILE=/user/ChanCarsten/out_GMM
IN_FILE=/user/ChanCarsten/input_GMM/image_train.txt
GMM () {
hadoop dfs -rm -R $OUT_FILE
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapred.map.tasks=10 \
-D mapred.reduce.tasks=10 \
-file $PWD/train_paras.txt \
-file $PWD/map_GMM.py -mapper map_GMM.py \
-file $PWD/red_GMM.py -reducer red_GMM.py \
-input $IN_FILE \
-output $OUT_FILE
hadoop fs -getmerge $OUT_FILE ./supp_result.txt

hadoop dfs -rm -R $OUT_FILE
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapred.map.tasks=50 \
-D mapred.reduce.tasks=10 \
-file $PWD/train_paras.txt \
-file $PWD/supp_result.txt \
-file $PWD/map_GMM1.py -mapper map_GMM1.py \
-file $PWD/red_GMM1.py -reducer red_GMM1.py \
-input $IN_FILE \
-output $OUT_FILE
hadoop fs -getmerge $OUT_FILE ./paras_result.txt

}
echo $PWD
GMM
converging=( $(./check_converge.py) )
while [ ${converging[0]} = 1 ]; do
mv paras_result.txt train_paras.txt
echo ${converging[1]} >> log.txt
cp ./train_paras.txt ./result/paras_result.txt
cd ./result
python ./validate.py | tail -n3 | head -n1 >> ../log.txt
cd ../
GMM
converging=( $(./check_converge.py) )
done











