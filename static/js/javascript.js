
jQuery('.send_data').submit(function(){
	jQuery('.content').css('visibility', 'hidden');
	jQuery('.content').fadeOut('slow')
	jQuery('#dark_theme').css('visibility', 'hidden');
	jQuery('#light_theme').css('visibility', 'hidden');
	jQuery('html').css('cursor', 'wait');
	
	setTimeout(function(){
		jQuery('#loading').css('display', 'block');
	
		jQuery('#loading').fadeIn(900)
	}, 1500);
	
	
});



jQuery('#dark_theme').click(function(){
	var dark_theme = document.documentElement.style.cssText = "--blueviolet: black";
	
	localStorage.setItem('bg', 'night')
	
	var dark_theme = document.documentElement.style.cssText = "--blueviolet: black";
	
	jQuery('.crescent_moon').removeClass('filter-icons-black');
	jQuery('.crescent_moon').addClass('filter-icons-white');
	
	jQuery('#light_theme').removeClass('active')
	jQuery('#dark_theme').addClass('active')
		
});

if (localStorage.getItem('bg') == 'night'){
	
	var dark_theme = document.documentElement.style.cssText = "--blueviolet: black";
	
	jQuery('.crescent_moon').removeClass('filter-icons-black');
	jQuery('.crescent_moon').addClass('filter-icons-white');
	
	jQuery('#light_theme').removeClass('active')
	jQuery('#dark_theme').addClass('active')
}

jQuery('#light_theme').click(function(){
	
	localStorage.setItem('bg', 'light')
	
	document.documentElement.style.cssText = "--blueviolet: blueviolet";
	
	jQuery('#light_theme').addClass('active')
	jQuery('#dark_theme').removeClass('active')
	
	jQuery('.crescent_moon').addClass('filter-icons-black');
	jQuery('.crescent_moon').removeClass('filter-icons-white');
});

if (localStorage.getItem('bg') == 'light'){
	
	document.documentElement.style.cssText = "--blueviolet: blueviolet";
	
	jQuery('#light_theme').addClass('active')
	jQuery('#dark_theme').removeClass('active')
	
	jQuery('.crescent_moon').addClass('filter-icons-black');
	jQuery('.crescent_moon').removeClass('filter-icons-white');
}