@echo off
echo user amazon> ftpcmd.dat
echo Password!23>> ftpcmd.dat
echo bin>> ftpcmd.dat
echo put %1>> ftpcmd.dat
echo quit>> ftpcmd.dat
ftp -n -s:ftpcmd.dat ftp.bray.sdl.com

