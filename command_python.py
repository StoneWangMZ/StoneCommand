#PIL，与np互相转换
np_img = np.zeros([480, 640], dtype=np.uint8)
pil_img = PIL.Image.fromarray(np_img) #np>PIL
np_img = np.array(pil_img, dtype=np.uint8) #PIL>np
#PIL，图像的格式转换，如png>JPEG
f = io.BytesIO()
pil_img.save(f, format="JPEG")
f.seek(0)
pil_img = f.read()
#PIL，图像操作
pil_img.crop([min_x, min_y, max_x, max_y])
#opencv
np.array(pil_img, dtype=np.uint8)
#获取文件夹下所有文件路径c
file_lists = glob.glob(file_path) 
#文件读取与保存，保存Json文件
json.dump(data, open(filename, "w", encoding='utf-8'), ensure_ascii=False, indent=2)
#文件读取与保存，写入文本
json = json.load(open(json_path, 'r', encoding='utf-8'))
with open(file_path, "w") as f:
    f.write(datetime.now().strftime('%Y-%m-%d %H:%m:%S')) #获取当前时间
#关于os.path   https://www.runoob.com/python/python-os-path.html    https://www.cnblogs.com/wuxie1989/p/5623435.html
os.makedirs(image_dir, exist_ok=True)
os.path.join(jsonPath, "*.json")
file_name = os.path.basename(file_name)
files = os.listdir(parent_dir)  # 获取parent_dir下的所有文件名
os.path.isdir(file_path):
os.path.exists(path_predict):
os.unlink(path) #删除文件
os.getcwd() #返回当前工作目录
#图片显示
import matplotlib.pyplot as plt
img = cv2.imread(img_path)#cv2
img = plt.imread(img_path)#plt
img = Image.open(img_path)#PIL
ImageDraw.Draw(img).point(tuple_points, fill=(255,0,0)) #tuple_points=[(0,0),(0,0)]
plt.subplot(1, 1, 1)
plt.title('PIL')
plt.imshow(img)
plt.show()#show
#图片格式转换
image_array = np.asarray(image_PIL) # PIL转换为NumPy
image_PIL = Image.fromarray(image_array.astype('uint8')) # NumPy转换为PIL
image_tensor = torch.from_numpy(image_array) # NumPy转换为Tensor
image_array = image_tensor.numpy() # Tensor转换为NumPy
#array与list格式转换，如点集
array_points = np.array(list_points)
list_points = array_points.tolist()
# dict，遍历
my_dict = {"train": (TRAIN_PATH, TRAIN_JSON),"val": (VAL_PATH, VAL_JSON),}
for key, (image, json) in my_dict.items():
# cv2
img = cv2.imread(path_image)
cv2.imwrite(os.path.join(vis_path, file_name), vis_output.get_image()[:, :, ::-1])
cv2.imshow('show', vis.get_image()[:, :, ::-1])
# 文件中执行命令行
_,sample_num = subprocess.getstatusoutput("ls /data/myue/SXT_detect/coco/train2017/ -l | grep 'jpg' | wc -l") 
# 字符串format
"{}_predict_done.txt".format(model_id)
'鸭舌标签 {0} 与 上盖标签 {1} 不一致'.format(ducklabelSN, lidlabelSN)

# 关于时间日期
now = datetime.datetime.now()#当前时间
# 指定训练的GPU
CUDA_VISIBLE_DEVICES=3,2,1,0
# pandas,
import pandas as pd
data.append([sn, pmwg, pmwg_detail])
df = pd.DataFrame(data, columns=['SN', 'PMWG', 'PMWG_DETAIL'])
df.to_excel(sn_excel)
df = pd.read_excel("1.xls")
df_qj = df[df['PMWG'].str.contains('缺角') == True] # 筛选出'PMWG'这列中包含'缺角'的所有行
df_sn = df[df['SN'].isin(["111","222"])] # 筛选出'SN'这列中包含列表["111","222"]中值的所有行
for index, row in df.iterrows():
df['SN'] = df.filename.apply(lambda x: parse_property(x)['SN']) #获取列中具有特定规律的值
# Temp
for index in range(len(points)):
import sys
print(sys.path)




















