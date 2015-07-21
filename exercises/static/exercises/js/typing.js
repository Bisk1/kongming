 var getAjaxTranslateTextUrl = function() {
     return $("#translate_text_url").text();
 };

var updateTranslationsTable = function(translations) {
    var translationsTable = $("#translations_table").find("tbody").empty();
        for (var i = 0; i < translations.length; i++) {
            translationsTable
                .insertPopulatedTextInput(translations[i]);
        }
};


var checkAndUpdateTranslationsForm = function(text_to_translate) {
    if(typeof text_to_translate == "undefined") {
        text_to_translate = $(".text_to_search").val();
    }
    $.ajax({
        url: getAjaxTranslateTextUrl(),
        type: 'POST',
        dataType: "json",
        data: {
            text_to_translate : text_to_translate,
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


$.fn.insertPopulatedTextInput = function(translation) {
    this
    .append($('<tr>')
        .append($('<td>')
            .append($('<label>')
                .append('Zdanie: ')
            )
            .append('<input name="translations" value="' + translation.text + '">')
        )
        .append($('<td>')
            .append('<button id="remove" class="btn btn-default">Remove</button>')
        )
    );
    return this;
};


$.fn.insertEmptyTextInput = function() {
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
        var lastTranslationGroup = $(".translation-group").last();
        var newTranslationGroup = lastTranslationGroup.clone().insertAfter(lastTranslationGroup);
        newTranslationGroup.find("input").val('');
        newTranslationGroup.find(".delete-button").show();
    });

    $('#edit').click(function() {
        checkAndUpdateTranslationsForm();
    });

    $(".text_to_search").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm();
        }
    });

    $(document).on("click", ".delete-button", function() {
        ($(this)).parent().remove();
    });

    $(".text_to_search" ).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: getAjaxTranslateTextUrl(),
                type: 'POST',
                dataType: "json",
                data: {
                    text_to_search : request.term,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function(data) {
                    response(data['matching_texts']);
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