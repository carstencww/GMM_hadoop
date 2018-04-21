#!/bin/bash
NumOfP=5

iter=$((NumOfP-1))
n="pca_${NumOfP}part"

for j in `seq 0 1 $iter`; do
i="-$j"
out="$j-${NumOfP}_paras_result.txt"
vali="$j-${NumOfP}_eval.txt"
rm ./data/image_test.txt
rm ./data/label_test.txt

ls ./data/$n | grep 'label' | grep -e "$i" | while read filename
do
cp ./data/$n/$filename ./data/label_test.txt
done
ls ./data/$n | grep 'image' | grep -e "$i" | while read filename
do
cp ./data/$n/$filename ./data/image_test.txt
done

cp ./result/$out ./result/paras_result.txt
cd ./result
echo $out > $vali
python ./validate.py >> ./$vali
cd ..
rm ./result/paras_result.txt
done




































