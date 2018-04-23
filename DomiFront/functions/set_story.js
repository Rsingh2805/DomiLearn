function get_story_html(data){
	if(data.is_anonymous==true){
		username = 'Anonymous';
	}else{
		username = data.user.username;
	}
	var html="";
	html += '<div class="card container" style="margin:15px; padding:10px; white-space: pre-line"><div class="container"><h4><b>'+data.title+'</b></h4><br><p class="well">'+data.content+'</p></div><button class="btn pull-right btn-default">'+username+'</button></div>';
	return html;
	
}