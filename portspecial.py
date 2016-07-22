import os
IPS="10.1.1."#IP Range
NATIP="222.239.87.195"#Public IP
for num in range(100,256):
      num2=int(str(num)+"99")+20000
      num1=int(str(num)+"00")+20000
      num3=num1=int(str(num)+"00")+20001
      num4=num1=int(str(num)+"00")+20002
      command1="iptables -t nat -A PREROUTING -d "+NATIP+" -p tcp --dport "+str(num1)+" -j DNAT --to "+IPS+str(num)+":22"
      command7="iptables -t nat -A PREROUTING -d "+NATIP+" -p udp --dport "+str(num1)+" -j DNAT --to "+IPS+str(num)+":22"
      command5="iptables -t nat -A PREROUTING -d "+NATIP+" -p tcp --dport "+str(num3)+" -j DNAT --to "+IPS+str(num)+":3389"
      command6="iptables -t nat -A PREROUTING -d "+NATIP+" -p udp --dport "+str(num3)+" -j DNAT --to "+IPS+str(num)+":3389"      
      command4="iptables -t nat -A PREROUTING -p tcp --dport "+str(num4)+":"+str(num2)+" -j DNAT --to "+IPS+str(num)+":"+str(num4)+"-"+str(num2)
      command3="iptables -t nat -A PREROUTING -p udp --dport "+str(num4)+":"+str(num2)+" -j DNAT --to "+IPS+str(num)+":"+str(num4)+"-"+str(num2)
      command2="iptables -A INPUT -p tcp --dport "+str(num1)+":"+str(num2)+" --syn -m recent --name webpool --rcheck --seconds 60 --hitcount 10 -j DROP"
      os.system (command1)
      os.system (command2)
      os.system (command3)
      os.system (command4)
      os.system (command5)
      os.system (command6)
      os.system (command7)