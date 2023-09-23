::OLD
@echo off
cls
set PvP_Buckup=\PvP_Saves
set ZB_Server=\zomboid\server
set ZB_Multiplayer=\zomboid\saves\multiplayer
echo Check all path to files
echo:
echo Folder with your buckup files
echo %PvP_Buckup%
echo Files in folder \zomboid\server\
echo %ZB_Server%\Pvp.ini
echo %ZB_Server%\PvP_SandBoxVars.lua
echo %ZB_Server%\PvP_Spawnregions.lua
echo Files in folder \zomboid\multiplayer\
echo %ZB_Multiplayer%\Pvp
echo %ZB_Multiplayer%\Pvp_player
echo:
set chice=0
set /p "chice=1 for Yes, 0 for No: " & echo:
if %chice%==1 (Goto CYes)else (Goto end)
:CYes
xcopy %PvP_Buckup%\PvP %ZB_Multiplayer%\PvP /EYI
xcopy %PvP_Buckup%\PvP_player %ZB_Multiplayer%\PvP_player /EYI
copy %PvP_Buckup%\PvP.ini %ZB_Server%\PvP.ini /Y
copy %PvP_Buckup%\PvP_SandboxVars.lua %ZB_Server%\PvP_SandboxVars.lua /Y
copy %PvP_Buckup%\PvP_spawnregions.lua %ZB_Server%\PvP_spawnregions.lua /Y
:end
::OLD