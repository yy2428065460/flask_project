// JavaScript Document




	
/*�Զ�������Ʒ���ܽ��ܹ���ʡ�Ľ��ͻ���*/
function productCount(){
	var total=0;      //��Ʒ����ܼ�

	var price;     //ÿһ����Ʒ�ĵ���
	var subtotal;  //ÿһ����Ʒ��С��

     /*����IDΪshopping��������е�����*/
	var myTableTr=document.getElementById("shopping").getElementsByTagName("tr"); 
	if(myTableTr.length>0){
	for(var i=1;i<myTableTr.length;i++){/*��1��ʼ����һ�еı��ⲻ����*/
	    if(myTableTr[i].getElementsByTagName("td").length>2){ //���һ�в�����

		price=myTableTr[i].getElementsByTagName("td")[4].innerHTML;

		total+=price;
		myTableTr[i].getElementsByTagName("td")[6].innerHTML=price;
		}
	}
	document.getElementById("total").innerHTML=total;
	
	}
}
window.onload=productCount;

/*��ѡ��ȫѡ��ȫ��ѡЧ��*/
function selectAll(){
	var oInput=document.getElementsByName("cartCheckBox");
 for (var i=0;i<oInput.length;i++){
 	    oInput[i].checked=document.getElementById("allCheckBox").checked;
	}
}
	
/*���ݵ�����ѡ���ѡ�����ȷ��ȫѡ��ѡ���Ƿ�ѡ��*/
function selectSingle(){
	var k=0;
	var oInput=document.getElementsByName("cartCheckBox");
	 for (var i=0;i<oInput.length;i++){
	   if(oInput[i].checked==false){
		  k=1;
		  break;
	    }
	}
	if(k==0){
		document.getElementById("allCheckBox").checked=true;
		}
	else{
		document.getElementById("allCheckBox").checked=false;
		}
}

/*ɾ��������Ʒ*/
function deleteRow(rowId){
	var Index=document.getElementById(rowId).rowIndex; //��ȡ��ǰ�е�������
	document.getElementById("shopping").deleteRow(Index);
	document.getElementById("shopping").deleteRow(Index-1);
	productCount();
	}

/*ɾ��ѡ���е���Ʒ*/
function deleteSelectRow(){
	var oInput=document.getElementsByName("cartCheckBox");
	var Index;
	 for (var i=oInput.length-1;i>=0;i--){
	   if(oInput[i].checked==true){
		 Index=document.getElementById(oInput[i].value).rowIndex; /*��ȡѡ���е�������*/
		 document.getElementById("shopping").deleteRow(Index);
	     document.getElementById("shopping").deleteRow(Index-1);
	    }
	}
	productCount();
	}

$(function(){
	$('.order').click(function () {
			// ����`�˳���¼`
		$.ajax({
			url: '/index/order',
			type: 'post',
			success: function (resp) {
				if (resp.errno == 0) {
					# �ɹ�
					window.location.href='order.html'
					alert('123')
				}
			}
		})
	})
})




