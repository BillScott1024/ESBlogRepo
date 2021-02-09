layout: post
title: 处理 Android 打包环境配置不对，导致的打包报错问题
date: 2021-02-10
updated: 2021-02-10
robots: Android 打包 报错 AndroidStudio
keywords: Android 打包 报错 AndroidStudio
headimg: https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/post/20200904210131.jpg?x-oss-process=style/Post 
references:

 - title: 处理 Android 打包环境配置不对，导致的打包报错问题
   url: https://www.extingstudio.com/2021/02/10/2021-02-10-Package-Error-In-Android/
   categories:
 - [工作]
 - [疑难杂症]
 - [打包]
   tags:
 - [工作]
 - [疑难杂症]



# 处理 Android 打包环境配置不对，导致的打包报错问题



-  最近更新时间 2021-01-27 21:23:35

## 一. 前言



**打包安卓包 android.zip 流程:**



1. 在 `Constant.ts`脚本中,把 `buildEnv`改为 `platformTypeAndroid`:



```
export const buildEnv = platformTypeAndroid;
```



1. 在 Cocos 的构建发布面板, 发布平台选择 `Android`, 模板选择 `link`,API Level 选择 `android-22`, 秘钥库勾选`调试秘钥库`, 勾选`加密脚本`, `脚本加密秘钥`填写 `f4860e84-c60c-44`,勾选 `Zip 压缩`
   ![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751389695-3385da43-02b1-4a1c-a962-774388f6fdbc.png)
2. 先点击 `构建`,然后点击`编译`.或者不在 Cococs 发布面板点编译,使用 Android Studio 编译 APK 文件.



1. 没有报错的话会在 `./merge/build/jsb-link/publish/android/merge-release-signed.apk`生成 merge-release-signed.apk 文件,需要检查**文件路径**,**文件名**是否一致.



1. 在项目根目录下执行 `sh sh/packup_android.sh`, 执行完毕后,会在 `./merge/LittleGamePackage`路径下生成 android.zip 文件,在贪吃蛇大作战管理后台上传配置路径即可.



## 二. 环境配置



检查环境配置



> 示例是 MacOS,Widows 请自行对照系统修改路径
>
> 尽量使用相同的版本,这里选择的版本并不是最佳版本,只是可以正常打包的版本, 使用其他版本理论上应该也可以, 需要自行测试



1. CocosCreator 版本: **2.0.1**

下载地址： [Cocos Creator](https://www.cocos.com/creator)

1. Android Studio 国内镜像下载地址 [Android Studio](https://www.androiddevtools.cn/)
2. Java 版本:  **JDK 8**
   Java 下载地址: [JDK8](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)
   如果打包出现报错:
   ![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751831458-1ce24a1a-681b-4cb6-9bb5-d7de9a178298.png?x-oss-process=image%2Fresize%2Cw_2400)
   **请下载并安装相应的 JDK 版本**
   推荐使用命令 `brew cask install homebrew/cask-versions/adoptopenjdk8` 安装 JAVA 8
   如果提示没有 brew 命令,请自行 google 安装
3. NDK 版本: ndk16
   NDK下载地址: 

检查 NDK 文件完整性，检查是否有 platforms 文件夹，AndroidStudio 自动下载的 NDK 有时候会没有这个目录导致打包报错：

![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611752554279-cb87ade1-d1d5-42b1-a7a8-b8b87dd36902.png)
下载到系统中任意位置保存, 复制下目录路径,例如: `/Users/wangjun/Library/Android/sdk/ndk-bundle16`
NDK 需要配置路径的地方:

> 使用 Cocos 编译，配置路径 a,使用 Android Studio 编译，配置路径 b

1. 1. Cocos 配置路径:![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751424568-150f57e2-e039-4560-9aa4-c0d559ee0363.png?x-oss-process=image%2Fresize%2Cw_2400)
   2. Android Studio 配置路径:![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751446542-b73743d3-cfb9-418b-b6a4-bbb626f86857.png?x-oss-process=image%2Fresize%2Cw_2400)

![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751458053-e80f0bcd-30db-4ddf-a67d-4969f775d649.png?x-oss-process=image%2Fresize%2Cw_2400)

1. Gradle 版本: Gradle-5.4.1
   修改 `proj.android-studio/gradle/wrapper/gradle-wrapper.properties` 文件中的 `distributionUrl` 路径为 `https://services.gradle.org/distributions/gradle-5.4.1-all.zip`
2. `![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751496003-dbeba006-415e-439e-8665-c87aa7c50fe8.png?x-oss-process=image%2Fresize%2Cw_2400)`
3. build.grade
   修改 `proj.android-studio/build.gradle` 文件中的 `classpath`为 `com.android.tools.build:gradle:3.2.0`
4. `![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751507299-b48d6e46-093d-4f01-88b9-699c97facf75.png?x-oss-process=image%2Fresize%2Cw_2400)`
5. gradle.properties
   修改 `proj.android-studio/gradle.properties` 中的 `PROP_TARGET_SDK_VERSION=22` 和 `PROP_BUILD_TOOLS_VERSION=28.0.3`
6. ![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751527444-19401d0f-a91d-43b2-8cc7-4368a0b38df8.png?x-oss-process=image%2Fresize%2Cw_2400)
7. 项目路径
   如果在 Android Studio 中的 `./app` 路径后没有识别到 merge 项目, 则需要把 `settings.grade` 中的 `"app"`,改为 `".app"`, 点击 gradle sync,一次, 然后再改回来,就会同步到项目目录了,例如:



```
project(':merge').projectDir = new File(settingsDir, 'app')
=>
project(':merge').projectDir = new File(settingsDir, '.app')
```



![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751537709-ea67ab90-ea4b-49ed-bef6-b3be113c76bf.png?x-oss-process=image%2Fresize%2Cw_2400)



1. 修改 copy 项目资源的路径
   如果打包后,运行 `sh sh_android.sh`,出现报错,并且无法在`./LittleGamePackage/`下生成android.zip,或者 `android.zip` 包体很大(300MB+,正常大小是 7.2MB左右).
   首先检查打包 APK 成功后,在解压 APK 文件后的路径下没有 assets 文件夹,需要修改 `proj.android-studio/app/src/build.gradle` 中的 `android.applicationVariants.all`方法:
   原方法:



```
android.applicationVariants.all { variant ->
    // delete previous files first
    delete "${buildDir}/intermediates/merged_assets/${variant.dirName}"

    variant.mergeAssets.doLast {
        copy {
           from "${buildDir}/../../../../../res"
           into "${buildDir}/intermediates/merged_assets/${variant.dirName}/res"
        }

        copy {
            from "${buildDir}/../../../../../src"
            into "${buildDir}/intermediates/merged_assets/${variant.dirName}/src"
        }        

        copy {
            from "${buildDir}/../../../../../jsb-adapter"
            into "${buildDir}/intermediates/merged_assets/${variant.dirName}/jsb-adapter"
        }

        copy {
            from "${buildDir}/../../../../../main.js"
            from "${buildDir}/../../../../../project.json"
            into "${buildDir}/intermediates/merged_assets/${variant.dirName}"
        }
    }
}
```



改为



```
android.applicationVariants.all { variant ->
    // delete previous files first
    delete "${buildDir}/intermediates/merged_assets/${variant.dirName}"

    variant.mergeAssets.doLast {
        def sourceDir = "${buildDir}/../../../../.."
        copy {
            from "${sourceDir}/res"
            into "${outputDir}/res"
        }

        copy {
            from "${sourceDir}/src"
            into "${outputDir}/src"
        }

        copy {
            from "${sourceDir}/jsb-adapter"
            into "${outputDir}/jsb-adapter"
        }

        copy {
            from "${sourceDir}/main.js"
            from "${sourceDir}/project.json"
            into outputDir
        }
    }
}
```



如图示:

![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751551490-20ea10c1-72c8-458b-8dfe-967812cdacff.png?x-oss-process=image%2Fresize%2Cw_2400)



## 三. 正常的打包结果



打完包后正常的 APK 解包结构是:

![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751556341-e951c6c4-41c2-4780-bfad-7e0821d600fe.png)

执行完 sh 脚本后,正常的 zip 文件解压后的结构是:

![image.png](https://cdn.nlark.com/yuque/0/2021/png/169620/1611751561692-e4f3a5ff-1b6d-45fa-a6f1-216b4c1d1cdc.png)



**如果有文件缺失,或者打包失败,请自行检查以上配置环境**



## 四. 其他

1. 编译过程中需要下载一些依赖文件，最好打开全局代理
2. 配置路径中的用户名需要相应的改为自己的电脑的用户名
3. 配置完毕,打包APK,并执行 `sh sh_android.sh` 后,控制台仍然有可能会有红字报错,但是解包 `android.zip` 后子目录文件是正常,并且上传后能正常游戏,就不影响.
4. 待补充...