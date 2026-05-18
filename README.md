# 1. Pull the rebuild from the branch I pushed to
git clone --branch claude/deep-analysis-dS8H8 --depth 1 \
  https://github.com/con123-gif/URT-Enhanced-v2.0.git /tmp/urt-rebuild

# 2. Copy just the rebuild folder into a fresh checkout of your new repo
git clone https://github.com/con123-gif/Newtons-cathedral-.git ~/Newtons-cathedral
cp -r /tmp/urt-rebuild/newtons-cathedral/. ~/Newtons-cathedral/

# 3. Commit & push
cd ~/Newtons-cathedral
git add .
git commit -m "Newton's Cathedral v0.2.0 — 56 predictions, median 0.03% rel-err"
git push -u origin main
