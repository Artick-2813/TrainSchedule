
jQuery('.send_data').submit(function(){
	jQuery('.content').css('visibility', 'hidden');
	jQuery('.content').fadeOut('slow')
	jQuery('html').css('cursor', 'wait');
	
	setTimeout(function(){
		jQuery('#loading').css('display', 'block');
	
		jQuery('#loading').fadeIn(900)
	}, 1500);
	
});