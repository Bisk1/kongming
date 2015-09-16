var ExplanationExerciseController = (function () {
    return {
        prepare: function (json) {
            $('#explanation_text').html(json.text);
            $('#explanation_exercise').show();
            $('#check').hide();
            $('#next').html('Dalej').show();
        }
    };

}());
