function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(function(){

    // 打开登录框
    $('.comment_form_logout').click(function () {
        $('.login_form_con').show();
    });

    // 收藏
    $(".collection").click(function () {
        // 获取收藏的`商品id`
        var shop_id = $(this).attr("data-news-id");
        var action = "do";

        // 组织参数
        var params = {
            "shop_id": shop_id,
            "action": action
        };

        // TODO 请求收藏新闻
        $.ajax({
            url: "/news/collect",
            type: "post",
            data: JSON.stringify(params),
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    // `收藏`成功
                    // 隐藏`收藏`按钮
                    $(".collection").hide();
                    // 显示`已收藏`按钮
                    $(".collected").show();
                }
                else if (resp.errno == "5002") {
                    // 用户登录
                    $(".login_form_con").show();
                }
                else {
                    // `收藏`失败
                    alert(resp.errmsg);
                }
            }
        })


    });

    // 取消收藏
    $(".collected").click(function () {
        // 获取收藏的`新闻id`
        var shop_id = $(this).attr("data-news-id");
        var action = "undo";

        // 组织参数
        var params = {
            "shop_id": shop_id,
            "action": action
        };

        // TODO 请求取消收藏新闻
        $.ajax({
            url: "/news/collect",
            type: "post",
            data: JSON.stringify(params),
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    // `取消收藏`成功
                    // 显示`收藏`按钮
                    $(".collection").show();
                    // 隐藏`已收藏`按钮
                    $(".collected").hide();
                }
                else if (resp.errno == "4101") {
                    // 用户登录
                    $(".login_form_con").show();
                }
                else {
                    // `收藏`失败
                    alert(resp.errmsg);
                }
            }
        })

    });

});