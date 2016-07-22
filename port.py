import os
IPS="10.1.0."#IP Range
NATIP="222.239.87.195"#Public IP
for num in range(10,256):
  length=len(str(num))
  if 39< num < 90:
      print "block" 
  elif length <= 10:
    for num1 in range(int(str(num)+"00"),int(str(num)+"99")):
      if str(num1) == str(num)+"00":
        command1="iptables -t nat -A PREROUTING -d "+NATIP+" -p all --dport "+str(num1)+" -j DNAT --to-destination "+IPS+str(num)+":22"
      elif  str(num1) == str(num)+"01":
        command1="iptables -t nat -A PREROUTING -d "+NATIP+" -p all --dport "+str(num1)+" -j DNAT --to-destination "+IPS+str(num)+":3389"
      else:      
        command1="iptables -t nat -A PREROUTING -d "+NATIP+" -p all --dport "+str(num1)+" -j DNAT --to-destination "+IPS+str(num)+":"+str(num1)
      command2="iptables -A INPUT -p tcp --dport "+str(num1)+" --syn -m recent --name webpool --rcheck --seconds 60 --hitcount 10 -j DROP"
      os.system(command1)
      os.system(command2)
      print command1
      print command2