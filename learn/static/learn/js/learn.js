/*global window */

var LessonController = (function () {
    var lc = {};

    var exerciseControllers = {
        choice: ChoiceExerciseController,
        typing: TypingExerciseController,
        explanation: ExplanationExerciseController,
        listening: ListeningExerciseController
    };

    lc.updateStatusIcons = function (success) {
        if (success) {
            $("#status-icons-container").append('<i style="color: green" class="icon-ok"></i>');
        } else {
            $("#status-icons-container").append('<i style="color: red" class="icon-remove">');
        }
    };

    lc.updateProgressbar = function (exercisesFinished) {
        var totalExercises = $('#total_exercises_number').val();
        var coverage = (100 * exercisesFinished / totalExercises) + "%";
        $('#progress-bar')
            .attr('aria-valuenow', coverage)
            .width(coverage)
            .text(exercisesFinished + " / " + totalExercises);
    };

    /**
     * Handle the status of exercise (positive or negative)
     */
    lc.handleExerciseStatus = function (success) {
        if (success) {
            $('#positive_status').show();
            $('#negative_status').hide();
        } else {
            $('#negative_status').show();
            $('#positive_status').hide();
        }
        lc.updateStatusIcons(success);
    };

    /**
     * Move the exercise from json response to appropriate HTML divs
     * and clean old data in divs
     * @param json JSON response
     */
    lc.prepareExercise = function (json) {
        switch (json.exercise_type) {
        case ('typing'):
            exerciseControllers.typing.prepare(json, lc);
            break;
        case ('explanation'):
            exerciseControllers.explanation.prepare(json);
            break;
        case ('choice'):
            exerciseControllers.choice.prepare(json, lc);
            break;
        case ('listening'):
            exerciseControllers.listening.prepare(json, lc);
            break;
        }
    };

    /**
     * Update screen after checking exercise
     */
    lc.handleLessonCheckResponse = function (json) {
        lc.handleExerciseStatus(json.success);
        $('#fails').html(json.fails);
        $('#status').show();
        $('#next').html('Next').show();
    };

    /**
     * Check user's input to the exercise
     * @param proposition user's input - proposed answer
     * @param handleExerciseCheckResponse function to be called after checking,
     * specific to the exercise (e.g. show the right answer)
     */
    lc.checkExercise = function (proposition, handleExerciseCheckResponse) {
        $.ajax({
            url: window.location.href,
            type: 'POST',
            dataType: 'json',
            data: {
                operation: 'check',
                lesson_action_id: $('#lesson_action_id').val(),
                proposition: proposition,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (json) {
                lc.handleLessonCheckResponse(json);
                handleExerciseCheckResponse(json);
            }
        });
    };

    /**
     * Prepare screen for next exercise or final summary
     * @param json JSON data to prepare exercises
     */
    lc.handleLessonPrepare = function (json) {
        $('#positive_status').hide();
        $('#negative_status').hide();
        if (json.final) { // if true there is no more exercises - show final screen
            $('#exercise-container').remove();
            $('#final').show();
        } else {
            lc.prepareExercise(json);
        }
        lc.updateProgressbar(json.current_exercise_number);
    };

    return lc;
}());


$(document).ready(function () {
    var lessonController = LessonController;
    $('#next').click(function () {
        $('#next').hide();
        $.ajax({
            url: window.location.href,
            type: 'POST',
            dataType: 'json',
            data: {
                operation: 'prepare',
                lesson_action_id: $('#lesson_action_id').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (json) {
                lessonController.handleLessonPrepare(json);
            }
        });
    });
    // Enter key press clicks the current visible button
    $(document).keypress(function(e){
        if(e.which == 13){
            clickFirstVisible(['#next', '#check', '#to-lesson-map']);
        }
    });

    // suppress any attempts to submit a form
    $('form').submit(function () {
        return false;
    });
});

var clickFirstVisible = function(elementsIds) {
    for (var i = 0; i < elementsIds.length; i++) {
        var element = $(elementsIds[i]);
        if (!element.is(':hidden')) {
            element.click(); // does not work with 'a' element
            if (element.is('a')) {
                document.getElementById(element.attr('id')).click();
            }
            return;
        }
    }

};