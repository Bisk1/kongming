var exercise_type;

// Handles the result of user action
function handleResult(success) {
    if (success) {
        $('#positive_result').show();
        $('#negative_result').hide();
    } else {
        $('#negative_result').show();
        $('#positive_result').hide();
    }
}

/**
 * Moves the exercise content from json response to appropriate HTML divs
 * @param exercise_type exercise type
 * @param json JSON response
 */
function showExerciseContent(exercise_type, json) {
    switch (exercise_type) {
        case('word_zh'):
        case('word_pl'):
            $('#word_or_sentence').html(json.word);
            break;
        case('sentence_zh'):
        case('sentence_pl'):
            $('#word_or_sentence').html(json.sentence);
            break;
        case('explanation_image'):
        case('explanation'):
            $('#explanation_text').html(json.text);
            break;
    }
}

/**
 * Displays the div for the specified exercise
 * @param exercise_type exercise type
 */
function showDivForExerciseType(exercise_type) {
    switch (exercise_type) {
        case('word_zh'):
        case('word_pl'):
        case('sentence_zh'):
        case('sentence_pl'):
            $('#word_or_sentence_exercise').show();
            $('#explanation_exercise').hide();
            break;
        case('explanation'):
            $('#word_or_sentence_exercise').hide();
            $('#explanation_exercise').show();
            break;
    }
}

/**
 * Switches Chinese input feature -
 * @param active if true than input box works as Chinese characters input, otherwise as normal input
 */
function toggleChineseInput(active) {
    if (active) {
        $("#proposition").chineseInput({
            debug: false, // print debug messages
            input: {
                initial: 'simplified', // or 'traditional'
                allowChange: false // allow transition between traditional and simplified
            },
            active: true // whether or not the plugin should be active by default
        });
    } else {
        $("#proposition").unbind(); // remove all events from element
    }
}
$(document).ready(function() {
    $("#check").click(function() {
        var proposition = $("#proposition").val();
        var lesson_id = $("#lesson_id").val();
        $.ajax({
            url : window.location.href,
            type : "POST",
            dataType: "json",
            data : {
                proposition : proposition,
                lesson_id : lesson_id,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
            success : function(json) {
                $('#proposition').hide();
                $('#check').hide();
                $('#next').html("Continue").show();
                $('#result').show();
                handleResult(json.success);
                switch (exercise_type) {
                    case('word_zh'):
                    case('word_pl'):
                        $('#correct').html(json.correct_word).show();
                        break;
                    case('sentence_zh'):
                    case('sentence_pl'):
                        $('#correct').html(json.correct_sentence).show();
                        break;
                }
                $('#current_exercise_number').html(json.current_exercise_number);
                $('#fails').html(json.fails);
            },
            error : function(xhr,errmsg,err) {
                $('#result').html((xhr.status + ": " + xhr.responseText)).show();
            }
        });
    });

    $("#next").click(function() {
        var lesson_id = $("#lesson_id").val();
        $.ajax({
            url : window.location.href,
            type : "POST",
            dataType: "json",
            data : {
                lesson_id : lesson_id,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
            success : function(json) {
                $(this).hide();
                $('#correct').hide();
                $('#fails').show();
                $('#result').hide();
                if (json.final) {
                    $('#check').hide();
                    $('#return_link').show();
                    $('#final').show();
                }
                else {
                    $('#current_exercise_number').html(json.current_exercise_number).show();
                    exercise_type = json.exercise_type;
                    showExerciseContent(exercise_type, json);
                    showDivForExerciseType(exercise_type);
                    if (exercise_type == 'explanation' || exercise_type == 'explanation_image') {
                        // explanation exercise is not checked - user goes to next exercise after reading
                        $('#check').hide();
                        $('#next').html("Continue").show();
                    } else {
                        $('#proposition').val('').show();
                        $('#check').html("Check").show();
                    }
                    switch (exercise_type) {
                        case('word_pl'):
                        case('sentence_pl'):
                            toggleChineseInput(true);
                            break;
                        case('word_zh'):
                        case('sentence_zh'):
                            toggleChineseInput(false);
                            break;
                    }
                }
            },
            error : function(xhr,errmsg,err) {
                $('#result').html((xhr.status + ": " + xhr.responseText)).show();
            }
        });
    })
});