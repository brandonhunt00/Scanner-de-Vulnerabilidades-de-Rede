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

Abaixo está um exemplo da utilização dsse Scanner de Redes:
![scanner](https://github.com/user-attachments/assets/5c65e70a-3fb0-4330-b6b0-f59e73312f39)
O print acima mostra o código em python clonado em um arquivo .py no terminal do linux.

Quando executamos o código, recebemos a seguinte resposta:
![script rodando](https://github.com/user-attachments/assets/f4f3858f-907f-4d55-a050-3cd23e309c1d)
![resultado portas](https://github.com/user-attachments/assets/c3e7f471-fda8-4f9f-98f0-0d687cb406f7)
![print readme](https://github.com/user-attachments/assets/9590f41a-80e5-45e3-bf7a-c9e0c5d5eba7)
Após a execução do scanner, percebemos que não existe nenhuma porta aberta.  

## Configurações
Hosts e Portas: Você pode modificar o script network_scan.py para alterar a faixa de IPs (hosts) e o intervalo de portas (ports) que deseja escanear.

## Contribuições
Contribuições para o projeto são bem-vindas.

Este README serve como um guia completo para alguém que queira usar ou contribuir para meu projeto de scanner de rede.
