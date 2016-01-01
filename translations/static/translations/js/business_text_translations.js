var checkAndUpdateTranslationsForm = function(source_text) {
    $.ajax({
        url: textsTranslationsApi,
        type: 'POST',
        dataType: "json",
        data: {
            operation: "get_translations",
            source_language: getSourceLanguage(),
            source_text : source_text,
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

    BusinessTextInput.registerOnSelectCallback(checkAndUpdateTranslationsForm);

    $("#source_text").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm($("#source_text").val());
        }
    });

});