Please put the input data into the folder ./model_zoo/DeepOpenLung_nifti_cpu/INPUTS, 

Then, run the following command lines. The output will be saved in ./model_zoo/DeepOpenLung_nifti_cpu/OUTPUTS


>> cd DeepOpenLung
>> export input_dir=./model_zoo/DeepOpenLung_nifti_cpu/INPUTS
>> export output_dir=./model_zoo/DeepOpenLung_nifti_cpu/OUTPUTS
>> export config_dir=./model_zoo/DeepOpenLung_nifti_cpu/Config

>> sudo $config_dir/run_docker.sh ${input_dir} ${output_dir} ${config_dir} ${output_dir}/log


