import json
import os 
import argparse
from collections import defaultdict
parser = argparse.ArgumentParser(description='Change config for evaluation')
parser.add_argument('--pred_path', type=str, required=True,
                            help='path to prediction file')

parser.add_argument('--format', type=str , help='format dataset that u want to convert', default="coco")
args = parser.parse_args()

SAVE_FOLDER = "../evaluations"
idx2name = {1: "person"}

def read_json(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def write_file(data, file):
    print("Write data to ", file)
    with open(file, "wt") as f:
        for sp in data:
            cls_name = idx2name[int(sp["category_id"])]
            xmin, ymin, xmax, ymax = list(map(str, xywh_to_xyxy(sp["bbox"])))
            score = str(sp["score"])
            line = cls_name + " " + score + " " + xmin + " " + ymin + " " + xmax + " " + ymax + "\n"
            f.write(line)

def xywh_to_xyxy(coord):
    x, y, w, h = coord
    xmin, ymin, xmax, ymax = x, y, x+w, y+h
    return [xmin, ymin, xmax, ymax]


def paddle_to_mmdet(file):
    """
      Convert paddle output format to mmdet format
      [{}] -> cls conf x y w h
    """

    data = read_json(file)
    file_name = file.split("/")[-1].split(".")[0]
    save_path = os.path.join(SAVE_FOLDER, file_name)
    if(not os.path.exists(save_path)):
        os.mkdir(save_path)
    group_frame = defaultdict(list)
    for i in data:
        frame_id = i["image_id"]
        group_frame[int(frame_id)].append(i)
    

    max_pref = 6
    # get value and write to txt file, each file correspond to 1 frame
    for frame_id, val in group_frame.items():
        frame_len = len(str(frame_id))
        frame_name = "frame_" + "0" * (6 - frame_len) + str(frame_id) + ".txt"
        save_file = os.path.join(save_path, frame_name)
        write_file(val, save_file)
        if(frame_id == 10):
            break

if __name__ == "__main__":
    print(paddle_to_mmdet(args.pred_path))
