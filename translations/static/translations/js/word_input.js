var getSourceLanguage = function() {
    return $("#id_source_language").val();
};

var WordInput = (function() {
    var wi = {};

    var onSelectCallbacks = [];

    wi.init = (function() {
        $("#id_source_word" ).autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: Django.url("translations：words_translations_api"),
                    type: 'POST',
                    dataType: "json",
                    data: {
                        operation: 'get_matches',
                        source_language: getSourceLanguage(),
                        source_word : request.term,
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
                onSelectCallbacks.forEach(function(callback) {
                    callback(ui.item.value);
                });
            }
        });
    });


    wi.registerOnSelectCallback = (function(new_callback) {
        onSelectCallbacks.push(new_callback);
    });

    return wi;

}());

$(document).ready(function() {
    WordInput.init();
});