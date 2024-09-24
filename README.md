# Network Scanner Project

## Descrição
Este projeto consiste em um scanner de rede simples desenvolvido em Python que utiliza a biblioteca `python-nmap` para identificar dispositivos em uma rede. O scanner verifica portas específicas e identifica serviços rodando nos dispositivos detectados. Os resultados são salvos em um arquivo JSON para análise posterior.

## Requisitos
- Python 3.x
- Nmap
- Biblioteca python-nmap

## Instalação

### Instalar Nmap
Nmap deve ser instalado em seu sistema. No Debian/Ubuntu/Kali Linux, você pode instalar usando:

sudo apt-get install nmap

## Instalar python-nmap
A biblioteca python-nmap pode ser instalada via pip. Certifique-se de que você tem o pip instalado e execute:
pip install python-nmap

## Configuração
Clone este repositório ou baixe os arquivos para o seu sistema local.
Abra o terminal na pasta onde estão os arquivos do projeto.
Siga as instruções na seção "Uso" para começar a usar o scanner de rede.

## Uso
Para usar o scanner de rede, execute o script network_scan.py com Python. Certifique-se de que você está no diretório correto onde o script está localizado:

python network_scan.py
O script executará o escaneamento da rede conforme configurado e salvará os resultados em scan_results.json.

Configurações
Hosts e Portas: Você pode modificar o script network_scan.py para alterar a faixa de IPs (hosts) e o intervalo de portas (ports) que deseja escanear.
Contribuições
Contribuições para o projeto são bem-vindas.

Este README serve como um guia completo para alguém que queira usar ou contribuir para o seu projeto de scanner de rede.
