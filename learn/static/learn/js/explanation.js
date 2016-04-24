var ExplanationExerciseController = (function () {
    return {
        prepare: function (json) {
            $('#exercise-container').html(json.html);
            $('#check').hide();
            $('#next').html('Next').show();
        }
    };

}());
