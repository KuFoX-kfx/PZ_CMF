@echo off
::Check all reg files and create
:check_reg
cls
for /f "tokens=1*" %%i In ('reg query "HKCU\Software\KuFoX\PZCMF" /v ZB_Server') DO set ZB_Server=%%i
for /f "tokens=1*" %%i In ('reg query "HKCU\Software\KuFoX\PZCMF" /v ZB_Multiplayer') DO set ZB_Multiplayer=%%i
for /f "tokens=1*" %%i In ('reg query "HKCU\Software\KuFoX\PZCMF" /v BCKP_Save') DO set BCKP_Save=%%i
if "%ZB_Server%" == "" (Goto Create_Reg_ZB_Server)else (
if "%ZB_Multiplayer%" == "" (Goto Create_Reg_ZB_Multiplayer)else (
if "%BCKP_Save%" == "" (Goto Create_Reg_BCKP_Save)else (
Goto Menu)))
:Create_Reg_ZB_Server
reg add "HKCU\Software\KuFoX\PZCMF" /v ZB_Server /t REG_EXPAND_SZ /d \zomboid\server /f
Goto check_reg
:Create_Reg_ZB_Multiplayer
reg add "HKCU\Software\KuFoX\PZCMF" /v ZB_Multiplayer /t REG_EXPAND_SZ /d \zomboid\saves\multiplayer /f
Goto check_reg
:Create_Reg_BCKP_Save
reg add "HKCU\Software\KuFoX\PZCMF" /v BCKP_Save /t REG_EXPAND_SZ /d \MapAndFiles /f
Goto check_reg
::Just Menu
:Menu
@echo off
cls
echo 0.Exit from program(Default)
echo 1.Specify path to the folder `\Project_Zomboid\server`
echo 2.Specify path to the folder `\Project_Zomboid\saves\multiplayer`
echo 3.Specify path to the folder `\Project_Zomboid\buckup`
echo 4.Change files from SAVE to PZ
echo 5.Change files from PZ to SAVE
set /p "C1= Select: " & echo:
If "%C1%"=="0" (
    exit /b
)else (
If "%C1%"=="1" (
    Goto CRT_Reg_ZB_Server
)else (
If "%C1%"=="2" (
    Goto CRT_Reg_ZB_Multiplayer
)else (
If "%C1%"=="3" (
    Goto CRT_reg_BCKP_Save
)else (
If "%C1%"=="4" (
    Goto RPLC_SAVEtoPZ
)else (
If "%C1%"=="5" (
    Goto RPLC_PZtoSAVE
)else (Goto Menu)
)))))
Goto Menu
::Heart of programm
:CRT_Reg_ZB_Server
set /p "Patch=Enter patch to `\zomboid\server` folder: "
reg add "HKCU\Software\KuFoX\PZCMF" /v ZB_Server /t REG_EXPAND_SZ /d %Patch% /f
Goto Menu
:CRT_Reg_ZB_Multiplayer
set /p "Patch=Enter patch to `\zomboid\saves\multiplayer` folder: "
reg add "HKCU\Software\KuFoX\PZCMF" /v ZB_Multiplayer /t REG_EXPAND_SZ /d %Patch% /f
Goto Menu
:CRT_reg_BCKP_Save
set /p "Patch=Enter patch to `\SAVE` folder: "
reg add "HKCU\Software\KuFoX\PZCMF" /v BCKP_Save /t REG_EXPAND_SZ /d %Patch% /f
Goto Menu
:RPLC_SAVEtoPZ
xcopy %BCKP_Save%\PvP %ZB_Multiplayer%\PvP /EYI
xcopy %BCKP_Save%\PvP_player %ZB_Multiplayer%\PvP_player /EYI
copy %BCKP_Save%\PvP.ini %ZB_Server%\PvP.ini /Y
copy %BCKP_Save%\PvP_SandboxVars.lua %ZB_Server%\PvP_SandboxVars.lua /Y
copy %BCKP_Save%\PvP_spawnregions.lua %ZB_Server%\PvP_spawnregions.lua /Y
Goto Menu
:RPLC_PZtoSAVE
xcopy %ZB_Multiplayer%\PvP /EYI %BCKP_Save%\PvP
xcopy %ZB_Multiplayer%\PvP_player /EYI %BCKP_Save%\PvP_player
copy %ZB_Server%\PvP.ini /Y %BCKP_Save%\PvP.ini
copy %ZB_Server%\PvP_SandboxVars.lua /Y %BCKP_Save%\PvP_SandboxVars.lua
copy %ZB_Server%\PvP_spawnregions.lua /Y %BCKP_Save%\PvP_spawnregions.lua
Goto Menu
