
file = open('/home/casper/Desktop/Vidrone/VisDrone2019-MOT-train/annotations/uav0000013_00000_v.txt','r')
z = file.read()
x = z.split('\n')
print(x[0])

