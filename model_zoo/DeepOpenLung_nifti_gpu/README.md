Please put the input data into the folder ./model_zoo/DeepOpenLung_nifti_gpu/input_dir. For example, the nifti file should be placed as ./model_zoo/DeepOpenLung_nifti_gpu/input_dir/NIfTI/{EXAM_ID}.nii.gz

Then, run the following command lines. The output will be saved in ./model_zoo/DeepOpenLung_nifti_gpu/output_dir

Example can be downloaded from https://vanderbilt.box.com/s/6h6388kw6h4jbjogd8yk1xqp9eotd3tv



> cd DeepOpenLung

> export input_dir=./model_zoo/DeepOpenLung_nifti_gpu/input_dir

> export output_dir=./model_zoo/DeepOpenLung_nifti_gpu/output_dir

> export config_dir=./model_zoo/DeepOpenLung_nifti_gpu/config_dir

> sudo $config_dir/run_docker.sh ${input_dir} ${output_dir} ${config_dir} ${output_dir}/log


