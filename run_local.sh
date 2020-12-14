#!/bin/bash



echo "Run step 1 data preprocessing ..."

python3 ./1_preprocess/step1_main.py --sess_csv ${SPLIT_CSV} --prep_root ${PREP_ROOT} --ori_root ${ORI_ROOT} 

echo " step 1 data preprocess finished !"

echo "Run step 2 nodule detection ... (CPU version, 3 - 4 mins per scan needed)"


python3 ./2_nodule_detection/step2_main.py --sess_csv ../DeepOpenLungData/INPUTS/SUBINFO/test.csv --bbox_root ../DeepOpenLungData/OUTPUTS/temp/bbox --prep_root ../DeepOpenLungData/OUTPUTS/temp/prep --config ../DeepOpenLungData/config.yaml

echo "step 2 nodule detection finished ! "

echo "Run step 3 feat extract ... "

python3 ./3_feature_extraction/step3_main.py --sess_csv ../DeepOpenLungData/INPUTS/SUBINFO/test.csv --bbox_root ../DeepOpenLungData/OUTPUTS/temp/bbox --prep_root ../DeepOpenLungData/OUTPUTS/temp/prep --feat_root ../DeepOpenLungData/OUTPUTS/temp/feat --config ../DeepOpenLungData/config.yaml

echo "step 3 feat extract finished ! "

echo "Run step 4 co-predicting ... "

python3 ./4_co_learning/step4_main.py --sess_csv ${SPLIT_CSV} --feat_root ${FEAT_ROOT} --save_csv_path ${PRED_CSV}

echo "step 4 co-predicting finished ! "

echo "Run step 5 generating PDF ... "

python3 ./5_create_pdf.py --save_csv_path ${PRED_CSV} --save_txt_path ${CLS_TXT} --save_prep_path ${PREP_ROOT} --save_pdf_path ${PDF_ROOT}

echo "all finished "
