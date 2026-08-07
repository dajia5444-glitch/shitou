# -*- coding: utf-8 -*-
"""生产问题看板更新 2026-08-07 18:15 轮"""
import re

PATH = '/Users/shitou/Desktop/星河无界/项目跟踪/生产问题看板.html'
with open(PATH, 'r', encoding='utf-8') as f:
    c = f.read()

CHANGES = []  # (描述, 状态)

def do(desc, old, new, cnt=1):
    global c
    n = c.count(old)
    if n != cnt:
        CHANGES.append((desc, f"FAIL count={n} (期望{cnt})"))
        return False
    c = c.replace(old, new)
    CHANGES.append((desc, f"OK x{n}"))
    return True

def get_card(no):
    m = re.search(rf'(<article class="issue-card" data-id="no-{no}" data-no="{no}">.*?</article>)', c, re.S)
    return m.group(1) if m else None

def put_card(no, new_card):
    global c
    old = get_card(no)
    if old:
        c = c.replace(old, new_card)
        return True
    return False

# ========== 全局：时间戳 / hero ==========
do('hero时间戳', '最后更新 · 北京时间 2026-08-07 16:10', '最后更新 · 北京时间 2026-08-07 18:15')
do('右上角40→43', 'border-radius:999px;">40 个问题</div>', 'border-radius:999px;">43 个问题</div>')
do('hero处理中28→26', '<div class="hero-stat"><div class="v nums">28</div><div class="l">处理中</div></div>',
   '<div class="hero-stat"><div class="v nums">26</div><div class="l">处理中</div></div>')
do('hero已修复12→14', '<div class="hero-stat"><div class="v nums">12</div><div class="l">已修复</div></div>',
   '<div class="hero-stat"><div class="v nums">14</div><div class="l">已修复</div></div>')

# 08-06 date-stat：处理中4→2、已修复3→5
old_ds = '''      处理中
      <span class="chip" style="background:#ef4444">4</span>
      待处理
      <span class="chip" style="background:#a855f7">0</span>
      已修复
      <span class="chip" style="background:#22c55e">3</span>'''
new_ds = '''      处理中
      <span class="chip" style="background:#ef4444">2</span>
      待处理
      <span class="chip" style="background:#a855f7">0</span>
      已修复
      <span class="chip" style="background:#22c55e">5</span>'''
do('08-06 date-stat', old_ds, new_ds)

anchor32 = '</div></div></div>\n    <div class="detail-section"><div class="detail-label">处理方案'

# ========== 0032 卡片 ==========
c32 = get_card('0032')
assert c32, "0032 卡片未找到"
def c32_do(desc, old, new):
    global c32
    n = c32.count(old)
    if n != 1:
        CHANGES.append((f"0032 {desc}", f"FAIL count={n}"))
        return False
    c32 = c32.replace(old, new)
    CHANGES.append((f"0032 {desc}", "OK"))
    return True

c32_do('meta条数', '<span>10 条沟通</span>', '<span>19 条沟通</span>')
t32 = ''
t32 += '<div class="t-row"><div class="t-time">08-07 16:31</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">风渊-OP-XHWJ-KH</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">客服派单：51品茶 23584995（上海 iPhone16ProMax）无法显示图片一直转圈、视频也打不开，@yahu188 @lirui0930</div></div></div>'
t32 += '<div class="t-row"><div class="t-time">08-07 16:40</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">李瑞-BE-XHWJ-VN</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">@yahu188 @ding_2656 看一下 pwa 和安卓</div></div></div>'
t32 += '<div class="t-row"><div class="t-time">08-07 16:42</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">天辰-FE-XHWJ-CN</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">我试了可以，估计还是上海地区的 CDN 节点有问题了吧 @lirui0930</div></div></div>'
t32 += '<div class="t-row"><div class="t-time">08-07 16:44</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">飞策-QA-XHWJ-CN</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">我这边看了下俩端也是正常的</div></div></div>'
t32 += '<div class="t-row"><div class="t-time">08-07 16:48</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">李瑞-BE-XHWJ-VN</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">@blockingb935 现在更换域名是怎么操作的？域名现在是负责解析</div></div></div>'
t32 += '<div class="t-row"><div class="t-time">08-07 17:05</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">吴天北-OP-XHWJ-VN</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">上海地区好像确实有问题 我这也是有上海地区的反应 图片白屏</div></div></div>'
t32 += '<div class="t-row"><div class="t-time">08-07 17:43</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">文龙-TL-XHWJ-CN</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">@yahu188 看一下API接口是从哪里获取到的，我们换一下对应的API</div></div></div>'
t32 += '<div class="t-row"><div class="t-time">08-07 17:51</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">风渊-OP-XHWJ-KH</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">https://296.3zeja.cc 我联系人换了链接了</div></div></div>'
t32 += '<div class="t-row"><div class="t-time">08-07 18:01</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">李瑞-BE-XHWJ-VN</span><span class="t-channel">【DX-055】茶馆（APP）｜项目群</span></div><div class="t-text">这是一个新的域名吗? 是不是要用这个域名?</div></div></div>'
if c32.count(anchor32) != 1:
    CHANGES.append(("0032 时间线锚点", f"FAIL count={c32.count(anchor32)}"))
else:
    c32 = c32.replace(anchor32, t32 + anchor32)
    CHANGES.append(("0032 时间线追加x9", "OK"))
c32_do('0032 描述追加', '20:05 风渊转发客服派单：广东江门用户反馈无法联系茶女郎客服（14383577），20:06 李瑞受理排查',
 '20:05 风渊转发客服派单：广东江门用户反馈无法联系茶女郎客服（14383577），20:06 李瑞受理排查；08-07 16:31 风渊再收客服派单：51品茶 23584995（上海 iPhone16ProMax）无法显示图片一直转圈、视频也打不开（@李瑞 @天辰）；17:05 吴天北确认「上海地区好像确实有问题 图片白屏」；开发侧复测 pwa/安卓两端正常（天辰 16:42 试了可以、飞策 16:44 两端正常），疑上海地区 CDN 节点异常，正评估更换域名/API（home/config）方案')
c32_do('0032 处理方案追加', '20:05 再收客服派单（广东江门用户无法联系茶女郎客服），20:06 李瑞受理，需前端/运维检测加载链路（疑同时影响图片与客服入口）',
 '20:05 再收客服派单（广东江门用户无法联系茶女郎客服），20:06 李瑞受理，需前端/运维检测加载链路（疑同时影响图片与客服入口）；08-07 16:31 上海新用户派单（图片+视频均异常）→ 16:40-16:44 开发复测 pwa/安卓两端正常（飞策确认）→ 16:42 天辰判断疑上海地区 CDN 节点问题 → 16:48 李瑞评估更换域名（域名解析在武吉侧）→ 17:43 文龙指示更换 API（home/config）→ 17:51-18:01 风渊提供新链接、李瑞确认新域名方案')
c32_do('0032 根因更新', '待定位：疑地区性 CDN 节点/网络链路或图片存储服务异常（范围从上海扩大到广东，用户其他 app 网速正常，用户侧网络判断存疑），需开发检测图片加载链路（图片存储→CDN→客户端）',
 '待定位（收敛中）：08-07 16:42 天辰复测正常、判断疑上海地区 CDN 节点异常（pwa/安卓两端均正常排除客户端问题），正评估更换域名/API（home/config）切换方案；需确认新域名解析与 CDN 分发是否可绕开故障节点（域名解析在武吉侧）')
c32_do('0032 当前状态更新', '处理中：17:06-17:12 开发侧复测（未稳定复现），18:22 吴天北反馈广东地区同样有用户反映（范围扩大），18:25 秋野建议检测（联系不上的用户可能更多）；20:05 客服派单广东江门用户无法联系茶女郎客服（印证秋野判断），20:06 李瑞受理排查中',
 '处理中（08-07 18:01）：17:06-17:12 开发侧复测（未稳定复现），18:22 吴天北反馈广东地区同样有用户反映（范围扩大）；08-07 16:31 上海新用户派单（图片+视频打不开）→ 16:40-16:44 开发复测两端正常 → 16:42 天辰疑上海 CDN 节点 → 17:05 吴天北确认上海确实有问题 → 17:43 文龙指示换 API（home/config）→ 17:51-18:01 新域名方案确认中')
c32_do('0032 PMO 追加', '影响面进一步扩大</div></div>',
 '影响面进一步扩大；08-07 16:31 上海新用户派单（图片+视频均打不开）且 17:05 吴天北确认上海地区确实有问题，问题从「个别用户」升级为「地区性 CDN 节点」高度嫌疑；开发侧 pwa/安卓两端复测正常（16:40-16:44）指向地区网络/CDN 而非客户端；李瑞 16:48 发现域名解析在武吉侧，文龙 17:43 指示切换 API（home/config），跨部门（开发/运维/域名）协调中</div></div>')
c32_do('0032 建议追加', '并确认客服侧是否有备选上报路径（用户联系不上时如何反馈）</div></div>',
 '并确认客服侧是否有备选上报路径（用户联系不上时如何反馈）；6) 08-07 17:43 文龙已指示切换 API（home/config），请跟进新域名/API 切换执行与上线后上海地区复测；7) 已连续两天有上海/广东用户反馈（08-05 图片→08-07 图片+视频），建议运维核查上海/广东地区 CDN 节点健康状态，必要时做地域路由调整</div></div>')
put_card('0032', c32)

# ========== 0033 卡片 ==========
c33 = get_card('0033')
assert c33, "0033 卡片未找到"
def c33_do(desc, old, new):
    global c33
    n = c33.count(old)
    if n != 1:
        CHANGES.append((f"0033 {desc}", f"FAIL count={n}"))
        return False
    c33 = c33.replace(old, new)
    CHANGES.append((f"0033 {desc}", "OK"))
    return True

c33_do('meta条数', '<span>21 条沟通</span>', '<span>25 条沟通</span>')
t33 = ''
t33 += '<div class="t-row"><div class="t-time">08-07 17:24</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">周子然-OM-XHWJ-VN</span><span class="t-channel">【DX-119】抖阴（WEB）｜项目群</span></div><div class="t-text">小说 和 GA4流量来源异常问题及修复方案 这两个一起更新吧 @qingqing0001111</div></div></div>'
t33 += '<div class="t-row"><div class="t-time">08-07 17:37</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">朔月-BE-XHWJ-CN</span><span class="t-channel">【DX-119】抖阴（WEB）｜项目群</span></div><div class="t-text">代码已发布</div></div></div>'
t33 += '<div class="t-row"><div class="t-time">08-07 17:49</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">飞策-QA-XHWJ-CN</span><span class="t-channel">【DX-119】抖阴（WEB）｜项目群</span></div><div class="t-text">小说新内容还未更新</div></div></div>'
t33 += '<div class="t-row"><div class="t-time">08-07 17:49</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">朔月-BE-XHWJ-CN</span><span class="t-channel">【DX-119】抖阴（WEB）｜项目群</span></div><div class="t-text">需要手动执行以下定时任务，我提个工单</div></div></div>'
if c33.count(anchor32) != 1:
    CHANGES.append(("0033 时间线锚点", f"FAIL count={c33.count(anchor32)}"))
else:
    c33 = c33.replace(anchor32, t33 + anchor32)
    CHANGES.append(("0033 时间线追加x4", "OK"))
c33_do('0033 处理方案追加', '朔月 15:20 重新执行两遍仍无数据，正在查日志（验收后复发）',
 '朔月 15:20 重新执行两遍仍无数据，正在查日志（验收后复发）；08-07 17:24 周子然指示「小说 和 GA4流量来源异常问题及修复方案 这两个一起更新」→ 17:37 朔月「代码已发布」→ 17:49 飞策「小说新内容还未更新」→ 朔月「需要手动执行以下定时任务，我提个工单」，数据补录待定时任务执行')
c33_do('0033 根因追加', '朔月手动重跑仍无数据，定时任务持久化疑点增强',
 '朔月手动重跑仍无数据，定时任务持久化疑点增强；08-07 17:37 修复代码已发布生产、17:49 新内容仍未更新，朔月确认需手动执行定时任务（提工单），定时任务未持久化/未自动执行根因待修复后观察')
c33_do('0033 当前状态更新', '处理中（08-07 10:55 续报）：08-06 15:19 周子然再问采集 → 朔月 15:20 重跑两遍仍无数据查日志中；08-07 10:55 周子然「小说这里还是没有更新」→ 朔月 10:56 回应「今日开完晨会就提工单发代码」，采集恢复动作已明确，待工单发出验证',
 '处理中（08-07 17:49 续报）：08-06 15:19 周子然再问采集 → 朔月 15:20 重跑两遍仍无数据查日志中；08-07 10:55 周子然「小说这里还是没有更新」→ 朔月 10:56 回应开完晨会提工单发代码；17:24 周子然让小说与 GA4 一起更新 → 17:37 朔月代码已发布 → 17:49 飞策确认新内容仍未更新，朔月提工单手动执行定时任务，数据补录中')
c33_do('0033 PMO 追加', '⚠️ 建议将 0033 状态由已修复调整为处理中（复发）</div></div>',
 '⚠️ 建议将 0033 状态由已修复调整为处理中（复发）；08-07 17:24-17:37 修复代码已发布生产（周子然指示小说+GA4 一起更新），但 17:49 小说新内容仍未更新——采集根因（定时任务持久化）未随代码发布解决，需手动执行任务补数据，属修复不彻底，持续跟踪</div></div>')
c33_do('0033 建议追加', '需定位 syncNovelV2 定时任务配置</div></div>',
 '需定位 syncNovelV2 定时任务配置；6) 17:37 代码已发布后 17:49 数据仍未恢复，请朔月跟进手动执行定时任务进度并确认数据入库；7) 建议彻底修复定时任务持久化配置（当前每次需手动执行），避免第三次复发</div></div>')
put_card('0033', c33)

# ========== 0036 卡片 ==========
c36 = get_card('0036')
assert c36, "0036 卡片未找到"
def c36_do(desc, old, new):
    global c36
    n = c36.count(old)
    if n != 1:
        CHANGES.append((f"0036 {desc}", f"FAIL count={n}"))
        return False
    c36 = c36.replace(old, new)
    CHANGES.append((f"0036 {desc}", "OK"))
    return True

c36_do('状态→已修复', '<span class="tag status" style="background:#ef4444">处理中</span>',
       '<span class="tag status" style="background:#22c55e">已修复</span>')
c36_do('meta条数', '<span>18 条沟通</span>', '<span>21 条沟通</span>')
t36 = ''
t36 += '<div class="t-row"><div class="t-time">08-07 16:05</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">姜子牙-SEO-XHWJ-CN</span><span class="t-channel">【DX-119】抖阴（WEB）｜项目群</span></div><div class="t-text">验收没有问题 统计放好了 资源id是对的 可以更新</div></div></div>'
t36 += '<div class="t-row"><div class="t-time">08-07 17:24</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">周子然-OM-XHWJ-VN</span><span class="t-channel">【DX-119】抖阴（WEB）｜项目群</span></div><div class="t-text">小说 和 GA4流量来源异常问题及修复方案 这两个一起更新吧 @qingqing0001111</div></div></div>'
t36 += '<div class="t-row"><div class="t-time">08-07 17:37</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">朔月-BE-XHWJ-CN</span><span class="t-channel">【DX-119】抖阴（WEB）｜项目群</span></div><div class="t-text">代码已发布</div></div></div>'
if c36.count(anchor32) != 1:
    CHANGES.append(("0036 时间线锚点", f"FAIL count={c36.count(anchor32)}"))
else:
    c36 = c36.replace(anchor32, t36 + anchor32)
    CHANGES.append(("0036 时间线追加x3", "OK"))
c36_do('0036 处理方案追加', '16:55 高睿建议改按播放时长统计，16:59 约定次日验证',
 '16:55 高睿建议改按播放时长统计，16:59 约定次日验证；08-07 16:05 姜子牙(SEO) 测试服验收通过「统计放好了 资源id是对的 可以更新」→ 17:24 周子然指示与小说一起更新 → 17:37 朔月代码已发布生产')
c36_do('0036 根因更新', '与运营预期（按播放时长统计）不符；15:58 朔月已发测试环境修复版',
 '与运营预期（按播放时长统计）不符；15:58 朔月已发测试环境修复版；08-07 16:05 姜子牙测试服验收通过（资源 id 正确、统计正常），17:37 修复代码已发布生产')
c36_do('0036 当前状态更新', '处理中：08-06 14:47 高睿(OL) 上报统计异常 → 朔月 15:10 排查、15:58 修复代码发测试环境（16:40 解释统计口径）→ 16:54-16:55 高睿质疑统计无意义建议改播放时长 → 16:59 约定明日验证，统计口径对齐待产品/运营确认',
 '已修复（08-07 17:37）：08-06 14:47 高睿(OL) 上报统计异常 → 朔月 15:10 排查、15:58 修复发测试环境（16:40 解释口径）→ 08-07 16:05 姜子牙(SEO) 验收通过「统计放好了 资源id是对的」→ 17:24 周子然指示小说+GA4 一起更新 → 17:37 朔月代码已发布生产；统计口径（浏览/采样 vs 播放时长）与高睿的最终确认待生产数据验证')
c36_do('0036 PMO 追加', '需产品对齐指标定义（浏览/采样/播放时长三口径差异）</div></div>',
 '需产品对齐指标定义（浏览/采样/播放时长三口径差异）；08-07 16:05 姜子牙(SEO) 测试服验收通过（统计正常、资源 id 正确）→ 17:24 周子然指示更新 → 17:37 代码已发布生产，修复闭环（首报 08-06 14:47 至上线约 27h）；统计口径差异虽已修复数据准确性，但运营侧（高睿）期望按播放时长统计的口径问题仍待产品决策，建议跟进防止二次返工</div></div>')
c36_do('0036 建议追加', '避免同类偏差再次出现</div></div>',
 '避免同类偏差再次出现；6) 17:37 代码已发布，请高睿验证生产统计数据是否恢复正常；7) 统计口径（是否改按播放时长）待产品/运营拍板，避免同类口径争议再次出现</div></div>')
put_card('0036', c36)

# ========== 0037 卡片 ==========
c37 = get_card('0037')
assert c37, "0037 卡片未找到"
def c37_do(desc, old, new):
    global c37
    n = c37.count(old)
    if n != 1:
        CHANGES.append((f"0037 {desc}", f"FAIL count={n}"))
        return False
    c37 = c37.replace(old, new)
    CHANGES.append((f"0037 {desc}", "OK"))
    return True

c37_do('状态→已修复', '<span class="tag status" style="background:#ef4444">处理中</span>',
       '<span class="tag status" style="background:#22c55e">已修复</span>')
c37_do('meta条数', '<span>9 条沟通</span>', '<span>13 条沟通</span>')
t37 = ''
t37 += '<div class="t-row"><div class="t-time">08-07 17:01</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">厉飞雨-BE-XHWJ-VN</span><span class="t-channel">【DX-062】KISSAV（WEB）｜项目群</span></div><div class="t-text">远程发布后视频地址不正确，导致后台无法播放的bug要更新到生产，分支 feature/fix-m3u8-url-regex-delimiter</div></div></div>'
t37 += '<div class="t-row"><div class="t-time">08-07 17:03</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">李瑞-BE-XHWJ-VN</span><span class="t-channel">【DX-062】KISSAV（WEB）｜项目群</span></div><div class="t-text">好了（修复代码已合并更新生产）</div></div></div>'
t37 += '<div class="t-row"><div class="t-time">08-07 17:34</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">厉飞雨-BE-XHWJ-VN</span><span class="t-channel">【DX-062】KISSAV（WEB）｜项目群</span></div><div class="t-text">这个问题已经做了处理了，后面观察一下还会不会复现，再复现跟我说一下</div></div></div>'
t37 += '<div class="t-row"><div class="t-time">08-07 17:34</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">大胜-OP-XHWJ-CN</span><span class="t-channel">【DX-062】KISSAV（WEB）｜项目群</span></div><div class="t-text">好的，辛苦</div></div></div>'
if c37.count(anchor32) != 1:
    CHANGES.append(("0037 时间线锚点", f"FAIL count={c37.count(anchor32)}"))
else:
    c37 = c37.replace(anchor32, t37 + anchor32)
    CHANGES.append(("0037 时间线追加x4", "OK"))
c37_do('0037 处理方案更新', '协同定位视频 61551 后台播放失败原因',
 '协同定位视频 61551 后台播放失败原因；08-07 17:01 厉飞雨定位根因（远程发布后视频地址不正确，m3u8 url 正则分隔符问题）提交修复分支 feature/fix-m3u8-url-regex-delimiter → 17:03 李瑞合并代码更新生产 → 17:34 厉飞雨「已经做了处理了，后面观察一下还会不会复现」+ 大胜确认收到')
c37_do('0037 根因更新', '待定位：疑视频 61551 转码未完成/存储源异常或后台播放器兼容问题（上传侧可播、后台不可播，前台未确认）',
 '已定位（08-07 17:01）：远程发布后视频地址生成不正确（m3u8 url 正则分隔符问题，分支 feature/fix-m3u8-url-regex-delimiter），导致后台播放器拿不到正确地址无法播放；17:03 修复代码已合并更新生产')
c37_do('0037 当前状态更新', '处理中：08-06 15:06 大胜(OP) 上报后台无法播放 → 文龙转派厉飞雨 15:07 受理排查中',
 '已修复（08-07 17:34）：08-06 15:06 大胜(OP) 上报后台无法播放 → 文龙转派厉飞雨 15:07 受理（含 15:22 zoom 线上联调）→ 08-07 17:01 定位根因（远程发布视频地址 m3u8 正则分隔符问题）→ 17:03 修复代码合并更新生产 → 17:34 厉飞雨确认已处理、大胜确认收到，观察期（复现将再报）')
c37_do('0037 PMO 追加', '文龙转派厉飞雨已受理，处理时效关注</div></div>',
 '文龙转派厉飞雨已受理，处理时效关注；08-07 17:01 厉飞雨定位根因（远程发布后视频地址 m3u8 正则分隔符错误）→ 17:03 代码合并更新生产 → 17:34 确认处理完成+大胜确认收到，修复闭环（首报 08-06 15:06 至上线约 26h，含 zoom 联调与代码发布）；涉及远程发布链路（0031 发布端同域），建议纳入发布后冒烟验证，防止同类地址生成问题复发</div></div>')
c37_do('0037 建议追加', '评估是否需要批量排查存量视频</div></div>',
 '评估是否需要批量排查存量视频；5) 17:34 已修复并更新生产，请大胜在后台验证视频 61551 可正常播放；6) m3u8 地址生成属远程发布链路（0031 同域），建议增加发布后视频地址格式校验/冒烟测试</div></div>')
put_card('0037', c37)

# ========== 0041 卡片 ==========
c41 = get_card('0041')
assert c41, "0041 卡片未找到"
def c41_do(desc, old, new):
    global c41
    n = c41.count(old)
    if n != 1:
        CHANGES.append((f"0041 {desc}", f"FAIL count={n}"))
        return False
    c41 = c41.replace(old, new)
    CHANGES.append((f"0041 {desc}", "OK"))
    return True

c41_do('meta条数', '<span>2 条沟通</span>', '<span>4 条沟通</span>')
t41 = ''
t41 += '<div class="t-row"><div class="t-time">08-07 17:45</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">林笑尘-OL-XHWJ-VN</span><span class="t-channel">【JHG-056】91楼凤（APP）｜项目群</span></div><div class="t-text">老师 数据还是没更新呢</div></div></div>'
t41 += '<div class="t-row"><div class="t-time">08-07 17:49</div><div class="t-dot"></div><div class="t-body"><div class="t-meta"><span class="t-who">朔月-BE-XHWJ-CN</span><span class="t-channel">【JHG-056】91楼凤（APP）｜项目群</span></div><div class="t-text">定时任务关联的ip和服务器的不对称，在查原因</div></div></div>'
if c41.count(anchor32) != 1:
    CHANGES.append(("0041 时间线锚点", f"FAIL count={c41.count(anchor32)}"))
else:
    c41 = c41.replace(anchor32, t41 + anchor32)
    CHANGES.append(("0041 时间线追加x2", "OK"))
c41_do('0041 处理方案追加', '需排查后台数据统计任务执行状态与首页数据源（昨日数据未生成/未入库）',
 '需排查后台数据统计任务执行状态与首页数据源（昨日数据未生成/未入库）；08-07 17:49 朔月定位方向：定时任务关联的 IP 与服务器不对称，正在查原因')
c41_do('0041 根因追加', '与 0034（滴滴数据缺失）同类、与 0035（91后台登录不上）同属 lfadmin 后台链路',
 '与 0034（滴滴数据缺失）同类、与 0035（91后台登录不上）同属 lfadmin 后台链路；17:49 朔月已定位方向：定时任务关联的 IP 与服务器不对称（任务调度指向错误主机/IP 绑定错误）')
c41_do('0041 当前状态更新', '处理中（08-07 10:39 首报）：林笑尘反馈后台统计无昨日数据、首页无内容，朔月已受理排查',
 '处理中（08-07 17:49 进展）：10:39 林笑尘反馈后台统计无昨日数据、首页无内容 → 朔月受理 → 17:45 林笑尘催「数据还是没更新」→ 17:49 朔月定位「定时任务关联的 ip 和服务器的不对称，在查原因」')
c41_do('0041 PMO 追加', '建议排查统计任务执行状态与首页数据源，确认是否与 0035 后台登录问题存在共性根因</div></div>',
 '建议排查统计任务执行状态与首页数据源，确认是否与 0035 后台登录问题存在共性根因；08-07 17:45 林笑尘续报数据仍未更新 → 17:49 朔月定位定时任务关联 IP 与服务器不对称（调度指向错误主机），与 0034/0035 的 lfadmin 后台链路问题（0030/0035/0041）进一步印证后台服务配置管理薄弱，建议系统梳理</div></div>')
c41_do('0041 建议追加', '建议统一梳理后台服务健康检查与数据对账机制</div></div>',
 '建议统一梳理后台服务健康检查与数据对账机制；4) 朔月 17:49 已定位 IP/服务器不对称，请修正定时任务调度配置并验证昨日数据补生成；5) lfadmin 后台链路问题已多次出现（0030/0035/0041），建议建立后台服务配置基线审计</div></div>')
put_card('0041', c41)

# ========== 写出 ==========
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(c)

print("===== 变更结果 =====")
allok = True
for desc, status in CHANGES:
    print(f"  {'OK' if status.startswith('OK') else 'XX'} {desc}: {status}")
    if not status.startswith('OK'):
        allok = False
print("全部成功" if allok else "!!! 有失败项 !!!")
