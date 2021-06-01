**************************************************************************************************
一.python文件说明
1.baseline for test：处理test的基准时间数据——》baseline/baselineO2_dsyr2k.txt
2.features for train and valiation:生成和训练集验证集行数一致的手工提取的特征——》features/dsyr2k_featrues.txt
2.features for test:生成和测试集行数一致的手工提取的特征——》features/dsyr2k_test_featrues.txt
3.totalfeatures for test 32:将原始数据除分块大小这一特征外进行标准化处理，然后将其与对应的2中的手工特征进行拼接，形成用于测试的数据；
3.totalfeatures for test:将原始数据进行标准化处理，然后将其与对应的2中的手工特征进行拼接，形成用于测试的数据；
3.totalfeatrues for train and valiation:将原始数据进行标准化处理，然后将其与对应的2中的手工特征进行拼接，形成用于训练和验证的数据；
**************************************************************************************************
二.文件级文件夹命名规则：
baseline/
	sourceCodeOutb.txt为dsyr2k的测试集的基准（未分块）时间的原始数据
	baselineO2_dsyr2k.txt是经1.baseline for test处理后的
data_8/
	sourceCodeOut(32000)为dsyr2k的训练集和验证集的原始数据
features/
	dsyr2k_train&valiation_featrues.txt
	dsyr2k_test_featrues.txt
test/
	test_dsyr2k.txt测试集的原始数据
totalfeatures/
	dsyr2k_test_totalfeatures.txt		
	dsyr2k_test_totalfeatures_32.txt	
	dsyr2k_train&valiation_totalfeatures.txt
**************************************************************************************************
三.将处理完的文件进行拷贝
（1）totalfeatures/
	①dsyr2k_test_totalfeatures.txt
	②dsyr2k_test_totalfeatures_32.txt
	③dsyr2k_train&valiation_totalfeatures.txt
（2）baseline/
	①baselineO2_dsyr2k.txt
拷贝到《模型搭建》对应目录
*****************************************************************************************
四.
dsyr2k_features = [1,0,0,0,1,3,0,2,1,0,0,2,1,2,0,1,0,0,4,1,0,0,1]
dsyrk_features = [1,0,0,0,1,2,0,1,1,0,0,1,1,1,0,1,0,0,2,1,0,0,1]
gemm_features = [1,0,1,0,0,2,0,1,1,0,0,1,1,1,0,0,1,0,2,1,0,1,0]
matmul_features = [1,0,1,0,0,2,0,1,1,0,0,1,1,1,0,0,1,0,2,1,0,1,0]
tmm_features = [0,1,0,1,0,2,0,1,1,0,0,1,1,1,0,0,1,0,2,1,0,1,0]
trmm_features = [1,0,0,1,0,2,0,1,1,0,0,0,2,1,0,0,1,1,1,1,0,1,0]