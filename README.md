# Convert paddledetection format output -> mmdet format output for ensembling bounding boxes:
- paddle prediction files in folder: evaluations/
- Convert file: scripts/converter.py
- Run cmd: python converter.py --pred_path ../evaluations/{pred_name} --mode coco
