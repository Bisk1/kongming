 var getAjaxTranslateTextUrl = function() {
     return $("#translate_text_url").text();
 };

 var emptyTranslationGroup;

var updateTranslationsTable = function(translations) {
    var newTranslationGroup = ($(".translation-group")).first().cloneAndEmptyInputs;
    $(".translation-group").remove();
    for (var i = 0; i < translations.length; i++) {
        translationsTable
            .insertPopulatedTextInput(translations[i]);
    }
};

 $.fn.cloneAndEmptyInputs = function() {
    var newTranslationGroup = this.clone();
    newTranslationGroup.find("input").val('');
    return newTranslationGroup;
 };

$.fn.showDeleteButton = function() {
    this.find(".delete-button").show();
    return this;
};

var checkAndUpdateTranslationsForm = function(text_to_translate) {
    if(typeof text_to_translate == "undefined") {
        text_to_translate = $(".text_to_translate").val();
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


$(document).ready(function() {


    $(document).on("click", "#add_translation_button", function() {
        var lastTranslationGroup = $(".translation-group").last();
        lastTranslationGroup.cloneAndEmptyInputs().showDeleteButton().insertAfter(lastTranslationGroup);
    });

    $('#edit').click(function() {
        checkAndUpdateTranslationsForm();
    });

    $(".text_to_translate").keypress(function(e) {
        if (e.which == 13) {
            checkAndUpdateTranslationsForm();
        }
    });

    $(document).on("click", ".delete-button", function() {
        ($(this)).parent().remove();
    });

    $(".text_to_translate" ).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: getAjaxTranslateTextUrl(),
                type: 'POST',
                dataType: "json",
                data: {
                    text_to_translate : request.term,
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