# import StopWordRemoverFactory class
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
#import sent_tokenize, word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
#import modul re
import re


#buatkan variabel factory yang berisi fungsi StopWordRemoverFactory() berasal dari library sastrawi
factory = StopWordRemoverFactory()
#buatkan variabel daftar_stopword yang berisi fungsi get_stop_words()
daftar_stopword = factory.get_stop_words()

stopword = factory.create_stop_word_remover()
#menampilkan daftar stopword dari library sastrawi
#print(daftar_stopword)

# Kalimat
kalimat = open('doc_2.txt','r')
dokumen = kalimat.read()

#case folding
#mengubah semua huruf kapital menjadi huruf kecil
lower_case = dokumen.lower()
#print(lower_case)

#menghapus angka
no_number = re.sub(r"\d+", "",lower_case)
#print(hasil)

#menghapus tanda baca
tanda_baca = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_tanda_baca = ""
for karakter in no_number:
    if karakter not in tanda_baca:
        no_tanda_baca = no_tanda_baca + karakter
#print(no_tanda_baca)
        
#menghapus whitepace(karakter kosong)
no_whitepace = no_tanda_baca.strip()
dokumen_fix = no_whitepace
#print(dokumen_fix)

doc_setelah_remove_stop = stopword.remove(dokumen_fix)
#menampilkan hasil setelah removal stopword sastrawi
#print(doc_setelah_remove_stop)

#menampilkan tokenize word hasil setelah removal stopword sastrawi
#print(word_tokenize(doc_setelah_remove_stop))

dokumen_tokenize = word_tokenize(doc_setelah_remove_stop)

kata2 = dokumen_tokenize
kata_unik = sorted(set(kata2),reverse=True)
#print(kata_unik)

path = "E:/Snake/b_kataunik.txt"
output =open(path,"w")

for Kata in kata_unik[0:30]:
    barisan = (Kata,kata2.count(Kata))
    tanda_baca = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_tanda_baca = "\n"
    for karakter in str(barisan):
        if karakter not in tanda_baca:
            no_tanda_baca = no_tanda_baca + karakter
            output_fix = no_tanda_baca;
            
    output.write(output_fix)
output.close()
    

        
