#!/bin/sh
# Regénère vendor/anthropic-sdk.mjs : le SDK officiel Anthropic (TypeScript/JS) en un seul fichier ESM
# pour le navigateur. Utilisé par l'appli installée quand l'utilisateur a enregistré sa clé API.
set -e
VERSION=${1:-0.131.0}
TMP=$(mktemp -d)
cd "$TMP"
npm init -y >/dev/null
npm install --silent "@anthropic-ai/sdk@$VERSION" esbuild@0.24.0
echo 'export { default } from "@anthropic-ai/sdk";' > entry.mjs
npx esbuild entry.mjs --bundle --format=esm --platform=browser --minify --legal-comments=eof --outfile=anthropic-sdk.mjs
cd - >/dev/null
cp "$TMP/anthropic-sdk.mjs" vendor/anthropic-sdk.mjs
cp "$TMP/node_modules/@anthropic-ai/sdk/LICENSE" vendor/LICENSE-anthropic-sdk.txt
echo "vendor/anthropic-sdk.mjs mis à jour (SDK $VERSION)"
