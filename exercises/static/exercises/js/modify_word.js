var getSourceLanguage = function() {
    return $("#source_language").text();
};

var updateTranslationsTable = function(translations) {
    var translationsTable = $("#translations_table").find("tbody").empty();
        for (var i = 0; i < translations.length; i++) {
            translationsTable
                .insertWordInputWithWord(translations[i]);
        }
};


var checkAndUpdateTranslationsForm = function(word_to_translate) {
    if(typeof word_to_translate == "undefined") {
        word_to_translate = $("#word_to_search").val();
    }
    $.ajax({
        url: window.location.href,
        type: 'POST',
        dataType: "json",
        data: {
            word_to_translate : word_to_translate,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            $("#translations_header").html('Word: '  + word_to_translate);
            updateTranslationsTable(data.translations);
            $('#add_translation_button').show();
        },
        error: function(xhr, errmsg, err) {
            $('#error_box').html(xhr.status + ": " + xhr.responseText).show();
        }
    });
};


$.fn.insertWordInputWithWord = function(translation) {
    if (getSourceLanguage() == 'chinese') {
        this
        .append($('<tr>')
            .append($('<td>')
                .append($('<label>')
                    .append('Tłumaczenie: ')
                )
                    .append('<input name="translations" value="' + translation.word + '">')
            )
            .append($('<td>')
                .append('<button id="remove" class="btn btn-default">Remove</button>')
            )
        )
    } else {
        this
        .append($('<tr>')
            .append($('<td>')
                .append($('<label>')
                    .append('Tłumaczenie: ')
                )
                .append('<input name="translations" value="' + translation.word + '">')
            )
            .append($('<td>')
                .append('Pinyin')
            )
            .append($('<td>')
                .append('<input name="pinyin" value="' + translation.pinyin + '">')
            )
            .append($('<td>')
                .append('<button id="remove" class="btn btn-default">Remove</button>')
            )
        )
    }
    return this;
};


$.fn.insertWordInput = function() {
    if (getSourceLanguage() == 'chinese') {
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
        )
    } else {
        this
        .append($('<tr>')
            .append($('<td>')
                .append($('<label>')
                    .append('Tłumaczenie: ')
                )
                .append('\n<input name="translations"/>\n')
                .append($('<label>')
                    .append('Pinyin: ')
                )
                .append('\n<input name="pinyin"/>')
            )
            .append($('<td>')
                .append('<button id="remove" class="btn btn-default">Remove</button>')
            )
        )
    }
    return this;
};

$(document).ready(function() {

    $(document).on("click", "#add_translation_button", function() {
        $("#translations_table").find("tbody")
        .insertWordInput();
    });

    $(".word_to_search").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm();
        }
    });

    $(document).on("click", "#remove", function() {
        ($(this)).parent().parent().remove();
    });

    $(".word_to_search" ).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: window.location.href,
                type: 'POST',
                dataType: "json",
                data: {
                    word_to_search : request.term,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function(data) {
                    response(data['matching_words']);
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