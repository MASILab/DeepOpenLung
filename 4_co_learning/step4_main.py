import numpy as np 
import torch 
import torch.nn as nn 
import pandas as pd
from model import *
import argparse
import pdb

parser = argparse.ArgumentParser()

parser.add_argument('--sess_csv', type=str, default='100004time1999',
                    help='sessions want to be tested')
parser.add_argument('--feat_root', type=str, default='/nfs/masi/gaor2/tmp/justtest/bbox',
                    help='the root for save feat data')
parser.add_argument('--save_csv_path', type=str, default='/nfs/masi/gaor2/tmp/justtest/prep',
                    help='the root for save result data')

args = parser.parse_args()

need_factor = ['with_image', 'with_marker',  'age',  'education',  'bmi',  'phist', 'fhist', 'smo_status', 'quit_time', 'pkyr', 'plco', 'kaggle_cancer']

sess_mark_dict = {}

df = pd.read_csv(args.sess_csv)


sess_splits = df['exam_id'].tolist()
testsplit = sess_splits

for i, item in df.iterrows():
    test_biomarker = np.zeros(12).astype('float32')
    for j in range(len(need_factor)):
        test_biomarker[j] = item[need_factor[j]]
    sess_mark_dict[item['exam_id']] = test_biomarker

data_path = args.feat_root


model = MultipathModelBL(1)

model_pth = './4_co_learning/pretrain.pth'

model.load_state_dict(torch.load(model_pth, map_location=lambda storage, location: storage))
#model.load_state_dict(torch.load(model_pth))

patient_list = []
exam_list = []
pred_list = []

for i, item in df.iterrows():
    pid = item['patient_id']
    sess_id = item['exam_id']
    patient_list.append(pid)
    exam_list.append(sess_id)
    test_biomarker = sess_mark_dict[sess_id]
    
    test_imgfeat = np.load(data_path + '/' + sess_id + '.npy')
    test_biomarker = torch.from_numpy(test_biomarker).unsqueeze(0)
    test_imgfeat = torch.from_numpy(test_imgfeat).unsqueeze(0)
    imgPred, clicPred, bothImgPred, bothClicPred, bothPred = model(test_imgfeat, test_biomarker, test_imgfeat, test_biomarker)
    pred_list += list(bothPred.data.cpu().numpy())
    

desc_list = ["Based on the image and clinical elements, the likelihood of lung cancer in this patient is {:.4f}".format(prob) for prob in pred_list]
pred_list = ['{:.4f}'.format(prob) for prob in pred_list]
data = pd.DataFrame()
data['patient_id'] = patient_list
data['exam_id'] = exam_list
data['pred'] = pred_list
data['desciption'] = desc_list

data.to_csv(args.save_csv_path, index = False)



