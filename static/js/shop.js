$(function (event) {
    category = function (obj) {
        var category_detail = obj.options[obj.selectedIndex];
        var cid = category_detail.value;

        console.log(cid)
    };
   event.stopPropagation();
});