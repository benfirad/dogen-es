#!/bin/bash
# dogen.es: onaylanmış bir blog taslağını yayınlar.
# Yalnızca Fırat'ın Duffy onayıyla (veya elle) çalıştırılır.
# Kullanım: tools/blog_publish.sh <slug>
set -euo pipefail
SLUG="${1:?slug gerekli}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
F="$ROOT/content/blog/$SLUG.md"
cd "$ROOT"

[ -f "$F" ] || { echo "Taslak yok: $F"; exit 1; }
if grep -q "\[KONTROL\]" "$F"; then
  echo "Yayın durduruldu: $F içinde $(grep -o '\[KONTROL\]' "$F" | wc -l | tr -d ' ') adet [KONTROL] işareti var. Önce düzeltin."
  exit 2
fi
if [ -n "$(git status --porcelain -- . ':!content/blog/'"$SLUG"'.md' ':!content/blog/topics.txt')" ]; then
  echo "Yayın durduruldu: depoda başka commit edilmemiş değişiklik var."
  git status --short
  exit 3
fi

TODAY="$(date +%Y-%m-%d)"
/usr/bin/sed -i '' -e '/^draft: true$/d' -e "s/^date: .*/date: $TODAY/" -e "s/^updated: .*/updated: $TODAY/" "$F"
/usr/bin/python3 src/build.py
git add -A content blog sitemap.xml index.html es 404.html robots.txt
git -c user.name=daak -c user.email=70284321+benfirad@users.noreply.github.com \
  commit -q -m "blog: $SLUG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
GIT_TERMINAL_PROMPT=0 git push -q origin HEAD
echo "Yayında: https://dogen.es/blog/$SLUG/ ($(git rev-parse --short HEAD))"
