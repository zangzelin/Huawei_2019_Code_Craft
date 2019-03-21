def graph_data(data):  # 1，读取txt文件；2，根据规则进行数据转换融合
    data_graph = {}
    for i in data:
        if i[4] not in data_graph.keys():
            # 道路id 0、道路长度 1、最高速度 2、车道数目 3
            data_graph[i[4]] = [i[0], i[1], i[2], i[3], i[5]]
        else:
            data_graph[i[4]].extend([i[0], i[1], i[2], i[3], i[5]])
        if i[6]:
            if i[5] not in data_graph.keys():
                data_graph[i[5]] = [i[4]]
            else:
                data_graph[i[5]].extend([i[0], i[1], i[2], i[3], i[4]])
    return data_graph


if __name__ == "__main__":
    road_path = u'E:\\data\\personal\\项目\\2019华为软件挑战赛\\2019软挑-初赛-SDK\\SDK\\SDK_python\\CodeCraft-2019\\src\\road.txt'
    import read_txt

    data = read_txt.read_txt(road_path)
    data_graph = graph_data(data)
    print(data_graph)
