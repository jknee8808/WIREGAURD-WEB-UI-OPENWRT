#!/bin/sh

echo Content-type: text/html
echo



procss=`cat /etc/config/network | grep #`
if [ -n "$procss" ]; then


echo pls save or select a config
else

/etc/init.d/network reload
ifdown wg0
ifup wg0
echo wireguard has been started

fi

