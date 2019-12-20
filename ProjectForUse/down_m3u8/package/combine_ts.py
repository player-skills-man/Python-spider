# encoding=utf-8
import os


def file_walker(path):
    file_list = []
    files_read = os.listdir(path)
    for file in files_read:
        if file.endswith(".ts"):
            file = file.strip(".ts")
            file_list.append(file)
    file_list.sort(key=int)
    for i in range(len(file_list)):
        file_list[i] = path + "/" + file_list[i] + ".ts"
    # print("/n".join(file_list))
    return file_list


def combine(ts_path,file_name):
    file_list = file_walker(ts_path)
    with open(file_name, 'wb+') as fw:
        for i in range(len(file_list)):
            fw.write(open(file_list[i], 'rb').read())


if __name__ == '__main__':
    combine("ts_list", "result/hh")
