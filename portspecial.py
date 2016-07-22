import os
IPS="10.1.1."#IP Range
NATIP="222.239.87.195"#Public IP
for num in range(100,256):
    for num2 in range(int(str(num)+"00"),int(str(num)+"99")):
      num2=num2+20000
      command3="iptables -t nat -A PREROUTING -d "+NATIP+" -p all --dport "+str(num2)+" -j DNAT --to-destination "+IPS+str(num)+":"+str(num2)
      command4="iptables -A INPUT -p tcp --dport "+str(num2)+" --syn -m recent --name webpool --rcheck --seconds 60 --hitcount 10 -j DROP"
      os.system(command3)
      os.system(command4)
      print command3
      print command4