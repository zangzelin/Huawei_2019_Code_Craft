
def write_txt(data,path): # 读取txt文件，返回二维数组
    file = open(path, 'w')
    for i in data:
        file.write('(' + str(i)[1:-1] + ')\n')
    file.close()

if __name__ == "__main__":
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\华为2019软件精英挑战赛\\write_test.txt'
    data = [[1001,1,2,3,4,5],[1002,1,2,3,4,5]]
    write_txt(data,road_path)
    # print(data)