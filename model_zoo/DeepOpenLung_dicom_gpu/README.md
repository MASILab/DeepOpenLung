Please put the input data into the folder ./model_zoo/DeepOpenLung_dicom_gpu/INPUTS, 

Then, run the following command lines. The output will be saved in ./model_zoo/DeepOpenLung_dicom_gpu/OUTPUTS


>> cd DeepOpenLung
>> export input_dir=./model_zoo/DeepOpenLung_dicom_gpu/INPUTS
>> export output_dir=./model_zoo/DeepOpenLung_dicom_gpu/OUTPUTS
>> export config_dir=./model_zoo/DeepOpenLung_dicom_gpu/Config

>> sudo $config_dir/run_docker.sh ${input_dir} ${output_dir} ${config_dir} ${output_dir}/log
