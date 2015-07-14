 var getAjaxTranslateSentenceUrl = function() {
     return $("#translate_sentence_url").text();
 };

var updateTranslationsTable = function(translations) {
    var translationsTable = $("#translations_table").find("tbody").empty();
        for (var i = 0; i < translations.length; i++) {
            translationsTable
                .insertSentenceInputWithSentence(translations[i]);
        }
};


var checkAndUpdateTranslationsForm = function(sentence_to_translate) {
    if(typeof sentence_to_translate == "undefined") {
        sentence_to_translate = $(".sentence_to_search").val();
    }
    $.ajax({
        url: getAjaxTranslateSentenceUrl(),
        type: 'POST',
        dataType: "json",
        data: {
            sentence_to_translate : sentence_to_translate,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            $("#translations_header").html('Sentence: '  + sentence_to_translate);
            updateTranslationsTable(data.translations);
            $('#add_translation_button').show();
        },
        error: function(xhr, errmsg, err) {
            $('#error_box').html(xhr.status + ": " + xhr.responseText).show();
        }
    });
};


$.fn.insertSentenceInputWithSentence = function(translation) {
    this
    .append($('<tr>')
        .append($('<td>')
            .append($('<label>')
                .append('Zdanie: ')
            )
            .append('<input name="translations" value="' + translation.sentence + '">')
        )
        .append($('<td>')
            .append('<button id="remove" class="btn btn-default">Remove</button>')
        )
    );
    return this;
};


$.fn.insertSentenceInput = function() {
    this
    .append($('<tr>')
        .append($('<td>')
            .append($('<label>')
                .append('Tłumaczenie: ')
            )
            .append('\n<input name="translations"/>')

        )
        .append($('<td>')
            .append('<button id="remove" class="btn btn-default">Remove</button>')
        )
    );
    return this;
};

$(document).ready(function() {

    $(document).on("click", "#add_translation_button", function() {
        $("#translations_table").find("tbody")
        .insertSentenceInput();
    });

    $('#edit').click(function() {
        checkAndUpdateTranslationsForm();
    });

    $(".sentence_to_search").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm();
        }
    });

    $(document).on("click", "#remove", function() {
        ($(this)).parent().parent().remove();
    });

    $(".sentence_to_search" ).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: getAjaxTranslateSentenceUrl(),
                type: 'POST',
                dataType: "json",
                data: {
                    sentence_to_search : request.term,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function(data) {
                    response(data['matching_sentences']);
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