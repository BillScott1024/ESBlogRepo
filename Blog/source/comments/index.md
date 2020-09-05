---
meta:
 header: [centertitle]
 body: [article, comments]
 footer: [updated]
sidebar: [blogger, tagcloud, webinfo] # 放置任何你想要显示的侧边栏部件
music:
 server: netease   # netease, tencent, kugou, xiami, baidu
 type: song        # song, playlist, album, search, artist
 id: 16846091      # song id / playlist id / album id / search keyword
---

{% p center logo large, 留言板 📘 %}
{% p center small,Comments %}


# 欢迎留言 <i class="fas fa-signature"></i><i class="fas fa-pen-nib"></i>
![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/wallhaven-42kgzg%20%281%29.png)


<div class="poem-wrap">
  <div class="poem-border poem-left"></div>
  <div class="poem-border poem-right"></div>
    <h1>一言</h1>
    <p id="poem">挑选中...</p>
    <p id="info">
</div>


<script>
    $.get("https://v1.hitokoto.cn?c=i&c=j", function (data, status) {
        if (status == 'success') {
            $('#poem').html(data.hitokoto);
            if (data.from_who != null) {
                $('#info').html(data.from_who + " · " + "《 " + data.from + " 》");
            } else {
                $('#info').html(data.from);
            }
        } else {
            $('#poem').html("获取出错啦");
        }
    });
</script>

<style>
.poem-wrap {
    position: relative;
    width: 730px;
    max-width: 80%;
    border: 2px solid #797979;
    border-top: 0;
    text-align: center;
    margin: 80px auto;
}

.poem-wrap h1 {
    position: relative;
    margin-top: -20px;
    display: inline-block;
    letter-spacing: 4px;
    color: #797979;
    border-bottom: none;
}

.poem-wrap p {
    width: 70%;
    margin: auto;
    line-height: 30px;
    color: #797979;
}

.poem-wrap p#poem {
    text-align: center;
    font-size: 25px;
}

.poem-wrap p#info {
    text-align: center;
    font-size: 15px;
    margin: 15px auto;
}

.poem-border {
    position: absolute;
    height: 2px;
    width: 27%;
    background-color: #797979;
}

.poem-right {
    right: 0;
}

.poem-left {
    left: 0;
}

@media (max-width: 685px) {
    .poem-border {
        width: 18%;
    }
}

@media (max-width: 500px) {
    .poem-wrap {
        margin-top: 60px;
        margin-bottom: 20px;
        border-top: 2px solid #797979;
    }

    .poem-wrap h1 {
        margin: 20px 6px;
    }

    .poem-border {
        display: none;
    }
}
</style>