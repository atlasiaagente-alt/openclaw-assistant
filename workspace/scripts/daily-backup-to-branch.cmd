@echo off
setlocal EnableExtensions

set "REPO=C:\Users\Gustavo\.openclaw"
set "BRANCH=backup"
set "TS=%DATE% %TIME%"

cd /d "%REPO%" || exit /b 1

git rev-parse --is-inside-work-tree >nul 2>nul || exit /b 2

for /f "delims=" %%i in ('git branch --show-current') do set "ORIG_BRANCH=%%i"
if not defined ORIG_BRANCH set "ORIG_BRANCH=main"

git fetch origin %BRANCH% >nul 2>nul

git show-ref --verify --quiet refs/heads/%BRANCH%
if errorlevel 1 (
  git ls-remote --exit-code --heads origin %BRANCH% >nul 2>nul
  if errorlevel 1 (
    git branch %BRANCH% %ORIG_BRANCH% || exit /b 3
  ) else (
    git branch --track %BRANCH% origin/%BRANCH% || exit /b 4
  )
)

git checkout %BRANCH% || exit /b 5
git pull --ff-only origin %BRANCH% >nul 2>nul

git add -A || exit /b 6
git commit -m "backup: %TS%" >nul 2>nul
if errorlevel 1 (
  echo No changes to commit.
) else (
  git push origin %BRANCH% || exit /b 7
)

git checkout %ORIG_BRANCH% >nul 2>nul
if errorlevel 1 exit /b 8
exit /b 0
