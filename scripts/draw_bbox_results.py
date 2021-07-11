import json
import argparse
parser = argparse.ArgumentParser(description='Change config for evaluation')
parser.add_argument('--video_path', type=str, required=True, help='path to your video')
parser.add_argument('--pred_path', type=str, required=True, help='path to your predict files')
args = parser.parse_args()

with open(args.pred_path, "r") as f:
    pred = json.load(f)

print(pred.keys())
pred_out = pred["annotations"]
for s in pred_out:
    print(s)
    break
