def print_file_info(file_name):
    """
    打开文件
    :param file_name: 文件名
    :return: 无返回值
    """
    file = None
    try:
        file = open(file_name, 'r', encoding='utf-8')
        content = file.read()
        print(content)
    except Exception as e:
        print('打开文件出错了，文件未找到')
        print(e)
    finally:
        if file is not None:
            file.close()