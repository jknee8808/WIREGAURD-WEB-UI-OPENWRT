#!/bin/ash
echo Content-type: text/html
echo
echo

USERNAME=${QUERY_STRING#*username=}
USERNAME=${USERNAME%%&*}
USERNAME=${USERNAME//+/ }

USERNAME2=${QUERY_STRING#*username2=}
USERNAME2=${USERNAME2%%&*}
USERNAME2=${USERNAME2//+/ }

USERNAME3=${QUERY_STRING#*username3=}
USERNAME3=${USERNAME3%%&*}
USERNAME3=${USERNAME3//+/ }

USERNAME4=${QUERY_STRING#*username4=}
USERNAME4=${USERNAME4%%&*}
USERNAME4=${USERNAME4//+/ }


echo "$USERNAME" > /www/wifiname.txt

echo "$USERNAME2" > /www/wifipass.txt

PASS=`cat /www/wifipass.txt`
NAME=`cat /www/wifiname.txt`


uci set wireless.@wifi-iface[0].key="$PASS"
uci set wireless.@wifi-iface[0].ssid="$NAME"
uci set wireless.@wifi-iface[0].encryption="psk"
uci set wireless.@wifi-iface[1].key="$PASS"
uci set wireless.@wifi-iface[1].ssid="enjoylifevpn"
uci set wireless.@wifi-iface[1].encryption="psk"


uci commit wireless
wifi reload
uci set wireless.@wifi-device[1].disabled=0
uci set wireless.@wifi-device[0].disabled=0; uci commit wireless; wifi

#CODED BY JECJECKOH

cat << EOF


<HTML>

<meta http-equiv="Refresh" content="1; url=http://192.168.1.1/index.html">

</HTML>