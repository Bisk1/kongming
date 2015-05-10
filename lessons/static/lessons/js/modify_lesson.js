// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({

    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$("#save").click(function(){
        var url = $("#adding_exercise").attr("action");
        var lesson = $("#adding_exercise").attr("lesson");
        var formData = {};
        $("#adding_exercise").find("input[name]").each(function (index, node) {
            formData[node.name] = node.value;
        });
        $("#adding_exercise").find("textarea[name]").each(function (index, node) {
            formData[node.name] = node.value;
        });
        console.log("my object: %o", formData);
       $.ajax({
            url : url,
            type: "POST",
            data : formData,
            success: function() {
                var link = $("#exercises").attr("link");
                $("#exercises").load(link);

            }
        });
    });
        $(".delete").click(function(){
            var url = $(this).attr("action");
            var exercise_id = $(this).attr("value");
            var formData = {};
            formData["exercise_to_remove"] = exercise_id;
            console.log("my object: %o", formData);

       $.ajax({
            url : url,
            type: "POST",
            data : formData,
            success: function() {
                var link = $("#exercises").attr("link");
                $("#exercises").load(link);

            }
       });
    });
    $(function(){
       $("#menu").change(function(){
           $("#content").load($("#menu option:selected").attr('addr'));
               return false;
       });
    });

    $(function(){
       $("#add").click(function(){
           $("#add_exercise").toggle();
           $("#content").load($("#menu option:selected").attr('addr'));

       });
    });
    $(function(){
        $("#update").click(function(){
            var topic = $("#topic").val();
            var exercises_number = $("#exercises_number").val();
            var new_requirement = $("#new_requirement option:selected").val();


           var url = $(this).attr("action");
            var formData = {};
            formData["topic"] = topic
            formData["exercises_number"] = exercises_number
            formData["new_requirement"] = new_requirement

            $.ajax({
                url : url,
                type: "POST",
                data : formData,
                success: function() {
                    $("#updated").show();
                    $("#update").css("background-color", "green");
                }
            });

       });
    });


    //
    //<input type="text" id="topic" name="topic" value="{{ lesson.topic }}"/>
    //<button action="{% url 'lessons:modify_lesson' lesson.id %}">Update</button>