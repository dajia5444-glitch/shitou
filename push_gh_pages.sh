#!/bin/zsh
# 三看板 GitHub Pages 推送脚本
# 用法：/bin/zsh /Users/shitou/Desktop/星河无界/项目跟踪/push_gh_pages.sh
# token 从 ~/.workbuddy/secrets/gh_pages_token 读取（不打印）
set -e
cd "$(dirname "$0")"

TOKEN=$(cat ~/.workbuddy/secrets/gh_pages_token | tr -d '\n')
REMOTE="https://x-access-token:${TOKEN}@github.com/dajia5444-glitch/shitou.git"

# 强制刷新 mtime，确保 git diff 总能触发（内容变化以 最后更新时间 为准）
touch index.html 项目需求排期看板.html 生产问题看板.html 资源甘特图.html 2>/dev/null || true

git add -A
if ! git diff --cached --quiet; then
  git -c user.name="xhwj-bot" -c user.email="xhwj-bot@users.noreply.github.com" commit -m "看板更新 $(date '+%Y-%m-%d %H:%M')" >/dev/null
fi

# 首次推送（远端已有无关历史）时自动回退 force push；之后均为增量推送
git push "$REMOTE" main 2>&1 | sed 's/x-access-token:[^@]*/x-access-token:***/g' || \
  git push -f "$REMOTE" main 2>&1 | sed 's/x-access-token:[^@]*/x-access-token:***/g'

echo "PUSHED"
