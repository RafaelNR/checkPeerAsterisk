import argparse
import os

# Trata os argumentos
def handleArgs():
	# create and execute command line parser
	parser = argparse.ArgumentParser(description="Gera arquivo de ramais do cliente")
	parser.add_argument("-n", default=f"{os.uname().nodename}", help="Hostname.")
	parser.add_argument("-f", help="Você pode adicionar somente nome do arquivo que deseja analise dentro da pasta de log ou um path inteiro.")
	parser.add_argument("-m", help="Analise para quedas dos ramais. Você pode adicionar somente nome do arquivo que deseja analise dentro da pasta de log ou um path inteiro.")
	# parser.add_argument("-i", metavar="ip", default="*", help="IP no header que enviará a solicitação (Tentara obter o IP Local)")
	# parser.add_argument("-d", metavar="domain", default="seg.eti", help="Domain do header (necessário se o host filtra domínio)")
	# parser.add_argument("-p", metavar="port", default=5060, help="Porta de destino (padrão 5060)")
	# parser.add_argument("--ttl", metavar="ttl", default=70, help="valor para ser usando no campo Max-Forwards field (padrão 70)")
	# parser.add_argument("-w", metavar="file", default="[[default]]", help="Onde será salvo os arquivos. (padrão logs/[ip] - * para desabilitar.")
	# parser.add_argument("-t", metavar="timeout", default="1000", help="Time (ms) to wait da resposta (padrão 1000)")
	# parser.add_argument("-c", metavar="count", default="0", help="Número de pings enviados (padrão infinite)")
	# parser.add_argument("-x", nargs="?", default=False, help="Exibir pacotes OPTIONS enviados")
	# parser.add_argument("-X", nargs="?", default=False, help="Exibir pacotes OPTIONS recebidos")
	# parser.add_argument("-q", nargs="?", default=True, help="Não existe msg de transmissão, somente estatística.")
	# parser.add_argument("-S", nargs="?", default=True, help="Não exibe estatística a cada 5 pings, somente no Ctrl+C.")
	return vars(parser.parse_args())

