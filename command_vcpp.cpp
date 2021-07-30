/*vector相关，************************/
//计算vector中符合要求的数目，可以是正则表达式或函数，https://blog.csdn.net/dark_cy/article/details/88903828
int nNum = 1;
vector<int> vecValue{0,2,4,6,8};
int nCount = count_if(vecValue.begin(), vecValue.end(), [nNum](int val) {return nNum + 2 < val; });//等于3

弧度=角度*pi/180

for (map<int, vector<cv::Point>>::iterator it = labelPtMap.begin(); it != labelPtMap.end(); it++)