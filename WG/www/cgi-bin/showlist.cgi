#!/bin/sh



echo Content-type: text/html
echo
SET=`cat /www/cfg.sys`
echo "<select class='y' name='config'>"
echo "<option>$SET</option>"
cd /tmp/ && ls *.txt | busybox sed 's/.txt//' | while read LINE; do
     echo "<option>$LINE</option>"
done
echo "</select>"
