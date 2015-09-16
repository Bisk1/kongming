var TypingExerciseController = (function () {
    /**
     * Switch Chinese input feature -
     * @param active if true - then input box works as Chinese characters input,
     * otherwise as normal input
     */
    var toggleChineseInput = function (active) {
        if (active) {
            $('#proposition').chineseInput({
                debug: false, // print debug messages
                input: {
                    initial: 'simplified', // or 'traditional'
                    allowChange: false // allow transition between traditional and simplified
                },
                active: true // whether or not the plugin should be active by default
            });
        } else {
            $('#proposition').unbind(); // remove all events from element
        }
    };

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

    return {
        prepare: function (json, lessonController) {
            $('#correct').hide();
            $('#typing_text').html(json.text);
            $('#proposition').val('').show();
            $('#bad-proposition').hide();
            $('#check').show();
            switch (json.language) {
            case ('pl'):
                toggleChineseInput(true);
                break;
            case ('zh'):
                toggleChineseInput(false);
                break;
            }
            registerCheckEvent(lessonController);
            $('#typing_exercise').show();
        }
    };

}());
