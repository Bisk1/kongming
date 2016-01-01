var checkAndUpdateTranslationsForm = function(source_word) {
    $.ajax({
        url: wordsTranslationsApi,
        type: 'POST',
        dataType: "json",
        data: {
            operation: 'get_translations',
            source_language: getSourceLanguage(),
            source_word : source_word,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            TranslationsApi.updateTranslations(data.translations);
        },
        error: function(xhr, errmsg, err) {
            $('#error_box').html(xhr.status + ": " + xhr.responseText).show();
        }
    });
};


$(document).ready(function() {

    WordInput.registerOnSelectCallback(checkAndUpdateTranslationsForm);

    $("#source_word").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm($("#source_word").val());
        }
    });

});