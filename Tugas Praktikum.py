# Tugas Praktikum

Nama = []
NIM = []
Tugas = []
Uts = []
Uas = []
Total = []

while True:
    nama = input('Nama: ')
    Nama.append(nama)
    nim = int(input('NIM: '))
    NIM.append(nim)
    tugas = float(input('Nilai Tugas: '))
    Tugas.append(tugas)
    uts = float(input('Nilai UTS: '))
    Uts.append(uts)
    uas = float(input('Nilai UAS: '))
    Uas.append(uas)

    _ = int(tugas)*.3 + (int(uts)*.35) + (int(uas)*.35)
    Total.append(_)

    tambah = ''
    while tambah !='y' and tambah !='t':
        tambah = input('tambah data (y/t) ? ')
    if tambah =='t':
        print('='*100)
        print('| No |\t Nama \t|   NIM   |   Tugas   |   UTS   |   UAS   |   Akhir   |')
        print('='*100)

        for i in range(len(NIM)):
            nm = '| %d. |\t%s|' % (i+1, Nama[i])
            im = '| %d' % NIM[i]
            tg = '| %.2f' % Tugas[i]
            ut = '| %.2f' % Uts[i]
            ua = '| %.2f' % Uas[i]
            tl = '| %.2f' % Total[i]

            gabung = nm + im + tg + ut + ua + tl
            print(gabung)
        break