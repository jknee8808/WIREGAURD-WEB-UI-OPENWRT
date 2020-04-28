#!/bin/sh


echo Content-type: text/plain
echo
DOWNLOAD=`ifconfig wg0 2> /dev/null | grep "RX bytes" |  busybox awk '{print $3,$4}' | busybox tr -d '()'`
if [ -n "$DOWNLOAD" ]; then
echo "<input type='button'  onclick='javascript:ovpnstop()' class='n' value='STOP'>"
else
echo "<input type='button'  onclick='javascript:ovpnstart()' class='m' value='START'>"
fi