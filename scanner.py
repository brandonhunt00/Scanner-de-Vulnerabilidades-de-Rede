import nmap
import json

# Inicializa o scanner Nmap
nm = nmap.PortScanner()

# Define a faixa de IPs ou domínio a ser escaneado
hosts = '192.168.1.0/24'  # Exemplo de faixa de IPs. Altere conforme necessário.
ports = '21-443'  # Escaneia as portas de 21 a 443.

# Realiza o escaneamento
nm.scan(hosts=hosts, arguments='-p' + ports)

# Dicionário para armazenar os resultados
scan_results = {}

# Coleta os resultados do escaneamento
for host in nm.all_hosts():
    scan_results[host] = {
        'state': nm[host].state(),
        'protocols': list(nm[host].all_protocols()),
        'ports': {}
    }
    for proto in nm[host].all_protocols():
        scan_results[host]['ports'][proto] = []
        for port in nm[host][proto]:
            scan_results[host]['ports'][proto].append({
                'port': port,
                'state': nm[host][proto][port]['state'],
                'service': nm[host][proto][port]['name']
            })

# Salva os resultados em um arquivo JSON
with open('scan_results.json', 'w') as outfile:
    json.dump(scan_results, outfile, indent=4)

print("O escaneamento foi concluído e os resultados foram salvos em 'scan_results.json'")
