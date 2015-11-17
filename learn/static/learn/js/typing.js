var TypingExerciseController = (function () {

    var handleCheckResponse = function (json) {
        $('#proposition').hide();
        $('#check').hide();
        $('#correct').html(json.correct_translation).show();
        if (!json.success) {
            $('#bad-proposition').html($('#proposition').val()).show();
        }
    };

    var registerCheckEvent = function (lessonController) {
        $('#check').click(function () {
            $(this).off('click');
            lessonController.checkExercise($('#proposition').val(), handleCheckResponse);
        });
    };

    var focusCursorOnInput = function() {
        $('#proposition').focus();
    };

    return {
        prepare: function (json, lessonController) {
            $('#exercise-container').html(json.html);
            $('#check').show();
            switch (json.language) {
            case ('en'):
                toggleChineseInput(true);
                break;
            case ('zh'):
                toggleChineseInput(false);
                break;
            }
            registerCheckEvent(lessonController);
            focusCursorOnInput();
        }
    };

}());
