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
            $('#choice_text_to_translate').html(json.text);
            $('#choice1').val(json.choices[0]);
            $('#choice2').val(json.choices[1]);
            $('#choice3').val(json.choices[2]);
            $('#choice4').val(json.choices[3]);

            $('.choice').removeClass('btn-primary').removeClass('btn-success').removeClass('btn-danger');
            $('#choice_exercise').show();
            registerCheckEvent(lessonController);
        }
    };

}());
