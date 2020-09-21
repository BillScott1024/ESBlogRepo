---
layout: friends     # 必须
# title: 友链   # 可选，这是友链页的标题
top_meta: false
bottom_meta: false
sidebar: false

---

{% p center logo large, 友链 👨‍💻 %}
{% p center small,friends & dalao %}


## 来自 GitHub 的朋友  <i class="fab fa-github"></i> 

{% issues sites | api=https://api.github.com/repos/BillScott1024/blog-friends/issues?sort=updated&state=open&page=1&per_page=100 %}


## 来自 Gitee 的朋友  <i class="fab fa-gitter"></i> 

{% issues sites | api=https://gitee.com/api/v5/repos/exting/friends-links/issues?sort=updated&state=open&page=1&per_page=100 %}



# 我可以交换友链吗？

当然可以，必须同时满足以下要求：

{% checkbox green checked, 合法的、非营利性、无商业广告站点 %}
{% checkbox green checked, 有实质性原创内容的个人博客或组织。 %}
{% checkbox green checked, 必须是 HTTPS 独立域名。 %}


{% timeline 如何添加自己的博客链接 %}


{% timenode 第一步：选择任意一个自助提交入口 %}

{% link GitHub Issues 友链自助提交入口 🔗, https://github.com/BillScott1024/blog-friends/issues/new/choose %}

{% link Gitee Issues 友链自助提交入口 🔗, https://gitee.com/exting/friends-links/issues %}


{% endtimenode %}

{% timenode 第二步：新建 Issue 按照**模板**格式填写并提交 %}

```JSON
{
    "title": "网站标题",
    "description": "个性签名/描述",
    "screenshot": "主页截图/封面",
    "url": "主页链接",
    "avatar": "头像/Logo"
}
```

为了提高图片加载速度，建议压缩优化图片尺寸：

打开图片压缩网站 [免费在线压缩图](https://www.yasuotu.com/) / [TinyPng](https://tinypng.com/) 上传自己的截图，将图片的高度调整到 360px , 将图片大小压缩到 200KB以下 下载。
将压缩后的图片上传到图床: [sm.ms](https://sm.ms/) / [去不图床](https://7bu.top/) (或自己的图床,**注意不要打开防盗链**,或者将本域名: {% u *.extingstudio.com %} 加入防盗链白名单)并使用此图片链接作为截图链接。
> 建议使用 [JsDelivr](https://www.jsdelivr.com/) 的方式使用头像图床, 安全, 快速, 稳定
{% endtimenode %}

{% timenode 第三步：刷新 %}

回来 {% kbd F5 %} 刷新本页面即可生效。

{% endtimenode %}

{% endtimeline %}

## 如何更新自己的博客链接

如果是自己创建的 issue ，可以自己修改。
如果是管理员创建的，请自己重新创建一份，然后让管理员删掉旧的。



# 请先添加本站友链, 再申请提交友链信息

JSON 格式:
```JSON
{
    "title": "忆星辰",
    "description": "游戏开发者, 业余摄影师",
    "screenshot": "https://cdn.jsdelivr.net/gh/BillScott1024/cdn-blog/images/homepage.webp",
    "url": "https://extingstudio.com",
    "avatar": "https://cdn.jsdelivr.net/gh/BillScott1024/cdn-blog/images/avatar.webp"
}

```

YAML 格式:
```YAML
  title: 忆星辰
  url: https://extingstudio.com
  avatar: https://cdn.jsdelivr.net/gh/BillScott1024/cdn-blog/images/avatar.webp
  description: 游戏开发者, 业余摄影师
  screenshot: https://cdn.jsdelivr.net/gh/BillScott1024/cdn-blog/images/homepage.webp
```
说明

|  选项   | 内容  |
|  ----  | ----  |
| 主页标题  | 忆星辰 |
| 链接  | https://extingstudio.com |
| 头像  | https://cdn.jsdelivr.net/gh/BillScott1024/cdn-blog/images/avatar.webp |
| 标签  | 游戏开发者, 业余摄影师 |
| 主页截图  | https://cdn.jsdelivr.net/gh/BillScott1024/cdn-blog/images/homepage.webp |
| 联系方式 | 邮箱：{% psw jaxsonwang@foxmail.com %} |


