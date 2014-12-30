var exercise_type;

$(document).ready(function() {
    $("#check").click(function() {
            var proposition = $("#proposition").val();
            var lesson_id = $("#lesson_id").val();
            $.ajax({
                url : "/learn/" + lesson_id + "/",
                type : "POST",
                dataType: "json",
                data : {
                    proposition : proposition,
                    lesson_id : lesson_id,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                    },
                success : function(json) {
                        $('#proposition').hide();
                        $('#check').hide();
                        $('#next').show();
                        $('#next').html("Continue");
                        $('#result').show();

                        if (json.success) {
                            $('#positive_result').show();
                            $('#negative_result').hide();
                        } else {
                            $('#negative_result').show();
                            $('#positive_result').hide();
                        }

                        switch (exercise_type) {
                            case('word_zh'):
                            case('word_pl'):
                                $('#correct').html(json.correct_word);
                                break;
                            case('sentence_zh'):
                            case('sentence_pl'):
                                $('#correct').html(json.correct_sentence);
                                break;
                        }
                        $('#correct').show();
                        $('#result').show();
                        $('#current_exercise_number').html(json.current_exercise_number);
                        $('#fails').html(json.fails);
                },
                error : function(xhr,errmsg,err) {
                    $('#result').show();
                    $('#result').html((xhr.status + ": " + xhr.responseText));
                }
            });
    });

    $("#next").click(function() {
            var lesson_id = $("#lesson_id").val();
            $.ajax({
                url : "/learn/" + lesson_id + "/",
                type : "POST",
                dataType: "json",
                data : {
                    lesson_id : lesson_id,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                    },
                success : function(json) {
                    $('#next').hide();
                    $('#correct').hide();
                    $('#fails').show();
                    $('#result').hide();
                    $('#proposition').val('');
                    if (json.final) {
                        $('#check').hide();
                        $('#return_link').show();
                        $('#final').show();
                    }
                    else {
                        $('#proposition').show();
                        $('#check').show();
                        $('#check').html("Check");
                        $('#current_exercise_number').show();
                        $('#current_exercise_number').html(json.current_exercise_number);
                        exercise_type = json.exercise_type;
                        switch (exercise_type) {
                            case('word_zh'):
                            case('word_pl'):
                                $('#word_or_sentence').html(json.word);
                                break;
                            case('sentence_zh'):
                            case('sentence_pl'):
                                $('#word_or_sentence').html(json.sentence);
                                break;
                            case('explanation'):
                                $('#explanation_text').html(json.text);
                                $('#check').hide();
                                $('#next').show();
                                break;
                        }
                        switch (exercise_type) {
                            case('word_zh'):
                            case('word_pl'):
                            case('sentence_zh'):
                            case('sentence_pl'):
                                $('#word_or_sentence_exercise').show();
                                $('#explanation_exercise').hide();
                                break;
                            case('explanation'):
                                $('#word_or_sentence_exercise').hide();
                                $('#explanation_exercise').show();
                                break;
                        }
                    }
                },
                error : function(xhr,errmsg,err) {
                    $('#result').show();
                    $('#result').html((xhr.status + ": " + xhr.responseText));
                }
            });
    })
});