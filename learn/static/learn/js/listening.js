var ListeningExerciseController = (function () {

    var handleCheckResponse = function (json) {
        $('#proposition').hide();
        $('#check').hide();
        $('#correct').html(json.text).show();
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

    // Space key is alternative method to play the audio
    var addSpaceHandler = function() {
        $(document).keypress(function(e){
            if(e.which == 32){
                audio = document.getElementById('listening_audio');
                audio.play();
                return false; // this prevents scrolling down
            }
        });
    };

    return {
        prepare: function (json, lessonController) {
            $('#exercise-container').html(json.html);
            $('#check').show();
            toggleChineseInput(true);
            registerCheckEvent(lessonController);
            addSpaceHandler();
            focusCursorOnInput();
        }
    };

}());
