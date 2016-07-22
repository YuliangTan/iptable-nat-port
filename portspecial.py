import os
IPS="10.1.1."#IP Range
NATIP="222.239.87.195"#Public IP
for num in range(100,256):
    for num1 in range(int(str(num)+"00"),int(str(num)+"99")):
      num2=num1+20000
      if str(num1) == str(num)+"00":
        command1="iptables -t nat -A PREROUTING -d "+NATIP+" -p tcp --dport "+str(num2)+" -j DNAT --to-destination "+IPS+str(num)+":22"
        command2="iptables -t nat -A PREROUTING -d "+NATIP+" -p udp --dport "+str(num2)+" -j DNAT --to-destination "+IPS+str(num)+":22"
      elif  str(num1) == str(num)+"01":
        command1="iptables -t nat -A PREROUTING -d "+NATIP+" -p tcp --dport "+str(num2)+" -j DNAT --to-destination "+IPS+str(num)+":3389"
        command2="iptables -t nat -A PREROUTING -d "+NATIP+" -p udp --dport "+str(num2)+" -j DNAT --to-destination "+IPS+str(num)+":3389"
      else:      
        command1="iptables -t nat -A PREROUTING -d "+NATIP+" -p tcp --dport "+str(num2)+" -j DNAT --to-destination "+IPS+str(num)+":"+str(num2)
        command2="iptables -t nat -A PREROUTING -d "+NATIP+" -p udp --dport "+str(num2)+" -j DNAT --to-destination "+IPS+str(num)+":"+str(num2)
      command4="iptables -A INPUT -p tcp --dport "+str(num1)+" --syn -m recent --name webpool --rcheck --seconds 60 --hitcount 10 -j DROP"
      os.system(command1)
      os.system(command2)
      os.system(command4)