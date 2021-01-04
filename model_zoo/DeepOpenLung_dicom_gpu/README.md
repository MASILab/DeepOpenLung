Please put the input data into the folder ./model_zoo/DeepOpenLung_dicom_gpu/input_dir. For example, the DICOM files should be placed as ./model_zoo/DeepOpenLung_dicom_gpu/input_dir/DICOM/{EXAM_ID}/*.dcm

Then, run the following command lines. The output will be saved in ./model_zoo/DeepOpenLung_dicom_gpu/output_dir


> cd DeepOpenLung

> export input_dir=./model_zoo/DeepOpenLung_dicom_gpu/input_dir

> export output_dir=./model_zoo/DeepOpenLung_dicom_gpu/output_dir

> export config_dir=./model_zoo/DeepOpenLung_dicom_gpu/config_dir

> sudo $config_dir/run_docker.sh ${input_dir} ${output_dir} ${config_dir} ${output_dir}/log
