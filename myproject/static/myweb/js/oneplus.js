//导航栏
$('.pdd2 li').mouseover(function(){
	var a = $(this).val()
	if (a==1) {
		$('#dss').attr('src','./static/myweb/images/fdb_hover.png')
	}if (a==2) {
		$('#dgwc').attr('src','./static/myweb/images/shopb.png')
	}if (a==3) {
		$('#dp').attr('src','./static/myweb/images/icon_person_hover.png')
	}
})
$('.pdd2 li').mouseout(function(){
	var a = $(this).val()
	if (a==1) {
		$('#dss').attr('src','./static/myweb/images/fdb.png')
	}if (a==2) {
		$('#dgwc').attr('src','./static/myweb/images/shopw.png')
	}if (a==3) {
		$('#dp').attr('src','./static/myweb/images/icon_person.png')
	}
})


// 轮播图
$(function () {
    $('#myCarousel,#myCarousel5').carousel({
        //设置自动播放/3 秒
        interval: 3000,
    });
});
//超大轮播图
$(function () {
    $('#myCarousel4').carousel({
        //设置自动播放/2 秒
        interval: 2500,
    });
});

// 众多特性选项卡
$('.all .optop .options li').click(function(){
			$(this).addClass('active').siblings().removeClass('active');
			$('.content li').eq($(this).index()).addClass('active').siblings().removeClass('active')
			$('.xxkdiv div').eq($(this).index()).addClass('active').siblings().removeClass('active')
		})

//照相机选项卡
$('.cameraoption .cameraoptions li').click(function(){
			$(this).addClass('active').siblings().removeClass('active');
			$('.cameracontent li').eq($(this).index()).addClass('active').siblings().removeClass('active')
			$('.camerapic div').eq($(this).index()).addClass('active').siblings().removeClass('active')
		})


//右侧选项卡
$('.rightoption .rightoptions li').click(function(){
			$(this).addClass('active').siblings().removeClass('active');
			$('.rightcontent li').eq($(this).index()).addClass('active').siblings().removeClass('active')
			$('.rightpic div').eq($(this).index()).addClass('active').siblings().removeClass('active')
		})


//手机详情页首图
$('.yyhxz ul li').mouseover(function(){
	$(this).css('cursor','pointer')
})
$('.yyhxz ul li').click(function(){
	var a = $(this).val();
	$(this).css('color','black').siblings().css('color')
	// console.log(a)
	if (a == 1) {
		$('.yueyanhui').css('background','#DADCE2')
		$('.yyhimg img').attr('src','./static/myweb/images/gray-phone.png')
		$('.yyhtext1 h2').css('color','#000000')
		$(this).css('color','black').siblings().css('color','#A1A1A2')
		$('.daohang2 .navbar').css('background','#F8F8F9')

	}
	if (a == 2) {
		$('.yueyanhui').css('background','#171717')
		$('.yyhimg img').attr('src','./static/myweb/images/black-phone.png')
		$('.yyhtext1 h2').css('color','#FFFFFF')
		$(this).css('color','#FFFFFF').siblings().css('color','#A1A1A2')
		$('.daohang2 .navbar').css('background','#050505')
	}
	if (a == 3) {
		$('.yueyanhui').css('background','#F6F6F6')
		$('.yyhimg img').attr('src','./static/myweb/images/Unknown.png')
		$('.yyhtext1 h2').css('color','#524837')
		$(this).css('color','#524837').siblings().css('color','#A1A1A2')
		$('.daohang2 .navbar').css('background','#FDFDFD')
	}
})
//详情页导航栏2固定
$(window).scroll(function(){
	var dh2 = $(window).scrollTop();
	// console.log(dh2)
	if (dh2>110) {
		$('.daohang2 .navbar').addClass('navbar-fixed-top')
		$('.dh2mobile, .bukenenga').addClass('navbar-fixed-top')
		$('.daohang2 .navbar').css('background','rgba(255,255,255,0.8)')
		$('.hahaha').css('display','none');
		$('.bukeneng li').css('background','rgba(255,255,255,0.0)')
		$('.bukenenga').css('background','rgba(255,255,255,0.8)')
		$('.bukeneng').css('background','rgba(255,255,255,0)')
		$('.bukeneng li').css('height','60px')
		// $('.bukeneng li').animate({
		// 	height:'60px',
		// },2000);
	}
	if (dh2<110) {
		$('.daohang2 .navbar').removeClass('navbar-fixed-top')
		$('.dh2mobile, .bukenenga').removeClass('navbar-fixed-top')
		$('.hahaha').css('display','block');
		$('.bukeneng li').css('height','120px')
		// $('.bukeneng li').animate({
		// 	height:'120px',
		// },2000);
	}
});

// 商城不可能完成的导航栏
$('.bukeneng li').mouseover(function(){
	var a = $(this).val()
	$(this).css('color','#ED0A2B')
	if (a == 1) {
		$('#a1').attr('src','./static/myweb/images/shoujic.png')
	}
	if (a == 2) {
		$('#a2').attr('src','./static/myweb/images/erjic.png')
	}
	if (a == 3) {
		$('#a3').attr('src','./static/myweb/images/kec.png')
	}
	if (a == 4) {
		$('#a4').attr('src','./static/myweb/images/xianc.png')
	}
	if (a == 5) {
		$('#a5').attr('src','./static/myweb/images/taozhuangc.png')
	}
	if (a == 6) {
		$('#a6').attr('src','./static/myweb/images/baoc.png')
	}
})
$('.bukeneng li').mouseout(function(){
	var a = $(this).val()
	$(this).css('color','#808080')
	if (a == 1) {
		$('#a1').attr('src','./static/myweb/images/shoujib.png')
	}
	if (a == 2) {
		$('#a2').attr('src','./static/myweb/images/erjib.png')
	}
	if (a == 3) {
		$('#a3').attr('src','./static/myweb/images/keb.png')
	}
	if (a == 4) {
		$('#a4').attr('src','./static/myweb/images/xianb.png')
	}
	if (a == 5) {
		$('#a5').attr('src','./static/myweb/images/taozhuangb.png')
	}
	if (a == 6) {
		$('#a6').attr('src','./static/myweb/images/baob.png')
	}
})
//不可能的固定
// $(window).scroll(function(){
// 	var dh2 = $(window).scrollTop();
// 	console.log(dh2)
// 	if (dh2>110) {
// 		$('.daohang2 .navbar').addClass('navbar-fixed-top')
// 		$('.dh2mobile').addClass('navbar-fixed-top')
// 		$('.daohang2 .navbar').css('background','rgba(255,255,255,0.8)')
// 	}
// 	if (dh2<110) {
// 		$('.daohang2 .navbar').removeClass('navbar-fixed-top')
// 		$('.dh2mobile').removeClass('navbar-fixed-top')
// 	}
// });
// // 表单验证
// //声明全局变量
// 	var NameOk = false;
// 	var PassOk = false;
// 	var Pass2Ok = false;
// 	var EmailOk = false;

// 	//获取焦点事件 focus
// 	$('input').focus(function(){
// 		//获取焦点时,给予提示信息
// 		var at = $(this).attr('readme');
// 		$(this).next('span').html(at).css('color','blue');
// 		// $(this).css('border','1px solid blue');
// 	})

// 	//用户名验证
// 	$('input[name=username]').blur(function(){
// 		console.log(321)
// 		//获取用户的输入信息
// 		var v = $(this).val();
// 		var reg = /^\w{6,18}$/;
// 		if(reg.test(v)){
// 			// $(this).next('span').html('√').css('color','green');
// 			$(this).css('border','1px solid green');
// 			//修改全局变量
// 			NameOk = true;
// 			console.log(312)
// 		}else{
// 			// $(this).next('span').html('用户名格式不正确').css('color','red');
// 			$(this).css('border','1px solid red');
// 			//修改全局变量
// 			NameOk = false;
// 		}
// 	})
// 	//密码验证
// 	$('input[name=password]').blur(function(){
// 		//获取用户的输入信息
// 		 var v = $(this).val();
// 		// console.log(v)
// 		var reg = /^\w{6,18}$/;
// 		if(reg.test(v)){
// 			console.log(1111)
// 			// $(this).next('span').html('√').css('color','green');
// 			$(this).css('border','1px solid green');
// 			//修改全局变量
// 			PassOk = true;
// 		}else{
// 			// $(this).next('span').html('密码格式不正确').css('color','red');
// 			$(this).css('border','1px solid red');
// 				//修改全局变量
// 			PassOk = false;
// 		}
// 	})

// 	$('input[name=password2]').blur(function(){
// 		//获取用户的输入信息
// 		var v2 = $(this).val();
// 		// console.log(v)
// 		var reg = /^\w{6,18}$/;
// 		if(reg.test(v2)){
// 			// $(this).next('span').html('√').css('color','green');
// 			$(this).css('border','1px solid green');
// 			//修改全局变量
// 			Pass2Ok = true;
// 		}else{
// 			// $(this).next('span').html('密码格式不正确').css('color','red');
// 			$(this).css('border','1px solid red');
// 				//修改全局变量
// 			Pass2Ok = false;
// 		}
// 	})

	
// 	// 	//邮箱验证
// 	// $('input[name=email]').blur(function(){
// 	// 	//获取用户的输入信息
// 	// 	var v = $(this).val();
// 	// 	var reg = /^\w+@\w+\.(com|cn|org|net)$/;
// 	// 	if(reg.test(v)){
// 	// 		$(this).next('span').html('√').css('color','green');
// 	// 		$(this).css('border','1px solid green');
// 	// 		//修改全局变量
// 	// 		EmailOk = true;
// 	// 	}else{
// 	// 		$(this).next('span').html('邮箱格式不正确').css('color','red');
// 	// 		$(this).css('border','1px solid red');
// 	// 		//修改全局变量
// 	// 		EmailOk = false;
// 	// 	}
// 	// })

	

// 	// 提交验证
// 	$('form').submit(function(){
// 		console.log(NameOk,PassOk)
// 		//触发input 丧失焦点事件
// 		// $('input').trigger('blur');

// 		//判断如果都正确
// 		if(NameOk && PassOk ){
// 			return true;
// 			console.log('zhen')
// 		}
// 		//阻止默认行为
// 		return false;
// 		console.log('jia')
// 	})





















