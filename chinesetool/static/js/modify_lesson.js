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

            },
        });
    });
