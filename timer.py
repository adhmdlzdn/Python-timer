import time

# Mulai timer
starttime = time.time()
lasttime = starttime
lapnum = 1
value = ""

print("Press ENTER untuk setiap lap.\nTekan Q dan lalu ENTER untuk berhenti")

while value.lower() != "q":

    # Input jika user menekan enter
    value = input()

    # Current lap
    laptime = round((time.time() - lasttime), 2)

    # Total waktu sejak timer dimulai
    totaltime = round((time.time() - starttime), 2)

    # Output jumlah lah, waktu, dan total
    print("Lap No. " + str(lapnum))
    print("Total Waktu: " + str(totaltime))
    print("Waktu: " + str(laptime))

    print("*"*20)

    # Mengupdate total keseluruhan waktu dan jumlah lap
    lasttime = time.time()
    lapnum += 1

print("Timer selesai!!")
