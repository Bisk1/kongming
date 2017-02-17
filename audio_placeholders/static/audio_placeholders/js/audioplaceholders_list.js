$(document).ready(function() {
    setupRecorderButtons();
    $('#cleanup_audios').click(function() {
        $.ajax({
            url: Django.url("audio_placeholders:cleanup_audios"),
            type: 'GET',
            success: function (json) {
                console.log("Removed " + json.removed_audios + " audios");
            },
            error: function(error) {
                console.log(error);
            }
        });
    })
});

function setupRecorderButtons() {
    $('.record-btn').click(function() {
        $this = $(this);
        $this.hide();
        $('div[placeholder-id=' + this.id + ']').recorder(function(blob) {
            var file = new File([blob], guid() + '.wav');
            fillPlaceholder(file, $this[0].id, $this);
            $this.show();
        });
    });
}

function fillPlaceholder(file, placeholder_id, button) {
    var formData = new FormData();
    formData.append("file", file);
    formData.append("placeholder_id", placeholder_id);
    $.ajax({
        url: Django.url("audio_placeholders:fill_placeholder"),
        type: 'POST',
        dataType: 'json',
        data: formData,
        success: function (json) {
            button.closest('tr').remove(); // remove row with completed placeholder
        },
        error: function(error) {
            console.log(error);
        },
        cache: false,
        processData: false,
        contentType: false
    });
}