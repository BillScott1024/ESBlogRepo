---
layout: post
title: 在GitHub仓库使用Git命令 遇到ssh_exchange_identification错误的解决办法
description: 记录一次遇到在GitHub上使用Git命令Pull仓库遇到的“疑难杂症”。
date: 2020-08-10
tags: Git
music-id: 829845
---

*  目录
{:toc}

-------
![GitHub](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/what-is-github-1-1.png)

# 前言

> 记录一次遇到在GitHub上使用Git命令Pull仓库遇到的“疑难杂症”。



# 起因

起因是我写了一个Cocos Creator的通用的组件代码，想在GitHub上的个人仓库中保存下来，方便分享给他人，也以便今后自己用到方便查看，于是在GitHub上新建了一个公开的仓库，地址是：[RichTextTypingDemo](https://github.com/BillScott1024/RichTextTypingDemo)， 然后在本地使用SourceTree去拉取Git仓库到本地，但是一直在加载，过一会儿就出现报错：
![img-01](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/QQ20200810-164246.png)
![img-02](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/20200810164404.png)
点开报错信息后显示：
![img-03](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/20200810164446.png)

```git

ssh_exchange_identification: read: Operation timed out
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
fatal: not a git repository (or any of the parent directories): .git
ssh_exchange_identification: read: Operation timed out
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
ssh_exchange_identification: read: Operation timed out
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

```
使用Git命令报错：
![img-04](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/20200810170612.png)

```git
git pull --rebase
ssh_exchange_identification: read: Operation timed out
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

# 解决过程

1. 我开始以为是我的GitHub的权限问题，或者是我的SSH 私钥Key过期了，因为我看到报错信息里有：`Please make sure you have the correct access rights`  于是删除了本地的SSH Key，并重新生成私钥，保存到GitHub的后台上，但重试后问题依旧。排除权限问题。

2. 然后我怀疑的原因是可能是我的梯子有问题，导致我的SourceTree无法链接GitHub的仓库，于是我打开Chrome进GitHub，连接正常，打开关闭ClashX Pro都可以正常进入GitHub主页，但是有可能是浏览器可以正常进去，但是命令行无法进入，我打开iTerm Ping了一下GitHub.com，果然无法Ping通,全都超时了：
![img-05](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/20200810165338.png)
    于是我把ClashX Pro提供的命令行翻♂墙命令`export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890`， 复制到iTerm中，依然无法Ping通，百度是可以正常Ping通的，排除WiFi网络问题:
![img-06](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/20200810165523.png)

3. 网上搜索了一番，没有找到解决问题的方法。但我突然想起来，我之前改过一次GitHub的Host，有可能是这个原因导致的于是找到Mac的Host文件，删除GitHub的Host：
    ![img-07](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/20200810165855.png)
    Binggo！解决问题,代码仓库可以正常Pull和Push了：
    ![img-08](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/20200810170048.png)

当初改这个Host的原因是我的GitHub和WIki上所有的用户头像和图标都无法加载，显示裂开，在网上找到的修改Host的方法解决的，现在删掉这条Host好像也没有问题了。



到此，问题解决完毕。



