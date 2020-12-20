import torch
import numpy as np
from torch.utils.data import DataLoader
from torch import optim
from torch.autograd import Variable
from importlib import import_module
from data_classifier import DataBowl3Classifier
import argparse
import pandas as pd
import yaml

from cls_config import config as config2

parser = argparse.ArgumentParser()

parser.add_argument('--sess_csv', type=str, default='./test.csv',
                    help='sessions want to be tested')
parser.add_argument('--prep_root', type=str, default='/nfs/masi/gaor2/tmp/justtest',
                    help='the root for save preprocessed data')
parser.add_argument('--bbox_root', type=str, default='/nfs/masi/gaor2/tmp/justtest',
                    help='the root of original data')
parser.add_argument('--feat_root', type=str, default='/nfs/masi/gaor2/tmp/justtest',
                    help='the root of original data')
parser.add_argument('--config', type=str, default='../config.yaml',
                    help='the root of original data')

args = parser.parse_args()

f = open(args.config, 'r').read()
cfig = yaml.load(f)
config2 = cfig['cls']


casemodel = import_module('net_classifier')
casenet = casemodel.CaseNet(topk=5)

# load_state_dict

config2 = casemodel.config
state_dict = torch.load('./3_feature_extraction/classifier_state_dictpy3.ckpt')

model_dict = casenet.state_dict()
pretrained_dict = {k: v for k, v in state_dict.items() if k in model_dict}

casenet.load_state_dict(state_dict)
casenet = casenet #.cuda()

config2['bboxpath'] = args.bbox_root
config2['datadir'] = args.prep_root
config2['feat128_root'] = args.feat_root


sess_splits = pd.read_csv(args.sess_csv)['exam_id'].tolist()
testsplit = sess_splits

def test_casenet(model,testset):
    data_loader = DataLoader(
        testset,
        batch_size = 1,
        shuffle = False,
        num_workers = 4,
        pin_memory=False)
    
    model.eval()
    predlist = []
    device = torch.device('cuda' if torch.cuda.is_available() and cfig['cls']['gpu'] else 'cpu')
    
    for i,(x,coord, subj_name) in enumerate(data_loader):
        print (i, subj_name[0])   
        coord = Variable(coord).to(device) #.cuda()
        x = Variable(x).to(device) #.cuda()
        model = model.to(device)
        nodulePred,casePred, feat128, feat64 = model(x,coord)
        predlist.append(casePred.data.cpu().numpy())
        #print (out.data.cpu().numpy().shape, out[0].data.cpu().numpy().shape)
        fname128 = config2['feat128_root'] + '/' + subj_name[0] + '.npy'

        np.save(fname128, feat128.cpu().data.numpy())

    predlist = np.concatenate(predlist)
    return predlist    



dataset = DataBowl3Classifier(testsplit, config2, phase = 'test')
predlist = test_casenet(casenet,dataset).T
#print (predlist)