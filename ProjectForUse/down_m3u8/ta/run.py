#-*- coding:utf-8 -*-
from Crypto.Cipher import AES
import re, os

input_path = "D:/Videos/Manu/normal_list" #输入路径，请替换成自己的
output_path = "D:/Videos/Manu/output" #输出路径，请替换成自己的

# 这里是为了划分数据段，因为AES128加密每次操作的数据长度是128位，也就是16个字节
def splite_data(data):
	res = []
	LEN = 16
	idx = 0
	seg = data[idx:LEN]
	while len(seg) == LEN:
		res.append(seg)
		idx += LEN
		seg = data[idx:idx+LEN]
	if LEN > len(seg) > 0:
		res.append(seg.zjust(LEN, b'\0'))
	return res

# 解密单个ts文件
def decrypt_single_ts(key_path, iv_str, ts_path):
	fi = open(key_path, 'rb')
	key = fi.read()
	fi.close()
	fi = open(ts_path, 'rb')
	ts = fi.read()
	fi.close()
	iv = bytes.fromhex(iv_str)
	pad_len = AES.block_size - len(ts) % AES.block_size
	if pad_len != AES.block_size:
		ts = ts[:-pad_len] + bytes([0] * pad_len)
	cipher = AES.new(key, AES.MODE_CBC, iv=iv)
	out_data = cipher.decrypt(ts)
	if pad_len != AES.block_size:
		out_data = out_data[:-pad_len]
	return out_data

# 解密并合并一个m3u8文件
def decrypt_single(m3u8_path):
	fp = open(m3u8_path, 'r')
	lines = fp.readlines()
	fp.close()
	pat_uri = r"URI=\"(.+)\"" #搜索URI的模式
	pat_iv = r"IV=0x(\w+)" #搜索IV的模式
	regex_uri = re.compile(pat_uri)
	regex_iv = re.compile(pat_iv)
	datas = b''
	for idx in range(2, len(lines), 3):
		if lines[idx] is not None and "ENDLIST" not in lines[idx]:
			key = regex_uri.search(lines[idx])[1].strip()
			iv = regex_iv.search(lines[idx])[1].strip()
			ts = lines[idx + 2].strip()
			datas += decrypt_single_ts(key, iv, ts)
	return datas


def decrypt():
	file_list = os.listdir(input_path) # m3u8文件列表
	for fi in file_list:
		full_path = os.path.join(input_path, fi)
		data = decrypt_single(full_path) #解密一个m3u8
		fi_output_path = os.path.join(output_path, os.path.splitext(fi)[0] + ".mp4") #获取输出路径
		fi = open(fi_output_path, 'wb')
		fi.write(data) #写入解密数据
		fi.close()

if __name__ == '__main__':
	decrypt()