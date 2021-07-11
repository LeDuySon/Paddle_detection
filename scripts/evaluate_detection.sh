
configs=$1
echo "SETUP CONFIG FOR EVALUATION"
python scripts/setup_config.py --config_path $1 --data_path ../datasets/vtx_coco_detection.yml

echo "Wait 3 seconds"
sleep 3

echo "<-------------------START EVALUATE-------------------------------->"
export CUDA_VISIBLE_DEVICES=0

#model_weights=$2
arrIN=(${configs//// })
echo ${arrIN[2]} 
config_name=(${arrIN[2]//./ })
name=${config_name[0]}
echo "model name: ${name}"
model_weights="https://paddledet.bj.bcebos.com/models/${name}.pdparams"
echo "Start evaluate ${name}"
python -u tools/eval.py -c $configs -o weights=$model_weights --output_eval evaluations/ 

sleep 5
echo "Finish evaluate ${name}"

echo "Change output file name"

cd evaluations/
mv bbox.json bbox_${name}.json 
cd ..

echo "[FINISH]"
