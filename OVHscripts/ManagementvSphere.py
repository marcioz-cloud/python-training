from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl
import atexit
import smtplib
from email.mime.text import MIMEText

# Ignorar verificação de certificado SSL
ssl_context = ssl._create_unverified_context() #Contexto SSL que ignora a verificação do certificado SSL, útil para ambientes de teste ou quando o certificado do vCenter não é confiável.

# Função para conectar ao vCenter
def connect_to_vcenter(host, user, pwd):
    si = SmartConnect(host=host, user=user, pwd=pwd, sslContext=ssl_context) #É um método da biblioteca pyvmomi usado para estabelecer uma conexão com o servidor vCenter.
    atexit.register(Disconnect, si) #Registra uma função para ser executada automaticamente quando o script terminar.
    return si #O si é um objeto que representa sua conexão com o vCenter. Depois que você cria o si, ele é usado para "pegar" as informações do vCenter.

# 1. Listar todas as VMs no ambiente vSphere
def list_vms(content):
    print("=== Lista de VMs ===")
    vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vms = vm_view.view
    for vm in vms:
        summary = vm.summary
        print(f"Nome: {summary.config.name}")
        print(f"Status: {'Ligada' if summary.runtime.powerState == 'poweredOn' else 'Desligada'}")
        print(f"CPU (MHz): {summary.quickStats.overallCpuUsage}")
        print(f"Memória (MB): {summary.quickStats.guestMemoryUsage}")
        print(f"IP: {summary.guest.ipAddress}")
        print("-" * 20)
    vm_view.Destroy()

# 2. Gerenciar estados das VMs
def manage_vm_states(content, action, cluster_name=None):
    cluster_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.ClusterComputeResource], True)
    for cluster in cluster_view.view:
        if cluster_name and cluster.name != cluster_name:
            continue
        for host in cluster.host:
            for vm in host.vm:
                if action == "on" and vm.runtime.powerState == "poweredOff":
                    vm.PowerOn()
                    print(f"Ligando VM: {vm.name}")
                elif action == "off" and vm.runtime.powerState == "poweredOn":
                    vm.PowerOff()
                    print(f"Desligando VM: {vm.name}")
                elif action == "suspend" and vm.runtime.powerState == "poweredOn":
                    vm.SuspendVM_Task()
                    print(f"Suspender VM: {vm.name}")
    cluster_view.Destroy()

# 3. Monitorar recursos das VMs
def monitor_vm_resources(content):
    print("=== Monitoramento de Recursos ===")
    vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    for vm in vm_view.view:
        summary = vm.summary
        if vm.runtime.powerState == "poweredOn":
            print(f"Nome: {summary.config.name}")
            print(f"CPU (MHz): {summary.quickStats.overallCpuUsage}")
            print(f"Memória (MB): {summary.quickStats.guestMemoryUsage}")
            print(f"Latência de Disco: {summary.quickStats.hostMemoryUsage}")
            print("-" * 20)
    vm_view.Destroy()

# 4. Gerar relatórios de inventário
def generate_inventory_report(content):
    print("=== Relatório de Inventário ===")
    host_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True)
    for host in host_view.view:
        summary = host.summary
        print(f"Host: {summary.config.name}")
        print(f"CPU Total (MHz): {summary.hardware.cpuMhz} MHz")
        print(f"Memória Total (MB): {summary.hardware.memorySize / (1024 * 1024)} MB")
        print(f"Datastores:")
        for ds in host.datastore:
            ds_summary = ds.summary
            print(f" - {ds_summary.name}: {ds_summary.freeSpace / (1024**3):.2f} GB livres")
        print("-" * 20)
    host_view.Destroy()

# Configuração do vCenter
vcenter_host = "vcenter.example.com"
vcenter_user = "administrator@vsphere.local"
vcenter_password = "your_password"

# Conectar e executar funções
try:
    si = connect_to_vcenter(vcenter_host, vcenter_user, vcenter_password)
    content = si.RetrieveContent()

    # Chamar as funções
    list_vms(content)  # Listar todas as VMs
    manage_vm_states(content, "off")  # Desligar todas as VMs em um cluster
    monitor_vm_resources(content)  # Monitorar recursos de VMs
    generate_inventory_report(content)  # Gerar relatório de inventário

except Exception as e:
    print(f"Erro: {e}")


# Código repetitivo
#soma1 = 3 + 5
#soma2 = 7 + 2
#soma3 = 4 + 9
#print(soma1, soma2, soma3)

# Reutilizando a função com def
#def somar(a, b):
    #return a + b

#print(somar(3, 5))
#print(somar(7, 2))
#print(somar(4, 9))

