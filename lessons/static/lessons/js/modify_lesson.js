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


$(document).on('click', '#update', function() {
    var topic = $("#topic").val();
    var exercises_number = $("#exercises_number").val();
    var requirement = $("#requirement option:selected").val();

    var url = $(this).attr("action");
    var formData = {};
    formData["topic"] = topic;
    formData["exercises_number"] = exercises_number;
    formData["requirement"] = requirement;

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
