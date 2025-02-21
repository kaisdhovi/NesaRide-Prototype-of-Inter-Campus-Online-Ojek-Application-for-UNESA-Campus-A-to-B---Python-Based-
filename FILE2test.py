from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import time

window = Tk()

window.title("NesaRide")
window.geometry("1280x720")
window.configure(bg = "#F8F9FA")

#IMAGE FOR LOGIN PAGE
button2 = ImageTk.PhotoImage(Image.open("tombolbuat.png").resize((320, 44)))
login_image3 = ImageTk.PhotoImage(Image.open("frameentry2.png").resize((310, 55)))
button3 = ImageTk.PhotoImage(Image.open("tombolkirim.png").resize((119, 36)))
wall = ImageTk.PhotoImage(Image.open("putih.png").resize((660, 690)))
snkk = ImageTk.PhotoImage(Image.open("snk.png"))
login_image = ImageTk.PhotoImage(Image.open("Gedung_Rektorat_Unesa.png").resize((624, 690)))
logo_gojek = ImageTk.PhotoImage(Image.open("logo_nesaride.png").resize((373, 50)))
login_image2 = ImageTk.PhotoImage(Image.open("frameentry.png").resize((450, 55)))
button = ImageTk.PhotoImage(Image.open("butonlogin.png").resize((344, 44)))
background = ImageTk.PhotoImage(Image.open("background.png"))

#IMAGE FOR NESARIDE
header1 = ImageTk.PhotoImage(Image.open("header.png"))
logo_nesaride = ImageTk.PhotoImage(Image.open("nesaride.png"))
indikator = ImageTk.PhotoImage(Image.open("indikator_select.png"))
indikator2 = ImageTk.PhotoImage(Image.open("indikator_select.png").resize((65, 4)))
indikator3 = ImageTk.PhotoImage(Image.open("indikator_select.png").resize((100, 4)))
profil = ImageTk.PhotoImage(Image.open("profil.png"))
text1 = ImageTk.PhotoImage(Image.open("text1.png"))
text2 = ImageTk.PhotoImage(Image.open("text2.png"))
pesan_sekarang = ImageTk.PhotoImage(Image.open("pesan_sekarang.png"))
banner1 = ImageTk.PhotoImage(Image.open("banner2Rn.png"))
banner2 = ImageTk.PhotoImage(Image.open("banner1Rn.png"))
setlokasi = ImageTk.PhotoImage(Image.open("textsetlokasi.png"))
atur_lokasi = ImageTk.PhotoImage(Image.open("atur_lokasi.png"))
pin = ImageTk.PhotoImage(Image.open("icon_pin.png"))
titik_jemput = ImageTk.PhotoImage(Image.open("kotak.png"))
metode_pembayaran = ImageTk.PhotoImage(Image.open("kotak2.png"))
text_biaya = ImageTk.PhotoImage(Image.open("textbiaya.png"))
pesan = ImageTk.PhotoImage(Image.open("pesan.png"))
button_image_8 = ImageTk.PhotoImage(Image.open("button_22.png"))
denah_kampus = ImageTk.PhotoImage(Image.open("textdenah.png"))
denah = ImageTk.PhotoImage(Image.open("denah.png"))
notice = ImageTk.PhotoImage(Image.open("textdapatdriver.png"))
detailperjalanan = ImageTk.PhotoImage(Image.open("textdetailjalan.png"))
pin2 = ImageTk.PhotoImage(Image.open("icon_pin.png"))
titik_jemput2 = ImageTk.PhotoImage(Image.open("kotak.png"))
detaildriver = ImageTk.PhotoImage(Image.open("textdetaildriver.png"))
driver = ImageTk.PhotoImage(Image.open("kotak3.png"))
avatardriver = ImageTk.PhotoImage(Image.open("avatar.png").resize((88, 88)))
detailpembayaran = ImageTk.PhotoImage(Image.open("textdetailpembayaran.png"))
frame1 = ImageTk.PhotoImage(Image.open("frame_rating.png"))
textr = ImageTk.PhotoImage(Image.open("textrating.png"))
d1 = ImageTk.PhotoImage(Image.open("driver_rating.png"))
kirim = ImageTk.PhotoImage(Image.open("tombol_kirim.png"))
bintang0 = ImageTk.PhotoImage(Image.open("bintang0.png"))
bintang1 = ImageTk.PhotoImage(Image.open("bintang1.png"))
selesai = ImageTk.PhotoImage(Image.open("selesai.png"))
load1 = ImageTk.PhotoImage(Image.open("loading6.png"))
load2 = ImageTk.PhotoImage(Image.open("loading7.png"))
load3 = ImageTk.PhotoImage(Image.open("loading8.png"))
load4 = ImageTk.PhotoImage(Image.open("loading9.png"))
load5 = ImageTk.PhotoImage(Image.open("cekles2.png").resize((100,100)))
denah2 = ImageTk.PhotoImage(Image.open("denah.png").resize((460, 383)))
frame = ImageTk.PhotoImage(Image.open("frame_riwayat.png"))
head_table = ImageTk.PhotoImage(Image.open("head_riwayat.png"))
batal = ImageTk.PhotoImage(Image.open("batalkan.png"))
kembali = ImageTk.PhotoImage(Image.open("kembali.png"))
bintang2 = ImageTk.PhotoImage(Image.open("bintang2.png"))
bintang3 = ImageTk.PhotoImage(Image.open("bintang3.png"))
garis = ImageTk.PhotoImage(Image.open("garis.png"))
perjalanan = ImageTk.PhotoImage(Image.open("perjalanan.png"))
framer2 = ImageTk.PhotoImage(Image.open("frame_riwayat2.png"))
lihat1 = ImageTk.PhotoImage(Image.open("lihat1.png"))
lihat2 = ImageTk.PhotoImage(Image.open("lihat2.png"))

class loginpage :
    def __init__(self) :
        self.login = Frame(window, width=1280, height=720, bg = "#F8F9FA")
        self.login.place(x = 0, y = 0)
        Label(self.login, image = login_image, bg = "#faf9f9").place(x = -2, y = -42)
        self.loginn()

    def loginn(self) :
        self.popstat = 0
        self.frame = Frame(self.login, width = 500, height = 500, bg = "#faf9f9")
        self.frame.place(x = 707, y = 75)

        Label(self.frame, image = logo_gojek, bg = "#faf9f9").place(x = 60, y = 50)

        self.heading = Label(self.frame, text = "Selamat datang! Silahkan Login terlebih dahulu.", fg = "black", bg = "#faf9f9", font =("Poppins", 12))
        self.heading.place(x = 43, y = 130)

        Label(self.frame, text = "Username", fg = 'black', border = 0, bg = "#faf9f9", font = ("Poppins", 11)).place(x = 46, y = 173)
        Label(self.frame, image = login_image2, bg = "#faf9f9").place(x = 31, y = 193)
        self.user = Entry(self.frame, width = 43, fg = 'black', border = 0, bg = "#D9D9D9", font = ("Maison Neue Light", 11))
        self.user.place(x = 60, y = 212)
        self.user.insert(0, "Masukkan username anda")
        self.user.bind("<FocusIn>", self.on_enter)
        self.user.bind("<FocusOut>", self.on_leave)

        Label(self.frame, text = "Password", fg = 'black', border = 0, bg = "#faf9f9", font = ("Poppins", 11)).place(x = 46, y = 255)
        Label(self.frame, image = login_image2, bg = "#faf9f9").place(x = 31, y = 275)
        self.password = Entry(self.frame, width = 40, fg = 'black', border = 0, bg = "#D9D9D9", font = ("Maison Neue Light", 11))
        self.password.place(x = 60, y = 294)
        self.password.insert(0, "Masukkan password anda")
        self.password.bind("<FocusIn>", self.on_enter1)
        self.password.bind("<FocusOut>", self.on_leave1)
        self.lihat = 1
        self.button_show = Button(self.frame, image = lihat1, border = 0, bg = "#D9D9D9", command = self.show)
        self.button_show.place(x = 425, y = 288)

        Button(self.frame, image = button, bg = "#faf9f9", border = 0, command = self.home).place(x = 80, y = 355)

        self.label = Label(self.frame, text = "Tidak punya akun?", fg = "black", bg = "#faf9f9", font = ("Microsoft YaHei UI Light", 9))
        self.label.place(x = 175,y = 415)

        self.sign_up = Button(self.frame, width = 6, text = "Sign Up", border = 0, bg = "#faf9f9",cursor = "hand2", fg = "#03045E", command = self.change)
        self.sign_up.place(x = 285,y = 415)

        self.konfirmasi = Label(self.frame, text = "", bg = "#faf9f9")
        self.konfirmasi.place(x = 55, y = 333)

    def on_enter(self, event) :
        self.user.delete(0, 'end')

    def on_leave(self, event) :
        name = self.user.get()
        if name == '' :
            self.user.insert(0, "Masukkan username anda")

    def on_enter1(self, event) :
        self.password.delete(0, 'end')
        self.password.config(show = "*")

    def on_leave1(self, event) :
        passs = self.password.get()
        if passs == '' :
            self.password.insert(0, "Masukkan password anda")
            self.password.config(show = "")
            self.button_show.config(image = lihat1)

    def show(self) :
        if self.lihat == 1 :
            self.password.config(show = "")
            self.button_show.config(image = lihat2)
            self.lihat = 0
        else :
            self.password.config(show = "*")
            self.button_show.config(image = lihat1)
            self.lihat = 1

    def home(self) :
        lanjut = False
        username2 = self.user.get()
        password2 = self.password.get()
        file = open("akun.txt", "r")
        akunn = file.readlines()
        file.close()
        for line in akunn :
            data = line.strip().split(',')
            username1 = data[0]
            password1 = data[2]
            if username2 == username1 :
                lanjut = True
                break
            elif username2 == "Masukkan username anda" :
                self.konfirmasi.config(text = "*anda belum mengisi username", fg = "red")
            else :
                self.konfirmasi.config(text = "*akun tidak ada", fg = "red")

        if lanjut == True :
            if password2 == password1 :
                file = open("username.txt", 'w')
                print(username2, file = file)
                file.close()
                self.login.destroy()
                nesaride()
            else :
                self.konfirmasi.config(text = "*password salah", fg = "red")

    def change(self) :
        self.frame.destroy()
        self.signin()

    def change2(self) :
        if self.popstat == 1 :
            self.frame2.destroy()
            self.kodepop.destroy()
            self.loginn()
        else :
            self.frame2.destroy()
            self.loginn()

    def on_enter2(self, event) :
        self.nim.delete(0, 'end')

    def on_leave2(self, event) :
        nim = self.nim.get()
        if nim == '' :
            self.nim.insert(0, "Masukkan NIM anda") 

    def on_enter3(self, event) :
        self.kodekonfirmasi.delete(0, 'end')

    def on_leave3(self, event) :
        passs = self.kodekonfirmasi.get()
        if passs == '' :
            self.kodekonfirmasi.insert(0, "Masukkan kode konfirmasi")

    def kode(self) :
        import random

        global kodepop
        self.kodepop = Toplevel(window)
        self.kodepop.title("Kode Konfirmasi")
        self.kodepop.geometry("300x50")

        kode_list = ["9469", "3244", "0523", "7249"]
        global kode
        kode = random.choice(kode_list)
        Label(self.kodepop, text = kode, font = ("Maison Neue", 20)).pack() 
        self.popstat = 1

    def cek(self) :
        if self.buat["state"] == "disabled":
            self.buat["state"] = "normal"
        else:
            self.buat["state"] = "disabled"

    def syarat(self) :
        global snk
        snk = Toplevel(window)
        snk.title("Syarat dan Ketentuan")
        snk.geometry("520x520")
        ftsnk = Label(snk, image = snkk)
        ftsnk.pack()

    def buatakun(self) :
        kode1 = self.kodekonfirmasi.get()
        if kode1 == kode :
            nim = self.nim.get() 
            pw = self.password.get()
            usern = self.user.get()
            file = open("akun.txt", "r")
            akunn = file.readlines()
            panjang = len(akunn)
            file.close()
            n = 1
            for line in akunn :
                data = line.strip().split(',')
                nim2 = data[1]
                if nim == nim2 :
                    self.confirm.config(text = "*NIM sudah digunakan", fg = "red")
                    break 
                elif usern == "Masukkan username anda" :
                    self.confirm.config(text = "*Anda belum mengisi username", fg = "red")
                    break
                elif pw == "Masukkan password anda" :
                    self.confirm.config(text = "*Anda belum mengisi password", fg = "red")
                    break
                elif nim == "Masukkan NIM anda" :
                    self.confirm.config(text = "*Anda belum mengisi NIM", fg = "red")
                    break
                elif n == panjang :
                    akun = f'{usern},{nim},{pw}'
                    file_akun = open("akun.txt", "a")
                    print(akun, file = file_akun)
                    file_akun.close()
                    self.change2()
                    messagebox.showinfo("Pemberitahuan", "Akun berhasil dibuat")
                else :
                    n += 1
        else :
            self.confirm.config(text = "*kode konfirmasi salah", fg = "red")  

    def signin(self) :
        self.frame2 = Frame(window, width = 500, height = 640, bg = "#faf9f9")
        self.frame2.place(x = 702, y = -10)

        Label(self.frame2, image = logo_gojek, bg = "#faf9f9").place(x = 60, y = 50)

        self.heading = Label(self.frame2, text = "Mulai dengan gratis! Silahkan buat akun anda.", fg = "black", bg = "#faf9f9", font =("Poppins", 12))
        self.heading.place(x = 43, y = 130)

        Label(self.frame2, text = "Username", fg = 'black', border = 0, bg = "#faf9f9", font = ("Poppins", 11)).place(x = 46, y = 173)
        Label(self.frame2, image = login_image2, bg = "#faf9f9").place(x = 31, y = 193)
        self.user = Entry(self.frame2, width = 43, fg = 'black', border = 0, bg = "#D9D9D9", font = ("Maison Neue Light", 11))
        self.user.place(x = 60, y = 212)
        self.user.insert(0, "Masukkan username anda")
        self.user.bind("<FocusIn>", self.on_enter)
        self.user.bind("<FocusOut>", self.on_leave)

        Label(self.frame2, text = "NIM", fg = 'black', border = 0, bg = "#faf9f9", font = ("Poppins", 11)).place(x = 46, y = 255)
        Label(self.frame2, image = login_image2, bg = "#faf9f9").place(x = 31, y = 275)
        self.nim = Entry(self.frame2, width = 43, fg = 'black', border = 0, bg = "#D9D9D9", font = ("Maison Neue Light", 11))
        self.nim.place(x = 60, y = 294)
        self.nim.insert(0, "Masukkan NIM anda")
        self.nim.bind("<FocusIn>", self.on_enter2)
        self.nim.bind("<FocusOut>", self.on_leave2)

        Label(self.frame2, text = "Password", fg = 'black', border = 0, bg = "#faf9f9", font = ("Poppins", 11)).place(x = 46, y = 337)
        Label(self.frame2, image = login_image2, bg = "#faf9f9").place(x = 31, y = 357)
        self.password = Entry(self.frame2, width = 43, fg = 'black', border = 0, bg = "#D9D9D9", font = ("Maison Neue Light", 11))
        self.password.place(x = 60, y = 376)
        self.password.insert(0, "Masukkan password anda")
        self.password.bind("<FocusIn>", self.on_enter1)
        self.password.bind("<FocusOut>", self.on_leave1) 
        # self.lihat = 1
        self.button_show = Button(self.frame2, image = lihat1, border = 0, bg = "#D9D9D9", command = self.show)
        self.button_show.place(x = 425, y = 370)

        Label(self.frame2, text = "Kode Konfirmasi", fg = 'black', border = 0, bg = "#faf9f9", font = ("Poppins", 11)).place(x = 46, y = 419)
        Label(self.frame2, image = login_image3, bg = "#faf9f9").place(x = 35, y = 439)
        self.kodekonfirmasi = Entry(self.frame2, width = 26, fg = 'black', border = 0, bg = "#D9D9D9", font = ("Maison Neue Light", 11))
        self.kodekonfirmasi.place(x = 60, y = 458)
        self.kodekonfirmasi.insert(0, "Masukkan kode konfirmasi")
        self.kodekonfirmasi.bind("<FocusIn>", self.on_enter3)
        self.kodekonfirmasi.bind("<FocusOut>", self.on_leave3)

        Button(self.frame2, image = button3, bg = "#faf9f9", border = 0, command = self.kode).place(x = 350, y = 449)
        Checkbutton(self.frame2, command = self.cek, text = "Saya telah menyetujui                              yang berlaku", fg = "black", bg = "#faf9f9", font = ("Microsoft YaHei UI Light", 9)).place(x = 45,y = 514)
        Button(self.frame2, width = 15, command = self.syarat, text = "Syarat dan ketentuan", border = 0, bg = "#faf9f9",cursor = "hand2", fg = "#03045E").place(x = 194, y = 517)
        self.buat = Button(self.frame2, image = button2, bg = "#faf9f9", border = 0, command = self.buatakun, state= DISABLED)
        self.buat.place(x = 95, y = 548)
        label = Label(self.frame2, text = "Sudah punya akun?", fg = "black", bg = "#faf9f9", font = ("Microsoft YaHei UI Light", 9))
        label.place(x = 175,y = 600)
        log_in = Button(self.frame2, width = 6, text = "Log In", border = 0, bg = "#faf9f9",cursor = "hand2", fg = "#03045E", command = self.change2)
        log_in.place(x = 285,y = 600)
        self.confirm = Label(self.frame2, text = "", bg = "#faf9f9")
        self.confirm.place(x = 45, y = 493)

class nesaride :
    def __init__(self) :
        self.pesanan = 0
        self.canvas = Canvas(window,bg = "green",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        backgroundcanvas = self.canvas.create_image(640.0, 404.0, image = background)
        headerlabel = self.canvas.create_image(640, 46, image = header1)

        #HEADER
        #==========================================================================================
        self.header = Canvas(self.canvas, width=1280, height=90, bg = "#F8F9FA", border = 0, highlightthickness = 0)
        self.header.place(x = 0, y = 0)

        logolabel = self.header.create_image(200, 48, image = logo_nesaride)

        self.tombol_home = Button(self.header, text = "Home", bg = "#F8F9FA", fg = "#266DD3",border = 0, font = ("Myriad Pro", 18),command =lambda: self.switch(self.tombol_home, self.a, self.homepage))
        self.tombol_home.place(x=455.98138427734375,y=34.0,width=75.0,height=20.0)
        self.a = Label(self.header, image = indikator)
        self.a.place(x = 448, y = 60) 

        self.tombol_pesan = Button(self.header, text = "Pesan", bg = "#F8F9FA", fg = "#1D1E2C",border = 0, font = ("Myriad Pro", 19),command =lambda: self.switch(self.tombol_pesan, self.b, self.pesanpage))
        self.tombol_pesan.place(x=603.9813842773438,y=33.0,width=65.0,height=22.0)
        self.b = Label(self.header, image = indikator)
        self.b.place(x = 593, y = 60)
        self.b.place_forget()   

        self.tombol_map = Button(self.header,text = "Map",bg = "#F8F9FA", fg = "#1D1E2C",border = 0, font = ("Myriad Pro", 19),command = lambda: self.switch(self.tombol_map, self.c, self.mappage))
        self.tombol_map.place(x=745.9813842773438,y=30.0,width=47.0,height=29.0)
        self.c = Label(self.header, image = indikator2)
        self.c.place(x = 735, y = 60)
        self.c.place_forget()

        self.tombol_riwayat = Button(self.header,text = "Riwayat",bg = "#F8F9FA", fg = "#1D1E2C",border = 0, font = ("Myriad Pro", 19),command = lambda: self.switch(self.tombol_riwayat, self.d, self.riwayatpage))
        self.tombol_riwayat.place(x=875.9813842773438,y=30.0,width=89.0,height=29.0)
        self.d = Label(self.header, image = indikator3)
        self.d.place(x = 869, y = 60)
        self.d.place_forget()

        profillabel = self.header.create_image(1217.0, 44.0, image=profil)

        file_username = open("username.txt", "r")
        self.username = file_username.read()
        file_username.close()

        Label(self.header, text = f'{self.username}', width = 15, fg = "#1D1E2C", bg = "#F8F9FA", font = ("Poppins", 10, "bold"), anchor = "e", justify="right").place(x = 1045, y = 31)
        self.homepage()

    def homepage(self) :
        self.konten = Canvas(self.canvas, width=1270, height=632, bg = "black", border = 0, highlightthickness = 0)
        self.konten.place(x = 0, y = 93)

        backgroundcanvas1 = self.konten.create_image(630, 300, image = background)
        text1label = self.konten.create_image(363.0, 174.0, image=text1)
        text2label = self.konten.create_image(371.0, 305.0, image=text2)
        pesan_sekarang_tombol = Button(self.konten, image=pesan_sekarang, command = lambda:self.switch(self.tombol_pesan, self.b, self.pesanpage), borderwidth=0, highlightthickness=0, relief="flat")
        pesan_sekarang_tombol.place(x=70.0, y=374.0, width=309.0, height=56.0)
        self.banner = Label(self.konten, border = 0)
        self.banner.place(x = 720, y = 120)
        self.x = 1
        self.move()


    def switch(self, btn, idn, page) :
        for child in self.header.winfo_children() :
            if isinstance(child, Button) :
                child["fg"] = "#1D1E2C"

        btn["fg"] = "#266DD3"

        for frame in self.konten.winfo_children() :
            self.konten.destroy()

        page()

        if idn == self.b :
            self.a.place_forget()
            self.b.place(x = 593, y = 60)
            self.c.place_forget()
            self.d.place_forget()
        elif idn == self.c :
            self.a.place_forget()
            self.b.place_forget()
            self.c.place(x = 734, y = 60)
            self.d.place_forget()
        elif idn == self.d :
            self.a.place_forget()
            self.b.place_forget()
            self.c.place_forget()
            self.d.place(x = 869, y = 60)
        elif idn == self.a :
            self.a.place(x = 448, y = 60)
            self.b.place_forget()
            self.c.place_forget()
            self.d.place_forget()    
 
    def pesanpage(self) :
        self.konten = Canvas(self.canvas, width=1270, height=632, border = 0, highlightthickness = 0)
        self.konten.place(x = 0, y = 93)
        backgroundcanvas1 = self.konten.create_image(630, 300, image = background)

        setlokasilabel = self.konten.create_image(170.0, 103.0, image= setlokasi)
        tombol_atur = Button(self.konten,image=atur_lokasi,borderwidth=0,highlightthickness=0,command = self.atur_lokasi_pop,relief="flat")
        tombol_atur.place(x=442.0,y=93.0,width=136.0,height=25)
        pinlabel = self.konten.create_image(120.0, 185.0, image=pin)
        titikjemputlabel = self.konten.create_image(362.4823913574219, 157.10890197753906, image=titik_jemput)
        self.label_jemput = Label(self.konten,font = ("Maison Neue Light", 13),fg = "#FDFCFF",bg = "#1D1E2C", text = f'Titik jemput',width = 39,anchor = "w",justify = "left")
        self.label_jemput.place(x = 170, y = 139)
        tujuanpengantaranlabel = self.konten.create_image(362.4823913574219,222.71197509765625,image=titik_jemput)
        self.label_tujuan = Label(self.konten, font = ("Maison Neue Light", 13),fg = "#FDFCFF",bg = "#1D1E2C",text = f'Tujuan Pengantaran',width = 39,anchor = "w",justify = "left")
        self.label_tujuan.place(x = 170, y = 204)
        metodepembayaranlabel = self.konten.create_image(267.0594024658203,336.63226318359375,image=metode_pembayaran)
        label_metode = Label(self.konten,font = ("Maison Neue Light", 9),fg = "#FDFCFF",bg = "#1D1E2C",text = f'Metode pembayaran',width = 20,anchor = "w",justify = "left"    )
        label_metode.place(x = 165, y = 311)
        label_pembayaran = Label(self.konten,font = ("Maison Neue", 14),fg = "#FDFCFF",bg = "#1D1E2C",text = f'Tunai',width = 10,anchor = "w",justify = "left"    )
        label_pembayaran.place(x = 166, y = 328)
        textbiayalabel = self.konten.create_image(265.0,281.0,image=text_biaya)
        tarif = 0
        self.label_tarif = Label(self.konten,font = ("Maison Neue", 14),fg = "#1D1E2C",bg = "#e8e9ed",text = f'Rp {tarif}',width = 10,anchor = "e",justify = "right"    )
        self.label_tarif.place(x = 460, y = 266)
        tombol_pesan = Button(self.konten,image=pesan,borderwidth=0,highlightthickness=0,command= self.pesandriver,relief="flat")
        tombol_pesan.place(x=145.22222900390625,y=377.1944580078125,width=246.27777099609375,height=50.8055419921875)
        button_8 = Button(self.konten,image=button_image_8,borderwidth=0,highlightthickness=0,command=lambda: print("button_8 clicked"),relief="flat")
        button_8.place(x=351.02777099609375,y=320.52777099609375,width=17.326339721679688,height=22.388885498046875)
        denahkampuslabel = self.konten.create_image(968.2011108398438,60.0,image=denah_kampus)
        denahlabel = self.konten.create_image(960.0,274.0,image=denah)

    def pesanpage2(self) :
        self.konten = Canvas(self.canvas, width=1270, height=632, border = 0, highlightthickness = 0)
        self.konten.place(x = 0, y = 93)
        backgroundcanvas1 = self.konten.create_image(630, 300, image = background)

        noticelabel = self.konten.create_image(635.0, 73.0, image= notice)
        detailperjalananlabel = self.konten.create_image(235.0, 164.0, image= detailperjalanan)
        pinlabel2 = self.konten.create_image(145.0, 245.0, image=pin2)
        titikjemputlabel2 = self.konten.create_image(390.0, 215.0, image=titik_jemput2)
        label_jemput2 = Label(self.konten,font = ("Maison Neue Light", 13),fg = "#FDFCFF",bg = "#1D1E2C",text = f'{self.titikjemput}',width = 39,anchor = "w",justify = "left")
        label_jemput2.place(x = 195, y = 197)
        tujuanpengantaranlabel2 = self.konten.create_image(390.0, 281.0,image=titik_jemput2)
        label_tujuan2 = Label(self.konten, font = ("Maison Neue Light", 13),fg = "#FDFCFF",bg = "#1D1E2C",text = f'{self.tujuanpengantaran}',width = 39,anchor = "w",justify = "left")
        label_tujuan2.place(x = 195, y = 262)
        detaildriverlabel = self.konten.create_image(795.0, 164.0, image= detaildriver)
        driverlabel = self.konten.create_image(930.0, 243.0, image=driver)
        avatarlabel = self.konten.create_image(780.0, 242.0, image= avatardriver)
        label_driver = Label(self.konten, font = ("Maison Neue", 20, "bold"),fg = "#FDFCFF",bg = "#1D1E2C",text = f'{self.driver}',width = 10,anchor = "w",justify = "left")
        label_driver.place(x = 840, y = 210)
        label_plat = Label(self.konten, font = ("Maison Neue Light", 13),fg = "#FDFCFF",bg = "#1D1E2C",text = f'{self.plat}',width = 10,anchor = "w",justify = "left")
        label_plat.place(x = 841, y = 240)
        detailpembayaranlabel = self.konten.create_image(250.0, 374.0, image= detailpembayaran)
        label_tarif2 = Label(self.konten,font = ("Maison Neue", 14),fg = "#1D1E2C",bg = "#e8e9ed",text = f'Rp {self.tarif}',width = 10,anchor = "e",justify = "right")
        label_tarif2.place(x = 450, y = 365)
        label_metode = Label(self.konten,font = ("Maison Neue", 14),fg = "#1D1E2C",bg = "#e8e9ed",text = f'Tunai',width = 10,anchor = "e",justify = "right"    )
        label_metode.place(x = 450, y = 398)
        tombol_selesai = Button(self.konten,image= selesai,borderwidth=0,highlightthickness=0,command= self.struk,relief="flat")
        tombol_selesai.place(x=110.0,y=455.0,width=246.27777099609375,height=50.8055419921875)
        tombol_batal = Button(self.konten,image= batal,borderwidth=0,highlightthickness=0,command= self.batal,relief="flat", border = 0)
        tombol_batal.place(x=386.0,y=455.0,width=243.0,height=51.0)

    def riwayatpage(self) :
        self.konten = Canvas(self.canvas, width=1270, height=632, bg = "black", border = 0, highlightthickness = 0)
        self.konten.place(x = 0, y = 93)
        backgroundcanvas1 = self.konten.create_image(630, 300, image = background)

        framelabel = self.konten.create_image(641.0, 275.0, image=frame)
        framehead = self.konten.create_image(640.0, 121.0, image=head_table)
        self.isi_riwayat = Frame(self.konten, width = 1069, height= 360, bg = "#F8F9FA")
        self.isi_riwayat.place(x = 105, y = 145)
        if self.pesanan == 0 :
            self.pesanan = 0
        if 0 < self.pesanan <= 5 :
            self.tambah_riwayat(1, 0)
        if 1 < self.pesanan <= 5 :
            self.tambah_riwayat(2, 38)
        if 2 < self.pesanan <= 5 :
            self.tambah_riwayat(3, 76)
        if 3 < self.pesanan <= 5 :
            self.tambah_riwayat(4, 114)
        if 4 < self.pesanan <= 5 :
            self.tambah_riwayat(5, 152)

    def mappage(self) :
        self.konten = Canvas(self.canvas, width=1270, height=632, bg = "black", border = 0, highlightthickness = 0)
        self.konten.place(x = 0, y = 93)
        backgroundcanvas1 = self.konten.create_image(630, 300, image = background)

    def atur_lokasi_pop(self) :
        global atur_widget
        atur_widget = Toplevel(window)
        atur_widget.title("Set Lokasi")
        atur_widget.geometry("460x390")

        self.frame = Frame(atur_widget)
        self.frame.pack()

        self.kampus = {
            "" : [""],
            "Ketintang" : ["", "FMIPA", "FT", "FEB", "FISH", "Vokasi"],
            "Lidah Wetan" : ["", "FIP", "FBS", "FK", "FIKK"]
        }

        #TITIK JEMPUT
        #============================================================================
        self.titik_jemput = LabelFrame(self.frame, text = "Titik Jemput")
        self.titik_jemput.grid(row = 0, column = 0, padx = 20, pady = 10)

        lokasi_kampus = Label(self.titik_jemput, text = "Lokasi Kampus")
        lokasi_kampus.grid(row = 0, column=0)
        self.kampus_box = ttk.Combobox(self.titik_jemput, values = list(self.kampus.keys()))
        self.kampus_box.bind('<<ComboboxSelected>>', self.getFakultas)
        self.kampus_box.grid(row = 1, column=0)

        fakultas_label = Label(self.titik_jemput, text = "Fakultas")
        fakultas_label.grid(row = 2, column=0)
        self.fakultas_box = ttk.Combobox(self.titik_jemput)
        self.fakultas_box.grid(row = 3, column=0)

        gedung1 = Label(self.titik_jemput, text = "Gedung (Opsional)")
        gedung1.grid(row = 2, column=1)
        self.gedung_box = Entry(self.titik_jemput, width = 23)
        self.gedung_box.grid(row = 3, column=1)

        for widget in self.titik_jemput.winfo_children() :
            widget.grid_configure(padx = 20, pady = 3)

        kosong = Label(self.titik_jemput)
        kosong.grid(row = 4, column=0)

        #TUJUAN PENGANTARAN
        #============================================================================
        self.tujuan_pengantaran = LabelFrame(self.frame, text = "Tujuan Pengantaran")
        self.tujuan_pengantaran.grid(row = 1, column = 0, padx = 20, pady = 10)

        lokasi_kampus2 = Label(self.tujuan_pengantaran, text = "Lokasi Kampus")
        lokasi_kampus2.grid(row = 0, column=0)
        self.kampus_box2 = ttk.Combobox(self.tujuan_pengantaran, values = list(self.kampus.keys()))
        self.kampus_box2.bind('<<ComboboxSelected>>', self.getFakultas2)
        self.kampus_box2.grid(row = 1, column=0)

        fakultas2 = Label(self.tujuan_pengantaran, text = "Fakultas")
        fakultas2.grid(row = 2, column=0)
        self.fakultas_box2 = ttk.Combobox(self.tujuan_pengantaran)
        self.fakultas_box2.grid(row = 3, column=0)

        gedung2 = Label(self.tujuan_pengantaran, text = "Gedung (Opsional)")
        gedung2.grid(row = 2, column=1)
        self.gedung_box2 = Entry(self.tujuan_pengantaran, width = 23)
        self.gedung_box2.grid(row = 3, column=1)

        for widget in self.tujuan_pengantaran.winfo_children() :
            widget.grid_configure(padx = 20, pady = 3)

        kosong2 = Label(self.tujuan_pengantaran)
        kosong2.grid(row = 4, column=0)

        #BUTTON ATUR
        #============================================================================
        self.button = Button(self.frame, text = "Atur lokasi", bg = "blue", fg = "white", border = 0, command = self.update_lokasi)
        self.button.grid(sticky="news", padx = 20, pady = 10)

    def getFakultas(self, event) :
        self.fakultas_box["values"] = self.kampus[self.kampus_box.get()]

    def getFakultas2(self, event) :
        self.fakultas_box2["values"] = self.kampus[self.kampus_box2.get()]   

    def update_lokasi(self) :
        q = self.kampus_box.get() 
        r = self.fakultas_box.get()
        s = self.gedung_box.get()
        self.titikjemput = f'{s} - {r}/{q}'
        if s == "" :
            self.titikjemput = f'{r}/{q}'
        self.label_jemput.config(text = f'{self.titikjemput}')

        x = self.kampus_box2.get() 
        y = self.fakultas_box2.get()
        z = self.gedung_box2.get()
        self.tujuanpengantaran = f'{z} - {y}/{x}'
        if z == "" :
            self.tujuanpengantaran = f'{y}/{x}'
        self.label_tujuan.config(text = f'{self.tujuanpengantaran}')  

        self.lolos = True
        if r == y :
            messagebox.showinfo("Pemberitahuan", "Titik jemput dan tujuan pengantaran tidak bisa fakultas yang sama")
            self.lolos = False
        elif r == "FMIPA" :
            if y == "FT" :
                tarif = 3000
            elif y == 'Vokasi' or y == 'FEB':
                tarif = 5000
            elif y == "FISH":
                tarif = 7000
            else:
                tarif = 20000
        elif r == 'FT':
            if y == 'FEB':
                tarif = 5000
            elif y == 'FISH'or y == 'Vokasi':
                tarif = 7000
            elif y == 'FMIPA':
                tarif = 3000
            else:
                tarif = 20000
        elif r == 'FEB':
            if y == 'FISH':
                tarif = 3000
            elif y == 'Vokasi' or y == 'FT' or y == 'FMIPA':
                tarif = 5000
            else:
                tarif = 20000
        elif r == 'FISH':
            if y == 'Vokasi':
                tarif = 5000
            elif y == 'FT' or y == 'FMIPA':
                tarif = 7000
            elif y == 'FEB':
                tarif = 3000
            else:
                tarif = 20000
        elif r == 'Vokasi':
            if y == 'FISH'or y == 'FEB':
                tarif = 5000
            elif y == 'FMIPA':
                tarif = 5000
            elif y == 'FT':
                tarif = 7000
            else:
                tarif = 20000
        elif r == 'FIP':
            if y == 'FK':
                tarif = 3000
            elif y == 'FIKK' or y == 'FBS':
                tarif = 5000
            else:
                tarif = 20000
        elif r == 'FBS':
            if y == 'FIP':
                tarif = 5000
            elif y == 'FK'or y == 'FIKK':
                tarif = 7000
            else:
                tarif = 20000
        elif r == 'FK':
            if y == 'FIP':
                tarif = 3000
            elif y == 'FBS' or y == 'FIKK':
                tarif = 7000
            else:
                tarif = 20000
        elif r == 'FIKK':
            if y == 'FIP':
                tarif = 5000
            elif y == 'FBS' or y == 'FK':
                tarif = 7000
            else:
                tarif = 20000

        self.label_tarif.config(text = f'Rp {tarif}')
        self.tarif = tarif
        atur_widget.destroy()

    def pesandriver(self) :
        import random

        if self.label_jemput.cget("text") == self.label_tujuan.cget("text") :
            messagebox.showinfo("Pemberitahuan", "Titik jemput dan tujuan pengantaran tidak bisa fakultas yang sama")
        elif self.label_jemput.cget("text") == 'Titik jemput' or self.label_tujuan.cget("text") == 'Tujuan Pengantaran' :
            messagebox.showinfo("Pemberitahuan", "Anda belum mengisi lokasi yang diperlukan untuk pemesanan")
        elif self.label_jemput.cget("text") == '/' or self.label_jemput.cget("text") == '/Ketintang' or self.label_jemput.cget("text") == '/Lidah Wetan' :
            messagebox.showinfo("Pemberitahuan", "Anda belum mengisi lokasi yang diperlukan untuk pemesanan")
        elif self.label_tujuan.cget("text") == '/' or self.label_tujuan.cget("text") == '/Ketintang' or self.label_tujuan.cget("text") == '/Lidah Wetan' :
            messagebox.showinfo("Pemberitahuan", "Anda belum mengisi lokasi yang diperlukan untuk pemesanan")
        else :
            driver_list = {
                "Hidayat" : "L 3456 DH",
                "Abdul" : "L 3297 NG",
                "Wahyu" : "L 1968 WT",
                "Budi" : "L 6143 WRU",
                "Kurniawan" : "L 6546 OG",
                "Agung" : "L 2584 PJ",
                "Setiawan" : "L 2617 ET"
            }
            self.driver = random.choice(list(driver_list.keys()))
            self.plat = driver_list[self.driver]
            self.tanggal = time.strftime("%#d %B %Y")
            self.jam = time.strftime("%R")

            self.konten = Canvas(self.canvas, width=1270, height=632, border = 0, highlightthickness = 0)
            self.konten.place(x = 0, y = 93)
            backgroundcanvas1 = self.konten.create_image(630, 300, image = background)
            denahlabel = self.konten.create_image(648.0,270.0,image=denah2)
            self.banner = Label(self.konten, border = 0)
            self.banner.place(x = 600, y = 180)
            self.loadtext = Label(self.konten, text = "Mencari driver ...", font = ("Poppins", 30), bg = "#FDFCFF")
            self.loadtext.place(x = 490, y = 280)
            self.x = 1
            self.y = 1
            self.move2()

    def struk(self) :
        self.pesanan += 1
        brp = self.pesanan
        self.status = "Sudah sampai tujuan"

        # isiriwayat = f'{self.status}, {self.titikjemput}, {self.tujuanpengantaran}, {self.tarif}, Tunai, {self.driver}, {self.plat}, {self.tanggal}, {self.jam}'
        # file_pesanan = open(f'pesanan{brp}.txt', "w")
        # print(isiriwayat, file = file_pesanan)
        # file_pesanan.close()

        global strukk
        self.strukk = Toplevel(window)
        self.strukk.title("Struk pemesanan")
        self.strukk.geometry("400x380")

        Label(self.strukk, text = "**NESARIDE**", font = ("Fake Receipt Fontt", 16)).place(x = 130, y = 1)
        Label(self.strukk, text= f"Nama pemesan     \t   :  {self.username}", font = ("Fake Receipt Font", 11)).place(x = 10, y = 50)
        Label(self.strukk, text= f"Tanggal pemesanan  :  {self.tanggal}", font = ("Fake Receipt Font", 11)).place(x = 10, y = 75)
        Label(self.strukk, text= f"Waktu pemesanan \t   :  {self.jam}", font = ("Fake Receipt Font", 11)).place(x = 10, y = 100)
        Label(self.strukk, text="="*34, font = ("Fake Receipt Fontt", 14)).place(x=5,y=125)
        Label(self.strukk, text= f"Nama driver              \t :  {self.driver}", font = ("Fake Receipt Font", 11)).place(x=10, y=150)
        Label(self.strukk, text= f"Titik jemput                 \t :  {self.titikjemput}", font = ("Fake Receipt Font", 11)).place(x=10, y=171)
        Label(self.strukk, text= f"Tujuan pengantaran \t :  {self.tujuanpengantaran}", font = ("Fake Receipt Font", 11)).place(x=10, y=192)
        Label(self.strukk, text= f"Biaya perjalanan         \t :  Rp {self.tarif}", font = ("Fake Receipt Font", 11)).place(x=10, y=213)
        Label(self.strukk, text= f"Metode pembayaran\t :  Tunai", font = ("Fake Receipt Font", 11)).place(x=10, y=234)
        Label(self.strukk, text="="*34, font = ("Fake Receipt Fontt", 14)).place(x=5,y=259)
        Label(self.strukk, text = "TERIMAKASIH", font = ("Fake Receipt Fontt", 13)).place(x = 145, y = 280)
        Button(self.strukk, text = "Ok", fg = "white", bg = "blue", border = 0, font = ("Poppins",10), width=9, command = self.back).place(x = 300, y = 330)

    def back(self) :
        self.strukk.destroy()
        self.switch(self.tombol_home, self.a, self.homepage)
        self.konten.after(1000, self.rating)

    def rating(self) :
        self.frame_rating = Frame(self.konten, width = 355, height=360)
        self.frame_rating.place(x = 500, y = 57)

        self.canvas_rating = Canvas(self.frame_rating, width = 355, height = 360)
        self.canvas_rating.place(x = 0, y = 0)

        framelabel = self.canvas_rating.create_image(178.0, 181.0, image=frame1)

        textlabel = self.canvas_rating.create_image(177.0, 45.0, image=textr)

        self.bintang0tombol = Button(self.canvas_rating, image=bintang0, command = lambda: self.isi(1), borderwidth=0, highlightthickness=0, relief="flat")
        self.bintang0tombol.place(x=24.0, y=82.0, width=50.0, height=50.0)

        self.bintang1tombol = Button(self.canvas_rating, image=bintang0, command = lambda: self.isi(2), borderwidth=0, highlightthickness=0, relief="flat")
        self.bintang1tombol.place(x=88.0, y=82.0, width=50.0, height=50.0)

        self.bintang2tombol = Button(self.canvas_rating, image=bintang0, command = lambda: self.isi(3), borderwidth=0, highlightthickness=0, relief="flat")
        self.bintang2tombol.place(x=152.0, y=82.0, width=50.0, height=50.0)

        self.bintang3tombol = Button(self.canvas_rating, image=bintang0, command = lambda: self.isi(4), borderwidth=0, highlightthickness=0, relief="flat")
        self.bintang3tombol.place(x=216.0, y=82.0, width=50.0, height=50.0)

        self.bintang4tombol = Button(self.canvas_rating, image=bintang0, command = lambda: self.isi(5), borderwidth=0, highlightthickness=0, relief="flat")
        self.bintang4tombol.place(x=280.0, y=82.0, width=50.0, height=50.0)

        d1label = self.canvas_rating.create_image(178.0, 213.0, image=d1)

        label_driver2 = Label(self.canvas_rating, font = ("Maison Neue", 20, "bold"),fg = "#FDFCFF",bg = "#1D1E2C",text = f'{self.driver}',width = 10,anchor = "w",justify = "left")
        label_driver2.place(x = 145, y = 190)
        label_plat = Label(self.canvas_rating, font = ("Maison Neue Light", 13),fg = "#FDFCFF",bg = "#1D1E2C",text = f'{self.plat}',width = 10,anchor = "w",justify = "left")
        label_plat.place(x = 146, y = 220)

        self.lolos = False
        kirimtombol = Button(self.canvas_rating, image=kirim, borderwidth=0, highlightthickness=0, relief="flat", command = self.kirimm)
        kirimtombol.place(x=30.0, y=295.0, width=296.0, height=48.0)

    def isi(self, urutan) :
        self.lolos = True
        if urutan == 1 :
            self.bintang0tombol.config(image = bintang1)
            self.bintang1tombol.config(image = bintang0)
            self.bintang2tombol.config(image = bintang0)
            self.bintang3tombol.config(image = bintang0)
            self.bintang4tombol.config(image = bintang0)
            self.bintang = 1
        elif urutan == 2 :
            self.bintang0tombol.config(image = bintang1)
            self.bintang1tombol.config(image = bintang1)
            self.bintang2tombol.config(image = bintang0)
            self.bintang3tombol.config(image = bintang0)
            self.bintang4tombol.config(image = bintang0)
            self.bintang = 2
        elif urutan == 3 :
            self.bintang0tombol.config(image = bintang1)
            self.bintang1tombol.config(image = bintang1)
            self.bintang2tombol.config(image = bintang1)
            self.bintang3tombol.config(image = bintang0)
            self.bintang4tombol.config(image = bintang0)
            self.bintang = 3
        elif urutan == 4 :
            self.bintang0tombol.config(image = bintang1)
            self.bintang1tombol.config(image = bintang1)
            self.bintang2tombol.config(image = bintang1)
            self.bintang3tombol.config(image = bintang1)
            self.bintang4tombol.config(image = bintang0)
            self.bintang = 4
        elif urutan == 5 :
            self.bintang0tombol.config(image = bintang1)
            self.bintang1tombol.config(image = bintang1)
            self.bintang2tombol.config(image = bintang1)
            self.bintang3tombol.config(image = bintang1)
            self.bintang4tombol.config(image = bintang1)
            self.bintang = 5

    def kirimm(self) :
        if self.lolos == False :
            messagebox.showinfo("Pemberitahuan", "Mohon beri rating untuk driver.")
        else : 
            self.frame_rating.destroy()
            brp = self.pesanan
            isiriwayat = f'{self.status},{self.titikjemput},{self.tujuanpengantaran},{self.tarif},Tunai,{self.driver},{self.plat},{self.bintang},{self.tanggal},{self.jam}'
            file_pesanan = open(f'pesanan{brp}.txt', "w")
            print(isiriwayat, file = file_pesanan)
            file_pesanan.close()

    def tambah_riwayat(self, urutan, letak) :
        bukafile = open(f"pesanan{urutan}.txt", "r")
        lines = bukafile.readlines()
        for kata in lines :
            data = kata.strip().split(',')
            rstatus = data[0]
            rakhir = data[2]
            rtanggal = data[8]
            rjam = data[9]
        bukafile.close()

        isi1 = Frame(self.isi_riwayat, bg = "#d9d9d9", width = 1068, height=28)
        isi1.place(x = 0, y = letak)
        Label(isi1, text = f'{rakhir}', bg = "#d9d9d9", fg = "#1D1E2C", font = ("Maison Neue", 10, "bold")).place(x = 12, y = 6)
        Label(isi1, text = f'{rstatus}', bg = "#d9d9d9", fg = "#1D1E2C", font = ("Maison Neue", 10, "bold")).place(x = 303, y = 6)
        Label(isi1, text = f'{rtanggal}', bg = "#d9d9d9", fg = "#1D1E2C", font = ("Maison Neue", 10, "bold")).place(x = 587, y = 6)
        Label(isi1, text = f'{rjam}', bg = "#d9d9d9", fg = "#1D1E2C", font = ("Maison Neue", 10, "bold")).place(x = 837, y = 6)
        Button(isi1, text = "Lihat Detail", bg = "#d9d9d9", fg = "#1D1E2C", font = ("Maison Neue Light", 10), border = 0, cursor = "hand2", command = lambda: self.tampilkan_riwayat(urutan)).place(x = 975, y = 2)

    def batal(self) :
        self.frame_batal = Frame(self.konten, width = 355, height=360)
        self.frame_batal.place(x = 500, y = 57)
        self.canvas_batal = Canvas(self.frame_batal, width = 355, height = 360)
        self.canvas_batal.place(x = 0, y = 0)
        framelabel = self.canvas_batal.create_image(178.0, 181.0, image=frame1)

        Button(self.frame_batal, text = "X", command = self.batalback, border = 0, width= 1, bg = "#F8F9FA", font = ("Maison Neue", 10)).place(x = 335, y = 5)
        Label(self.frame_batal, text = "Kenapa kamu ingin membatalkan", bg = "#F8F9FA", font = ("Maison Neue", 15, "bold")).place(x = 20, y = 20)
        Label(self.frame_batal, text = "pesanan?", bg = "#F8F9FA", font = ("Maison Neue", 15, "bold")).place(x = 20, y = 43)
        self.selec = StringVar(value = " ")
        Radiobutton(self.frame_batal, text = "Driver minta order dibatalkan", variable=self.selec, value = "Driver minta order dibatalkan", font = ("Maison Neue Light", 13), bg = "#F8F9FA").place(x = 20, y = 80)
        Radiobutton(self.frame_batal, text = "Saya sudah menunggu terlalu lama", variable=self.selec, value = "Saya sudah menunggu terlalu lama", font = ("Maison Neue Light", 13), bg = "#F8F9FA").place(x = 20, y = 120)
        Radiobutton(self.frame_batal, text = "Saya menemukan transportasi lain", variable=self.selec, value = "Saya menemukan transportasi lain", font = ("Maison Neue Light", 13), bg = "#F8F9FA").place(x = 20, y = 160)
        Radiobutton(self.frame_batal, text = "Driver tidak bisa dihubungi", variable=self.selec, value = "Driver tidak bisa dihubungi", font = ("Maison Neue Light", 13), bg = "#F8F9FA").place(x = 20, y = 200)
        lainnya = Entry(self.frame_batal, text = "", bg = "#F8F9FA", border = 0, font = ("Maison Neue Light", 13), width = 25)
        lainnya.place(x = 45, y = 245)
        lainnya.insert(0, "Lainnya")
        Frame(self.frame_batal, width = 275, height = 3, bg = "black").place(x = 40, y = 270)
        kirimtombol = Button(self.frame_batal, image=kirim, borderwidth=0, highlightthickness=0, relief="flat", command = self.batalkirim)
        kirimtombol.place(x=30.0, y=295.0, width=296.0, height=48.0)

    def batalback(self) :
        self.frame_batal.destroy()

    def batalkirim(self) :
        self.pesanan += 1
        brp = self.pesanan
        self.status = "Pesanan dibatalkan"
        alasan = self.selec.get()

        isiriwayat = f'{self.status},{self.titikjemput},{self.tujuanpengantaran},{self.tarif},Tunai,{self.driver},{self.plat},{alasan},{self.tanggal},{self.jam}'
        file_pesanan = open(f'pesanan{brp}.txt', "w")
        print(isiriwayat, file = file_pesanan)
        file_pesanan.close()

        self.switch(self.tombol_home, self.a, self.homepage)

    def tampilkan_riwayat(self, urutan) :
        self.konten.destroy()
        bukafile = open(f"pesanan{urutan}.txt", "r")
        lines = bukafile.readlines()
        for kata in lines :
            data = kata.strip().split(',')
            rstatus = data[0]
            rawal = data[1]
            rakhir = data[2]
            rtarif = data[3]
            rmetode = data[4]
            rdriver = data[5]
            rplat =  data[6]
            rbintang = data[7]
            rtanggal = data[8]
            rjam = data[9]
        bukafile.close()

        self.konten = Canvas(self.canvas, width=1270, height=632, bg = "black", border = 0, highlightthickness = 0)
        self.konten.place(x = 0, y = 93)

        backgroundcanvas1 = self.konten.create_image(630, 300, image = background)

        framelabel = self.konten.create_image(641.0,286.0,image=framer2)

        logo2 = self.konten.create_image(275.0,81.0,image= logo_nesaride)
        Label(self.konten, text = rstatus, font = ("poppins Medium", 18), bg = "#F8F9FA").place(x = 110, y = 105)
        Label(self.konten,font = ("Maison Neue Light", 14),fg = "#1D1E2C",bg = "#F8F9FA",text = f'{rtanggal},  {rjam}',width = 20,anchor = "e",justify = "right").place(x = 928, y = 65)

        framedlabel = self.konten.create_image(355.0,257.0,image=driver)
        avatarlabel = self.konten.create_image(205.0, 257.0, image= avatardriver)
        label_driver = Label(self.konten, font = ("Maison Neue", 20, "bold"),fg = "#FDFCFF",bg = "#1D1E2C",text = rdriver,width = 10,anchor = "w",justify = "left")
        label_driver.place(x = 265, y = 225)
        label_plat = Label(self.konten, font = ("Maison Neue Light", 13, "bold"),fg = "#FDFCFF",bg = "#1D1E2C",text = rplat,width = 10,anchor = "w",justify = "left")
        label_plat.place(x = 265, y = 255)

        if rstatus == "Sudah sampai tujuan":
            rrbintang = int(rbintang)
            self.bintang_akhir(rrbintang)
        else :
            Label(self.konten, text = f'Dibatalkan - {rbintang}', bg = "#F8F9FA", font = ("Maison Neue", 15)).place(x =155, y = 360)

        garislabel = self.konten.create_image(642.0,316.0,image=garis)

        perjalananlabel = self.konten.create_image(917.0,245.0,image=perjalanan)
        label_jemput = Label(self.konten,font = ("Maison Neue Light", 13),fg = "#FDFCFF",bg = "#1D1E2C", text = rawal,width = 39,anchor = "w",justify = "left")
        label_jemput.place(x = 750, y = 215)
        label_tujuan = Label(self.konten,font = ("Maison Neue Light", 13),fg = "#FDFCFF",bg = "#1D1E2C", text = rakhir,width = 39,anchor = "w",justify = "left")
        label_tujuan.place(x = 750, y = 280)

        text1label = self.konten.create_image(811.0,403.0,image=detailpembayaran)
        label_tarif2 = Label(self.konten,font = ("Maison Neue", 14),fg = "#1D1E2C",bg = "#F8F9FA",text = f'Rp {rtarif}',width = 10,anchor = "e",justify = "right")
        label_tarif2.place(x = 950, y = 398)
        label_metode = Label(self.konten,font = ("Maison Neue", 14),fg = "#1D1E2C",bg = "#F8F9FA",text = rmetode,width = 10,anchor = "e",justify = "right"    )
        label_metode.place(x = 950, y = 428)

        kembalil = Button(self.konten, image=kembali, borderwidth=0, highlightthickness=0, relief="flat", command = lambda: self.switch(self.tombol_riwayat, self.d, self.riwayatpage))
        kembalil.place(x=1053.0, y=487.0, width=134.0, height=35.0)

    def bintang_akhir(self, berapa) :
        if berapa == 1 :
            bintangke1 = self.konten.create_image(187.0,379.0,image=bintang2)
            bintangke2 = self.konten.create_image(271.4967346191406,379.0,image=bintang3)
            bintangke3 = self.konten.create_image(355.99346923828125,379.0,image=bintang3)
            bintangke4 = self.konten.create_image(440.49017333984375,379.0,image=bintang3)
            bintangke5 = self.konten.create_image(524.9869079589844,379.0,image=bintang3)
        elif berapa == 2 :
            bintangke1 = self.konten.create_image(187.0,379.0,image=bintang2)
            bintangke2 = self.konten.create_image(271.4967346191406,379.0,image=bintang2)
            bintangke3 = self.konten.create_image(355.99346923828125,379.0,image=bintang3)
            bintangke4 = self.konten.create_image(440.49017333984375,379.0,image=bintang3)
            bintangke5 = self.konten.create_image(524.9869079589844,379.0,image=bintang3)
        elif berapa == 3 :
            bintangke1 = self.konten.create_image(187.0,379.0,image=bintang2)
            bintangke2 = self.konten.create_image(271.4967346191406,379.0,image=bintang2)
            bintangke3 = self.konten.create_image(355.99346923828125,379.0,image=bintang2)
            bintangke4 = self.konten.create_image(440.49017333984375,379.0,image=bintang3)
            bintangke5 = self.konten.create_image(524.9869079589844,379.0,image=bintang3)
        elif berapa == 4 :
            bintangke1 = self.konten.create_image(187.0,379.0,image=bintang2)
            bintangke2 = self.konten.create_image(271.4967346191406,379.0,image=bintang2)
            bintangke3 = self.konten.create_image(355.99346923828125,379.0,image=bintang2)
            bintangke4 = self.konten.create_image(440.49017333984375,379.0,image=bintang2)
            bintangke5 = self.konten.create_image(524.9869079589844,379.0,image=bintang3)
        elif berapa == 5 :
            bintangke1 = self.konten.create_image(187.0,379.0,image=bintang2)
            bintangke2 = self.konten.create_image(271.4967346191406,379.0,image=bintang2)
            bintangke3 = self.konten.create_image(355.99346923828125,379.0,image=bintang2)
            bintangke4 = self.konten.create_image(440.49017333984375,379.0,image=bintang2)
            bintangke5 = self.konten.create_image(524.9869079589844,379.0,image=bintang2)

    def move(self) :
        if self.x == 3 :
            self.x = 1
        if self.x == 1 :
            self.banner.config(image = banner1)
        elif self.x == 2 :
            self.banner.config(image = banner2)
        self.x += 1
        self.banner.after(4000, self.move)

    def move2(self) :
        if self.y != 20 :
            if self.x == 5 :
                self.x = 1
            if self.x == 1 :
                self.banner.config(image = load1)
            elif self.x == 2 :
                self.banner.config(image = load2)
            elif self.x == 3 :
                self.banner.config(image = load3)
            elif self.x == 4 :
                self.banner.config(image = load4)
            self.x += 1
            self.y += 1
            self.banner.after(150, self.move2)
        else :
            self.banner.config(image = load5)
            self.loadtext.config(text = "Driver telah didapat")
            self.loadtext.place(x = 445)
            self.banner.after(2000, self.pesanpage2)


loginpage()
window.mainloop()