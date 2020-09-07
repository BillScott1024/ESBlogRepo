----
layout: post
title: 使用Git Submodule 对Hexo 博客主题进行管理与更新
date: 2020-09-03
updated: 2020-09-03
robots: Git fork 更新 Submodule Hexo 主题 静态博客
keywords: Git fork 更新 Submodule Hexo 主题 静态博客
headimg: https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904210131.jpg?x-oss-process=style/Post 
references:
 - title: 工作中最常用的Git命令及常见错误解决方案
   url: https://www.extingstudio.com/2019/09/10/2019-09-10-The_Most%20Commonly_Used_Git_Command_At_Work/
categories:
 - [Git]
 - [Hexo]
 - [博客]
tags:
 - [Git]
 - [Hexo]

----



> 在使用Hexo搭建静态博客的时候，通常都会使用一个他人(自己)开发的主题，而这个主题往往是一个独立的Git仓库，自己的Hexo静态博客一般也是一个Git仓库，他们之间的关系是 博客仓库 **包含** 主题仓库： .../BlogRepo/themes/volantis/...  ，主仓库由使用者自己维护，主题仓库由主题作者进行维护与更新，无论是自己开发主题，还是是用别人开发的主题，都需要在主题更新或者修复BUG的时候对自己正在使用的主题代码进行更新，如果自己想要对主题进行修改也需要对这个仓库进行维护, 这时候就需要使用 Git Submodule 来对这个在主仓库中的子仓库进行 Git 管理
> 

<!-- more -->

{% noteblock 准备环境 %}
Node.js (Node.js 版本需不低于 10.13，建议使用 Node.js 12.0 及以上版本)
Git
注：
Hexo版本：5.0+	最低兼容版本：10.13.0
{% endnoteblock %}


# Git 介绍
[Git](https://git-scm.com/)是一个免费的开源 分布式版本控制系统，旨在快速高效地处理从小型到大型项目的所有内容。Git下载地址：[Git](https://git-scm.com/)
Git 常用命令可见这片文章：[工作中最常用的Git命令及常见错误解决方案](https://www.extingstudio.com/2019/09/10/2019-09-10-The_Most%20Commonly_Used_Git_Command_At_Work/)

# Git 子模块 Submodule介绍

# 使用Git Submodule子模块对主题进行管理与更新
> 已有Hexo仓库和主题仓库的，可以直接跳到步骤8。




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

5. 在GitHub上，点击 fork 将主题仓库fork到自己的账号下：
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904200830.png?x-oss-process=style/Post)

6. 与步骤1，2一样，cd 到themes目录下，使用命令： `git clone https://github.com/volantis-x/hexo-theme-volantis volantis`，将fork的仓库 clone 到本地：
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904200935.png?x-oss-process=style/Post)

![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904195752.png?x-oss-process=style/Post)

7. 返回到Blog目录， 使用 `npm hexo-generator-search hexo-generator-json-content` 安装相关 node 依赖，使用 `npm hexo-renderer-stylus` 安装渲染器：
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904200224.png?x-oss-process=style/Post)

8. 返回到主目录BlogMainTest下，添加 主题仓库volantis为主仓库的子模块，使用命令 `$ git submodule add fork的主题仓库地址 主题目录路径` ：
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904202228.png?x-oss-process=style/Post)

9. 输入 `git status`，看是否多了一个 .gitmodules:
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904202444.png?x-oss-process=style/Post)
 
10. 输入 `git submodule` 查看子模块信息：
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904202604.png?x-oss-process=style/Post)

11. 此时，子模块已经添加成功，当主题作者更新了主题仓库时，由于我们自己的子模块主题仓库是fork原作者的仓库，我们想要更新时，需要先从源仓库更新我们本地的子模块，再推送到我们自己的主题仓库。输入： `cd Blog/themes/volantis`,到主题子模块下，并输入 `git remote -v`,查看远程源仓库状态：
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904203734.png?x-oss-process=style/Post)
可以看到当前的远程仓库是我们fork的自己的主题仓库，使用命令 `git remote add upstream git@github.com:xxx/xxx.git`，将源作者仓库设为上游仓库，并拉取更新，命令步骤为：


```
git remote add upstream git@github.com:xxx/xxx.git
git fetch upstream
git merge upstream/master
```
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904204121.png?x-oss-process=style/Post)
在本地合并完冲突后，add,并commit提交，最后使用 ` git push origin master` ，推送到远端。

1. 以上就是整个管理博客仓库，并通过fork来及时更新主题仓库代码的整个流程了，有任何问题，可以再下方评论区留言告知，我会尽力解答。

# Git Submodule的常用命令及使用

子模块的添加
`git submodule add <url> <path>`
查看子模块

```
git submodule
e33f854d3f51f5ebd771a68da05ad0371a3c0570 assets (heads/master)
```
更新子模块
更新项目内子模块到最新版本
```
git submodule update
```
更新子模块为远程项目的最新版本
```
$ git submodule update --remote
```
删除子模块
`rm -rf` 子模块目录 删除子模块目录及源码
`vi .gitmodules` 删除项目目录下.gitmodules文件中子模块相关条目
`vi .git/config` 删除配置项中子模块相关条目
`rm .git/module/*` 删除模块下的子模块目录，每个子模块对应一个目录，注意只删除对应的子模块目录即可
执行完成后，再执行添加子模块命令即可，如果仍然报错，执行如下：
`git rm --cached` 子模块名称
完成删除后，提交到仓库即可。

# 常见问题

1. 当主仓库中包含子仓库时，直接在主仓库提交代码会报错，无法提交，使用子模块的方式，才能正常提交代码。
2. 如果你已经删除了主题仓库的.git相关文件夹，那么就无法成功添加子模块，这个时候需要从 步骤6 开始重新clone代码，重新添加 子模块，并设置上游仓库。

# 参考资料

[Git-工具-子模块](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97)

[Git 子模块：git submodule](https://juejin.im/post/6844903572950401038)

[git中submodule子模块的添加、使用和删除](https://blog.csdn.net/guotianqing/article/details/82391665)

[github上fork了别人的项目后，再同步更新别人的提交](https://blog.csdn.net/qq1332479771/article/details/56087333)