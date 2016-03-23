var audioContext;
var recorder;

(function($)
{
	$.Redactor.prototype.audio = function()
	{
		return {

            beforeStart: function()
            {   // microphone will work only over secure connection (HTTPS) or on localhost (for testing purposes)
                if (window.location.protocol == "https:" || document.location.hostname == "localhost") {
                    $('#direct-recording').html('<button type="button" class="btn btn-default" id="record-start">Start</button>');
                    $('#record-start').click(this.audio.startRequested);
                } else {
                    $('#direct-recording').html('<h3>Only available over HTTPS!</h3>');
                }
            },
            startRequested: function()
            {
                $('#record-start').off();
                var afterSetup = this.audio.started;
                if (recorder === undefined) {
                    navigator.getUserMedia({audio: true},
                        function(stream) {
                            var input = audioContext.createMediaStreamSource(stream);
                            console.log('Media stream created.');
                            // Uncomment if you want the audio to feedback directly
                            //input.connect(audioContext.destination);
                            //console.log('Input connected to audio context destination.');

                            recorder = new Recorder(input);
                            console.log('Recorder initialised.');
                            afterSetup();
                        },
                        function(e) {
                          console.log('No live audio input: ' + e);
                        });
                } else {
                    afterSetup();
                }
            },
            started: function()
            {
                recorder.clear();
                recorder.record();
                $('#direct-recording').html('<button type="button" class="btn btn-default" id="record-stop">Stop</button>');
                $('#record-stop').click(this.audio.stopped);
                console.log('Recording started');

            },
            stopped: function()
            {
                $('#record-stop').off();
                recorder.stop();
                $('#direct-recording').html('<button type="button" class="btn btn-default" id="record-confirm">Confirm</button>' +
                '<button type="button" class="btn btn-default" id="record-play">Play</button>' +
                '<button type="button" class="btn btn-default" id="record-cancel">Cancel</button>');
                $('#record-confirm').click(this.audio.export);
                $('#record-play').click(this.audio.playRequested);
                $('#record-cancel').click(this.audio.beforeStart);
                console.log('Recording stopped');
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
                console.log('Export triggered');
                recorder.exportWAV(this.audio.upload);
            },
            upload: function(blob)
            {
                console.log('Upload triggered');
                file = new File([blob], "recording.wav");
                this.upload.traverseFile(file);
            },
			getTemplate: function()
			{
				return String()
                    + '<h5>1) File upload</h5>'
				    + '<div id="upload-recording">'
                        + '<section id="redactor-modal-audio-insert">'
                            + '<div id="redactor-modal-audio-droparea"></div>'
                        + '</section>'
                    + '</div>'
                    + '<h5>2) Direct recording</h5>'
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


window.onload = function init() {
    try {
        // webkit shim
        window.AudioContext = window.AudioContext || window.webkitAudioContext;
        navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
        window.URL = window.URL || window.webkitURL;

        audioContext = new AudioContext;
        console.log('Audio context set up.');
        console.log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
    } catch (e) {
        alert('No web audio support in this browser!');
    }
};