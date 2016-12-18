@echo off
dir /b/s \\Sea-6900078045\c$\7z\Tier2\*.xml >list.txt
REM remove \\Sea-6900078045\c$\7z\Tier2\
replace \\ with \t
