# IPS ENVOLVIDOS
obtidos com
`tcpdump -n -r attack-trace.pcap | cut -d' ' -f3,5 | sed -e 's/ /\n/g' |
cut -d. -f-4 | sort -u`

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

```
--- p0f 3.09b by Michal Zalewski <lcamtuf@coredump.cx> ---

[+] Closed 1 file descriptor.
[+] Loaded 322 signatures from '/etc/p0f/p0f.fp'.
[+] Will read pcap data from file 'attack-trace.pcap'.
[+] Default packet filtering configured [+VLAN].
[+] Processing capture data.

.-[ 192.168.122.150/65192 -> 204.79.197.203/80 (syn) ]-
|
| client   = 192.168.122.150/65192
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65192 -> 204.79.197.203/80 (mtu) ]-
|
| client   = 192.168.122.150/65192
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65193 -> 204.79.197.203/80 (syn) ]-
|
| client   = 192.168.122.150/65193
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65193 -> 204.79.197.203/80 (mtu) ]-
|
| client   = 192.168.122.150/65193
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65192 -> 204.79.197.203/80 (syn+ack) ]-
|
| server   = 204.79.197.203/80
| os       = ???
| dist     = 10
| params   = none
| raw_sig  = 4:118+10:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65192 -> 204.79.197.203/80 (mtu) ]-
|
| server   = 204.79.197.203/80
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65192 -> 204.79.197.203/80 (http request) ]-
|
| client   = 192.168.122.150/65192
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[text/html, application/xhtml+xml, */*],Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65193 -> 204.79.197.203/80 (syn+ack) ]-
|
| server   = 204.79.197.203/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:119+9:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65193 -> 204.79.197.203/80 (mtu) ]-
|
| server   = 204.79.197.203/80
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65194 -> 204.79.197.203/80 (syn) ]-
|
| client   = 192.168.122.150/65194
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65194 -> 204.79.197.203/80 (mtu) ]-
|
| client   = 192.168.122.150/65194
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65195 -> 204.79.197.203/80 (syn) ]-
|
| client   = 192.168.122.150/65195
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65195 -> 204.79.197.203/80 (mtu) ]-
|
| client   = 192.168.122.150/65195
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65194 -> 204.79.197.203/80 (syn+ack) ]-
|
| server   = 204.79.197.203/80
| os       = ???
| dist     = 10
| params   = none
| raw_sig  = 4:118+10:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65194 -> 204.79.197.203/80 (mtu) ]-
|
| server   = 204.79.197.203/80
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65194 -> 204.79.197.203/80 (http request) ]-
|
| client   = 192.168.122.150/65194
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[text/html, application/xhtml+xml, */*],Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65195 -> 204.79.197.203/80 (syn+ack) ]-
|
| server   = 204.79.197.203/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:119+9:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65195 -> 204.79.197.203/80 (mtu) ]-
|
| server   = 204.79.197.203/80
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65192 -> 204.79.197.203/80 (http response) ]-
|
| server   = 204.79.197.203/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:?Cache-Control,?Pragma,?Content-Length,Content-Type,Content-Encoding=[gzip],?Expires,?Vary,?Set-Cookie,?Set-Cookie,?Set-Cookie,?Set-Cookie,Access-Control-Allow-Origin=[*],X-AspNetMvc-Version=[5.2],X-AppVersion=[20200913_27036221],X-Activity-Id=[cb9eea41-029c-4a06-9339-4d63ddb9e5ae],X-Az=[{did:a50ac9605f704ff085607b853101e440, rid: 27, sn: eastus-prod-hp, dt: 2020-09-18T11:09:02.0910735Z, bt: 2020-09-14T00:15:16.7442237Z}],nel=[{"report_to":"network-errors","max_age":604800,"success_fraction":0.001,"failure_fraction":1.0}],report-to=[{"group":"network-errors","max_age":604800,"endpoints":[{"url":"https://deff.nelreports.net/api/report?cat=msn"}],X-UA-Compatible=[IE=Edge;chrome=1],X-Content-Type-Options=[nosniff],X-FRAME-OPTIONS=[SAMEORIGIN],X-Powered-By=[ASP.NET],Access-Control-Allow-Methods=[HEAD,GET,OPTIONS],X-XSS-Protection=[1],X-MSEdge-Ref=[Ref A: CB9EEA41029C4A0693394D63DDB9E5AE Ref B: SAO03EDGE0515 Ref C: 2020-09-18T11:41:10Z],Date:Connection,Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65194 -> 204.79.197.203/80 (http response) ]-
|
| server   = 204.79.197.203/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:?Cache-Control,?Pragma,?Content-Length,Content-Type,Content-Encoding=[gzip],?Expires,?Vary,?Set-Cookie,?Set-Cookie,?Set-Cookie,?Set-Cookie,Access-Control-Allow-Origin=[*],X-AspNetMvc-Version=[5.2],X-AppVersion=[20200913_27036221],X-Activity-Id=[6f5f39cd-742b-4301-a4bb-98117f5d7db6],X-Az=[{did:a50ac9605f704ff085607b853101e440, rid: 24, sn: eastus-prod-hp, dt: 2020-09-04T05:13:12.9888556Z, bt: 2020-09-14T00:15:16.7442237Z}],nel=[{"report_to":"network-errors","max_age":604800,"success_fraction":0.001,"failure_fraction":1.0}],report-to=[{"group":"network-errors","max_age":604800,"endpoints":[{"url":"https://deff.nelreports.net/api/report?cat=msn"}],X-UA-Compatible=[IE=Edge;chrome=1],X-Content-Type-Options=[nosniff],X-FRAME-OPTIONS=[SAMEORIGIN],X-Powered-By=[ASP.NET],Access-Control-Allow-Methods=[HEAD,GET,OPTIONS],X-XSS-Protection=[1],X-MSEdge-Ref=[Ref A: 6F5F39CD742B4301A4BB98117F5D7DB6 Ref B: SAO03EDGE0218 Ref C: 2020-09-18T11:41:10Z],Date:Connection,Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65196 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65196
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65196 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65196
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65197 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65197
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65197 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65197
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65198 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65198
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65198 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65198
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65199 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65199
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65199 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65199
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65200 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65200
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65200 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65200
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65201 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65201
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65201 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65201
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65202 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65202
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65202 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65202
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65203 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65203
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65203 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65203
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65204 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65204
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65204 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65204
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65205 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65205
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65205 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65205
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65206 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65206
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65206 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65206
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65207 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65207
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65207 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65207
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65208 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65208
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65208 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65208
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65209 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65209
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65209 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65209
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65210 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65210
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65210 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65210
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65211 -> 200.143.247.10/80 (syn) ]-
|
| client   = 192.168.122.150/65211
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65211 -> 200.143.247.10/80 (mtu) ]-
|
| client   = 192.168.122.150/65211
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65196 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65196 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65197 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65197 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65203 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65203 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65199 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65199 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65196 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65196
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[application/javascript, */*;q=0.8],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65197 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65197
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[application/javascript, */*;q=0.8],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65203 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65203
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65199 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65199
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[text/css, */*],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65207 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65207 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65198 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65198 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65206 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65206 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65200 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65200 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65201 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65201 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65205 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65205 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65202 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65202 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65207 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65207
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65204 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65204 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65201 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65201
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65205 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65205
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65208 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65208 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65208 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65208
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65198 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65198
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[text/css, */*],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65206 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65206
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65200 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65200
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65202 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65202
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65204 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65204
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65209 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65209 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65209 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65209
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65210 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65210 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65210 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65210
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65211 -> 200.143.247.10/80 (syn+ack) ]-
|
| server   = 200.143.247.10/80
| os       = ???
| dist     = 8
| params   = none
| raw_sig  = 4:56+8:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65211 -> 200.143.247.10/80 (mtu) ]-
|
| server   = 200.143.247.10/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65211 -> 200.143.247.10/80 (http request) ]-
|
| client   = 192.168.122.150/65211
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65203 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB10TDvk?h=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[1265777],X-CMS-CDNInvalKey=[amp:BB10TDvk],X-Datacenter=[eastus],X-ActivityId=[ce2578aa-469f-4b15-87e7-87ada3fc0c36],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65196 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Content-Type,Content-Encoding=[gzip],?Last-Modified,?Vary,Server,Access-Control-Allow-Origin=[*],X-AspNetMvc-Version=[5.2],X-AppVersion=[20200909_26914858],X-Activity-Id=[00000000-a512-4b63-9672-768579fc5596],X-Az=[{did:a50ac9605f704ff085607b853101e440, rid: 8, sn: eastus-prod-hp, dt: 2020-09-04T05:41:42.4636499Z, bt: 2020-09-09T21:16:23.2910113Z}],nel=[{"report_to":"network-errors","max_age":604800,"success_fraction":0.001,"failure_fraction":1.0}],report-to=[{"group":"network-errors","max_age":604800,"endpoints":[{"url":"https://deff.nelreports.net/api/report?cat=msn"}],X-Content-Type-Options=[nosniff],X-FRAME-OPTIONS=[SAMEORIGIN],X-S1=[2020-09-15T21:24:57],X-Powered-By=[ASP.NET],Access-Control-Allow-Methods=[HEAD,GET,OPTIONS],X-XSS-Protection=[1],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:Microsoft-IIS/8.5
|
`----

.-[ 192.168.122.150/65197 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Content-Type,Content-Encoding=[gzip],?Last-Modified,?Vary,Server,Access-Control-Allow-Origin=[*],X-AspNetMvc-Version=[5.2],X-AppVersion=[20200909_26914858],X-Activity-Id=[00000000-a512-4b63-9672-768579fc5596],X-Az=[{did:a50ac9605f704ff085607b853101e440, rid: 8, sn: eastus-prod-hp, dt: 2020-09-04T05:41:42.4636499Z, bt: 2020-09-09T21:16:23.2910113Z}],nel=[{"report_to":"network-errors","max_age":604800,"success_fraction":0.001,"failure_fraction":1.0}],report-to=[{"group":"network-errors","max_age":604800,"endpoints":[{"url":"https://deff.nelreports.net/api/report?cat=msn"}],X-Content-Type-Options=[nosniff],X-FRAME-OPTIONS=[SAMEORIGIN],X-S1=[2020-09-15T21:24:57],X-Powered-By=[ASP.NET],Access-Control-Allow-Methods=[HEAD,GET,OPTIONS],X-XSS-Protection=[1],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:Microsoft-IIS/8.5
|
`----

.-[ 192.168.122.150/65199 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Content-Type,Content-Encoding=[gzip],?Last-Modified,?Vary,Server,Access-Control-Allow-Origin=[*],X-AspNetMvc-Version=[5.2],X-AppVersion=[20200909_26914858],X-Activity-Id=[00000000-7773-41a1-b950-ade671a199ef],X-Az=[{did:a50ac9605f704ff085607b853101e440, rid: 27, sn: eastus-prod-hp, dt: 2020-09-15T10:08:37.4715902Z, bt: 2020-09-09T21:16:23.2910113Z}],nel=[{"report_to":"network-errors","max_age":604800,"success_fraction":0.001,"failure_fraction":1.0}],report-to=[{"group":"network-errors","max_age":604800,"endpoints":[{"url":"https://deff.nelreports.net/api/report?cat=msn"}],X-Content-Type-Options=[nosniff],X-FRAME-OPTIONS=[SAMEORIGIN],X-S1=[2020-09-15T21:28:31],X-Powered-By=[ASP.NET],Access-Control-Allow-Methods=[HEAD,GET,OPTIONS],X-XSS-Protection=[1],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:Microsoft-IIS/8.5
|
`----

.-[ 192.168.122.150/65207 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB16cON1?h=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[18164],X-CMS-CDNInvalKey=[amp:BB16cON1],X-Datacenter=[eastus],X-ActivityId=[ef9b9e22-e455-429c-ad71-5c8121650194],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65208 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB16dkPz?h=333&w=311&m=6&q=60&u=t&o=t&l=f&f=jpg&x=331&y=169],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[382034],X-CMS-CDNInvalKey=[amp:BB16dkPz],X-Datacenter=[eastus],X-ActivityId=[f9552cbe-1d80-487a-b9c6-9d9252e28a64],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65205 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB14CVtq?h=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[7929],X-CMS-CDNInvalKey=[amp:BB14CVtq],X-Datacenter=[eastus],X-ActivityId=[227bcf8d-3940-4e86-88ae-3a2d3bcf285d],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65209 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB16dkPz?h=333&w=311&m=6&q=60&u=t&o=t&l=f&f=jpg&x=331&y=169],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[382034],X-CMS-CDNInvalKey=[amp:BB16dkPz],X-Datacenter=[eastus],X-ActivityId=[f9552cbe-1d80-487a-b9c6-9d9252e28a64],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65206 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB16cON1?h=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[18164],X-CMS-CDNInvalKey=[amp:BB16cON1],X-Datacenter=[eastus],X-ActivityId=[ef9b9e22-e455-429c-ad71-5c8121650194],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65201 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:?Last-Modified,Access-Control-Allow-Origin=[*],X-Datacenter=[eastus],X-ActivityId=[8873067c-3e81-40d2-9321-9057a21cd1d1],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/AAK75JY?h=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png],X-Source-Length=[10734],X-CMS-CDNInvalKey=[amp:AAK75JY],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65198 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Content-Type,Content-Encoding=[gzip],?Last-Modified,?Vary,Server,Access-Control-Allow-Origin=[*],X-AspNetMvc-Version=[5.2],X-AppVersion=[20200909_26914858],X-Activity-Id=[00000000-c259-4fee-b534-cba3c370e1a4],X-Az=[{did:a50ac9605f704ff085607b853101e440, rid: 16, sn: eastus-prod-hp, dt: 2020-09-04T05:28:32.5558718Z, bt: 2020-09-09T21:16:23.2910113Z}],nel=[{"report_to":"network-errors","max_age":604800,"success_fraction":0.001,"failure_fraction":1.0}],report-to=[{"group":"network-errors","max_age":604800,"endpoints":[{"url":"https://deff.nelreports.net/api/report?cat=msn"}],X-Content-Type-Options=[nosniff],X-FRAME-OPTIONS=[SAMEORIGIN],X-S1=[2020-09-15T21:26:54],X-Powered-By=[ASP.NET],Access-Control-Allow-Methods=[HEAD,GET,OPTIONS],X-XSS-Protection=[1],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:Microsoft-IIS/8.5
|
`----

.-[ 192.168.122.150/65200 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:?Last-Modified,Access-Control-Allow-Origin=[*],X-Datacenter=[eastus],X-ActivityId=[8873067c-3e81-40d2-9321-9057a21cd1d1],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/AAK75JY?h=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png],X-Source-Length=[10734],X-CMS-CDNInvalKey=[amp:AAK75JY],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65202 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB10TDvk?h=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[1265777],X-CMS-CDNInvalKey=[amp:BB10TDvk],X-Datacenter=[eastus],X-ActivityId=[ce2578aa-469f-4b15-87e7-87ada3fc0c36],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65204 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB14CVtq?h=27&w=27&m=6&q=60&u=t&o=t&l=f&f=png],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[7929],X-CMS-CDNInvalKey=[amp:BB14CVtq],X-Datacenter=[eastus],X-ActivityId=[227bcf8d-3940-4e86-88ae-3a2d3bcf285d],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65210 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB197k2U?h=166&w=310&m=6&q=60&u=t&o=t&l=f&f=jpg&x=417&y=274],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[63441],X-CMS-CDNInvalKey=[amp:BB197k2U],X-Datacenter=[eastus],X-ActivityId=[c56f7d65-a002-413c-be12-e1955be3678c],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65211 -> 200.143.247.10/80 (http response) ]-
|
| server   = 200.143.247.10/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:Content-Type,Content-Location=[http://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB197k2U?h=166&w=310&m=6&q=60&u=t&o=t&l=f&f=jpg&x=417&y=274],?Last-Modified,Access-Control-Allow-Origin=[*],X-Source-Length=[63441],X-CMS-CDNInvalKey=[amp:BB197k2U],X-Datacenter=[eastus],X-ActivityId=[c56f7d65-a002-413c-be12-e1955be3678c],X-Deployment=[48814558152342d6a910966088fd07b2],Timing-Allow-Origin=[*],X-Frame-Options=[deny],?Content-Length,?Cache-Control,?Expires,Date,Connection=[keep-alive]:Keep-Alive,Accept-Ranges:
|
`----

.-[ 192.168.122.150/65212 -> 23.2.178.31/443 (syn) ]-
|
| client   = 192.168.122.150/65212
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65212 -> 23.2.178.31/443 (mtu) ]-
|
| client   = 192.168.122.150/65212
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65213 -> 23.2.178.31/443 (syn) ]-
|
| client   = 192.168.122.150/65213
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65213 -> 23.2.178.31/443 (mtu) ]-
|
| client   = 192.168.122.150/65213
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65212 -> 23.2.178.31/443 (syn+ack) ]-
|
| server   = 23.2.178.31/443
| os       = ???
| dist     = 5
| params   = none
| raw_sig  = 4:59+5:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65212 -> 23.2.178.31/443 (mtu) ]-
|
| server   = 23.2.178.31/443
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65213 -> 23.2.178.31/443 (syn+ack) ]-
|
| server   = 23.2.178.31/443
| os       = ???
| dist     = 5
| params   = none
| raw_sig  = 4:59+5:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65213 -> 23.2.178.31/443 (mtu) ]-
|
| server   = 23.2.178.31/443
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65214 -> 23.2.178.31/443 (syn) ]-
|
| client   = 192.168.122.150/65214
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65214 -> 23.2.178.31/443 (mtu) ]-
|
| client   = 192.168.122.150/65214
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65214 -> 23.2.178.31/443 (syn+ack) ]-
|
| server   = 23.2.178.31/443
| os       = ???
| dist     = 5
| params   = none
| raw_sig  = 4:59+5:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65214 -> 23.2.178.31/443 (mtu) ]-
|
| server   = 23.2.178.31/443
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65215 -> 23.2.178.31/443 (syn) ]-
|
| client   = 192.168.122.150/65215
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65215 -> 23.2.178.31/443 (mtu) ]-
|
| client   = 192.168.122.150/65215
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65215 -> 23.2.178.31/443 (syn+ack) ]-
|
| server   = 23.2.178.31/443
| os       = ???
| dist     = 5
| params   = none
| raw_sig  = 4:59+5:0:1460:mss*20,7:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65215 -> 23.2.178.31/443 (mtu) ]-
|
| server   = 23.2.178.31/443
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65216 -> 104.18.24.243/80 (syn) ]-
|
| client   = 192.168.122.150/65216
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65216 -> 104.18.24.243/80 (mtu) ]-
|
| client   = 192.168.122.150/65216
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65217 -> 104.18.24.243/80 (syn) ]-
|
| client   = 192.168.122.150/65217
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65217 -> 104.18.24.243/80 (mtu) ]-
|
| client   = 192.168.122.150/65217
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65218 -> 104.18.24.243/80 (syn) ]-
|
| client   = 192.168.122.150/65218
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65218 -> 104.18.24.243/80 (mtu) ]-
|
| client   = 192.168.122.150/65218
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65219 -> 104.18.24.243/80 (syn) ]-
|
| client   = 192.168.122.150/65219
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65219 -> 104.18.24.243/80 (mtu) ]-
|
| client   = 192.168.122.150/65219
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65216 -> 104.18.24.243/80 (syn+ack) ]-
|
| server   = 104.18.24.243/80
| os       = ???
| dist     = 7
| params   = none
| raw_sig  = 4:57+7:0:1400:65535,10:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65216 -> 104.18.24.243/80 (mtu) ]-
|
| server   = 104.18.24.243/80
| link     = generic tunnel or VPN
| raw_mtu  = 1440
|
`----

.-[ 192.168.122.150/65216 -> 104.18.24.243/80 (http request) ]-
|
| client   = 192.168.122.150/65216
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65217 -> 104.18.24.243/80 (syn+ack) ]-
|
| server   = 104.18.24.243/80
| os       = ???
| dist     = 7
| params   = none
| raw_sig  = 4:57+7:0:1400:65535,10:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65217 -> 104.18.24.243/80 (mtu) ]-
|
| server   = 104.18.24.243/80
| link     = generic tunnel or VPN
| raw_mtu  = 1440
|
`----

.-[ 192.168.122.150/65217 -> 104.18.24.243/80 (http request) ]-
|
| client   = 192.168.122.150/65217
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65218 -> 104.18.24.243/80 (syn+ack) ]-
|
| server   = 104.18.24.243/80
| os       = ???
| dist     = 7
| params   = none
| raw_sig  = 4:57+7:0:1400:65535,10:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65218 -> 104.18.24.243/80 (mtu) ]-
|
| server   = 104.18.24.243/80
| link     = generic tunnel or VPN
| raw_mtu  = 1440
|
`----

.-[ 192.168.122.150/65218 -> 104.18.24.243/80 (http request) ]-
|
| client   = 192.168.122.150/65218
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65219 -> 104.18.24.243/80 (syn+ack) ]-
|
| server   = 104.18.24.243/80
| os       = ???
| dist     = 7
| params   = none
| raw_sig  = 4:57+7:0:1400:65535,10:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65219 -> 104.18.24.243/80 (mtu) ]-
|
| server   = 104.18.24.243/80
| link     = generic tunnel or VPN
| raw_mtu  = 1440
|
`----

.-[ 192.168.122.150/65219 -> 104.18.24.243/80 (http request) ]-
|
| client   = 192.168.122.150/65219
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65216 -> 104.18.24.243/80 (http response) ]-
|
| server   = 104.18.24.243/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Date,Content-Type,?Content-Length,Connection=[keep-alive],?Set-Cookie,?Expires,X-Powered-By=[Undertow/1],?ETag,?Last-Modified,?Cache-Control,CF-Cache-Status=[HIT],Age=[3000],Accept-Ranges=[bytes],cf-request-id=[05429ddc2c0000f6fc10349200000001],Server,CF-RAY=[5d4acc0d1826f6fc-GRU]:Keep-Alive:cloudflare
|
`----

.-[ 192.168.122.150/65217 -> 104.18.24.243/80 (http response) ]-
|
| server   = 104.18.24.243/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Date,Content-Type,?Content-Length,Connection=[keep-alive],?Set-Cookie,?Expires,X-Powered-By=[Undertow/1],?ETag,?Last-Modified,?Cache-Control,CF-Cache-Status=[HIT],Age=[3000],Accept-Ranges=[bytes],cf-request-id=[05429ddc2c0000f6e383a9f200000001],Server,CF-RAY=[5d4acc0d1cc4f6e3-GRU]:Keep-Alive:cloudflare
|
`----

.-[ 192.168.122.150/65219 -> 104.18.24.243/80 (http response) ]-
|
| server   = 104.18.24.243/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Date,Content-Type,?Content-Length,Connection=[keep-alive],?Set-Cookie,?Expires,X-Powered-By=[Undertow/1],?ETag,?Last-Modified,?Cache-Control,CF-Cache-Status=[HIT],Age=[3000],Accept-Ranges=[bytes],cf-request-id=[05429ddc2e0000d044c2a65200000001],Server,CF-RAY=[5d4acc0d1faad044-GRU]:Keep-Alive:cloudflare
|
`----

.-[ 192.168.122.150/65218 -> 104.18.24.243/80 (http response) ]-
|
| server   = 104.18.24.243/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Date,Content-Type,?Content-Length,Connection=[keep-alive],?Set-Cookie,?Expires,X-Powered-By=[Undertow/1],?ETag,?Last-Modified,?Cache-Control,CF-Cache-Status=[HIT],Age=[3000],Accept-Ranges=[bytes],cf-request-id=[05429ddc2d0000eed63029b200000001],Server,CF-RAY=[5d4acc0d1beaeed6-GRU]:Keep-Alive:cloudflare
|
`----

.-[ 192.168.122.150/65220 -> 152.199.55.15/80 (syn) ]-
|
| client   = 192.168.122.150/65220
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65220 -> 152.199.55.15/80 (mtu) ]-
|
| client   = 192.168.122.150/65220
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65221 -> 152.199.55.15/80 (syn) ]-
|
| client   = 192.168.122.150/65221
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65221 -> 152.199.55.15/80 (mtu) ]-
|
| client   = 192.168.122.150/65221
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65222 -> 152.199.55.15/80 (syn) ]-
|
| client   = 192.168.122.150/65222
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65222 -> 152.199.55.15/80 (mtu) ]-
|
| client   = 192.168.122.150/65222
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65223 -> 152.199.55.15/80 (syn) ]-
|
| client   = 192.168.122.150/65223
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65223 -> 152.199.55.15/80 (mtu) ]-
|
| client   = 192.168.122.150/65223
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65220 -> 152.199.55.15/80 (syn+ack) ]-
|
| server   = 152.199.55.15/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65220 -> 152.199.55.15/80 (mtu) ]-
|
| server   = 152.199.55.15/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65221 -> 152.199.55.15/80 (syn+ack) ]-
|
| server   = 152.199.55.15/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65221 -> 152.199.55.15/80 (mtu) ]-
|
| server   = 152.199.55.15/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65222 -> 152.199.55.15/80 (syn+ack) ]-
|
| server   = 152.199.55.15/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65222 -> 152.199.55.15/80 (mtu) ]-
|
| server   = 152.199.55.15/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65220 -> 152.199.55.15/80 (http request) ]-
|
| client   = 192.168.122.150/65220
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[application/javascript, */*;q=0.8],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65221 -> 152.199.55.15/80 (http request) ]-
|
| client   = 192.168.122.150/65221
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[application/javascript, */*;q=0.8],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65223 -> 152.199.55.15/80 (syn+ack) ]-
|
| server   = 152.199.55.15/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65223 -> 152.199.55.15/80 (mtu) ]-
|
| server   = 152.199.55.15/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65220 -> 152.199.55.15/80 (http response) ]-
|
| server   = 152.199.55.15/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:?Cache-Control,Date,?Expires,?Location,?Pragma,Server,?Content-Length:Content-Type,Connection,Keep-Alive,Accept-Ranges:nginx
|
`----

.-[ 192.168.122.150/65221 -> 152.199.55.15/80 (http response) ]-
|
| server   = 152.199.55.15/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:?Cache-Control,Date,?Expires,?Location,?Pragma,Server,?Content-Length:Content-Type,Connection,Keep-Alive,Accept-Ranges:nginx
|
`----

.-[ 192.168.122.150/65224 -> 152.199.55.24/80 (syn) ]-
|
| client   = 192.168.122.150/65224
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65224 -> 152.199.55.24/80 (mtu) ]-
|
| client   = 192.168.122.150/65224
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65225 -> 152.199.55.24/80 (syn) ]-
|
| client   = 192.168.122.150/65225
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65225 -> 152.199.55.24/80 (mtu) ]-
|
| client   = 192.168.122.150/65225
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65226 -> 152.199.55.24/80 (syn) ]-
|
| client   = 192.168.122.150/65226
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65226 -> 152.199.55.24/80 (mtu) ]-
|
| client   = 192.168.122.150/65226
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65227 -> 152.199.55.24/80 (syn) ]-
|
| client   = 192.168.122.150/65227
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65227 -> 152.199.55.24/80 (mtu) ]-
|
| client   = 192.168.122.150/65227
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65224 -> 152.199.55.24/80 (syn+ack) ]-
|
| server   = 152.199.55.24/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65224 -> 152.199.55.24/80 (mtu) ]-
|
| server   = 152.199.55.24/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65226 -> 152.199.55.24/80 (syn+ack) ]-
|
| server   = 152.199.55.24/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65226 -> 152.199.55.24/80 (mtu) ]-
|
| server   = 152.199.55.24/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65225 -> 152.199.55.24/80 (syn+ack) ]-
|
| server   = 152.199.55.24/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65225 -> 152.199.55.24/80 (mtu) ]-
|
| server   = 152.199.55.24/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65227 -> 152.199.55.24/80 (syn+ack) ]-
|
| server   = 152.199.55.24/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65227 -> 152.199.55.24/80 (mtu) ]-
|
| server   = 152.199.55.24/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65224 -> 152.199.55.24/80 (http request) ]-
|
| client   = 192.168.122.150/65224
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[application/javascript, */*;q=0.8],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65225 -> 152.199.55.24/80 (http request) ]-
|
| client   = 192.168.122.150/65225
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[application/javascript, */*;q=0.8],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65224 -> 152.199.55.24/80 (http response) ]-
|
| server   = 152.199.55.24/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Access-Control-Allow-Credentials=[true],Access-Control-Allow-Methods=[POST,GET,HEAD,OPTIONS],Date,?Location,Server,Strict-Transport-Security=[max-age=31536000; includeSubdomains],?Content-Length:Content-Type,Connection,Keep-Alive,Accept-Ranges:ECAcc (spb/E486)
|
`----

.-[ 192.168.122.150/65225 -> 152.199.55.24/80 (http response) ]-
|
| server   = 152.199.55.24/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Access-Control-Allow-Credentials=[true],Access-Control-Allow-Methods=[POST,GET,HEAD,OPTIONS],Date,?Location,Server,Strict-Transport-Security=[max-age=31536000; includeSubdomains],?Content-Length:Content-Type,Connection,Keep-Alive,Accept-Ranges:ECAcc (spb/E543)
|
`----

.-[ 192.168.122.150/65228 -> 152.199.55.24/443 (syn) ]-
|
| client   = 192.168.122.150/65228
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65228 -> 152.199.55.24/443 (mtu) ]-
|
| client   = 192.168.122.150/65228
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65229 -> 152.199.55.24/443 (syn) ]-
|
| client   = 192.168.122.150/65229
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65229 -> 152.199.55.24/443 (mtu) ]-
|
| client   = 192.168.122.150/65229
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65228 -> 152.199.55.24/443 (syn+ack) ]-
|
| server   = 152.199.55.24/443
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65228 -> 152.199.55.24/443 (mtu) ]-
|
| server   = 152.199.55.24/443
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65229 -> 152.199.55.24/443 (syn+ack) ]-
|
| server   = 152.199.55.24/443
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65229 -> 152.199.55.24/443 (mtu) ]-
|
| server   = 152.199.55.24/443
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65230 -> 192.16.48.200/80 (syn) ]-
|
| client   = 192.168.122.150/65230
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65230 -> 192.16.48.200/80 (mtu) ]-
|
| client   = 192.168.122.150/65230
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65231 -> 192.16.48.200/80 (syn) ]-
|
| client   = 192.168.122.150/65231
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65231 -> 192.16.48.200/80 (mtu) ]-
|
| client   = 192.168.122.150/65231
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65232 -> 192.16.48.200/80 (syn) ]-
|
| client   = 192.168.122.150/65232
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65232 -> 192.16.48.200/80 (mtu) ]-
|
| client   = 192.168.122.150/65232
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65233 -> 192.16.48.200/80 (syn) ]-
|
| client   = 192.168.122.150/65233
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65233 -> 192.16.48.200/80 (mtu) ]-
|
| client   = 192.168.122.150/65233
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65230 -> 192.16.48.200/80 (syn+ack) ]-
|
| server   = 192.16.48.200/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65230 -> 192.16.48.200/80 (mtu) ]-
|
| server   = 192.16.48.200/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65231 -> 192.16.48.200/80 (syn+ack) ]-
|
| server   = 192.16.48.200/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65231 -> 192.16.48.200/80 (mtu) ]-
|
| server   = 192.16.48.200/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65230 -> 192.16.48.200/80 (http request) ]-
|
| client   = 192.168.122.150/65230
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65231 -> 192.16.48.200/80 (http request) ]-
|
| client   = 192.168.122.150/65231
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65232 -> 192.16.48.200/80 (syn+ack) ]-
|
| server   = 192.16.48.200/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65232 -> 192.16.48.200/80 (mtu) ]-
|
| server   = 192.16.48.200/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65232 -> 192.16.48.200/80 (http request) ]-
|
| client   = 192.168.122.150/65232
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65233 -> 192.16.48.200/80 (syn+ack) ]-
|
| server   = 192.16.48.200/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65233 -> 192.16.48.200/80 (mtu) ]-
|
| server   = 192.16.48.200/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65233 -> 192.16.48.200/80 (http request) ]-
|
| client   = 192.168.122.150/65233
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65231 -> 192.16.48.200/80 (http response) ]-
|
| server   = 192.16.48.200/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Accept-Ranges=[bytes],Age=[4817],Content-MD5=[C2o+PfGPqS3OBLgjYnOBXw==],Content-Type,Date,Etag=[0x8D85B44489E3985],?Last-Modified,Server,X-Cache=[HIT],x-ms-blob-type=[BlockBlob],x-ms-lease-status=[unlocked],x-ms-request-id=[c466bd80-201e-0069-1130-8d18dc000000],x-ms-version=[2009-09-19],?Content-Length:Connection,Keep-Alive:ECAcc (spb/E56B)
|
`----

.-[ 192.168.122.150/65230 -> 192.16.48.200/80 (http response) ]-
|
| server   = 192.16.48.200/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Accept-Ranges=[bytes],Age=[4817],Content-MD5=[C2o+PfGPqS3OBLgjYnOBXw==],Content-Type,Date,Etag=[0x8D85B44489E3985],?Last-Modified,Server,X-Cache=[HIT],x-ms-blob-type=[BlockBlob],x-ms-lease-status=[unlocked],x-ms-request-id=[c466bd80-201e-0069-1130-8d18dc000000],x-ms-version=[2009-09-19],?Content-Length:Connection,Keep-Alive:ECAcc (spb/E56B)
|
`----

.-[ 192.168.122.150/65232 -> 192.16.48.200/80 (http response) ]-
|
| server   = 192.16.48.200/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Accept-Ranges=[bytes],Age=[4817],Content-MD5=[C2o+PfGPqS3OBLgjYnOBXw==],Content-Type,Date,Etag=[0x8D85B44489E3985],?Last-Modified,Server,X-Cache=[HIT],x-ms-blob-type=[BlockBlob],x-ms-lease-status=[unlocked],x-ms-request-id=[c466bd80-201e-0069-1130-8d18dc000000],x-ms-version=[2009-09-19],?Content-Length:Connection,Keep-Alive:ECAcc (spb/E56B)
|
`----

.-[ 192.168.122.150/65233 -> 192.16.48.200/80 (http response) ]-
|
| server   = 192.16.48.200/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Accept-Ranges=[bytes],Age=[4817],Content-MD5=[C2o+PfGPqS3OBLgjYnOBXw==],Content-Type,Date,Etag=[0x8D85B44489E3985],?Last-Modified,Server,X-Cache=[HIT],x-ms-blob-type=[BlockBlob],x-ms-lease-status=[unlocked],x-ms-request-id=[c466bd80-201e-0069-1130-8d18dc000000],x-ms-version=[2009-09-19],?Content-Length:Connection,Keep-Alive:ECAcc (spb/E56B)
|
`----

.-[ 192.168.122.150/65234 -> 76.13.32.147/80 (syn) ]-
|
| client   = 192.168.122.150/65234
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65234 -> 76.13.32.147/80 (mtu) ]-
|
| client   = 192.168.122.150/65234
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65235 -> 76.13.32.147/80 (syn) ]-
|
| client   = 192.168.122.150/65235
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65235 -> 76.13.32.147/80 (mtu) ]-
|
| client   = 192.168.122.150/65235
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65236 -> 76.13.32.147/80 (syn) ]-
|
| client   = 192.168.122.150/65236
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65236 -> 76.13.32.147/80 (mtu) ]-
|
| client   = 192.168.122.150/65236
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65237 -> 76.13.32.147/80 (syn) ]-
|
| client   = 192.168.122.150/65237
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65237 -> 76.13.32.147/80 (mtu) ]-
|
| client   = 192.168.122.150/65237
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65238 -> 52.8.221.8/80 (syn) ]-
|
| client   = 192.168.122.150/65238
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65238 -> 52.8.221.8/80 (mtu) ]-
|
| client   = 192.168.122.150/65238
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65239 -> 52.8.153.173/80 (syn) ]-
|
| client   = 192.168.122.150/65239
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65239 -> 52.8.153.173/80 (mtu) ]-
|
| client   = 192.168.122.150/65239
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65240 -> 52.8.221.8/80 (syn) ]-
|
| client   = 192.168.122.150/65240
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65240 -> 52.8.221.8/80 (mtu) ]-
|
| client   = 192.168.122.150/65240
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65241 -> 52.8.153.173/80 (syn) ]-
|
| client   = 192.168.122.150/65241
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65241 -> 52.8.153.173/80 (mtu) ]-
|
| client   = 192.168.122.150/65241
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65234 -> 76.13.32.147/80 (syn+ack) ]-
|
| server   = 76.13.32.147/80
| os       = ???
| dist     = 20
| params   = none
| raw_sig  = 4:44+20:0:1460:mss*20,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65234 -> 76.13.32.147/80 (mtu) ]-
|
| server   = 76.13.32.147/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65235 -> 76.13.32.147/80 (syn+ack) ]-
|
| server   = 76.13.32.147/80
| os       = ???
| dist     = 19
| params   = none
| raw_sig  = 4:45+19:0:1460:mss*20,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65235 -> 76.13.32.147/80 (mtu) ]-
|
| server   = 76.13.32.147/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65237 -> 76.13.32.147/80 (syn+ack) ]-
|
| server   = 76.13.32.147/80
| os       = ???
| dist     = 20
| params   = none
| raw_sig  = 4:44+20:0:1460:mss*20,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65237 -> 76.13.32.147/80 (mtu) ]-
|
| server   = 76.13.32.147/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65236 -> 76.13.32.147/80 (syn+ack) ]-
|
| server   = 76.13.32.147/80
| os       = ???
| dist     = 19
| params   = none
| raw_sig  = 4:45+19:0:1460:mss*20,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65236 -> 76.13.32.147/80 (mtu) ]-
|
| server   = 76.13.32.147/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65234 -> 76.13.32.147/80 (http request) ]-
|
| client   = 192.168.122.150/65234
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65235 -> 76.13.32.147/80 (http request) ]-
|
| client   = 192.168.122.150/65235
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive]:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65235 -> 76.13.32.147/80 (http response) ]-
|
| server   = 76.13.32.147/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Date,?Cache-Control,Content-Type,?Content-Length,Server,Age=[0],Connection=[keep-alive],X-Frame-Options=[DENY],X-Content-Type-Options=[nosniff],X-XSS-Protection=[1; mode=block],Referrer-Policy=[strict-origin-when-cross-origin]:Keep-Alive,Accept-Ranges:ATS
|
`----

.-[ 192.168.122.150/65234 -> 76.13.32.147/80 (http response) ]-
|
| server   = 76.13.32.147/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Date,Content-Type,?Location,?Content-Length,Server,Age=[0],Connection=[keep-alive],X-Frame-Options=[DENY],X-Content-Type-Options=[nosniff],X-XSS-Protection=[1; mode=block],Referrer-Policy=[strict-origin-when-cross-origin]:Keep-Alive,Accept-Ranges:ATS
|
`----

.-[ 192.168.122.150/65241 -> 52.8.153.173/80 (syn+ack) ]-
|
| server   = 52.8.153.173/80
| os       = ???
| dist     = 25
| params   = tos:0x01
| raw_sig  = 4:230+25:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65241 -> 52.8.153.173/80 (mtu) ]-
|
| server   = 52.8.153.173/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65241 -> 52.8.153.173/80 (http request) ]-
|
| client   = 192.168.122.150/65241
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65239 -> 52.8.153.173/80 (syn+ack) ]-
|
| server   = 52.8.153.173/80
| os       = ???
| dist     = 25
| params   = tos:0x01
| raw_sig  = 4:230+25:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65239 -> 52.8.153.173/80 (mtu) ]-
|
| server   = 52.8.153.173/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65238 -> 52.8.221.8/80 (syn+ack) ]-
|
| server   = 52.8.221.8/80
| os       = ???
| dist     = 25
| params   = tos:0x01
| raw_sig  = 4:230+25:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65238 -> 52.8.221.8/80 (mtu) ]-
|
| server   = 52.8.221.8/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65238 -> 52.8.221.8/80 (http request) ]-
|
| client   = 192.168.122.150/65238
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65240 -> 52.8.221.8/80 (syn+ack) ]-
|
| server   = 52.8.221.8/80
| os       = ???
| dist     = 25
| params   = tos:0x01
| raw_sig  = 4:230+25:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65240 -> 52.8.221.8/80 (mtu) ]-
|
| server   = 52.8.221.8/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65242 -> 52.73.227.203/80 (syn) ]-
|
| client   = 192.168.122.150/65242
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65242 -> 52.73.227.203/80 (mtu) ]-
|
| client   = 192.168.122.150/65242
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65243 -> 52.73.227.203/80 (syn) ]-
|
| client   = 192.168.122.150/65243
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65243 -> 52.73.227.203/80 (mtu) ]-
|
| client   = 192.168.122.150/65243
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65244 -> 52.73.227.203/80 (syn) ]-
|
| client   = 192.168.122.150/65244
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65244 -> 52.73.227.203/80 (mtu) ]-
|
| client   = 192.168.122.150/65244
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65245 -> 52.73.227.203/80 (syn) ]-
|
| client   = 192.168.122.150/65245
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65245 -> 52.73.227.203/80 (mtu) ]-
|
| client   = 192.168.122.150/65245
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65246 -> 204.79.197.200/443 (syn) ]-
|
| client   = 192.168.122.150/65246
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65246 -> 204.79.197.200/443 (mtu) ]-
|
| client   = 192.168.122.150/65246
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65247 -> 204.79.197.200/443 (syn) ]-
|
| client   = 192.168.122.150/65247
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65247 -> 204.79.197.200/443 (mtu) ]-
|
| client   = 192.168.122.150/65247
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65246 -> 204.79.197.200/443 (syn+ack) ]-
|
| server   = 204.79.197.200/443
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:119+9:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65246 -> 204.79.197.200/443 (mtu) ]-
|
| server   = 204.79.197.200/443
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65247 -> 204.79.197.200/443 (syn+ack) ]-
|
| server   = 204.79.197.200/443
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:119+9:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65247 -> 204.79.197.200/443 (mtu) ]-
|
| server   = 204.79.197.200/443
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65242 -> 52.73.227.203/80 (syn+ack) ]-
|
| server   = 52.73.227.203/80
| os       = ???
| dist     = 28
| params   = none
| raw_sig  = 4:227+28:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65242 -> 52.73.227.203/80 (mtu) ]-
|
| server   = 52.73.227.203/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65243 -> 52.73.227.203/80 (syn+ack) ]-
|
| server   = 52.73.227.203/80
| os       = ???
| dist     = 28
| params   = none
| raw_sig  = 4:227+28:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65243 -> 52.73.227.203/80 (mtu) ]-
|
| server   = 52.73.227.203/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65244 -> 52.73.227.203/80 (syn+ack) ]-
|
| server   = 52.73.227.203/80
| os       = ???
| dist     = 28
| params   = none
| raw_sig  = 4:227+28:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65244 -> 52.73.227.203/80 (mtu) ]-
|
| server   = 52.73.227.203/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65245 -> 52.73.227.203/80 (syn+ack) ]-
|
| server   = 52.73.227.203/80
| os       = ???
| dist     = 28
| params   = none
| raw_sig  = 4:227+28:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65245 -> 52.73.227.203/80 (mtu) ]-
|
| server   = 52.73.227.203/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65243 -> 52.73.227.203/80 (http request) ]-
|
| client   = 192.168.122.150/65243
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[application/javascript, */*;q=0.8],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65242 -> 52.73.227.203/80 (http request) ]-
|
| client   = 192.168.122.150/65242
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[application/javascript, */*;q=0.8],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65241 -> 52.8.153.173/80 (http response) ]-
|
| server   = 52.8.153.173/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Content-Type,Server,?Content-Length,Connection=[keep-alive]:Keep-Alive,Accept-Ranges,Date:ribs2.0
|
`----

.-[ 192.168.122.150/65238 -> 52.8.221.8/80 (http response) ]-
|
| server   = 52.8.221.8/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Content-Type,Server,?Content-Length,Connection=[keep-alive]:Keep-Alive,Accept-Ranges,Date:ribs2.0
|
`----

.-[ 192.168.122.150/65243 -> 52.73.227.203/80 (http response) ]-
|
| server   = 52.73.227.203/80
| app      = nginx 0.x
| lang     = none
| params   = dishonest
| raw_sig  = 1:Server,Date,Content-Type,?Content-Length,Connection=[keep-alive],?Location:Keep-Alive,Accept-Ranges:awselb/2.0
|
`----

.-[ 192.168.122.150/65242 -> 52.73.227.203/80 (http response) ]-
|
| server   = 52.73.227.203/80
| app      = nginx 0.x
| lang     = none
| params   = dishonest
| raw_sig  = 1:Server,Date,Content-Type,?Content-Length,Connection=[keep-alive],?Location:Keep-Alive,Accept-Ranges:awselb/2.0
|
`----

.-[ 192.168.122.150/65248 -> 52.73.227.203/443 (syn) ]-
|
| client   = 192.168.122.150/65248
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65248 -> 52.73.227.203/443 (mtu) ]-
|
| client   = 192.168.122.150/65248
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65249 -> 52.73.227.203/443 (syn) ]-
|
| client   = 192.168.122.150/65249
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65249 -> 52.73.227.203/443 (mtu) ]-
|
| client   = 192.168.122.150/65249
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65248 -> 52.73.227.203/443 (syn+ack) ]-
|
| server   = 52.73.227.203/443
| os       = ???
| dist     = 28
| params   = none
| raw_sig  = 4:227+28:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65248 -> 52.73.227.203/443 (mtu) ]-
|
| server   = 52.73.227.203/443
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65249 -> 52.73.227.203/443 (syn+ack) ]-
|
| server   = 52.73.227.203/443
| os       = ???
| dist     = 28
| params   = none
| raw_sig  = 4:227+28:0:1460:26883,8:mss,nop,nop,sok,nop,ws:df:0
|
`----

.-[ 192.168.122.150/65249 -> 52.73.227.203/443 (mtu) ]-
|
| server   = 52.73.227.203/443
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65250 -> 204.79.197.200/80 (syn) ]-
|
| client   = 192.168.122.150/65250
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65250 -> 204.79.197.200/80 (mtu) ]-
|
| client   = 192.168.122.150/65250
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65251 -> 204.79.197.200/80 (syn) ]-
|
| client   = 192.168.122.150/65251
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65251 -> 204.79.197.200/80 (mtu) ]-
|
| client   = 192.168.122.150/65251
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65251 -> 204.79.197.200/80 (syn+ack) ]-
|
| server   = 204.79.197.200/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:119+9:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65251 -> 204.79.197.200/80 (mtu) ]-
|
| server   = 204.79.197.200/80
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65250 -> 204.79.197.200/80 (syn+ack) ]-
|
| server   = 204.79.197.200/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:119+9:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65250 -> 204.79.197.200/80 (mtu) ]-
|
| server   = 204.79.197.200/80
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65251 -> 204.79.197.200/80 (http request) ]-
|
| client   = 192.168.122.150/65251
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65251 -> 204.79.197.200/80 (http response) ]-
|
| server   = 204.79.197.200/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:?Cache-Control,?Pragma,?Content-Length,Content-Type,?Last-Modified,Accept-Ranges=[bytes],?ETag,P3P=[CP="BUS CUR CONo FIN IVDo ONL OUR PHY SAMo TELo"],X-Powered-By=[ASP.NET],X-MSEdge-Ref=[Ref A: 9E066E1C94784B12B1D14335E8657B05 Ref B: SAO03EDGE0812 Ref C: 2020-09-18T11:41:22Z],Date:Connection,Keep-Alive:
|
`----

.-[ 192.168.122.150/65252 -> 204.79.197.200/80 (syn) ]-
|
| client   = 192.168.122.150/65252
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65252 -> 204.79.197.200/80 (mtu) ]-
|
| client   = 192.168.122.150/65252
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65253 -> 204.79.197.200/80 (syn) ]-
|
| client   = 192.168.122.150/65253
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65253 -> 204.79.197.200/80 (mtu) ]-
|
| client   = 192.168.122.150/65253
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65252 -> 204.79.197.200/80 (syn+ack) ]-
|
| server   = 204.79.197.200/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:119+9:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65252 -> 204.79.197.200/80 (mtu) ]-
|
| server   = 204.79.197.200/80
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65252 -> 204.79.197.200/80 (http request) ]-
|
| client   = 192.168.122.150/65252
| app      = MSIE 8 or newer
| lang     = Portuguese
| params   = none
| raw_sig  = 1:Accept=[image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5],?Referer,Accept-Language=[pt-BR],User-Agent,Accept-Encoding=[gzip, deflate],Host,Connection=[Keep-Alive],?Cookie:Accept-Charset,Keep-Alive:Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
|
`----

.-[ 192.168.122.150/65253 -> 204.79.197.200/80 (syn+ack) ]-
|
| server   = 204.79.197.200/80
| os       = ???
| dist     = 10
| params   = none
| raw_sig  = 4:118+10:0:1440:65535,8:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65253 -> 204.79.197.200/80 (mtu) ]-
|
| server   = 204.79.197.200/80
| link     = IPIP or SIT
| raw_mtu  = 1480
|
`----

.-[ 192.168.122.150/65252 -> 204.79.197.200/80 (http response) ]-
|
| server   = 204.79.197.200/80
| app      = ???
| lang     = none
| params   = anonymous
| raw_sig  = 1:?Cache-Control,?Pragma,?Content-Length,Content-Type,?Last-Modified,Accept-Ranges=[bytes],?ETag,P3P=[CP="BUS CUR CONo FIN IVDo ONL OUR PHY SAMo TELo"],X-Powered-By=[ASP.NET],X-MSEdge-Ref=[Ref A: 42281E44BD5B43EB8958E0D607234AB2 Ref B: SAO03EDGE0222 Ref C: 2020-09-18T11:41:22Z],Date:Connection,Keep-Alive:
|
`----

.-[ 192.168.122.150/65254 -> 192.16.58.8/80 (syn) ]-
|
| client   = 192.168.122.150/65254
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65254 -> 192.16.58.8/80 (mtu) ]-
|
| client   = 192.168.122.150/65254
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65254 -> 192.16.58.8/80 (syn+ack) ]-
|
| server   = 192.16.58.8/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65254 -> 192.16.58.8/80 (mtu) ]-
|
| server   = 192.16.58.8/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65254 -> 192.16.58.8/80 (http request) ]-
|
| client   = 192.168.122.150/65254
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Connection=[Keep-Alive],Accept=[*/*],User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65254 -> 192.16.58.8/80 (http response) ]-
|
| server   = 192.16.58.8/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Accept-Ranges=[bytes],Age=[5406],?Cache-Control,Content-Type,Date,Etag=["5f645a3d-1d7"],?Expires,?Last-Modified,Server,X-Cache=[HIT],?Content-Length:Connection,Keep-Alive:ECS (spb/E4E0)
|
`----

.-[ 192.168.122.150/65255 -> 192.16.58.8/80 (syn) ]-
|
| client   = 192.168.122.150/65255
| os       = Windows 7 or 8
| dist     = 0
| params   = none
| raw_sig  = 4:128+0:0:1460:8192,2:mss,nop,ws,nop,nop,sok:df,id+:0
|
`----

.-[ 192.168.122.150/65255 -> 192.16.58.8/80 (mtu) ]-
|
| client   = 192.168.122.150/65255
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65255 -> 192.16.58.8/80 (syn+ack) ]-
|
| server   = 192.16.58.8/80
| os       = ???
| dist     = 9
| params   = none
| raw_sig  = 4:55+9:0:1460:65535,9:mss,nop,nop,sok,nop,ws::0
|
`----

.-[ 192.168.122.150/65255 -> 192.16.58.8/80 (mtu) ]-
|
| server   = 192.16.58.8/80
| link     = Ethernet or modem
| raw_mtu  = 1500
|
`----

.-[ 192.168.122.150/65255 -> 192.16.58.8/80 (http request) ]-
|
| client   = 192.168.122.150/65255
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:?Cache-Control,Connection=[Keep-Alive],Accept=[*/*],?If-Modified-Since,?If-None-Match,User-Agent,Host:Accept-Encoding,Accept-Language,Accept-Charset,Keep-Alive:Microsoft-CryptoAPI/6.1
|
`----

.-[ 192.168.122.150/65255 -> 192.16.58.8/80 (http response) ]-
|
| server   = 192.16.58.8/80
| app      = ???
| lang     = none
| params   = none
| raw_sig  = 1:Accept-Ranges=[bytes],Age=[5766],?Cache-Control,Date,Etag=["5f645a3d-1d7"],?Expires,?Last-Modified,Server,X-Cache=[HIT]:Content-Type,Connection,Keep-Alive:ECS (spb/E560)
|
`----


All done. Processed 1429 packets.
```
