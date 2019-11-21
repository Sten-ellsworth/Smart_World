$(document).ready( function(){
$('.available').load('smart_world/dashboard/load.php');
setTimeout( function() {
	$('.available').fadeOut('slow').load('smart_world/dashboard/load.php').fadeIn('slow');
},1000);
});
