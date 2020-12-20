#!/bin/bash

python3 ./Tools/DCM2NII.py --sess_root ../DeepOpenLungData/INPUTS/DICOM --nifti_root ../DeepOpenLungData/INPUTS/NIfTI --sess_csv ../DeepOpenLungData/INPUTS/SUBINFO/test_dcm.csv


echo "Run step 1 data preprocessing ..."

python3 ./1_preprocess/step1_main.py --sess_csv ../DeepOpenLungData/INPUTS/SUBINFO/test_dcm.csv --prep_root ../DeepOpenLungData/OUTPUTS/temp/prep --ori_root ../DeepOpenLungData/INPUTS/NIfTI

echo " step 1 data preprocess finished !"

echo "Run step 2 nodule detection ... (CPU version, 3 - 4 mins per scan needed)"


python3 ./2_nodule_detection/step2_main.py --sess_csv ../DeepOpenLungData/INPUTS/SUBINFO/test_dcm.csv --bbox_root ../DeepOpenLungData/OUTPUTS/temp/bbox --prep_root ../DeepOpenLungData/OUTPUTS/temp/prep --config ../DeepOpenLungData/config.yaml

echo "step 2 nodule detection finished ! "

echo "Run step 3 feat extract ... "

python3 ./3_feature_extraction/step3_main.py --sess_csv ../DeepOpenLungData/INPUTS/SUBINFO/test_dcm.csv --bbox_root ../DeepOpenLungData/OUTPUTS/temp/bbox --prep_root ../DeepOpenLungData/OUTPUTS/temp/prep --feat_root ../DeepOpenLungData/OUTPUTS/temp/feat --config ../DeepOpenLungData/config.yaml

echo "step 3 feat extract finished ! "

echo "Run step 4 co-predicting ... "

python3 ./4_co_learning/step4_main.py --sess_csv ../DeepOpenLungData/INPUTS/SUBINFO/test_dcm.csv --feat_root ../DeepOpenLungData/OUTPUTS/temp/feat --save_csv_path ../DeepOpenLungData/OUTPUTS/Metrics/CSV/pred_dcm.csv

echo "step 4 co-predicting finished ! "

echo "Run step 5 generating PDF ... "

python3 ./5_create_pdf.py --save_csv_path ../DeepOpenLungData/OUTPUTS/Metrics/CSV/pred_dcm.csv --save_txt_path ../DeepOpenLungData/OUTPUTS/Classification/cls_dcm.txt --save_prep_path ../DeepOpenLungData/OUTPUTS/temp/prep --save_pdf_path ../DeepOpenLungData/OUTPUTS/PDF

echo "all finished "
