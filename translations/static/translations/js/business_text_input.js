var getSourceLanguage = function() {
    return $("#id_source_language").val();
};

var BusinessTextInput = (function() {
    var bti = {};

    var onSelectCallbacks = [];

    bti.init = (function() {
        $("#id_source_text" ).autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: Django.url("translations:texts_translations_api"),
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
                onSelectCallbacks.forEach(function(callback) {
                    callback(ui.item.value);
                });
            }
        });
    });


    bti.registerOnSelectCallback = (function(new_callback) {
        onSelectCallbacks.push(new_callback);
    });

    return bti;

}());


$(document).ready(function() {
    BusinessTextInput.init();
});