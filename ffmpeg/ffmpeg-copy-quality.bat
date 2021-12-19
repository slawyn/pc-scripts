SET currentpath=%CD%
SET execpath=%CD%\ffmpeg-N-101932-g309e3cc15c-win64-gpl-shared\bin
pushd %~dp0
rem %execpath%\ffmpeg -i %currentpath%\Joined.avi  -qscale 0 -y %currentpath%\Converted.mp4 
%execpath%\ffmpeg -i base.m4a -c:v copy -c:a libmp3lame -q:a 4 output.mp3
popd
pause