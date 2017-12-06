$(function() {
    $("#middle-left-menu ul li").each(function() {
        var a = "unselected",
        b = $(this).attr("id");
        $("#middle-left-menu #" + b + " span").css("background", "url(/static/images/" + a + "/" + b + ".png) no-repeat 0 0 ");
        "on" == $(this).attr("class") && (a = "Choice", $("#middle-left-menu #" + b + " span").css("background", "url(/static/images/" + a + "/" + b + ".png) no-repeat 0 0 "), $("#middle-left-menu #" + b + " span a").css("color", "#EE436D"), $(this).css("border-left", "solid 4px #EE436D"), $(this).css("background-color", "#f1f1f1"));
        $("#middle-left-menu ul li").hover(function() {
            var a = $(this).attr("id");
            $("#middle-left-menu #" + a + " span").css("background", "url(/static/images/Choice/" + a + ".png) no-repeat 0 0 ");
            $("#middle-left-menu #" + a + " span a").css("color", "#EE436D");
            $(this).css("border-left", "solid 4px #EE436D");
            $(this).css("background-color", "#f1f1f1");
            $(this).css("color", "red")
        },
        function() {
            var a = "unselected",
            b = $(this).attr("id");
            "on" == $(this).attr("class") ? (a = "Choice", $("#middle-left-menu #" + b + " span").css("background", "url(/static/images/" + a + "/" + b + ".png) no-repeat 0 0 "), $("#middle-left-menu #" + b + " span a").css("color", "#EE436D"), $(this).css("border-left", "solid 4px #EE436D"), $(this).css("background-color", "#f1f1f1")) : ($("#middle-left-menu #" + b + " span").css("background", "url(/static/images/" + a + "/" + b + ".png) no-repeat 0 0 "), $("#middle-left-menu #" + b + " span a").css("color", "#8A8A8A"), $(this).css("border-left", "solid 4px #F7F7F7"), $(this).css("background-color", "#F1F6F9"))
        })
    });
    $("#middle-left-menu ul li span a").hover(function() {
        $(this).css("color", "#EE436D")
    },
    function() {
        $(this).css("color", "#8A8A8A")
    });
    var c = $("#right_top_ad_one img").attr("tag"),
    d = $("#right_top_ad_one #f").attr("tag");
    $("#right_top_ad_img").attr("src", c);
    $("#right_top_ad_text").html(d);
    $("#right_top_ad_one").hover(function() {
        var a = $("#right_top_ad_one img").attr("tag"),
        b = $("#right_top_ad_one #f").attr("tag");
        $("#right_top_ad_text").html(b);
        $("#right_top_ad_img").attr("src", a)
    },
    function() {
        $("#right_top_ad_img").removeAttr("style")
    });
    $("#right_top_ad_two").hover(function() {
        var a = $("#right_top_ad_two img").attr("tag"),
        b = $("#right_top_ad_two #f").attr("tag");
        $("#right_top_ad_text").html(b);
        $("#right_top_ad_img").attr("src", a)
    },
    function() {
        $("#right_top_ad_img").removeAttr("style")
    });
    $("#right_top_ad_thr").hover(function() {
        var a = $("#right_top_ad_thr img").attr("tag"),
        b = $("#right_top_ad_thr #f").attr("tag");
        $("#right_top_ad_text").html(b);
        $("#right_top_ad_img").attr("src", a)
    },
    function() {
        $("#right_top_ad_img").removeAttr("style")
    });
    $("#filtrate").hover(function() {
        $(this).css({
            "border-bottom-right-radius": "0px"
        });
        $(this).css({
            "border-bottom-left-radius": "0px"
        });
        $("#filtrateresults", this).show()
    },
    function() {
        $(this).css({
            "border-bottom-right-radius": "10px"
        });
        $(this).css({
            "border-bottom-left-radius": "10px"
        });
        $("#filtrateresults", this).hide()
    });
    $("body").on("mouseover", ".yingshidiv",
    function(a) {
        $(".x", this).stop().css({
            left: "100px"
        }).show();
        $(".fire", this).show()
    });
    $("body").on("mouseout", ".yingshidiv",
    function() {
        $(".fire, .x", this).hide()
    });
    $("#s").html($("#filtrateresults li").attr("tag"));
    $("#filtrateresults li").each(function() {
        $(this).click(function() {
            var a = $(this).attr("tag"),
            b = $(this).attr("Genres_id");
            $(this).siblings("li").removeAttr("style");
            $(this).css({
                color: "#EC4069"
            });
            $("#s").html(a);
            $("#filtrateresults", this).hide();
            GetGenresVideo(b)
        })
    });
    switch (window.location.pathname) {
    case "/index/":
        $("#middle-left-menu #jingxuan span").attr("style", "background:url(/static/images/Choice/jingxuan.png) no-repeat 0 0 !important;");
        $("#middle-left-menu #jingxuan a").attr("style", "color: #EE436D!important;");
        $("#jingxuan").attr("class", "on");
        break;
    case "/video/":
        $("#middle-left-menu #yingshi span").attr("style", "background:url(/static/images/Choice/yingshi.png) no-repeat 0 0 !important;");
        $("#middle-left-menu #yingshi a").attr("style", "color: #EE436D!important;");
        $("#yingshi").attr("class", "on");
        break;
    case "/image/":
        $("#middle-left-menu #tupian span").attr("style", "background:url(/static/images/Choice/tupian.png) no-repeat 0 0 !important;");
        $("#middle-left-menu #tupian a").attr("style", "color: #EE436D!important;");
        $("#tupian").attr("class", "on");
        break;
    case "/game/":
        $("#middle-left-menu #youxi span").attr("style", "background:url(/static/images/Choice/youxi.png) no-repeat 0 0 !important;");
        $("#middle-left-menu #youxi a").attr("style", "color: #EE436D!important;");
        $("#youxi").attr("class", "on");
        break;
    case "/live/":
        $("#middle-left-menu #zhibo span").attr("style", "background:url(/static/images/Choice/zhibo.png) no-repeat 0 0 !important;");
        $("#middle-left-menu #zhibo a").attr("style", "color: #EE436D!important;");
        $("#zhibo").attr("class", "on");
        break;
    default:
        $("#middle-left-menu #jingxuan span").attr("style", "background:url(/static/images/Choice/jingxuan.png) no-repeat 0 0 !important;"),
        $("#middle-left-menu #jingxuan a").attr("style", "color: #EE436D!important;"),
        $("#jingxuan").attr("class", "on")
    }
});
function GetGenresVideo(c) {
    $.ajax({
        url: "/V1/GetGenresVideo/",
        type: "GET",
        async: !0,
        data: {
            Genres_id: c
        },
        timeout: 3E3,
        dataType: "json",
        beforeSend: function(d) {
            $("#tips").html("<img src='/static/images/loading.gif' style='width: 36px;height: 41px'/> <font color='#EC4069'> \u6570\u636e\u8f7d\u5165\u4e2d... </font>")
        },
        success: function(d, a, b) {
            if ("" == d) $(".right_middle_command").html("<br><BR><font color='#EC4069'> \u6682\u65e0\u6570\u636e </font>");
            else {
                a = "";
                $(".right_middle_command").html("");
                for (var c in d) a = a + "<div class='yingshidiv'><img src='" + d[c].Video_Cover + "'><span style='float: left;color: #5E5E5E'>" + d[c].name + "<p>" + d[c].starring + "</p></span><span style='float: right;margin-right: 21px;color: #EE436D;'>&hearts; &nbsp; " + d[c].score + "</span><a href=" + d[c].File_URL + "#video class=x target=_blank></a><div class=fire></div></div>";
                $(".right_middle_command").html(a)
            }
        },
        error: function(c, a) {
            "timeout" == a ? $(".right_middle_command").html("<br><BR><font color='#EC4069'> \u6570\u636e\u8f7d\u5165\u8d85\u65f6 </font>") : $(".right_middle_command").html("<br><BR><font color='#EC4069'> \u6570\u636e\u8f7d\u5165\u9519\u8bef </font>")
        },
        complete: function() {}
    })
}
// var omitformtags = ["input", "textarea", "select"],
// omitformtags = omitformtags.join("|");
// function disableselect(c) {
//     if ( - 1 == omitformtags.indexOf(c.target.tagName.toLowerCase())) return ! 1
// }
// function reEnable() {
//     return ! 0
// }
// "undefined" != typeof document.onselectstart ? document.onselectstart = new Function("return false") : (document.onmousedown = disableselect, document.onmouseup = reEnable);
// function stop() {
//     return ! 1
// }
// document.oncontextmenu = stop;