#!/bin/sh
PRINT=`cat`
FILENAME=`echo "$PRINT" | busybox sed -n '4p' | busybox sed 's/\r$//'`
rm "/tmp/$FILENAME.txt"
SET=`cat /www/cfg.sys`

if [ "$SET" = "$FILENAME" ]; then 
procss=`cat /tmp/$SSLOCATE.txt | grep wireguard`




rm "/www/cfg.sys"
ifdown wg0


fi
cat << EOF

<HTML>

<meta http-equiv="Refresh" content="0; url=http://192.168.1.1/index.html">

</HTML>