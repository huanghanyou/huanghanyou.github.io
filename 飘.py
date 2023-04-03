from pyecharts.charts import WordCloud

src_filename = './data/飘-pseg.csv'


src_file = open(src_filename, 'r')
line_list = src_file.readlines()
src_file.close()

print(line_list)


wordfreq_list = []
for line in line_list:
    line = line.strip()
    line_split = line.split(',')
    wordfreq_list.append((line_split[0],line_split[1]))

print(wordfreq_list)

del wordfreq_list[0]
cloud = WordCloud()


cloud.add('', wordfreq_list)


out_filename = './output/飘-词云.html'
cloud.render(out_filename)

print('生成结果文件：' + out_filename)