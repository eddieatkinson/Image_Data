$(document).ready(()=>{
	var file;
	// var inp = $('#get-files');
	$('#get-files').on('change', function(){
		// for(let i = 0; i < ('#get-files'.value.length); i++){
			// file = inp.files;
			var name = $(this).val().split(/[\\/]/);
			
			// name.split('.');
			console.log(name[name.length - 1]);

			// console.log($('#get-files').input);
		// }
	})
	
})