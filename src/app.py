import sys
import os
import signal
from datetime import datetime
import time

from src.functions.args import handleArgs
from src.functions.message import handleMessageAnalitico,handleMessageSintetico
from src.functions.full import checkRamaisRegisteredAnalitico, checkRamaisRegisteredSintetico
from src.functions.saveExcel import  saveExcel

def init():
  try:
    args = handleArgs()
    
    full = args["f"]
    message = args["m"]
    hostname = args["n"]
    fullPath = None
    messagePath = None
    
    if not hostname:
      hostname = os.uname().nodename
    
    if full:
      fullPath = full if "/" in full else f"/var/log/asterisk/{full}"
      if not os.path.exists(fullPath):
        raise Exception("Full não existe.")
      
    if message:
      messagePath = message if "/" in message else f"/var/log/asterisk/{message}"
      if not os.path.exists(messagePath):
        raise Exception("Message não existe.")
      
    if not hostname:
      raise Exception("Hostname não existe.")
    
    if not os.path.exists("relatorios"): os.mkdir("relatorios")
    
    # MESSAGE
    if messagePath:
      messagesFile = open(messagePath)
      messagesAnalitico = handleMessageAnalitico(messagesFile.readlines())    
      messagesSintetico = handleMessageSintetico(messagesAnalitico)
    
      saveExcel(f"message_analitico_{hostname}",messagesAnalitico)
      saveExcel(f"message_sintetico_{hostname}",messagesSintetico)
    
    
    # FULL
    if full:
      fullFile = open(fullPath)
      fullAnalitico = checkRamaisRegisteredAnalitico(fullFile.readlines())
      fullSintetico = checkRamaisRegisteredSintetico(fullAnalitico)
      
      saveExcel(f"full_analitico_{hostname}",fullAnalitico)
      saveExcel(f"full_sintetico_{hostname}",fullSintetico)
    
    
    sys.exit('CheckPeers Finalizado!')
    
  
  except Exception as e:
    # db.close()
    print("Error: ", e)
