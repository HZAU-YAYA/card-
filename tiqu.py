#!/usr/bin/env python3
#-*- encoding=UTF-8 -*-
import re
import argparse
import logging
import sys

LOG = logging.getLogger(__name__)
__version__ = "1.0.0"    #设置版本信息
__author__ = ("Boya Xu",)   #输入作者信息
__email__ = "xby@bioyigene.com"
__all__ = []

def add_help_args(parser): #帮助函数
    parser.add_argument('--sequence', default="", type=str, help='数据库')
    parser.add_argument('--name',  default="", type=str, help='耐药基因名')
    parser.add_argument('--out', '-o', type=str, default="", help="out put file")
    return parser


def run(sequence, name, out):
    fin = open(sequence, "r")
    gene_name = name.lower()
    fout=open(out, "w")
    for i in fin:
        if i.startswith(">"):
            n = 0
            s = i.strip().split("~~~")
            s[3] = s[3].lower()
            if gene_name in s[3]:
                if "resistance" in s[3]:
                    n = n+1
                    fout.write(">"+s[1]+"\n")
            else:
                continue
        else:
            if n == 1:
                fout.write(i)
            else:
                continue              

def main():   #主函数，执行函数
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="[%(levelname)s] %(message)s")
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=''' 
name:chtxt.py 
attention: python pipeise.py --name "" --sequence sequences.fasta -o out.fa
version: %s
contact: %s <%s>\ 
''' % (__version__, ' '.join(__author__), __email__))
    args = add_help_args(parser).parse_args()
    run(args.sequence, args.name, args.out)


if __name__ == "__main__":           #固定格式，使 import 到其他的 python 脚本中被调用（模块重用）执行
    main()
