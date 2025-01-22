import paramiko

# Configurações de conexão
HOST = 'IP_da_VM_alvo'
USER = 'usuario'
PASSWORD = 'senha'
CAMINHO_LOG = '/var/log/syslog'  # ou outro arquivo de log
ARQUIVO_LOCAL = 'log_coletado.txt'


def coletar_log_e_analisar(host, usuario, senha, caminho_log, arquivo_local):
    # Estabelece conexão SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=usuario, password=senha)

    # Usa SFTP para transferir o arquivo de log
    sftp = client.open_sftp()
    sftp.get(caminho_log, arquivo_local)
    sftp.close()
    client.close()

    # Lê o arquivo local coletado
    with open(arquivo_local, 'r') as f:
        linhas = f.readlines()

    # Filtra linhas contendo "ERROR"
    erros = [linha for linha in linhas if 'ERROR' in linha or 'Error' in linha]
    return erros

# Chama a função com os parâmetros configurados
erros_encontrados = coletar_log_e_analisar(HOST, USER, PASSWORD, CAMINHO_LOG, ARQUIVO_LOCAL)

# Exibe os erros encontrados
print("Erros encontrados no log:")
for erro in erros_encontrados:
    print(erro.strip())

