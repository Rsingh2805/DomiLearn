$(document).ready(function(){
	$('#add_button').click(function(){
		var title = $('#story-title').val();
		var content = $('#story-content').val();
		var anony_check = $('#anony_check').val();
		if(anony_check=='1'){
			anony = true;
		}else{
			anony = false;
		}
		var data = {
			"title": title,
			"content": content,
			"is_anonymous": anony
		}
		token=getCookie('token');
		console.log(token);
		$.ajax({
			type: 'post',
			url: 'http://localhost:8000/story/submit',
			data: data,
			headers: { "Authorization": 'Token ' + token },
			success:function(htm, textStatus, xhr){
				$('#error_dialog').html('<div class="notify alert alert-danger"><b>Success: </b>Submitted successfully</div>');
        setTimeout(function(){ $('.notify').hide(); }, 3000);
			},
			error:function(htm, textStatus, xhr){
				console.log(htm);

			}
		});
	});
});