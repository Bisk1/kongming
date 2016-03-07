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
                recorder.stop();
                $('#direct-recording').html('<button id="record-confirm">Confirm</button><button id="record-play">Play</button><button id="record-cancel">Cancel</button>');
                $('#record-confirm').click(this.audio.export);
                $('#record-play').click(this.audio.playRequested);
                $('#record-cancel').click(this.audio.beforeStart);
                __log('Recording stopped');
            },
            playRequested: function()
            {
                recorder.getBuffer(this.audio.play);
            },
            play: function(buffers)
            {
                var newSource = audioContext.createBufferSource();
                var newBuffer = audioContext.createBuffer( 2, buffers[0].length, audioContext.sampleRate );
                newBuffer.getChannelData(0).set(buffers[0]);
                newBuffer.getChannelData(1).set(buffers[1]);
                newSource.buffer = newBuffer;
                newSource.connect( audioContext.destination );
                newSource.start(0);
            },
            export: function()
            {
                __log('Export triggered');
                recorder.exportWAV(this.audio.upload);
            },
            upload: function(blob)
            {
                __log('Upload triggered');
                file = new File([blob], "recording.wav");
                this.upload.traverseFile(file);
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
				this.upload.init('#redactor-modal-audio-droparea', this.opts.fileUpload, this.file.insert);

                this.selection.save();
				this.modal.show();

				this.audio.beforeStart();

			}
		}
	}
})(jQuery);

function __log(e, data) {
    console.log("\n" + e + " " + (data || ''));
}

function startUserMedia(stream) {
    __log('startUserMedia.');
    var input = audioContext.createMediaStreamSource(stream);
    __log('Media stream created.');

    // Uncomment if you want the audio to feedback directly
    //input.connect(audioContext.destination);
    //__log('Input connected to audio context destination.');

    recorder = new Recorder(input);
    __log('Recorder initialised.');
}

var audioContext;
var recorder;

window.onload = function init() {
    try {
        // webkit shim
        window.AudioContext = window.AudioContext || window.webkitAudioContext;
        navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
        window.URL = window.URL || window.webkitURL;

        audioContext = new AudioContext;
        __log('Audio context set up.');
        __log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
    } catch (e) {
        alert('No web audio support in this browser!');
    }
};