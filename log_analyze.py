import matplotlib.pyplot as plt

# file="./pingplot_v1.1.0_172.101.1.16_2022-07-27.log"
file="./pingplot_v1.1.0_192.168.86.52_2022-07-27.log"

time = []
ping = []
total = 0
avg = 0
i = 0

for line in open(file, "r", encoding="utf-8"):

  if "TIME" in line:
    str1 = line.split(' ')
    print(str1[4], end='')
    time.append(str1[4])

  if "time" in line:
    # print(line, end='')
    str2 = line.split(' ')
    str3 = str2[6].split('time=')
    print(str3[1])
    ping.append(float(str3[1]))
    total = total + float(str3[1])
    i += 1


# print(time)
# print(ping)
print(i)
plt.axhline(y=total/i, color="red", label='avg ping time')
plt.plot(ping, linestyle=':', label='ping time') 
plt.xlabel('frequency')
plt.ylabel('round-trip times(ms)')
plt.title('Speedtest')

plt.text(i/2, total/i,'avg time =' + format(total/i, '.2f') + 'ms', 
        style='italic',
        bbox={'facecolor':'#C1FFC1', 'pad':10})  

plt.legend()
plt.show()