'''
ZIP 파일 파싱 프로그램 생성
- 파일명
- 파일 데이터가 시작하는 offset 출력
- 데이터 영역 따로 저장
파싱해주는 라이브러리 사용 X
'''


import sys
import argparse
import os
import struct
import shutil

filename = input("Enter Filename: ")
f = open('C:\\Users\\sst88\\'+filename, 'rb')
f.seek(0)

localheader1_signature = f.read(4)
localheader1_version = f.read(2)
localheader1_bitflag = f.read(2)
localheader1_compression = f.read(2)
localheader1_lmt = f.read(2)
localheader1_lmd = f.read(2)
localheader1_crc32 = f.read(4)
localheader1_compsize = f.read(4)
localheader1_uncompsize = f.read(4)
localheader1_filenamelength = f.read(2)
localheader1_extrafieldlength = f.read(2)
localheader1_filename = f.read(13)
localheader1_data = f.read(17)

localheader2_signature = f.read(4)
localheader2_version = f.read(2)
localheader2_bitflag = f.read(2)
localheader2_compression = f.read(2)
localheader2_lmt = f.read(2)
localheader2_lmd = f.read(2)
localheader2_crc32 = f.read(4)
localheader2_compsize = f.read(4)
localheader2_uncompsize = f.read(4)
localheader2_filenamelength = f.read(2)
localheader2_extrafieldlength = f.read(2)
localheader2_filename = f.read(13)
localheader2_data = f.read(11)

cd_signature = f.read(4)
cd_compver = f.read(2)
cd_uncompver = f.read(2)
cd_flag = f.read(2)
cd_compmethod = f.read(2)
cd_lmt = f.read(2)
cd_lmd = f.read(2)
cd_crc32 = f.read(4)
cd_compsize = f.read(4)
cd_uncompsize = f.read(4)
cd_filenamelength = f.read(2)
cd_extrafieldlength = f.read(2)
cd_commentlength = f.read(2)
cd_disknumber = f.read(2)
cd_internal = f.read(2)
cd_external = f.read(4)
cd_offset_lh1 = f.read(4)
cd_filename = f.read(13)
cd_extrafield = f.read(57)

ecd_signature = f.read(4)
ecd_disknumber = f.read(2)
ecd_disknumber_withcd = f.read(2)
ecd_diskentries = f.read(2)
ecd_totalentries = f.read(2)
ecd_cdsize = f.read(4)
ecd_offset_cd = f.read(4)
ecd_commentlength = f.read(2)


print('file names: ', localheader1_filename, localheader2_filename)
print('starting offset: ', cd_offset_lh1)
print('testfile1 data: ', localheader1_data)
print('testfile2 data: ', localheader2_data)

