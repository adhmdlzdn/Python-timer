# Simple Countdown Timer
# Original Code by Udacity (https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html)

import time, datetime

# Membuat class yang berfungsi sebagai penghitung mundur
def countdown(j, m, d):

    # Mengkalkulasi jumlah angka per detik
    total_detik = j * 3600 + m * 60 + d

    # Looping while berguna untuk mengchek apabila total_detik == 0
    # Jika total_detik != 0, pengurangan total dihitung per 1 detik
    while total_detik > 0:

        # Timer mewakili waktu yang tersisa pada penghitungan mundur
        timer = datetime.timedelta(seconds= total_detik)

        # Output waktu yang tersisa pada timer
        print(timer, end="\r")
        
        # Delay program selama 1 detik
        time.sleep(1)

        # Mengurangi total waktu tiap 1 detik
        total_detik -= 1

    print("Eittsss!!! Perhitungan udah selesai ngab!!")

# Input untuk seberapa lama waktu yang ingin dihitung mundur
j = input("Masukkan waktu dalam jam: ")
m = input("Masukkan waktu dalam menit: ")
d = input("Masukkan waktu dalam detik: ")
countdown(int(j), int(m), int(d))
