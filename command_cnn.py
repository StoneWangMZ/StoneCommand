pip install pip --upgrade
pip install tensorflow==2.3.0
conda env remove -n tensorflow-cpu
conda list
conda info --envs
conda activate pytorch-gpu
conda deactivate pytorch-cpu
conda activate detectron2
conda install nb_conda
jupyter notebook
pip install opencv-python
pip install tensorboard
pip install pillow
conda create --name mmlab python=3.6
conda create -n pytorch-gpu python==3.7.6
conda create -n detectron2wang python==3.6.13
conda create -n paddle python==3.6.13
conda create -n wanglei --clone AAA

conda remove -n pytorch-cpu --all
conda remove -n detectron2 --all
conda install torchvision -c pytorch
tensorboard --version
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.1 -c pytorch
pip install torch==1.3.1 torchvision==0.4.2 -f https://download.pytorch.org/whl/torch_stable.html
conda install pytorch==1.3.1 torchvision==0.4.2 cudatoolkit=10.1 -c pytorch
help()
dir()
tensorboard --logdir=Test9_efficientNet/logs
tensorboard --logdir=Pytorch-UNet/runs/May23_13-08-53_10120200200097LR_0.0001_BS_1_SCALE_0.5
torch.cuda.is_available()
python app.py db init
python app.py db migrate
python app.py db upgrade
python app.py runserver
nvcc --version


sudo cp cuda/targets/ppc64le-linux/include/cudnn.h    /usr/local/cuda-11.0/include
sudo cp cuda/targets/ppc64le-linux/lib/libcudnn*    /usr/local/cuda-11.0/lib64
sudo chmod a+r /usr/local/cuda-11.0/include/cudnn.h   /usr/local/cuda-11.0/lib64/libcudnn*

sudo ln -s /home/haoluo/Downloads/cuda/lib64/libcudnn.so.7.6.4 libcudnn.so
sudo ln -s /home/haoluo/anaconda3/lib/libcublas.so.10.2.1.243 libcublas.so
sudo ln -s /home/wang/deeplearning-suite/cuda/targets/ppc64le-linux/lib/libcudnn.so.8.0.2 libcudnn.so
sudo ln -s /home/haoluo/anaconda3/lib/libcublas.so.10.2.1.243 libcublas.so












