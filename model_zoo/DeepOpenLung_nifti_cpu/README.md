Please put the input data into the folder ./model_zoo/DeepOpenLung_nifti_cpu/input_dir. For example, the nifti file should be placed as ./model_zoo/DeepOpenLung_nifti_cpu/input_dir/NIfTI/{EXAM_ID}.nii.gz


> cd DeepOpenLung

> export input_dir=./model_zoo/DeepOpenLung_nifti_cpu/input_dir

> export output_dir=./model_zoo/DeepOpenLung_nifti_cpu/output_dir

> export config_dir=./model_zoo/DeepOpenLung_nifti_cpu/config_dir

> sudo $config_dir/run_docker.sh ${input_dir} ${output_dir} ${config_dir} ${output_dir}/log


