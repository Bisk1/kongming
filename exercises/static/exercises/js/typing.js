var getSourceLanguage = function() {
    return $("#id_source_language").find(":selected").val();
};

var getTranslateTextsServiceUrl = function() {
    return $("#texts_translations_api_url").text();
};

var updateTranslationsTable = function(translations) {
    var translationGroups = $("input[name^='translation_']").parent().parent();
    var translationGroupPattern = translationGroups.first().clone(); // for later cloning
    translationGroups.remove();
    for (var i = 0; i < translations.length; i++) {
        var predecessor = ($('.form-group')).last(); // append always to the last form-group
        var translationGroup = translationGroupPattern.cloneAndPopulateInputAndSetNumber(translations[i].text, i);
        predecessor.after(translationGroup);
    }
};

 $.fn.cloneAndEmptyInputAndSetNumber = function(number) {
    var newTranslationGroup = this.clone();
    newTranslationGroup.find("input")
        .val('')
        .attr("id", "id_translation_" + number)
        .attr("name", "translation_" + number);
    return newTranslationGroup;
 };

$.fn.cloneAndPopulateInputAndSetNumber = function(text, number) {
    var newTranslationGroup = this.clone();
    newTranslationGroup.find("input")
        .val(text)
        .attr("id", "id_translation_" + number)
        .attr("name", "translation_" + number);
    return newTranslationGroup;
};

var checkAndUpdateTranslationsForm = function(text_to_translate) {
    if(typeof text_to_translate == "undefined") {
        text_to_translate = $(".text_to_translate").val();
    }
    $.ajax({
        url: getTranslateTextsServiceUrl(),
        type: 'POST',
        dataType: "json",
        data: {
            operation: 'get_translations',
            text_to_translate : text_to_translate,
            source_language: getSourceLanguage(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            $("#translations_header").html('Tekst: '  + text_to_translate);
            updateTranslationsTable(data.translations);
            $('#add_translation_button').show();
        },
        error: function(xhr, errmsg, err) {
            $('#error_box').html(xhr.status + ": " + xhr.responseText).show();
        }
    });
};

$(document).ready(function() {

    $(document).on("click", "#add_translation_button", function() {
        var lastTranslationInput = $("input[name^='translation_']").last();
        var lastTranslationNumber = parseInt(lastTranslationInput.attr("id").replace("id_translation_", ""));
        var lastTranslationGroup = lastTranslationInput.parent().parent();
        lastTranslationGroup.cloneAndEmptyInputAndSetNumber(lastTranslationNumber + 1).insertAfter(lastTranslationGroup);
    });

    $('#edit').click(function() {
        checkAndUpdateTranslationsForm();
    });

    $(".text_to_translate").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm();
        }
    });

    $("input[name='text_to_translate']" ).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: getTranslateTextsServiceUrl(),
                type: 'POST',
                dataType: "json",
                data: {
                    operation: 'get_matches',
                    text_to_translate : request.term,
                    source_language: getSourceLanguage(),
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function(data) {
                    response(data['matches']);
                },
                error: function(xhr, errmsg, err) {
                    $('#error_box').html(xhr.status + ": " + xhr.responseText).show();
                }
            });
        },
        select: function(event, ui) {
            checkAndUpdateTranslationsForm(ui.item.value);
        }
    });

});