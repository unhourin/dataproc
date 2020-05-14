# coding = utf-8

import os
import fnmatch
from win32com import client as wc

'''
Description:多格式文档文本抽取工具
Author:YUN
Prompt:code in Python3.0+ env
'''

'''
功能描述：word文件转存txt，默认保存在根目录下，支持自定义
参数描述：1 filePath 文件路径 2 savePath 保存路径
'''


def FilesToTxt(filePath, savePath=''):
    # 1  切分文件路径文件目录和文件名
    dirs, filename = os.path.split(filePath)
    # print(dirs + '\n' + filename)

    # 2 修改切分后的文件后缀
    #  获得文件后缀
    typename = os.path.splitext(filename)[-1].lower()
    new_name = TranType(filename, typename)

    # 3 设置新的文件保存路径
    if savePath == '':
        savePath = dirs
    else:
        savePath = savePath
    pdfToTxtPath = os.path.join(savePath, new_name)
    print('-->', pdfToTxtPath)
    print(filePath)

    # 4 加载文本提取的处理程序， pdf-->txt
    wordapp = wc.Dispatch('Word.Application')
    mytxt = wordapp.Documents.Open(filePath)

    # 5 保存文本信息
    mytxt.SaveAs(pdfToTxtPath, 4)
    mytxt.Close()


'''
功能描述：根据文件后缀修改文件名
参数描述：1 filePath 2 typename 文件后缀
'''


def TranType(filename, typename):
    new_name = ''
    if typename == '.pdf':
        if fnmatch.fnmatch(filename, '*.pdf'):
            new_name = filename[:-4] + '.txt'
        else:
            return
    elif typename == '.doc' or typename == '.docx':
        if fnmatch.fnmatch(filename, '*.doc'):
            new_name = filename[:-4] + '.txt'
        elif fnmatch.fnmatch(filename, '*.docx'):
            new_name = filename[:-5] + '.txt'
        else:
            return
    # elif....
    else:
        print('警告：\n 您输入的【', typename, '】不合法，本抽取工具仅支持/doc/docx/pdf格式的文件 ')
        return
    return new_name


if __name__ == '__main__':
    filePath = os.path.abspath(r'file/test4.pdf')
    FilesToTxt(filePath)
