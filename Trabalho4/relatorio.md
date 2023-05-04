# Questão 1) quais são os ips envolvidos

Usando o seguinte comando

`$ tcpdump -n -r attack-trace.pcap | cut -d' ' -f3,5 | sed -e 's/ /\n/g' | cut -d. -f-4 | sort -u`

Foi possível ver que se tem 2 ips

```
reading from file attack-trace.pcap, link-type EN10MB (Ethernet), snapshot length 65535
192.150.11.111
98.114.205.102
```

# Questão 2) o que da para saber sobre a máquina do atacante? (ex.: lugar?)
whois
dig | nslookup
tcpflow
tshark
wireshark

# Questão 3) quantas sessões tcp tem no arquivo?

# Questão 4) quanto tempo o atacante levou?
