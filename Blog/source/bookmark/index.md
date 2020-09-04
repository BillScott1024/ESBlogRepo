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
{% site Volantis, url=https://xaoxuu.com/wiki/volantis/v4/tag-plugins/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/volantis.webp, description=Volantis 官方文档 %}
{% site Emoji Homepage, url=http://emojihomepage.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/emojihomepage.webp, description=一个可以在Markdown直接使用Emoji的网站 %}
{% site FontAwesome, url=https://fontawesome.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/fontawesome.webp, description=一个 Icon 网站 %}
{% site BNXB综合管理平台, url=http://cdn.bnxb.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/bnxb.webp, description=智能域名解析网站 %}
{% site CloudFlare, url=https://dash.cloudflare.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/CloudFlare.webp, description=CloudFlare 域名解析网站 %}
{% site Vercel, url=https://vercel.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/Vercel.webp, description=Vercel 域名解析网站 %}
{% site U-Meng, url=https://web.umeng.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/UMeng.webp, description=友盟-数据分析平台/CNZZ %}
{% site 百度统计, url=https://tongji.baidu.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/baidu-tongji.webp, description=百度统计 %}
{% site LeanCloud, url=https://console.leancloud.app/applist.html#/apps, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/LeanCloud.webp, description=LeanCloud %}
{% site WebPushr, url=https://app.webpushr.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/webpushr.webp, description=浏览器通知 %}
{% site Google Adsense, url=https://www.google.com/adsense/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/google-ad.webp, description=Google Adsense %}
{% site ImageOptim, url=https://imageoptim.com/, screenshot=https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/websites/ImageOptim.png?x-oss-process=style/WebSiteCover, description=非常好用的免费图片压缩工具 ImageOptim %}
{% endsitegroup %}

<!-- endtab -->

<!-- tab 素材 🌐 -->

# 素材

<!-- endtab -->

<!-- tab 其他 🌐 -->

# 其他

<!-- endtab -->

{% endtabs %}



<!-- 
<script type="text/javascript">

function urlToImage(url,callback){

    var xmlhttp = new XMLHttpRequest();
    // xmlhttp.addEventListener("load" , transferComplete);
    xmlhttp.open("POST", "https://v2.convertapi.com/convert/web/to/jpg?Secret=tgLIc81YVOMJLxca");
    xmlhttp.setRequestHeader("Content-type","application/json");
    const param = {
        "Parameters": [
            {
                "Name": "Url",
                "Value": url
            },
            {
                "Name": "StoreFile",
                "Value": true
            },
            {
                "Name": "ImageWidth",
                "Value": "1280"
            },
            {
                "Name": "ImageHeight",
                "Value": "750"
            },
            {
                "Name": "ImageQuality",
                "Value": "30"
            }
        ]
    }
    console.log("====JSON.stringify(param):", JSON.stringify(param));
    xmlhttp.send(JSON.stringify(param));

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            callback(JSON.parse(xmlhttp.response));
        } else if(xmlhttp.readyState == 4){
            console.error(JSON.parse(xmlhttp.response));
        }
    }
}


urlToImage("https://baidu.com", (res) =>{
    console.log("===urlToImage res", res);
    console.log("===urlToImage imageUrl", res.Files[0].Url);

    console.log("====page.screenshot", document.getElementById('page.screenshot'));
}); -->


<!-- </script> -->