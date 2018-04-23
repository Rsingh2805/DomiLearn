function check_session(url){
	token=getCookie('token');
	if(typeof token === 'undefined' || token === null || token==''){
		location.href = url;
	}
}
