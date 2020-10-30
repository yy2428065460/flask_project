$(function (event) {
    category = function (obj) {
        var category_detail = obj.options[obj.selectedIndex];
        var cid = category_detail.value;

        console.log(cid)
    };
   event.stopPropagation();
});

$(function(){
	$('#shop_details').click(function () {
			// 请求`退出登录`
		$.ajax({
			url: '/index/shop_details',
			type: 'get',
			success: function (resp) {
				if (resp.errno == 0) {
					window.location.href='shop_details.html'
					alert('123')
				}
			}
		})
	})
})