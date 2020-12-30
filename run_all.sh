#!/bin/bash

IN_ROOT=$(readlink -f ${1-/INPUTS}) #/INPUTS
OUT_ROOT=$(readlink -f ${2-/OUTPUTS}) # /OUTPUTS
CONFIG_PATH=$(readlink -f ${3-/config.yaml}) # /config.yaml

PREP_ROOT=${OUT_ROOT}/temp/prep
BBOX_ROOT=${OUT_ROOT}/temp/bbox
FEAT_ROOT=${OUT_ROOT}/temp/feat
PRED_CSV=${OUT_ROOT}/Metrics/CSV/pred.csv
CLS_TXT=${OUT_ROOT}/Classification/cls.txt
PDF_ROOT=${OUT_ROOT}/PDF


mkdir -p ${OUT_ROOT}/temp
mkdir -p ${OUT_ROOT}/Classification
mkdir -p ${OUT_ROOT}/Metrics
mkdir -p ${OUT_ROOT}/Metrics/CSV
mkdir -p ${PDF_ROOT}
mkdir -p ${PREP_ROOT}
mkdir -p ${BBOX_ROOT}
mkdir -p ${FEAT_ROOT}

ORI_ROOT=${IN_ROOT}/NIfTI
SPLIT_CSV=${IN_ROOT}/SUBINFO/test_nifti.csv

echo "Run step 1 data preprocessing ..."

python3 ./1_preprocess/step1_main.py --sess_csv ${SPLIT_CSV} --prep_root ${PREP_ROOT} --ori_root ${ORI_ROOT} 

echo " step 1 data preprocess finished !"

echo "Run step 2 nodule detection ... (CPU version, 3 - 4 mins per scan needed)"

python3 ./2_nodule_detection/step2_main.py --sess_csv ${SPLIT_CSV} --bbox_root ${BBOX_ROOT} --prep_root ${PREP_ROOT} --config ${CONFIG_PATH}

echo "step 2 nodule detection finished ! "

echo "Run step 3 feat extract ... "

python3 ./3_feature_extraction/step3_main.py --sess_csv ${SPLIT_CSV} --bbox_root ${BBOX_ROOT} --prep_root ${PREP_ROOT} --feat_root ${FEAT_ROOT} --config ${CONFIG_PATH}

echo "step 3 feat extract finished ! "

echo "Run step 4 co-predicting ... "

python3 ./4_co_learning/step4_main.py --sess_csv ${SPLIT_CSV} --feat_root ${FEAT_ROOT} --save_csv_path ${PRED_CSV}

echo "step 4 co-predicting finished ! "

echo "Run step 5 generating PDF ... "

python3 ./5_create_pdf.py --save_csv_path ${PRED_CSV} --save_txt_path ${CLS_TXT} --save_prep_path ${PREP_ROOT} --save_pdf_path ${PDF_ROOT}

echo "all finished "
