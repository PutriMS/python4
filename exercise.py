#Latihan 1
data1 =[i for i in range (10, 21) if i % 2 == 0]
data2 =[i for i in range (90, 100) if i % 2 == 1]

print(data1 + data2)

#Latihan 2

data = ["Do","Re","Mi","Fa","So","la","Ti"]
print(f"Data awal = {data}")
# data[0] = "Mi"
# data[1] = "Do"
# data[2] = "Fa"
# data[-1] = "Re"
# data[3] = "So"
# data[4] = "La"
# data[5] = "Ti"
# print(data)

del data[1]

data.append("Re")
data.remove("Do")
data.insert(1, "Do")
print(f"Data akhir = {data}")

#Latihan 3
dataa = "IgNatIus"
hasildata = []
for hbesar in dataa:
    if hbesar.isupper():
        hasildata.append(hbesar)
        
print(f"Hasil data = {hasildata}")
