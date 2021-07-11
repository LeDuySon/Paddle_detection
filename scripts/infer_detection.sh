 
n tools/infer.py -c configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.yml \
	                    --infer_img=demo/000000570688.jpg \
			                        --output_dir=infer_output/ \
						                    --draw_threshold=0.5 \
								                        -o weights=output/faster_rcnn_r50_fpn_1x_coco/model_final \
											                    --use_vdl=Ture
