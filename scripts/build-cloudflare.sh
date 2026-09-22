#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip
pip install -e .

cd web
npm install
npm run build

test -f dist/index.html
test -f dist/data/dashboard-v2.json
grep -q '"contract_version": "2.0"' dist/data/dashboard-v2.json
grep -q '"data_mode": "official_public"' dist/data/dashboard-v2.json

echo "Cloudflare v2 real-data build artifact ready at web/dist"
