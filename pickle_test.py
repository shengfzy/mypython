import pickle
ip_list = []
counter = 0
f = open(r'C:/Users/沈恺/Desktop/ip_list.pk', 'rb')
while True:
    try:
        l = pickle.load(f)
    except Exception as e:
        print(str(e))
        break
    else:
        ip_list.append(l)
        counter += 1

f.close()
