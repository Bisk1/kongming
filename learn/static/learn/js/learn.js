
/**
 * Handle the status of exercise (positive or negative)
 */
function handleExerciseStatus(success) {
    if (success) {
        $('#positive_status').show();
        $('#negative_status').hide();
    } else {
        $('#negative_status').show();
        $('#positive_status').hide();
    }
    updateStatusIcons(success);
}

function updateStatusIcons(success) {
    if (success) {
        $("#status-icons-container").append('<i style="color: green" class="icon-ok"></i>');
    } else {
        $("#status-icons-container").append('<i style="color: red" class="icon-remove">');
    }
}

function updateProgressbar(exercisesFinished) {
    var totalExercises = $('#total_exercises_number').val();
    var coverage = (100 * exercisesFinished/totalExercises) + "%";
     $('#progress-bar').attr('aria-valuenow', coverage)
                       .width(coverage)
                        .text(exercisesFinished + " / " + totalExercises);
}

/**
 * Move the exercise from json response to appropriate HTML divs
   and clean old data in divs
 * @param json JSON response
 */
function prepareExercise(json) {
    switch (json.exercise_type) {
        case('typing'):
            prepareTypingExercise(json);
            break;
        case('explanation'):
            prepareExplanationExercise(json);
            break;
        case('choice'):
            prepareChoiceExercise(json);
            break;
    }
}

/**
 * Hide all exercises' divs
 */
function hideAllExercisesContainers() {
    $('.exercise-type-container').hide();
}

/**
 * Update screen after checking exercise
 */
function handleLessonCheckResponse(json) {
    handleExerciseStatus(json.success);
    $('#fails').html(json.fails);
    $('#status').show();
    $('#next').html('Dalej').show();
}


/**
 * Check user's input to the exercise
 * @param proposition user's input - proposed answer
 * @param handleExerciseCheckResponse function to be called after checking,
 * specific to the exercise (e.g. show the right answer)
 */
function checkExercise(proposition, handleExerciseCheckResponse) {
    $.ajax({
        url : window.location.href,
        type : 'POST',
        dataType: 'json',
        data : {
            proposition : proposition,
            lesson_action_id: $('#lesson_action_id').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
        success : function(json) {
            handleLessonCheckResponse(json);
            handleExerciseCheckResponse(json);
        }
    });
}

/**
 * Prepare screen for next exercise or final summary
 * @param json JSON data to prepare exercises
 */
function handleLessonPrepare(json) {
        $('#positive_status').hide();
        $('#negative_status').hide();
        hideAllExercisesContainers();
    if (json.final) { // if true there is no more exercises - show final screen
        $('#final').show();
    }
    else {
        prepareExercise(json);
    }
    updateProgressbar(json.current_exercise_number);
}

$(document).ready(function() {
    $('#next').click(function() {
        $('#next').hide();
        $.ajax({
            url : window.location.href,
            type : 'POST',
            dataType: 'json',
            data : {
                lesson_action_id: $('#lesson_action_id').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
            success : function(json) {
                handleLessonPrepare(json);
            }
        });
    });

    // suppress any attempts to submit a form
    $('form').submit(function() {
      return false;
    })
});