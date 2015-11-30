var getSourceLanguage = function() {
    return $("#source_language").val();
};

var getTextsTranslationsApi = function() {
    return "/translations/texts_translations_api/";
}

var updateTranslationsTable = function(translations) {
    var translationsTable = $("#translations_table").find("tbody").empty();
        for (var i = 0; i < translations.length; i++) {
            translationsTable
                .insertPopulatedTextInput(translations[i]);
        }
};


var checkAndUpdateTranslationsForm = function(text_to_translate) {
    if(typeof text_to_translate == "undefined") {
        text_to_translate = $("#text_to_translate").val();
    }
    $.ajax({
        url: getTextsTranslationsApi(),
        type: 'POST',
        dataType: "json",
        data: {
            operation: "get_translations",
            source_language: getSourceLanguage(),
            source_text : text_to_translate,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
            $("#translations_header").html('text: '  + text_to_translate);
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
    var text_to_translate = $("#text_to_search").val();
    var translations = [];
    var isTranslationsChinese = (getSourceLanguage() == 'english');
    $("#translations_table tr").each(function() {
        if (isTranslationsChinese) {
            translations.push({text: $(this).find(":nth-child(2) > input").val()});
        } else {
            translations.push({text: $(this).find(":nth-child(2) > input").val()});
        }
    });
    $.ajax({
        url: getTextsTranslationsApi(),
        type: 'POST',
        dataType: "json",
        data: {
            operation: "set_translations",
            source_language: getSourceLanguage(),
            source_text : text_to_translate,
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
            .append('<input name="translations" value="' + translation + '">')
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

    $("#text_to_search").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm();
        }
    });

    $(document).on("click", "#remove", function() {
        ($(this)).parent().parent().remove();
    });

    $("#text_to_search" ).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: getTextsTranslationsApi(),
                type: 'POST',
                dataType: "json",
                data: {
                    operation: "get_matches",
                    source_language: getSourceLanguage(),
                    source_text : request.term,
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

    $("#save_button").click(function() {
        saveTranslations();
    })
});