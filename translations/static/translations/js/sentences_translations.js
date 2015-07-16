var getSourceLanguage = function() {
    return $("#source_language").val();
};

var updateTranslationsTable = function(translations) {
    var translationsTable = $("#translations_table").find("tbody").empty();
        for (var i = 0; i < translations.length; i++) {
            translationsTable
                .insertPopulatedTextInput(translations[i]);
        }
};


var checkAndUpdateTranslationsForm = function(sentence_to_translate) {
    if(typeof sentence_to_translate == "undefined") {
        sentence_to_translate = $("#sentence_to_search").val();
    }
    $.ajax({
        url: window.location.href,
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

var saveTranslations = function() {
    $("#save_message").html('Saving...');
    var sentence_to_translate = $("#sentence_to_search").val();
    var translations = [];
    var isTranslationsChinese = (getSourceLanguage() == 'polish');
    $("#translations_table tr").each(function() {
        if (isTranslationsChinese) {
            translations.push({sentence: $(this).find(":nth-child(2) > input").val()});
        } else {
            translations.push({sentence: $(this).find(":nth-child(2) > input").val()});
        }
    });
    $.ajax({
        url: window.location.href,
        type: 'POST',
        dataType: "json",
        data: {
            sentence_to_translate : sentence_to_translate,
            translations : JSON.stringify(translations),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            $("#save_message").html('Saved!');
        },
        error: function(xhr, errmsg, err) {
            $('#error_box').html(xhr.status + ": " + xhr.responseText).show();
        }
    });
};


$.fn.insertPopulatedTextInput = function(translation) {
    this
    .append($('<tr>')
        .append($('<td>')
            .append('Translation: ')
        )
        .append($('<td>')
            .append('<input name="translations" value="' + translation.sentence + '">')
        )
        .append($('<td>')
            .append('<button id="remove">Remove</button>')
        )
    );
    return this;
};


$.fn.insertEmptyTextInput = function() {
    this
    .append($('<tr>')
        .append($('<td>')
            .append('Translation: ')
        )
        .append($('<td>')
            .append('<input name="translations"/>')
        )
        .append($('<td>')
            .append('<button id="remove">Remove</button>')
        )
    );
    return this;
};

$(document).ready(function() {

    $(document).on("click", "#add_translation_button", function() {
        $("#translations_table").find("tbody")
        .insertEmptyTextInput();
    });

    $('#edit').click(function() {
        checkAndUpdateTranslationsForm();
    });

    $("#sentence_to_search").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm();
        }
    });

    $(document).on("click", "#remove", function() {
        ($(this)).parent().parent().remove();
    });

    $("#sentence_to_search" ).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: window.location.href,
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

    $("#save_button").click(function() {
        saveTranslations();
    })
});