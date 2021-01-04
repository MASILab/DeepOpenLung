# https://github.com/anibali/docker-pytorch/blob/master/dockerfiles/1.5.0-cuda10.2-ubuntu18.04/Dockerfile

FROM nvidia/cuda:10.2-base-ubuntu18.04

# Install some basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
 && rm -rf /var/lib/apt/lists/*

# Create a working directory
RUN mkdir /app
WORKDIR /app

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /app
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user

# All users can use /home/user as their home directory
ENV HOME=/home/user
RUN chmod 777 /home/user

# Install Miniconda and Python 3.8
ENV CONDA_AUTO_UPDATE_CONDA=false
ENV PATH=/home/user/miniconda/bin:$PATH
RUN curl -sLo ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-py38_4.8.2-Linux-x86_64.sh 
RUN chmod +x ~/miniconda.sh 
RUN ~/miniconda.sh -b -p ~/miniconda 
RUN rm ~/miniconda.sh 
RUN conda install -y python==3.8.1 
RUN conda clean -ya

# CUDA 10.2-specific steps
RUN conda install -y -c pytorch \
    cudatoolkit=10.2 \
    "pytorch=1.5.0=py3.8_cuda10.2.89_cudnn7.6.5_0" \
    "torchvision=0.6.0=py38_cu102" \
     && conda clean -ya

RUN conda install pandas
RUN conda install numpy
RUN conda install pyyaml
RUN conda install -c anaconda scipy
RUN conda install -c conda-forge nibabel
RUN conda install -c anaconda scikit-image

RUN pip install --upgrade pip && \
    pip install --no-cache-dir pypdf2 pymupdf
    
COPY . .

# Set the default command to python3
CMD ["python3"]