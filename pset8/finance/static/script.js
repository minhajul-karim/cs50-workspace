
$(document).ready(function(){

	// Form submission status, 0 = false; 1 = true
	$submission_status = 0;

	// Global var to store user provided passwords
	$pwd1 = "";
	$pwd2 = "";
	
	// When user presses a key is username field
	$("#usr").on('keyup', function(e){
        
        // Declare an empty string
        $str = "";

        // Concatenate user input
        $str += e.target.value;
        
        // Ajax call with str if it's len is more than 2
        if ($str.length > 2){
        	$.ajax({
	        	data: {
	        		username: $str
        		},

        		type: 'GET',
        		url: '/check',

        		// If ajax call ends successfully
	        	success: function(data){

	        		// Check returned data
	        		if (data.status == 'true'){
	        			
	        			// Notify user
	        			$('#username_avalability').html('username is not avalaible');
	        			$('#username_avalability').css({'color': '#dc3545'});

	        			// Set submission_status to 0 so that the form can't be submitted 
	        			$submission_status = 0;

	        		}
	        		else{

	        			// Notify user
	        			$('#username_avalability').html('username is available');
	        			$('#username_avalability').css({'color': '#008000'});

	        			// Set submission_status to 1 to submit form 
	        			$submission_status = 1;
	        		}

	        	}
        	});

        }

        // If the length of str is less than 3
        else{

        	// Notify user
        	$('#username_avalability').html('username must be more than 2 characters');
        	$('#username_avalability').css({'color': '#dc3545'});

        	// Set submission_status to 0 so that the form can't be submitted 
        	$submission_status = 0;
        }

    });

    // Grab the first password
    $('#pwd1').on('keyup', function(e){
	    $pwd1 = "";

	    // Concatenate user's 1st password
	    $pwd1 += e.target.value;

	    // Hide password mismatched error message if correction is going on
	    $('#password_check').html('');
	});

	// Grab the confirmation password
    $('#pwd2').on('keyup', function(e){
	    $pwd2 = "";

	    // Concatenate user's 2nd input
	    $pwd2 += e.target.value;

	    // Hide password mismatched error message if correction is going on
	    $('#password_check').html('');
	});


	// When user submits the registration form
    $('#reg_form').on('submit', function(){

    	// Restrict user from submitting when submission_status is set to 0
    	if ($submission_status == 0)
    		return false;

    	// Submit otherwise
    	 else{
        
	        // Submit if both passwords match
	        if ($pwd1 == $pwd2)
	            return true;

	        // Restrict if passwords didn't match
	        else{

	        	// Nofity user
	            $('#password_check').html('passwords didn\'t match');
	            $('#password_check').css({'color': '#dc3545'});
	            return false;
	        }
    	}
    });

    // When user clicks the buy button of index page

    $('[name="buy_button"]').on('click', function(){

    	// Grab the immediate parent of the button
    	$td = $(this).parent();

    	// Grab the immediate parent of $td
    	$tr = $td.parent();

    	// Grab the symbol of that row
    	$symbol = $tr.children('.symbol_row').children('.symbol').text();

    	// Ajax call to send $symbol to backend 
    	$.ajax({
		    data: {
		        sym: $symbol
		    },

		    type: 'GET',

		    // Send data to this route
		    url: '/save_symbol',

		    success: function(response) {
		    	// Redirect to this route
		        window.location.assign('/buythis');
		      },
		    
		});

    });

    // When user clicks the sell button
    $('[name="sell_button"]').on('click', function(){
    	
    	// Grab the immediate parent of the button
    	$td = $(this).parent();

    	// Grab the immediate parent of $td
    	$tr = $td.parent();

    	// Grab the symbol of that row
    	$symbol = $tr.children('.symbol_row').children('.symbol').text();
    
    	// Ajax call to send $symbol to backend 
    	$.ajax({
		    data: {
		        sym: $symbol
		    },

		    type: 'GET',

		    // Send data to this route
		    url: '/save_selected',

		    success: function(response) {
		    	// Redirect to this route
		        window.location.assign('/sellthis');
		      },
		    
		});
    });


});
