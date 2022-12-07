@echo off
FOR /L %%A IN (1,1,10) DO (
  @echo off
  neofetch
  echo %%A
)
pause