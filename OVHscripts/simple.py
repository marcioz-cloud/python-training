from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl
import atexit

# Configurações do vCenter
VCENTER_HOST = "seu_vcenter_host"  # Substitua pelo IP ou hostname do vCenter
VCENTER_USER = "seu_usuario"  # Substitua pelo usuário do vCenter
VCENTER_PASSWORD = "sua_senha"  # Substitua pela senha do vCenter
RELATORIO_PATH = "relatorio_vms.txt"  # Caminho do arquivo onde será salvo o relatório

# Ignorar verificação de certificado SSL
ssl_context = ssl._create_unverified_context()

def connect_to_vcenter(host, user, pwd):
    """Conecta ao vCenter e retorna a conexão"""
    si = SmartConnect(host=host, user=user, pwd=pwd, sslContext=ssl_context)
    atexit.register(Disconnect, si)  # Desconecta automaticamente ao finalizar
    return si

def list_vms(si):
    """Lista todas as VMs no ambiente vSphere e salva em um arquivo"""
    content = si.RetrieveContent()
    vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vms = vm_view.view

    # Abrir o arquivo de relatório
    with open(RELATORIO_PATH, "w") as relatorio:
        relatorio.write("Relatório de VMs no vSphere\n")
        relatorio.write("=" * 40 + "\n")
        for vm in vms:
            summary = vm.summary
            relatorio.write(f"Nome da VM: {summary.config.name}\n")
            relatorio.write(f"Status: {'Ligada' if summary.runtime.powerState == 'poweredOn' else 'Desligada'}\n")
            relatorio.write(f"CPU (MHz): {summary.quickStats.overallCpuUsage}\n")
            relatorio.write(f"Memória (MB): {summary.quickStats.guestMemoryUsage}\n")
            relatorio.write("-" * 40 + "\n")

    vm_view.Destroy()  # Limpar a view
    print(f"Relatório salvo em: {RELATORIO_PATH}")

if __name__ == "__main__":
    try:
        print("Conectando ao vCenter...")
        si = connect_to_vcenter(VCENTER_HOST, VCENTER_USER, VCENTER_PASSWORD)
        print("Conexão bem-sucedida!")
        list_vms(si)
    except Exception as e:
        print(f"Erro: {e}")
