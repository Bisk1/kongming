(function($)
{
	$.Redactor.prototype.audio = function()
	{
		return {

            beforeStart: function()
            {
                if (recorder === undefined) {
                    navigator.getUserMedia({audio: true}, startUserMedia, function(e) {
                      __log('No live audio input: ' + e);
                    });
                }
                $('#direct-recording').html('<button id="record-start">Start</button>');
                $('#record-start').click(this.audio.started);
            },
            started: function()
            {
                $('#record-start').off();
                recorder.clear();
                recorder.record();
                $('#direct-recording').html('<button id="record-stop">Stop</button>');
                $('#record-stop').click(this.audio.stopped);
                __log('Recording started');

            },
            stopped: function()
            {
                $('#record-stop').off();
                __log('Recording stop triggered');
                recorder.stop();
                $('#direct-recording').html('<button id="record-confirm">Confirm</button><button id="record-cancel">Cancel</button>');
                $('#record-confirm').click(this.audio.upload);
                $('#record-cancel').click(this.audio.beforeStart);
                __log('Recording stopped');
            },
            upload: function()
            {
                __log('Upload triggered');
                recorder.exportWAV(this.upload.traverseFile);
            },

			getTemplate: function()
			{
				return String()
				    + '<div id="upload-recording">'
                        + '<section id="redactor-modal-audio-insert">'
                            + '<div id="redactor-modal-audio-droparea"></div>'
                        + '</section>'
                    + '</div>'
                    + '<div id="direct-recording"></div>'
			},
			init: function()
			{
				var button = this.button.addAfter('image', 'audio', "Insert Audio...");
				button.attr("class", "icon-music redactor-btn-image");
				this.button.addCallback(button, this.audio.show);
			},
			show: function()
			{
				this.modal.addTemplate('audio', this.audio.getTemplate());

				this.modal.load('audio', 'Audio', 700);
				this.upload.init('#redactor-modal-audio-droparea', this.opts.fileUpload, this.audio.insert);

                this.selection.save();
				this.modal.show();

				this.audio.beforeStart();

			},
			insert: function(json, direct, e)
            {
                var audio = $(String()
                + '<div class="cp-container" audio-src="' + json.filelink + '">'
                    + '<div class="cp-jplayer"></div>'
                    + '<div class="cp-buffer-holder cp-gt50" style="display: block;">'
                        + '<div class="cp-buffer-1" style="transform: rotate(180deg);"></div>'
                        + '<div class="cp-buffer-2" style="display: block; transform: rotate(271.362deg);"></div>'
                    + '</div>'
                    + '<div class="cp-progress-holder" style="display: block;">'
                        + '<div class="cp-progress-1" style="transform: rotate(94.2428deg);"></div>'
                        + '<div class="cp-progress-2" style="transform: rotate(0deg); display: none;"></div>'
                    + '</div>'
                    + '<div class="cp-circle-control"></div>'
                    + '<ul class="cp-controls">'
                        + '<li><a class="cp-play" tabindex="1" style="display: block;">play</a></li>'
                        + '<li><a class="cp-pause" style="display: none;" tabindex="1">pause</a></li>'
                    + '</ul>'
                + '</div>');

                audio.uniqueId();

                this.modal.close();
                this.selection.restore();
                this.buffer.set();

                this.insert.html(this.utils.getOuterHtml(audio), false);

                new CirclePlayer("#" + audio.attr("id"));

                if (typeof json == 'string') return;
                this.core.setCallback('fileUpload', audio, json);

            }
		}
	}
})(jQuery);

function __log(e, data) {
    console.log("\n" + e + " " + (data || ''));
}

function startUserMedia(stream) {
    __log('startUserMedia.');
    var input = audio_context.createMediaStreamSource(stream);
    __log('Media stream created.');

    // Uncomment if you want the audio to feedback directly
    //input.connect(audio_context.destination);
    //__log('Input connected to audio context destination.');

    recorder = new Recorder(input);
    __log('Recorder initialised.');
}

var audio_context;
var recorder;

window.onload = function init() {
    try {
        // webkit shim
        window.AudioContext = window.AudioContext || window.webkitAudioContext;
        navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
        window.URL = window.URL || window.webkitURL;

        audio_context = new AudioContext;
        __log('Audio context set up.');
        __log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
    } catch (e) {
        alert('No web audio support in this browser!');
    }
};