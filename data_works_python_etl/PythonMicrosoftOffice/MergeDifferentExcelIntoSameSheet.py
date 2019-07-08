import glob
import xlrd
import xlwt
import os

# 待搜索的所有目录文件夹
_list_of_all_folders = []
_list_of_all_files = []

def get_all_sub_folder(file_paths, sub_folder_level=0):
    """
       遍历提供目录列表下的指定查询层级的所有子目录
    :param file_paths: 一个文件夹目录的列表，例如 ['c:\\folder1'] 或 ['c:\\folder1','c:folder_2']
    :param sub_folder_level: 要向下查找子文件夹的层数，例如 c:\\folder1下还有两个文件夹folder11、folder12,需要返回
                             ['c:\\folder1','c:\\folder1\\folder11','c:\\folder1\\folder12'].
                             则参数为get_all_sub_folder(['c:\\folder1'], sub_folder_level=1)
    :return: 返回一个文件夹列表，返回内容取决于 file_paths 和 sub_folder_level
    """
    try:
        if sub_folder_level == 0:
            for file_path in file_paths:
                if os.path.isdir(file_path) and os.path.exists(file_path):
                    _list_of_all_folders.append(file_path)
                else:
                    continue
            return
        elif sub_folder_level < 0:
            raise Exception("Sub Folder Level Should Not Negative Number")
        else:
            sub_folder_level -= 1
            temp_list_file_path = []
            for file_path in file_paths:
                if os.path.isdir(file_path):
                    _list_of_all_folders.append(file_path)
                    # 获取目录下的有效文件夹目录，并加载到temp_list_file_path
                    temp_list_file_path.extend([file_path + "\\" + x for x in os.listdir(file_path) if os.path.isdir(file_path + "\\" + x)])
                else:
                    continue
            get_all_sub_folder(temp_list_file_path, sub_folder_level)
    except Exception as e:
        print("Exception: "+str(e))


def search_file(file_path, key_name, end_with='.xls'):
    """
       查看制定目录下，包含关键字且满足对应文本类型的文件路径
    :param file_path: 给定目录
    :param key_name: 关键字--待查找的文件名中包含的关键内容
    :param end_with: 文件类型--文件以什么结尾
    :return: 返回满足条件的所有查到文件路径
    """
    try:
        get_list_of_file = []
        get_pattern = str('*' + key_name + '*' + end_with)
        if os.path.isdir(file_path) and os.path.exists(file_path):
            get_list_of_file.extend(glob.glob(file_path + '\\' + get_pattern))
        else:
            raise Exception("This "+file_path+" is not an available director!")
        return get_list_of_file
    except Exception as e:
        print("There is an Exception :"+str(e))


# def create_target_file():


def main():
    """
       程序的入口，也是总控
    :return:
    """
    get_folder_path = input(r"请输入待处理的根目录（例如 c:\test）：")
    get_all_sub_folder([get_folder_path])
    print("当前查询范围："+str(_list_of_all_folders))
    sub_type = input(r"是否要调整查询范围，如需调整请输入Y（Y/N）：")
    if sub_type.upper() == 'Y':
        _list_of_all_folders.clear()
        sub_folder_level = input(r"请输入待查询的层级（正整数）：")
        get_all_sub_folder([get_folder_path],sub_folder_level=int(sub_folder_level))
        print("查询范围变更为：" + str(_list_of_all_folders))
    key_name = input(r"请输入关键内容，在上面范围内，查找包含该内容的文件：")
    end_with_type = input(r"当前默认查找.xls结尾的文件，是否需要修改（Y/N）：")
    if end_with_type.upper() == "Y":
        end_with = input(r"请输入你想要的文本类型（即:以什么结尾的文件，例如.txt）")
    else:
        end_with = '.xls'
    for folder_path in _list_of_all_folders:
        _list_of_all_files.extend(search_file(folder_path, key_name, end_with))
    print("获取到了说有要查看的文件路径："+str(_list_of_all_files))


if __name__ == '__main__':

    # print(search_file("C:\\test", "get", ".txt"))
    # print(os.listdir("C:\\test"))
    # get_all_sub_folder(["C:\\test"], 3)
    # print(_list_of_all_folders)
    main()
