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
conda create -n detectron2 python==3.6.13
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

D:\3rdPartyLib\OpenCV\opencv-4.5.0-vc14_vc15\source   s\samples\dnn 
python tf_text_graph_ssd.py 
--input D:\ModelZoo\ssd_inception_v2_coco_2017_11_17\frozen_inference_graph.pb 
--output D:\ModelZoo\ssd_inception_v2_coco_2017_11_17\Ha.pbtxt 
--config D:\ModelZoo\models-master\research\object_detection\samples\configs\ssd_mobilenet_v1_coco.config

python app.py db init
python app.py db migrate
python app.py db upgrade

python app.py runserver

nvcc --version




cd ./deeplearning-suite/pycharm-professional-2021.1.1/pycharm-2021.1.1/bin
sh pycharm.sh


#文件操作
for i, line in enumerate(open(args.labels).readlines()):	#读取文本每行内容
if osp.exists("") is None:#文件夹不存在创建
	os.makedirs("")
label_files = glob.glob(osp.join(args.input_dir, "*.json"))	#获取文件夹下所有json文件，list
name = os.path.basename("C:/Users/top/PycharmProjects/a_4.py")	#a_4.py
name = os.path.dirname("C:/Users/top/PycharmProjects/a_4.py")	#C:/Users/top/PycharmProjects

#其他
now = datetime.datetime.now()#当前时间




