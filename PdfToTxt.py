# coding = utf-8

import os
import fnmatch
from win32com import client as wc

'''
Description:Pdf文档信息提取
Author:Yun
Prompt:code in python3 env
'''

'''
功能描述：word文件转存txt，默认保存在根目录下，支持自定义
参数描述：1 filePath 文件路径 2 savePath 保存路径
'''


def PdfToTxt(filePath, savePath=''):
    # 1  切分文件路径文件目录和文件名
    dirs, filename = os.path.split(filePath)
    print(dirs + '\n' + filename)

    # 2 修改切分后的文件后缀
    new_name = ''
    if fnmatch.fnmatch(filename, '*.pdf') or fnmatch.fnmatch(filename, '*.PDF'):
        new_name = filename[:-4] + '.txt'
    else:
        print('格式不正确，仅支持pdf格式。')
        return

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


if __name__ == '__main__':
    filePath = os.path.abspath(r'./file/test3.pdf')
    PdfToTxt(filePath)
