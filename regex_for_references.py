#import library
import re      #untuk regex
import json    #untuk json

#array untuk menyimpan data kolektif dari semua dictionary
json_data = []

#pola regex
regex_nama = r"^([A-Z][a-z]+,\s[A-Z][a-z]+\s[A-Z]\.)|^([A-Z][a-z]+,\s[A-Z]\.)|^([A-Z][a-z]+,\s[A-Z][a-z]+\s[A-Z][a-z]+)|^([A-Z][a-z]+,\s[A-Z][a-z]+)|^([A-Z][a-z]+\s[A-Z][a-z]+)|^([A-z][a-z]+)|\;\s([A-Z][a-z]+,\s[A-Z][a-z]+\s[A-Z]\.)|\;\s([A-Z][a-z]+,\s[A-Z][a-z]+\s[A-Z]{1,2}\.)|([A-Z][a-z]+,\s[A-Z]\.)|\;\s([A-Z][a-z]+,\s[A-Z][a-z]+)"
regex_tahun = r"\((\d{4})\)|\s(\d{4})\.|[A-Z]{4}(\d{4})\.|\s(\d{4})\s|\/(\d{4})\/"
regex_judul = r"\"(.+)\"|^([A-Z]{6}.+)\s\(|\.\s([A-Z][a-z]+\s[a-z]+)\.|\)\.\s([A-Z][a-z]+\s[A-Z][a-z]+)\.|\(\d{4}\)\.\s([A-Z][a-z]+.+[A-Z][a-z]+)\.\s[A-Z][a-z]+\:\s[A-Z][a-z]+\.|\)\.\s(.+)\..+\:1602\.|^.+\.\s(.+\([a-z]{13}\)\s[a-z]+\.)|\)\.\s(.+)\s\([A-Z][a-z]+\)\."

#lokasi file doc_1.txt
path_input = "D:/kuliah/s6/PBA A/tugas/tugas1 - dedline = 23 Februari 2020/soal/doc_1.txt"

#method untuk menyimpan data ke dictionary
def saveToDic(nama, tahun, judul):
    dict = {'authors': nama, 'year': tahun, 'title': judul}
    return dict

#method untuk menyimpan data ke file json
def arrayToJSON(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

#buka file daftar pustaka, looping tiap baris
with open(path_input, "r") as doc:
    for line in doc:
        daf_pus = line.strip()
        
        #cek daftar pustaka bukan baris kosong
        if daf_pus != "":
            
            #ekstrak nama dengan regex
            nama = re.findall(regex_nama, daf_pus)
            temp_nama = ""
            for i in nama:
                for j in range(len(i)):
                    if i[j] !='':
                        if temp_nama == "":
                            temp_nama = i[j]
                        else:
                            temp_nama += "; "+i[j]
            
            #ekstrak tahun dengan regex
            tahun = re.findall(regex_tahun, daf_pus)
            temp_tahun = ""
            for i in tahun:
                for j in range(len(i)):
                    if i[j] != '':
                        temp_tahun = i[j]            
            
            #ekstrak judul dengan regex
            judul = re.findall(regex_judul, daf_pus)
            temp_judul = ""
            for i in judul:
                for j in range(len(i)):
                    if i[j] != '':
                        temp_judul = i[j]
            
            #simpan data ke dictionary
            data = saveToDic(temp_nama, temp_tahun, temp_judul)
            
            #simpan dictionary ke array
            json_data.append(data)
            
#tutup file
doc.close()

#path file json yang akan dibuat
path_output = "D:/kuliah/s6/PBA A/tugas/tugas1 - dedline = 23 Februari 2020/a_judul.json"

#simpan data ke file json
arrayToJSON(path_output, json_data)

#read file json
#with open(path_output, 'r') as json_file:
#    hasil = json.load(json_file)
#    print(hasil)
