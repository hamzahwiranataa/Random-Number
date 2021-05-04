from tkinter import *;
from tkinter import messagebox;
import random



""" 


    Nama : Hamzah Wiranata
    Name   : Hamzah Wiranata


"""


def nomorbenar(h): # fungsi nomorbenar akan berperan untuk fungsi di dalam hasilku
        if (h.isdigit()): # memeriksa bahwa yang di tulis tadi adalah nomor, bukan angka
            return True;

def panggil(no): # fungsi pangggil akan berperan untuk fungsi di dalam fungsi hasilku
    if("." in no): # jika ada tada '.' atau titik pada jawaban makan nanti titik tersebut akan hilang, di karenakan int(no)
        return int(no)
    else: # agar selain hasil yang menghasi kan tanda '.' atau titik di dalam jawaban maka simbol tersebut akan di hilangkan
        return int(no)
     
def dev():
    messagebox.showinfo("Info", "Name      : Hamzah Wiranata\nLocation : Indonesian ") # berfungsi jika button 'Pembuat' di kelik maka fungsi dev akan di gunakan

def hasilku(): # berfungsi jika button 'Lihat Hasil' di kelik maka fungsi hasilku akan di gunakan
    no1 = awal.get(); # menggambil tulisan yang telah di tulis oleh user di dalam box 'awal'
    no2 = akhir.get(); # menggambil tulisan yang telah di tulis oleh user di dalam box 'akhir'

    if(nomorbenar(no1) == True and nomorbenar(no2) == True and no1 != " " and no2 != " "):
        no1 = panggil(no1); # memanggil kembali tulisan yang telah di tulus oleh user tadi setelah melewati fungsi IF
        no2 = panggil(no2); # memanggil kembali tulisan yang telah di tulus oleh user tadi setelah melewati fungsi IF
        hasil = random.randint(no1, no2) # akan merandom angka yang telah di tulis oleh user tadi.

        hasilen = Label(layar, text=hasil, compound=CENTER) # berfungsi untuk memberi tahu hasil random tadi
        hasilen.place(rely=0.6, relx=0.5, anchor="center")

    else:
        messagebox.showinfo("Info", "Tidak Ada Hasil\n\nJika Kamu Memasukan Simbol Atau Huruf Maka Tidak Ada Hasil\nBox Tersebut Khusus Untuk Di Masukan Nomor Saja.")
layar = Tk(); # berperan untuk membuat box
layar.title("RandNomor"); # judul sebuah aplikas
layar.geometry("340x400+510+180"); # ukuran box, dan letak lokasi box

nama = Label(layar, text="Random Nomor", compound=CENTER) # text yang berada di bagian atas
nama.place(rely=0.2, relx=0.5, anchor="center") # mengatur posisi

texawal = Label(layar, text="Nomor Awal : ", compound=CENTER) #text nomor awal
texawal.place(rely=0.4, relx=0.2, anchor="center") # mengatur posisi

texakhir = Label(layar, text="Nomor Akhir : ", compound=CENTER) # text nomor akhir
texakhir.place(rely=0.5, relx=0.2, anchor="center") # mengatur posisi

awal = Entry(layar) # membuat box bertuliskan Nomor Awal
awal.place(rely=0.4, relx=0.5, anchor="center") # mengatur posisi

akhir = Entry(layar) # membuat box bertuliskan nomor akhir
akhir.place(rely=0.5, relx=0.5, anchor="center") # mengatrus posisi

jawb = Label(layar, text="Hasil : ", compound=CENTER) # memberi lebel untuk memberi tahu kepada user bahwa di di depan hasil telah bertuliskan hasil dari random nomor
jawb.place(rely=0.6, relx=0.4, anchor="center") # mengatur posisi

konfrim = Button(layar, text="Lihat Hasil", command=hasilku) # memanggil fungsi 'hasilku' di atas
konfrim.place(rely=0.8, relx=0.5, anchor="center") # mengatur posisi

pembuat = Button(layar, text="Pembuat", command=dev) # memanggil fungsi 'dev' di atas
pembuat.place(rely=0.1, relx=0.9, anchor="center") # mengatur posisi

layar.mainloop(); # berperan untuk membuat box