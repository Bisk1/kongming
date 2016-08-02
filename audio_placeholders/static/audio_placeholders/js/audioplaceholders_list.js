$(document).ready(function() {
    setupRecorderButtons();
});

function setupRecorderButtons() {
    $('.record-btn').click(function() {
        $this = $(this);
        $this.hide();
        $('div[placeholder-id=' + this.id + ']').recorder(function(file){
            fillPlaceholder(file, this.id, this);
            $this.show();
        });
    });
}

function fillPlaceholder(file, placeholder_id, button) {
    $.ajax({
            url: Django.url("audio_placeholders:fill_placeholder"),
            type: 'POST',
            dataType: 'json',
            data: {
                file: file,
                placeholder_id: placeholder_id
            },
            success: function (json) {
                button.closest('tr').remove(); // remove row with completed placeholder
            },
            error: function(error) {
                alert(error);
            }
        });
}