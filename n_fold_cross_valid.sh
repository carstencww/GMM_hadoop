#!/bin/bash
NumOfP=10

iter=$((NumOfP-1))
n="pca_${NumOfP}part"
for j in `seq 0 1 $iter`; do
i="-$j"
out="$j-${NumOfP}_paras_result.txt"
rm ./data/image_train.txt
rm ./data/image_test.txt
rm ./data/label_test.txt
rm ./data/label_train.txt

ls ./data/$n | grep 'image' | grep -v -e "$i" | while read filename
do
cat ./data/$n/$filename >> ./data/image_train.txt
done

ls ./data/$n | grep 'image' | grep -e "$i" | while read filename
do
cp ./data/$n/$filename ./data/image_test.txt
done

hadoop dfs -copyFromLocal -f ./data/image_train.txt input_GMM/
python ./random_init.py
./GMM_run.sh

cp ./paras_result.txt ./$out

done



