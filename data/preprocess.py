import csv

hiv1 = open('/Users/jeongrokyu/graphdata_analysis/data/regression/data_test.txt', 'r')
hiv2 = open('/Users/jeongrokyu/graphdata_analysis/data/regression/data_train.txt', 'r')
content1 = hiv1.read()
content2 = hiv2.read()
hiv1.close()
hiv2.close()
destination_classfication = open('/Users/jeongrokyu/graphdata_analysis/data/regression.txt', 'w')
destination_classfication.write(content1 + content2)
destination_classfication.close()