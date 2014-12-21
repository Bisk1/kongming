$(document).ready(function() {
    $("#check").click(function() {
            var proposition = $("#proposition").val();
            var lesson_id = $("#lesson_id").val();
            $.ajax({
                url : "/translate_word/",
                type : "POST",
                dataType: "json",
                data : {
                    proposition : proposition,
                    lesson_id : lesson_id,
                    csrfmiddlewaretoken: document.getElementById("csrf_token").value
                    },
                    success : function(json) {
                            $('#proposition').hide();
                            $('#check').hide();
                            $('#next').show();
                            $('#next').html("Continue");
                            $('#result').show();
                            $('#correct').show();
                            $('#total_exercises_number').show();
                            $('#fails').show();
                            $('#result').html("Wynik: "+json.success);
                            $('#correct').html("Poprawne haslo: "+json.correct_word);
                            $('#current_exercise_number').html("Numer slowka: "+json.current_exercise_number);
                            $('#total_exercises_number').html("Liczba wszystkich slow: "+json.total_exercises_number);
                            $('#total_number').html("Numer slowka: "+json.current_exercise_number);
                            $('#fails').html("Nieprawidlowe odpowiedzi: "+json.fails);
                            $('h1').html(json.word_to_display);
                    },
                    error : function(xhr,errmsg,err) {
                        $('#result').show();
                        $('#result').html((xhr.status + ": " + xhr.responseText));
                    }
            });
            return false;
    });

    $("#next").click(function() {
            var lesson_id = $("#lesson_id").val();
            $.ajax({
                url : "/translate_word/",
                type : "POST",
                dataType: "json",
                data : {
                    lesson_id : lesson_id,
                    csrfmiddlewaretoken: document.getElementById("csrf_token").value
                    },


                    success : function(json) {
                        $('#next').hide();
                        $('#correct').hide();
                        $('#fails').show();
                        $('#result').hide();
                        $('#proposition').val('');
                        if (json.final) {
                            $('#proposition').hide();
                            $('#check').hide();
                            $('#return_link').show();
                            $('h1').html("To koniec!");
                        }
                        else {
                            $('#proposition').show();
                            $('#check').show();
                            $('#check').html("Check");
                            $('#current_exercise_number').show();
                            $('#current_exercise_number').html("Numer slowka: "+json.current_exercise_number);
                            $('#total_exercises_number').html("Liczba wszystkich slow: "+json.total_exercises_number);
                            $('h1').html(json.word_to_display);

                        }
                    },
                    error : function(xhr,errmsg,err) {
                        $('#result').show();
                        $('#result').html((xhr.status + ": " + xhr.responseText));
                    }
            });
            return false;
    })
});