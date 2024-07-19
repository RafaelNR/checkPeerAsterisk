import re

from src.helper.remover_duplicatas import remover_duplicatas

def checkRamaisRegisteredAnalitico(lines):
  
  logArray = []
  
  for line in lines:
    if("VERBOSE[4122]" in line):
      
      dateRegex = r"\[(.*?)\]"
      dateMatch = re.match(dateRegex, line)
      date = dateMatch.group(1) if dateMatch else None
      
      peerRegex = r"Registered SIP '([^']+)'"
      peerMatch = re.search(peerRegex, line)
      peer = peerMatch.group(1) if peerMatch else None
      
      ipRegex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
      ipMatch = re.search(ipRegex, line)
      ip = ipMatch.group(1) if ipMatch else None
      
      portRegex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)\b"
      portMatch = re.search(portRegex, line)
      port = portMatch.group(1) if portMatch else None
      
      if(peer and ip):
        logArray.append({ "date": date, "peer":peer, "ip": ip, "port": port});
      
      
  return logArray



def checkRamaisRegisteredSintetico(full):
  
  ramais = remover_duplicatas(list(map(lambda d: d["peer"] , full)));
  
  logFinal = []
  
  for ramal in ramais:
    filterLog = list(filter(lambda d: ramal == d["peer"], full));
  
    if(filterLog and len(filterLog) > 0):
      ipsRamal = remover_duplicatas(list(map(lambda d: d["ip"] , filterLog)));
      
      logFinal.append({
        "peer": ramal,
        "ip": ",".join(ipsRamal),
        "logs": filterLog
      })
      
  print(logFinal)
      
  # return logFinal
  