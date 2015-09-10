function prepareTypingExercise(json) {
    $('#correct').hide();
    $('#typing_text').html(json.text);
    $('#proposition').val('').show();
    $('#bad-proposition').hide();
    $('#check').show();
    switch (json.language) {
        case('pl'):
            toggleChineseInput(true);
            break;
        case('zh'):
            toggleChineseInput(false);
            break;
    }
    activateTypingCheck();
    $('#typing_exercise').show();
}

/**
 * Switch Chinese input feature -
 * @param active if true - then input box works as Chinese characters input,
 * otherwise as normal input
 */
function toggleChineseInput(active) {
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
}

function handleTypingCheckResponse(json) {
    $('#proposition').hide();
    $('#check').hide();
    $('#correct').html(json.correct_translation).show();
    if (!json.success) {
        $('#bad-proposition').html($('#proposition').val()).show();
    }
}

function activateTypingCheck() {
    $('#check').click(function() {
        $(this).off('click');
        checkExercise($('#proposition').val(), handleTypingCheckResponse)
    });
}
