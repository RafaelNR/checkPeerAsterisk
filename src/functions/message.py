
import re

from src.helper.remover_duplicatas import remover_duplicatas


def handleMessageAnalitico(lines):
  
  logArray = []
  
  for line in lines:
    if("chan_sip.c: Peer" in line):
      
      dateRegex = r"\[(.*?)\]"
      dateMatch = re.match(dateRegex, line)
      date = dateMatch.group(1) if dateMatch else None
      
      
      peerRegex = r"Peer '([^']+)'"
      peerMatch = re.search(peerRegex, line)
      peer = peerMatch.group(1) if peerMatch else None
      
      
      statusRegex = r"is now (\w+)"
      statusMatch = re.search(statusRegex, line)
      status = statusMatch.group(1) if statusMatch else None
      
      
      global ms

      # Regex para capturar o ms
      if(status == "UNREACHABLE"):
        msRegex = r"Last qualify: (\w+)"
        msMatch = re.search(msRegex, line)
        ms = msMatch.group(1) if msMatch else None
        
      if(status == 'Lagged' or status == 'Reachable'):
        msRegex = r"\((\d+)ms \/ \d+ms\)"
        msMatch = re.search(msRegex, line)
        ms = msMatch.group(1) if msMatch else None
        
      if(peer):
        logArray.append({ "date": date, "peer":peer, "status": status, "ms": ms });
      
  
  return logArray

def handleMessageSintetico(messages):
  
  
  ramais = remover_duplicatas(list(map(lambda d: d["peer"] , messages)));
  
  logFinal = []

  
  for ramal in ramais:
    filterLog = list(filter(lambda d: ramal == d["peer"], messages));
  
    if(filterLog and len(filterLog) > 0):
      logFinal.append({
        "peer": ramal,
        "Lagged": len(list(filter(lambda d: d["status"] == "Lagged", filterLog))),
        "Reachable": len(list(filter(lambda d: d["status"] == "Reachable", filterLog))),
        "UNREACHABLE": len(list(filter(lambda d: d["status"] == "UNREACHABLE", filterLog))),
        "logs": filterLog
      })
      
  return logFinal
    
  
  

