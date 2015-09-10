function prepareChoiceExercise(json) {
    $('#choice_text_to_translate').html(json.text);
    $('#choice1').val(json.choices[0]);
    $('#choice2').val(json.choices[1]);
    $('#choice3').val(json.choices[2]);
    $('#choice4').val(json.choices[3]);

    $('.choice').removeClass('selected-choice').css("color", "");
    $('#choice_exercise').show();
    activateChoiceCheck();
}

function activateChoiceCheck() {
    $('.choice').click(function() {
        $(this).off('click');
        $(this).addClass('selected-choice');
        checkExercise($(this).val(), handleChoiceExerciseResponse)
    });
}

function handleChoiceExerciseResponse(json) {
    var correctButton = $('.choice[value=' + json.correct_translation + ']');
    var selectedButton = $('.selected-choice');
    correctButton.css('color', 'green');
    if (selectedButton.val() != correctButton.val()) {
        selectedButton.css('color', 'red');
    }
}