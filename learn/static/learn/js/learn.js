var exercise_type;
var language;

// Handles the result of user action
function handleResult(success) {
    if (success) {
        $('#positive_result').show();
        $('#negative_result').hide();
    } else {
        $('#negative_result').show();
        $('#positive_result').hide();
    }
    updateResultsIcons(success);
}

function updateResultsIcons(success) {
    if (success) {
        $("#results-icons-container").append('<i style="color: green" class="icon-ok"></i>');
    } else {
        $("#results-icons-container").append('<i style="color: red" class="icon-minus-sign">');
    }
}

/**
 * Moves the exercise content from json response to appropriate HTML divs
 * @param exercise_type exercise type
 * @param json JSON response
 */
function showExerciseContent(exercise_type, json) {
    switch (exercise_type) {
        case('typing'):
            $('#typing_text').html(json.text);
            break;
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
    $('#explanation_exercise').hide();
    $('#typing_exercise').hide();
    switch (exercise_type) {
        case('typing'):
            $('#typing_exercise').show();
            break;
        case('explanation'):
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

function updateProgressbar(exercisesFinished) {
    var totalExercises = $('#total_exercises_number').val();
    var coverage = (100 * exercisesFinished/totalExercises) + "%";
     $('#progress-bar').attr('aria-valuenow', coverage)
                       .width(coverage)
                        .text(exercisesFinished + " / " + totalExercises);
}

$(document).ready(function() {
    $("#check").click(function() {
        $.ajax({
            url : window.location.href,
            type : "POST",
            dataType: "json",
            data : {
                proposition : $("#proposition").val(),
                lesson_action_id: $("#lesson_action_id").val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
            success : function(json) {
                $('#proposition').hide();
                $('#check').hide();
                $('#next').html("Dalej").show();
                $('#result').show();
                handleResult(json.success);
                switch (exercise_type) {
                    case('text_zh'):
                    case('text_pl'):
                        $('#correct').html(json.correct_text).show();
                        break;
                }
                $('#current_exercise_number').html(json.current_exercise_number);
                $('#fails').html(json.fails);
                updateProgressbar(json.current_exercise_number);

            },
            error : function(xhr,errmsg,err) {
                $('#result').html((xhr.status + ": " + xhr.responseText)).show();
            }
        });
    });

    $("#next").click(function() {
        $.ajax({
            url : window.location.href,
            type : "POST",
            dataType: "json",
            data : {
                lesson_action_id: $("#lesson_action_id").val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
            success : function(json) {
                $(this).hide();
                $('#correct').hide();
                $('#fails').show();
                $('#result').hide();
                if (json.final) {
                    $('#check').hide();
                    $('#to-lesson-map').show();
                    $('#final').show();
                    $('#next').hide();
                    showDivForExerciseType();
                }
                else {
                    $('#current_exercise_number').html(json.current_exercise_number).show();
                    exercise_type = json.exercise_type;
                    language = json.language;
                    showExerciseContent(exercise_type, json);
                    showDivForExerciseType(exercise_type);
                    if (exercise_type == 'explanation') {
                        // explanation exercise is not checked - user goes to next exercise after reading
                        $('#check').hide();
                        $('#next').html("Continue").show();
                    } else {
                        $('#next').hide();
                        $('#proposition').val('').show();
                        $('#check').html("Check").show();
                        switch (language) {
                            case('pl'):
                                toggleChineseInput(true);
                                break;
                            case('zh'):
                                toggleChineseInput(false);
                                break;
                        }
                    }
                }
                updateProgressbar(json.current_exercise_number);
            },
            error : function(xhr,errmsg,err) {
                $('#result').html((xhr.status + ": " + xhr.responseText)).show();
            }
        });
    })
});