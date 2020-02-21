# -*- coding:utf-8 -*-
# source:https://github.com/crifan/crifanLibPython/blob/master/crifanLib/crifanFile.py
import os



def getFileFolderSize(fileOrFolderPath):
	"""get size for file or folder"""
	totalSize = 0

	if not os.path.exists(fileOrFolderPath):
		return totalSize

	if os.path.isfile(fileOrFolderPath):
		totalSize = os.path.getsize(fileOrFolderPath) # 5041481
		return totalSize

	if os.path.isdir(fileOrFolderPath):
		with os.scandir(fileOrFolderPath) as dirEntryList:
			for curSubEntry in dirEntryList:
				curSubEntryFullPath = os.path.join(fileOrFolderPath, curSubEntry.name)
				if curSubEntry.is_dir():
					curSubFolderSize = getFileFolderSize(curSubEntryFullPath) # 5800007
					totalSize += curSubFolderSize
				elif curSubEntry.is_file():
					curSubFileSize = os.path.getsize(curSubEntryFullPath) # 1891
					totalSize += curSubFileSize

			return totalSize


def test():
	normalFile =r"D:\SE_projects\pyCharm\Python-spider\tools\test-net\em2me.py"
	normalFileSize = getFileFolderSize(normalFile)
	print("normalFileSize=%s" % normalFileSize)


	userFolder = r"D:\SE_projects\pyCharm\Python-spider\tools"
	userFolderSize = getFileFolderSize(userFolder)
	print("userFolderSize=%s" % userFolderSize)

def get_size_just_blow_folder(folder_Path):
	file_names = os.listdir(folder_Path)
	sizedict = {}
	for fileOrFolderPath in file_names:
		size1 = getFileFolderSize(fileOrFolderPath)
		sizedict.setdefault(fileOrFolderPath,size1)
	# print(sizedict)
	new_sizedict = sorted(sizedict.items(),key=lambda item:item[1]) # 给字典排序。
	# print(new_sizedict)
	for f in new_sizedict:
		fname = f[0]
		byte = f[1]
		if byte > 1024:
			if byte/1024 > 1024:
				if byte/1024/1024 > 1024:
					byte = str(byte/1024/1024/1024)+" GB"
				else:
					byte = str(byte/1024/1024)+" MB"
			else:
				byte = str(byte/1024)+" KB"
		else:
			byte = str(byte)+" B"
		print("{:50}---{:50}".format(fname,byte))



if __name__ == '__main__':
	DIR = r"D:/SE_projects/pyCharm/Python-spider/tools"
	get_size_just_blow_folder(DIR)
