import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--sess_root', type=str, default='./DICOM',
                        help='sessions want to be tested')
    
    parser.add_argument('--nifti_root', type=str, default='./nifti_root',
                        help='the root of original data')
    args = parser.parse_args()
    
    sess_list = os.listdir(args.sess_root)
#    for sess in sess_list:
    print ('./Tools/dcm2niix -m y -z y -o ' + args.nifti_root + ' -f dcm_example ' + args.sess_root)
    os.system('./Tools/dcm2niix -m y -z y -o ' + args.nifti_root + ' -f dcm_example ' + args.sess_root)        

'''
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--sess_root', type=str, default='./DICOM',
                        help='sessions want to be tested')
    
    parser.add_argument('--nifti_root', type=str, default='./nifti_root',
                        help='the root of original data')
    args = parser.parse_args()
    
    sess_list = os.listdir(args.sess_root)
    for sess in sess_list:
        os.system('./Tools/dcm2niix -m y -z y -o ' + args.nifti_root + ' -f ' + sess + ' ' + args.sess_root + '/' + sess + '/DICOM')
    
# python Tools/DCM2NII.py --sess_root ../DeepOpenLungData/INPUTS/FOR_DCM/ --nifti_root ../DeepOpenLungData/INPUTS/NIfTI
'''
