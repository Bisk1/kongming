$(document).ready(function() {
    var check_words = function() {
            var word_to_search = $("#word_to_search").val();
            var source_language = $("#source_language").val();
            $.ajax({
                url : "/dictionary/" + source_language + "/",
                type : "POST",
                dataType: "json",
                data : {
                    word_to_search : word_to_search,
                    source_language: source_language,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                    },
                success : function(response) {
                    $("#translations_table > tbody").html("");
                    if (response['translations'].length == 0) {
                        $('#translations').hide();
                        $('#error_message').show();

                    } else {
                        $('#translations').show();
                        $('#error_message').hide();
                        for (i = 0; i < response['translations'].length; i++) {
                            $("#translations_table").find('tbody')
                                .append($('<tr>')
                                    .append($('<td>')
                                        .text(response['translations'][i])
                                        )
                                );
                        }
                    }
                }
            });
    };
    $("#search").click(check_words);
    $(document).keypress(function(e) {
        if (e.which == 13 && e.target.id=="word_to_search")
            check_words();
    });
});