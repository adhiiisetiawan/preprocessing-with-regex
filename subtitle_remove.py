# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:22:43 2020

@author: adhis
"""
#digunakan untuk melakukan import library regex
import re

#regex yang akan dihilangkan pada dokumen
regex = r"^\n|^([0-9]+)|\:\d[0-9]|\,\d[0-9]+\s|(\-\-\>\s)|\d[0-9]|<[^>]*>"

#direktori file yang akan dilakukan preprocessing
path = "C:/Users/adhis/OneDrive/Documents/Data Semester 6/Natural Language Processing/Assignment/doc_3.srt"

#direktori output file hasil preprocessing
path2 = "C:/Users/adhis/OneDrive/Documents/Data Semester 6/Natural Language Processing/Assignment/c_subtitle.txt"

#melakukan buka file yang mengarah pada direktori dalam variable path, kemudian disimpan dalam varible input
input = open(path)

#melakukan buka file yang mengarah pada direktori dalam varible path2 dan menggunakan mode write, kemudian disimpan dalam variable output
output = open(path2,"w")

#melakukan looping pada setiap baris pada file
for line in input:
    #menghapus whitespace yang ada pada file
    if line.strip():
    #melakukan write pada file, dan menggunakan regex untuk melakukan subtitusi dengan nilai kosong berdasarkan regex yang telah dibuat
        output.write(re.sub(regex,"",line))

#menutup dokumen yang disimpan pada variable input
input.close()

#menutup dokumen yang disimpan dalam variable output
output.close()