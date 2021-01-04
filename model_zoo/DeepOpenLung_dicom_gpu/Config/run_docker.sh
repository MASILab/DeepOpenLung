LOCAL_INPUTS_PATH=$(readlink -f ${1-/INPUTS}) #/INPUTS
LOCAL_OUTPUTS_PATH=$(readlink -f ${2-/OUTPUTS}) # /OUTPUTS
LCOAL_CONFIG_PATH=$(readlink -f ${3-/config.yaml}) # /config.yaml
LOCAL_LOG_PATH=$(readlink -f ${4-/LOG}) # log file

exec > ${LOG_PATH}

sudo nvidia-docker run -u root -v ${LOCAL_INPUTS_PATH}:/INPUTS/ -v ${LOCAL_OUTPUTS_PATH}:/OUTPUTS/ -v ${LCOAL_CONFIG_PATH}/config.yaml:/config.yaml -v ${LOCAL_LOG_PATH}:/LOG rg15/deeplunggpu:0.4 sh run_all_DICOM.sh /INPUTS /OUTPUTS /config.yaml /LOG
