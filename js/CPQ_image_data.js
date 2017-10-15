$(document).ready(()=>{
	var file;
	// var inp = $('#get-files');
	$('#get-files').on('change', function(){
		// for(let i = 0; i < ('#get-files'.value.length); i++){
			// file = inp.files;
			var name_all_chars = $(this).val().split(/[\\/]/);
			var name_1_char = $(this).val().split(/[\\]/);
			var name_none = $(this).val().split();
			
			// name.split('.');
			console.dir($(this));
			// console.log($(this).value());
			// console.log($(this).files());
			console.log(name_all_chars);
			console.log(name_1_char);
			console.log(name_none);

			// console.log($('#get-files').input);
		// }
	})
	
})