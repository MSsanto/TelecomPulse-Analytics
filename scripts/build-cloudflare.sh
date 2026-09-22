#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip
pip install -e .

cd web
npm install
npm run build

test -f dist/index.html
test -f dist/data/dashboard-v1.json

echo "Cloudflare build artifact ready at web/dist"
