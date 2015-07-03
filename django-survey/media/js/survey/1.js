$(document).ready(function(){
    $( "select" ).change(function(){
    	var f = $('#survey-form').serialize();
    // var q1 = $( "[name='question_1'] :selected").text();
    // var q2 = $( "[name='question_2'] :selected").text();
    // var q9 = $( "[name='question_9'] :selected").text();
    // var q10 = $( "[name='question_10'] :selected").text();
    // var q13 = $( "[name='question_13'] :selected").text();
    // var q14 = $( "[name='question_14'] :selected").text();
    // var q15 = $( "[name='question_15'] :selected").text();
    // var q16 = $( "[name='question_16'] :selected").text();
    // var q17 = $( "[name='question_17'] :selected").text();

    $.ajax({
                url: "{% url 'get_car_count' %}",
                type: "post",
                data: f,
                success: function(data) {
                    alert(data);
                },
                error: function(data) { 
                	$("#survey-extras").css({"position": "fixed", "float": "right","top": "20%","background-color": "yellow", "width": "20%"});
                	 
                	$("#survey-extras").html("<p>Got an error dude</p>");
                }
            });
    }); 

})
