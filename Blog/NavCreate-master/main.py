
f_output = open("fold/out.txt", 'w',encoding='UTF-8')  # 输出文件夹
f_text = open("fold/text.txt","r",encoding='UTF-8')  # 输入文件夹
title = "忆星辰 | 工具箱"  # 网页title
long_logo = "https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/images/white_left_icon.png"  # 长条 logo
logo = "https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/images/icon.png"  # logo
favicon = "https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/images/fa.ico"  # favicon
"""网站, 图标, 名字, 描述"""



head = """<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="author" content="JingFengJi">
    <title>工具箱丨忆星辰</title>
    <meta name="keywords" content="http://extingstudio.com,忆星辰,星辰,百宝箱,在线工具箱,素材资源网站,网站导航">
    <meta name="description" content="WebStack - 收集国内外优秀资源网站，https://www.extingstudio.com/">
    <link rel="icon" type="image/png" href="https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/avatar/favicon-cicle.png">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Arimo:400,700,400italic">
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/css/fonts/linecons/css/linecons.css">
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/css/fonts/fontsawesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/css/bootstrap.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/css/xenon-core.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/css/xenon-components.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/css/xenon-skins.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/css/nav.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/css/search.css">
    <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/jquery-1.11.1.min.js"></script>
    <!--[if lt IE 9]><script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script><script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script><![endif]-->
    <style>
        footer.main-footer .go-up {
            width: 45px;
            float: right;
            position: fixed;
            right: -10px;
            bottom: 30px;
            z-index: 10;
            margin: 0;
            padding: 0;
            list-style: none
        }

        footer.main-footer .go-up a {
            display: inline-block;
            width: 35px;
            height: 35px;
            text-align: center;
            border-radius: 50%;
            background: rgba(123, 123, 123, .5);
            color: #fff;
            font-size: 20px;
            line-height: 35px;
            padding: 0
        }
    </style>
<meta name="generator" content="Hexo 4.2.0"><link rel="alternate" href="/atom.xml" title="luckyzmj" type="application/atom+xml">
</head>
<body class="page-body">
    <div class="page-container">
        <div class="sidebar-menu toggle-others fixed">
            <div class="sidebar-menu-inner">
                <header class="logo-env">
                    <div class="logo" style="width:39px;height: 45px;text-align: center;"><a href="/tools/" class="logo-expanded"><img
                                src="https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/avatar/favicon-cicle.png"
                                width="100%" alt=""></a><a href="/tools/" class="logo-collapsed"><img
                                src="https://es-blogimg.oss-cn-hangzhou.aliyuncs.com/img/avatar/favicon-cicle.png"
                                width="80%" alt=""></a></div>
                    <div class="mobile-menu-toggle visible-xs"><a href="#" data-toggle="user-info-menu"><i
                                class="linecons-cog"></i></a><a href="#" data-toggle="mobile-menu"><i
                                class="fa-bars"></i></a></div>
                </header>
                <ul id="main-menu" class="main-menu">
"""

middle = """

                   
                </ul>
            </div>
        </div>
        <div class="main-content">
            <nav class="navbar user-info-navbar" role="navigation">
                <ul class="user-info-menu left-links list-inline list-unstyled">
                    <!-- <li class="hidden-sm hidden-xs"><a href="#" data-toggle="sidebar"><i class="fa-bars"></i>
                             隐藏/显示侧边栏</a></li> -->
                    <li><a href="/" target="_blank" style="padding:30px 20px"><i class="fa fa-home"></i> 博客首页</a></li>
                    <li><a href="/friends/" target="_blank" style="padding:30px 20px"><i class="fa fa-link"></i>
                            友情链接</a></li>
                 <!--    <li><a href="/contact/" target="_blank" style="padding:30px 20px"><i class="fa fa-comments"></i>
                            评论留言</a></li> -->
                    <li><a href="/about/" target="_blank" style="padding:30px 20px"><i class="fa fa-info-circle"></i>
                            关于博主</a></li>
                    <li><a id="tp-weather-widget" style="padding:28px 20px"></a>
                        <script>
                            ! function (e, t, n, a, o, i, c, r) {
                                r = function () {
                                        i = t.createElement(n), c = t.getElementsByTagName(n)[0], i.src = o, i.charset =
                                            "utf-8", i.async = 1, c.parentNode.insertBefore(i, c)
                                    }, e.SeniverseWeatherWidgetObject = a, e[a] || (e[a] = function () {
                                        (e[a].q = e[a].q || []).push(arguments)
                                    }), e[a].l = +new Date, e.attachEvent ? e.attachEvent("onload", r) : e
                                    .addEventListener("load", r, !1)
                            }(window, document, "script", "SeniverseWeatherWidget",
                                "//cdn.sencdn.com/widget2/static/js/bundle.js?t=" + parseInt(((new Date).getTime() /
                                    1e8).toString(), 10)), window.SeniverseWeatherWidget("show", {
                                flavor: "slim",
                                location: "WX4FBXXFKE4F",
                                geolocation: !0,
                                language: "auto",
                                unit: "c",
                                theme: "auto",
                                token: "a39cd5a0-4024-4cb2-85c6-0250317058db",
                                hover: "enabled",
                                container: "tp-weather-widget"
                            })
                        </script>
                    </li>
                </ul>
            </nav>
            <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/search.js"></script>
            <h2>
                <marquee behavior="alternate" scrollamount="6">导航内容不定期更新...</marquee>
            </h2>

            
            """
tail = """
         </div>
            <br />
        </div>
    </div>
    <footer class="main-footer sticky footer-type-1">
                <div class="footer-inner">
                    <div class="footer-text">COPYRIGHT<i class="far fa-copyright"></i> 2019 - 2020 <a
                            href="https://github.com/WebStackPage/WebStackPage.github.io"
                            target="_blank"><strong>WEBSTACK</strong></a> 丨 DESIGNED BY <a href="http://viggoz.com"
                            target="_blank"><strong>VIGGO</strong></a> 丨 CHANGED BY <a href="https://extingstudio.com"
                            target="_blank"><strong>忆星辰</strong></a></div>
                    <div class="go-up"><a href="#" rel="go-top"><i class="fa-angle-up"></i></a></div>
                </div>
            </footer>
    <script>
        $(document).ready(function () {
            return $(document).on("click", ".has-sub", function () {
                var e = $(this);
                $(this).hasClass("expanded") ? $(".has-sub ul").each(function (s, i) {
                    var t = $(this);
                    e.find("ul")[0] != i && setTimeout(function () {
                        t.attr("style", "")
                    }, 300)
                }) : setTimeout(function () {
                    e.find("ul").attr("style", "")
                }, 300)
            }), $(".user-info-menu .hidden-sm").click(function () {
                $(".sidebar-menu").hasClass("collapsed") ? $(".has-sub.expanded > ul").attr("style",
                    "") : $(".has-sub.expanded > ul").show()
            }), $("#main-menu li ul li").click(function () {
                $(this).siblings("li").removeClass("active"), $(this).addClass("active")
            }), $("a.smooth").click(function (s) {
                s.preventDefault(), public_vars.$mainMenu.add(public_vars.$sidebarProfile).toggleClass(
                    "mobile-is-visible"), ps_destroy(), $("html, body").animate({
                    scrollTop: $($(this).attr("href")).offset().top - 30
                }, {
                    duration: 500,
                    easing: "swing"
                })
            }), !1
        });
        var href = "",
            pos = 0;
        $("a.smooth").click(function (s) {
            $("#main-menu li").each(function () {
                    $(this).removeClass("active")
                }), $(this).parent("li").addClass("active"), s.preventDefault(), href = $(this).attr("href"),
                pos = $(href).position().top - 30
        })
    </script>
    <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/TweenMax.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/resizeable.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/joinable.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/xenon-api.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/xenon-toggles.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.1/source/box/js/xenon-custom.js"></script>
</body>

</html>
"""

li_head = "<li>"
li_tail = "</li>"
a_tail = "</a>"
ul_head = "<ul>"
ul_tail = "</ul>"
def a_head(name):
    return '<a href="#' + name + '" class="smooth">'
def span_all(name):
    return '<span class="title">' + name + '</span>'
def get_title_text(title):
    for i in range(len(title)):
        if title[i] != ' ':
            continue
        if title[-1] == '\n':
            return title[i + 1:-1]
        else:
            return title[i + 1:]
def get_title_level(line):
    temp = '#'
    sum = 0
    for i in line:
        if i == temp:
            sum += 1
        else:
            return sum
def create_list(title):
    tag = 0
    text_list = []
    text_list.insert(tag, a_head(title))
    tag += 1
    text_list.insert(tag, a_tail)
    text_list.insert(tag, span_all(title))
    return text_list


div_row_head = '<div class="row">'
div_tail = '</div>'
div_col = """<div class="col-sm-3">"""
div_x_com = '<div class="xe-comment">'
div_xe = '<div class="xe-comment-entry">'

block_list = []
tag_block = 0

def div_onclick_head(url):
    return """<div class="xe-widget xe-conversations box2 label-info" onclick="window.open('""" + url + """', '_blank')" data-toggle="tooltip" data-placement="bottom" title="" data-original-title=\"""" + url + """">"""
def a_img_all(src):
    return """<a class="xe-user-img"><img data-src=\"""" + src + """" class="lozad img-circle" width="40"></a>"""
def a_href_all(name):
    return """<a href="#" class="xe-user-name overflowClip_1"><strong>""" + name + """</strong></a>"""
def p_over_all(desc):
    return """<p class="overflowClip_2">""" + desc + "</p>"
def h_n_all(n, title):
    n = str(n)
    return '<h' + n + """ class="text-gray"><i class="linecons-tag" style="margin-right: 7px;" id=\"""" + title + """"></i>""" + title + '</h1>'

def c_4_block(line):
    block_list = []
    tag_block = 0
    if line[-1] == '\n':
        line = line[:-1]
    line_list = line.split(',')
    block_list.insert(tag_block, div_col)
    tag_block += 1
    block_list.insert(tag_block, div_tail)
    block_list.insert(tag_block, div_onclick_head(line_list[0]))
    tag_block += 1
    block_list.insert(tag_block, div_tail)
    block_list.insert(tag_block, div_xe)
    tag_block += 1
    block_list.insert(tag_block, div_tail)
    block_list.insert(tag_block, a_img_all(line_list[1]))
    tag_block += 1
    block_list.insert(tag_block, div_x_com)
    tag_block += 1
    block_list.insert(tag_block, div_tail)
    block_list.insert(tag_block, a_href_all(line_list[2]))
    tag_block += 1
    block_list.insert(tag_block, p_over_all(line_list[3]))
    return block_list

def new_block(now_title, now_level, f_text):
    block_list = []
    tag_block = 0
    while True:
        block_list.insert(tag_block, div_row_head)
        tag_block += 1
        block_list.insert(tag_block, div_tail)
        for i in range(4):
            fine_num = f_text.tell()
            line = f_text.readline()
            if line == '':
                break
            if get_title_level(line) != 0:
                f_text.seek(fine_num)
                break
            block_list[tag_block:tag_block] = c_4_block(line)
            tag_block += 11
        if line == '':
            break
        if get_title_level(line) != 0:
            break
        tag_block += 1
    return block_list

block_list = []
def create_block(now_level, now_title):
    text_list = []
    tag = 0
    while(True):
        now_line = f_text.readline()
        now_level = get_title_level(now_line)
        now_title = get_title_text(now_line)
        global block_list
        block_list.append(h_n_all(now_level, now_title))

        fine_num = f_text.tell()
        next_line = f_text.readline()
        next_title = get_title_text(next_line)
        next_level = get_title_level(next_line)
        if next_level == 0:
            f_text.seek(fine_num)
            block_list += new_block(now_title, now_level, f_text)
            fine_num = f_text.tell()
            next_line = f_text.readline()
            next_title = get_title_text(next_line)
            next_level = get_title_level(next_line)
        f_text.seek(fine_num)

        text_list.insert(tag, li_head)
        tag += 1
        text_list.insert(tag, li_tail)
        temp = create_list(now_title)
        text_list[tag:tag] = temp
        tag += len(temp)

        if next_line == '':
            return text_list, -1, block_list

        if(now_level < next_level):
            text_list.insert(tag, ul_head)
            tag += 1
            text_list.insert(tag, ul_tail)
            temp, re_next_level, an_temp = create_block(next_level, next_title)
            text_list[tag:tag] = temp
            tag += len(temp)
            tag += 2
            if re_next_level < now_level:
                return text_list, re_next_level, block_list
            elif re_next_level == -1:
                return text_list, -1, block_list
        if(now_level == next_level):
            tag += 1
            continue
        if(now_level > next_level):
            return text_list, next_level, block_list
my = create_block(0, 1)
f_output.write(head + ("".join(my[0])) + middle + ("".join(my[2])) + tail);
