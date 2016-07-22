import os
IPS="10.1.0."#IP Range
NATIP="222.239.87.195"#Public IP
for num in range(11,256):
  length=len(str(num))
  if 39< num < 90:
      print "block" 
  elif length <= 10:
      command1="iptables -t nat -A PREROUTING -d "+NATIP+" -p tcp --dport "+str(num)+"00"+" -j DNAT --to "+IPS+str(num)+":22"
      command7="iptables -t nat -A PREROUTING -d "+NATIP+" -p udp --dport "+str(num)+"00"+" -j DNAT --to "+IPS+str(num)+":22"
      command5="iptables -t nat -A PREROUTING -d "+NATIP+" -p tcp --dport "+str(num)+"01"+" -j DNAT --to "+IPS+str(num)+":3389"
      command6="iptables -t nat -A PREROUTING -d "+NATIP+" -p udp --dport "+str(num)+"01"+" -j DNAT --to "+IPS+str(num)+":3389"      
      command4="iptables -t nat -A PREROUTING -p tcp --dport "+str(num)+"02:"+str(num)+"99 -j DNAT --to "+IPS+str(num)+":"+str(num)+"02-"+str(num)+"99"
      command3="iptables -t nat -A PREROUTING -p udp --dport "+str(num)+"02:"+str(num)+"99 -j DNAT --to "+IPS+str(num)+":"+str(num)+"02-"+str(num)+"99"
      command2="iptables -A INPUT -p tcp --dport "+str(num)+"00"+":"+str(num)+"99"+" --syn -m recent --name webpool --rcheck --seconds 60 --hitcount 10 -j DROP"
      os.system (command1)
      os.system (command2)
      os.system (command3)
      os.system (command4)
      os.system (command5)
      os.system (command6)
      os.system (command7)