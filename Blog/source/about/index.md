---
layout: page
title: About Me
meta:
  header: []
  body: [article, comments]
  footer: []
valine:
  placeholder: 有什么想对我说的呢？
sidebar: []

---

{% p center logo large, About Me %}
{% p center small,关于我 & 我的博客 %}

# 简介 📃


{% radio green checked,  游戏开发者 %}
{% radio yellow checked, 业余摄影师 %}
{% radio cyan checked, 喜欢旅行 %}
{% radio blue checked, 会弹吉他 %}
{% radio checked, 沉迷代码 %}

<br>
<br>

喜欢我的博客可以给我 点赞/Star/{% psw 打赏 %}哦 🐈

也可以按快捷键  {% kbd command %} + {% kbd D %} 或者 键盘样式的文本 {% kbd ctrl %} + {% kbd D %} 添加网站到浏览器书签 📖

<br>
<br>

# 我的GitHub 👨‍💻 

{% ghcard BillScott1024, theme=algolia %}

<br>
<br>
<br>

# 技术栈 💻

{% noteblock quote %}

{% checkbox blue checked, 游戏引擎: Cocos Creator / Laya Box / Unity %}
{% checkbox green checked, 编程语言: JavaScript ( TypeScript ) / C# %}

{% endnoteblock %}

<br>
<br>
<br>

# 本站 TODO List 📜

{% checkbox blue checked, 博客速度优化 CDN/JsDelivr %}
{% checkbox blue checked, GitHubPages / Coding双线部署 %}
{% checkbox blue checked, WebPush 通知 %}
{% checkbox blue checked, 文章字数统计和阅读时长 %}
{% checkbox blue checked, live2d动画人物 %}
{% checkbox blue checked, 工具箱页面 %}
{% checkbox blue checked, 配置Artitalk %}

{% checkbox blue checked, 阅读量和访问数优化 %}
{% checkbox blue checked, 网站域名备案 %}
{% checkbox blue checked, leancloud的定时任务 %}
{% checkbox blue checked, 51统计页面 [51统计](https://web.51.la/) %}

{% checkbox blue, 点击烟花效果 %}
{% checkbox blue, 动态线条背景 %}

<br>
<br>

# 站点历程 📅

{% timeline  %}
{% timenode 2020-08-25 转移域名 %}

{% radio yellow checked, 转移域名注册商到 [阿里云](https://www.aliyun.com/) %}

{% endtimenode %}



{% timenode 2020-08-21 优化博客访问速度 %}

{% radio cyan checked, **双线部署博客**到 GitHub Pages 和 Coding， 并分别解析域名国内/境外IP %}
{% radio red checked, 使用**GitHub + [JsDelivr](https://www.jsdelivr.com/)** 优化博客静态资源访问速度 %}

{% endtimenode %}



{% timenode 2020-08-21 迁移域名 %}

{% radio cyan checked, 域名到期，不再续费，并换域名为 **www.extingstudio.com** %}

{% endtimenode %}


{% timenode 2020-07-15 转移到Hexo %}

{% radio yellow checked, 将博客从 ~~Jekyll~~ 转移 到 [Hexo](https://hexo.io/zh-cn/) %}

{% endtimenode %}


{% timenode 2018-06-18 优化博客 %}

{% radio cyan checked, 优化博客内容和样式 %}
{% radio blue checked, 接入 [Google Adsence](https://www.google.com/adsense) 广告 %}

{% endtimenode %}



{% timenode 2017-07-18 购买域名 %}

{% radio green checked, 在 [百度智能云](https://cloud.baidu.com/) 购买域名 ~~extingstudio.top~~，并解析GitHub Pages到自定义域名 %}

{% endtimenode %}


{% timenode 2017-06-18 **开始建站** %}

{% radio cyan checked, 在GitHub Pages上建站，使用 [jekyll](https://jekyllcn.com/) 静态博客引擎 %}

{% endtimenode %}



{% endtimeline %}


