var ChoiceExerciseController = (function () {
    var handleCheckResponse = function (json) {
        var correctButton = $('.choice[value="' + json.correct_translation + '"]');
        var selectedButton = $('.btn-primary');
        correctButton.removeClass('btn-primary').addClass('btn-success');
        if (selectedButton.val() !== correctButton.val()) {
            selectedButton.removeClass('btn-primary').addClass('btn-danger');
        }
    };

    var registerCheckEvent = function (lessonController) {
        $('.choice').click(function () {
            $('.choice').off('click');
            $(this).addClass('btn-primary');
            lessonController.checkExercise($(this).val(), handleCheckResponse);
        });
    };

    return {
        prepare: function (json, lessonController) {
            $('#exercise-container').html(json.html);
            registerCheckEvent(lessonController);
        }
    };

}());
