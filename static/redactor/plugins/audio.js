var placeholderActive = false;

if (typeof explanationId !== 'undefined') {
    placeholderActive = true;
}

function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
}

function guid() {
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
    s4() + '-' + s4() + s4() + s4();
}

function guid8() { // 8-characters unique id
  return s4() + s4();
}

(function ($) {
    $.Redactor.prototype.audio = function () {
        return {

            init: function () {
                var button = this.button.addAfter('image', 'audio', "Insert Audio...");
                button.attr("class", "icon-music redactor-btn-image");
                this.button.addCallback(button, this.audio.show);
            },
            beforeStart: function () {
                var audio = this.audio;
                // 1. Setup placeholder creating
                if (placeholderActive) {
                    $('#create-placeholder').click(function() {
                        var link_id = guid8();
                        var text_to_record = $('#placeholder-recording-text').val();
                        $.ajax({
                            url: Django.url('audio_placeholders:create_placeholder'),
                            type: 'POST',
                            dataType: "json",
                            data: {
                                link_id: link_id,
                                text: text_to_record,
                                explanation_id: explanationId,
                                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                            },
                            success: function (data) {
                                audio.placeholderInsert(link_id, text_to_record);
                            },
                            error: function (xhr, errmsg, err) {
                                $('#error_box').html(xhr.status + ": " + xhr.responseText).show();
                            }
                        });
                    });
                }
                $('#direct-recording').recorder(this.audio.upload);
            },
            upload: function (blob) {
                var name = guid();
                console.log('Upload triggered for ' + name);
                var file = new File([blob], name + '.wav');
                this.upload.traverseFile(file);
            },
            getTemplate: function () {
                if (placeholderActive) {
                    placeholderFormSchema = {
                        title: "Placeholder",
                        color: "blue",
                        fields: [{
                            type: "text",
                            id: "placeholder-recording-text",
                            label: "Text",
                            placeholder: "Text to record"
                        }, {
                            type: "button",
                            id: "create-placeholder",
                            text: "Create"
                        }]
                    }
                } else {
                    placeholderFormSchema = {
                        title: "Placeholder",
                        color: "blue",
                        fields: [{
                            type: "customHtml",
                            html: '<h4> You must save exercise first to use placeholders </h4>'
                        }]
                    }
                }
                return String() +
                    FormEngine.renderForm(placeholderFormSchema) +
                    FormEngine.renderForm({
                        title: "Direct recording",
                        color: "green",
                        fields: [{
                            type: "emptyDiv",
                            id: "direct-recording"
                        }]
                    }) +
                    FormEngine.renderForm({
                        title: "File upload",
                        color: "orange",
                        fields: [{
                            type: "customHtml",
                            html: '<div id="upload-recording">'
                            + '<section id="redactor-modal-audio-insert">'
                            + '<div id="redactor-modal-audio-droparea"></div>'
                            + '</section>'
                            + '</div>'
                        }]
                    });

            },
            show: function () {
                this.modal.addTemplate('audio', this.audio.getTemplate());

                this.modal.load('audio', 'Audio', 700);
                this.upload.init('#redactor-modal-audio-droparea', this.opts.fileUpload, this.file.insert);

                this.selection.save();
                this.modal.show();

                this.audio.beforeStart();

            },
            placeholderInsert: function(id, text_to_record) {
                // copy&paste from file insert
                this.modal.close();
                this.selection.restore();
                this.buffer.set();
                this.insert.htmlWithoutClean('<p><a id="' + id + ' placeholder=true ">{' + text_to_record + '}</a></p>');
            }
        }
    }
})(jQuery);

