---
layout: page
title: 收藏夹
top_meta: false
bottom_meta: [updated, share]
valine:
  placeholder: 有什么想对我说的呢？
sidebar: [blogger, tagcloud, webinfo]
---


{% p center logo large, 收藏夹 📘 %}
{% p center small,bookmarks %}

# 收藏夹

{% tabs tab-id %}

<!-- tab 常用网站 🌐 -->

# 常用网站

{% sitegroup %}
{% issues sites | api=https://gitee.com/api/v5/repos/exting/bookmark/issues?state=open&creator=exting&sort=created&direction=asc&page=1&per_page=100&labels=favorite %}
{% endsitegroup %}

<!-- endtab -->

<!-- tab 素材资源 🗂 -->

# 素材资源

{% sitegroup %}
{% issues sites | api=https://gitee.com/api/v5/repos/exting/bookmark/issues?state=open&creator=exting&sort=created&direction=asc&page=1&per_page=100&labels=asset %}
{% endsitegroup %}

<!-- endtab -->

<!-- tab 游戏相关 👾 -->

# 游戏相关

{% sitegroup %}
{% issues sites | api=https://gitee.com/api/v5/repos/exting/bookmark/issues?state=open&creator=exting&sort=created&direction=asc&page=1&per_page=100&labels=game %}
{% endsitegroup %}


<!-- endtab -->

<!-- tab 壁纸 🌄 -->

# 壁纸

{% gallery stretch, 2 %}

![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-10.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-11.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-12.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-13.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-14.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-15.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-16.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-17.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-18.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-19.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-20.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-21.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-22.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-24.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-23.webp?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-01.jpg?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-02.jpg?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-03.png?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-04.jpg?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-05.jpg?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-06.png?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-07.jpg?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-08.jpg?x-oss-process=style/WebSiteCover)
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/covers/cover-09.jpg?x-oss-process=style/WebSiteCover)

{% endgallery %}

<!-- endtab -->

{% endtabs %}
