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


<div class="poem-wrap">
  <div class="poem-border poem-left"></div>
  <div class="poem-border poem-right"></div>
    <h1>一言</h1>
    <p id="poem">挑选中...</p>
    <p id="info"></p>
    <p style="text-align:right" color="#696969" id="creator">- by</p>
</div>

***

![](https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/wallhaven-42kgzg%20%281%29.png)

***

<!-- 老式写法，兼容性最好; 支持 IE -->
<script>
  var xhr = new XMLHttpRequest();
  xhr.open('get', 'https://v1.hitokoto.cn');
  var hitokotoText = document.getElementById("poem");
  var hitokotoFrom = document.getElementById('info');
  var hitokotoCreator = document.getElementById('creator');
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      var data = JSON.parse(xhr.responseText);
      console.log("==data", data)
      hitokotoText.innerText = data.hitokoto
      if (data.from_who != null) {
        hitokotoFrom.innerText = (data.from_who + " · " + "《 " + data.from + " 》")
      } else {
        hitokotoFrom.innerText = data.from
      }
      if (data.creator != null) {
        hitokotoCreator.innerText = ("- by " + data.creator)
      } else {
        hitokotoCreator.innerText = ""
      }
    } else {
        hitokotoText.innerText = "获取出错啦"
    }
  }
  xhr.send();
</script>
