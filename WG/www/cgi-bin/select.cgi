#!/bin/sh

echo Content-type: text/html
echo
echo

FILE=`cat`
case "$REQUEST_METHOD" in
  POST)
    (
	
        #echo "$FILE" | busybox sed -n '3p' | busybox sed 's/\r$//' > /tmp/cfg.sys
	#echo "$FILE" | busybox sed -n '5p' | busybox sed 's/\r$//' >> /tmp/cfg.sys

		echo "$FILE" | busybox sed -n '4p' | busybox sed 's/\r$//' > /www/cfg.sys
		#echo "$FILE" | busybox sed -n '8p' | busybox sed 's/\r$//' > /www/host.sys
SSLOCATE=`cat /www/cfg.sys`
#HOST=`cat /www/host.sys`
SSLPORT=`cat /tmp/$SSLOCATE.ovpn | grep "remote " | busybox awk '{print $2}'`
#PAYLOAD=`cat /tmp/$HOST.host | grep "host " | busybox awk '{print $2}'`
	
 sed -i '/#/,/#/d' /etc/config/network
		
procss=`cat /tmp/$SSLOCATE.txt | grep #`
procss=`cat /tmp/$SSLOCATE.txt | grep wireguard`



 

if [ -n "$procss" ]; then
 sed -i '/#/,/#/d' /etc/config/network
		

cat /tmp/$SSLOCATE.txt >> /etc/config/network


 wg=`wg show`
echo '$WG' > /tmp/wireguard.log
/etc/init.d/openvpn stop
/etc/init.d/openvpn disable

ifdown wg0

else
ifdown wg0
 sed -i '/#/,/#/d' /etc/config/network		

fi


    )


    echo
    ;;

  *)

    echo

esac





/etc/init.d/network reload
ifdown wg0


cat << EOF

<HTML>

<meta http-equiv="Refresh" content="0; url=http://192.168.1.1/index.html">

</HTML>




