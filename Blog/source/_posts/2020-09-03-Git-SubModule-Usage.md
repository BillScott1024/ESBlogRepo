----
layout: post
title: 使用Git Submodule 对Hexo 博客主题进行管理与更新
date: 2020-09-03
updated: 2020-09-03
robots: Git Submodule Hexo
keywords: Git Submodule Hexo
cover: true
categories:
tags:
 - [Git]
 - [Hexo]
----

在使用Hexo搭建静态博客的时候，通常都会使用一个他人(自己)开发的主题，而这个主题往往是一个独立的Git仓库，自己的Hexo静态博客一般也是一个Git仓库，他们之间的关系是 博客仓库 **包含** 主题仓库： .../BlogRepo/themes/volantis/...  ，主仓库由使用者自己维护，主题仓库由主题作者进行维护与更新，无论是自己开发主题，还是是用别人开发的主题，都需要在主题更新或者修复BUG的时候对自己正在使用的主题代码进行更新，如果自己想要对主题进行修改也需要对这个仓库进行维护...


<!-- more -->

> 在使用Hexo搭建静态博客的时候，通常都会使用一个他人(自己)开发的主题，而这个主题往往是一个独立的Git仓库，自己的Hexo静态博客一般也是一个Git仓库，他们之间的关系是 博客仓库 **包含** 主题仓库： .../BlogRepo/themes/volantis/...  ，主仓库由使用者自己维护，主题仓库由主题作者进行维护与更新，无论是自己开发主题，还是是用别人开发的主题，都需要在主题更新或者修复BUG的时候对自己正在使用的主题代码进行更新，如果自己想要对主题进行修改也需要对这个仓库进行维护, 这时候就需要使用 Git Submodule 来对这个在主仓库中的子仓库进行 Git 管理
> 

准备环境：
Node.js (Node.js 版本需不低于 10.13，建议使用 Node.js 12.0 及以上版本)
Git
注：
Hexo版本：5.0+	最低兼容版本：10.13.0

# Git 介绍
[Git](https://git-scm.com/)是一个免费的开源 分布式版本控制系统，旨在快速高效地处理从小型到大型项目的所有内容。Git下载地址：[Git](https://git-scm.com/)
Git 常用命令可见这片文章：[工作中最常用的Git命令及常见错误解决方案](https://www.extingstudio.com/2019/09/10/2019-09-10-The_Most%20Commonly_Used_Git_Command_At_Work/)

# Git 子模块 Submodule介绍

# 使用Git Submodule子模块对主题进行管理与更新
1. 在自己的 GitHub 上新建一个仓库，用于存放自己博客的源码，注意：这个仓库不是 GitHub Pages 所在的仓库，并不用于发布博客，并且里面的配置文件可能会存放自己的一些用户名、秘钥、Token等信息，因此可以将此仓库权限设为 Private :


![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200903202924.png?x-oss-process=style/Post)

2. 点击Code，然后点击Use SSH， 复制下仓库地址：


![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200903204116.png?x-oss-process=style/Post)

3. 使用 `git clone`命令将主仓库clone到本地：

![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200903204749.png?x-oss-process=style/Post)

4. cd 到仓库根目录下，使用 `hexo init folder/` 初始化一个hexo目录

![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200903205318.png?x-oss-process=style/Post)

目录结构如下：
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200903205627.png?x-oss-process=style/Post)

# Git Submodule的常用命令及使用


# 常见问题

# 参考资料