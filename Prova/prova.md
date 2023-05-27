---
title: Prova
subtitle: Segurança
author: Iago Mello Floriano 
date: GRR20196049
---

# Objetivo
Objetivo dessa prova é analisar o trafego de rede dado pelo professor

# IPS ENVOLVIDOS
Foram obtidos os ips de todos os envolvidos no trafego com o seguinte comando

`tcpdump -n -r attack-trace.pcap | cut -d' ' -f3,5 | sed -e 's/ /\n/g' |
cut -d. -f-4 | sort -u`

Os ips envolvidos são esses:
```
104.18.24.243
152.199.55.15
152.199.55.24
192.16.48.200
192.16.58.8
192.168.122.150
192.168.122.251
200.143.247.10
204.79.197.200
204.79.197.203
23.2.178.31
52.73.227.203
52.8.153.173
52.8.221.8
76.13.32.147
```

## Informações obtidas dos ips

Essas informações foram obtidas com o comando `whois`

```
104.18.24.243
OrgName:        Cloudflare, Inc.
OrgId:          CLOUD14
Address:        101 Townsend Street
City:           San Francisco
```
```
152.199.55.15
152.199.55.24
OrgName:        ANS Communications, Inc
OrgId:          ANS
Address:        22001 Loudoun County Parkway
City:           Ashburn
```
```
192.16.48.200
192.16.58.8
192.168.122.150
192.168.122.251
OrgName:        Edgecast Inc.
OrgId:          EDGEC-25
Address:        13031 W Jefferson Blvd. Building 900
City:           Los Angeles
```
```
200.143.247.10
204.79.197.200
204.79.197.203
OrgName:        Microsoft Corporation
OrgId:          MSFT
Address:        One Microsoft Way
City:           Redmond
```
```
23.2.178.31
OrgName:        Akamai Technologies, Inc.
OrgId:          AKAMAI
Address:        145 Broadway
City:           Cambridge
```
```
52.73.227.203
52.8.153.173
52.8.221.8
OrgName:        Amazon Technologies Inc.
OrgId:          AT-88-Z
Address:        410 Terry Ave N.
City:           Seattle
```
```
76.13.32.147
OrgName:        Oath Holdings Inc.
OrgId:          OH-207
Address:        770 BROADWAY FL 4
City:           New York
```

# Numero de sessões
```
p0f -r attack-trace.pcap | grep "syn+ack" | wc -l

64
```
Foram 64 sessões tcp analisadas

# Tempo do ataque

Com o seguinte comando é possível obter o tempo do início da captura
```
tcpdump -n -r attack-trace.pcap | cut -d' ' -f1 | head -n 1
reading from file attack-trace.pcap, link-type EN10MB (Ethernet), snapshot length 262144
08:41:10.333828
```

Com o seguinte comando é possível obter o tempo do final da captura
```
tcpdump -n -r attack-trace.pcap | cut -d' ' -f1 | tail -n 1
reading from file attack-trace.pcap, link-type EN10MB (Ethernet), snapshot length 262144
08:43:33.250140
```

Com isso podemos saber que o ataque demorou 2 minutos.

# Arquivos envolvidos

Arquivos envolvidos são de tipos diversos.
Foi possível obter esses arquivos com o programa [_wireshark_](https://www.wireshark.org/)
Os arquivos obtidos foram os seguintes:

- 241a2c(1).woff
- 241a2c.woff
- %3focid=iehp&pc=EUPP_
- %3focid=iehp&pc=EUPP_(1)
- 4996b9.woff
- 58-acd805-185735b%3fver=20200913_27036221&fdhead=msnallexpusers,rrotbn,warmbingc,platagyedge3cf,bingcollabedge3cf,intllesstripe,starthp3cf,platagyhp1cf,audexhp3cf,moneyhp1cf,bingcollabhp1cf,article3cf,msnapp3cf,1s-bing-news,vebudumu04302020,bbh20200521(1)
- 58-acd805-185735b%3fver=20200913_27036221&fdhead=msnallexpusers,rrotbn,warmbingc,platagyedge3cf,bingcollabedge3cf,intllesstripe,starthp3cf,platagyhp1cf,audexhp3cf,moneyhp1cf,bingcollabhp1cf,article3cf,msnapp3cf,1s-bing-news,vebudumu04302020,bbh20200521msn
- 755f86.png
- 85-0f8009-68ddb2ab%3fver=20200913_27036221&fdhead=msnallexpusers,rrotbn,warmbingc,platagyedge3cf,bingcollabedge3cf,intllesstripe,starthp3cf,platagyhp1cf,audexhp3cf,moneyhp1cf,bingcollabhp1cf,article3cf,msnapp3cf,1s-bing-news,vebudumu04302020,bbh2020052(1)
- 85-0f8009-68ddb2ab%3fver=20200913_27036221&fdhead=msnallexpusers,rrotbn,warmbingc,platagyedge3cf,bingcollabedge3cf,intllesstripe,starthp3cf,platagyhp1cf,audexhp3cf,moneyhp1cf,bingcollabhp1cf,article3cf,msnapp3cf,1s-bing-news,vebudumu04302020,bbh20200521ms
- a8a064(1).gif
- a8a064.gif
- AAK75JY(1).img%3fh=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png
- AAK75JY.img%3fh=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png
- BB10TDvk(1).img%3fh=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png
- BB10TDvk.img%3fh=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png
- BB14CVtq(1).img%3fh=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png
- BB14CVtq.img%3fh=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png
- BB16cON1(1).img%3fh=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png
- BB16cON1.img%3fh=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png
- BB16dkPz(1).img%3fh=333&w=311&m=6&q=60&u=t&o=t&l=f&f=jpg&x=331&y=169
- BB16dkPz.img%3fh=333&w=311&m=6&q=60&u=t&o=t&l=f&f=jpg&x=331&y=169
- BB197k2U(1).img%3fh=166&w=310&m=6&q=60&u=t&o=t&l=f&f=jpg&x=417&y=274
- BB197k2U.img%3fh=166&w=310&m=6&q=60&u=t&o=t&l=f&f=jpg&x=417&y=274
- BB199OzT(1).img%3fh=166&w=310&m=6&q=60&u=t&o=t&l=f&f=jpg&x=470&y=271
- BB199OzT.img%3fh=166&w=310&m=6&q=60&u=t&o=t&l=f&f=jpg&x=470&y=271
- cms%3fpartner_id=MSFT
- MFEwTzBNMEswSTAJBgUrDgMCGgUABBTPJvUY%2Bsl%2Bj4yzQuAcL2oQno5fCgQUUWj%2FkK8CB3U8zNllZGKiErhZcjsCEAHO0huEvLBjxSLyACfvQUo%3D
- MFQwUjBQME4wTDAJBgUrDgMCGgUABBSIGkp0%2Fv9GUvNUu1EP06Tu7%2BChyAQUkZ47RGw9V5xCdyo010%2FRzEqXLNoCEyAABg8tj1700CLuBSYAAAAGDy0%3D
- MFQwUjBQME4wTDAJBgUrDgMCGgUABBSIGkp0%2Fv9GUvNUu1EP06Tu7%2BChyAQUkZ47RGw9V5xCdyo010%2FRzEqXLNoCEyAABg8tj1700CLuBSYAAAAGDy0%3D(1)
- MFQwUjBQME4wTDAJBgUrDgMCGgUABBSIGkp0%2Fv9GUvNUu1EP06Tu7%2BChyAQUkZ47RGw9V5xCdyo010%2FRzEqXLNoCEyAABg8tj1700CLuBSYAAAAGDy0%3D(2)
- MFQwUjBQME4wTDAJBgUrDgMCGgUABBSIGkp0%2Fv9GUvNUu1EP06Tu7%2BChyAQUkZ47RGw9V5xCdyo010%2FRzEqXLNoCEyAABg8tj1700CLuBSYAAAAGDy0%3D(3)
- MFQwUjBQME4wTDAJBgUrDgMCGgUABBSIGkp0%2Fv9GUvNUu1EP06Tu7%2BChyAQUkZ47RGw9V5xCdyo010%2FRzEqXLNoCEyAABg8tj1700CLuBSYAAAAGDy0%3D(4)
- MFQwUjBQME4wTDAJBgUrDgMCGgUABBSIGkp0%2Fv9GUvNUu1EP06Tu7%2BChyAQUkZ47RGw9V5xCdyo010%2FRzEqXLNoCEyAABg8tj1700CLuBSYAAAAGDy0%3D(5)
- MFQwUjBQME4wTDAJBgUrDgMCGgUABBSIGkp0%2Fv9GUvNUu1EP06Tu7%2BChyAQUkZ47RGw9V5xCdyo010%2FRzEqXLNoCEyAABg8tj1700CLuBSYAAAAGDy0%3D(6)
- MFQwUjBQME4wTDAJBgUrDgMCGgUABBSIGkp0%2Fv9GUvNUu1EP06Tu7%2BChyAQUkZ47RGw9V5xCdyo010%2FRzEqXLNoCEyAABg8tj1700CLuBSYAAAAGDy0%3D(7)
- Microsoft%20IT%20TLS%20CA%202(1).crl
- Microsoft%20IT%20TLS%20CA%202(2).crl
- Microsoft%20IT%20TLS%20CA%202(3).crl
- Microsoft%20IT%20TLS%20CA%202.crl
- occ
- occ(1)
- pt-br&Red3=MSAOL_pd
- pt-br&Red3=MSAOL_pd(1)
- sync%3frUrl=https%3A%2F%2Fpr-bh.ybp.yahoo(1).com%2Fsync%2Fadaptv_ortb%2F%7Buid%7D
- sync%3frUrl=https%3A%2F%2Fpr-bh.ybp.yahoo.com%2Fsync%2Fadaptv_ortb%2F%7Buid%7D

Os arquivos foram todos inpecionados pelo site [_virustotal_](https://www.virustotal.com/)
e nenhum deles tras alguma ressalva com excessão do que está nomeado como 
`pt-br&Red3=MSAOL_pd`. Esse arquivo aparenta não ser malicioso sozinho, porém aparenta
ser comunmente enviado junto de arquivos maliciosos de acordo com o usuário
[_sectestso do virustotal_](https://www.virustotal.com/gui/file/99c2917ee5b2a01459a923bdd1c676f15ee73b62b87f696e6735312d26f51e12/community).

Além disso é possível observar que foram enviados dois certificados digitais da microsoft
, caso seja um ataque é possível que sejam certificados falsificados para que possa ser
enviado algum arquivo malicioso sem a vítima suspeitar.

\pagebreak
# Outras informações obtidas

Utilizando o website [_apackets.com](https://apackets.com/) foi possível obter esse grafo
das conexões que foram feitas nessa captura.

![grafo](./grafo.png)


Olhando ainda as informações geradas pelo site [_apackets.com](https://apackets.com/) é
possível ver que todas as requisições http são get, comportamento que pode ser de alguem
usando um navegador. Como várias imagens e gifs são baixados, é possível que seja alguem
explorando páginas na internet.
