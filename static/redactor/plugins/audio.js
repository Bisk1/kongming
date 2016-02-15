(function($)
{
	$.Redactor.prototype.audio = function()
	{
		return {
			getTemplate: function()
			{
				return String()
                    + '<section id="redactor-modal-audio-insert">'
                        + '<div id="redactor-modal-audio-droparea"></div>'
                    + '</section>';
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

			},
			insert: function(json, direct, e)
            {
                var $aud;
                {
                    $aud = $('<audio>');
                    $aud.prop('controls').attr('data-redactor-inserted-audio', 'true');
                    $source = $('<source>').attr('src', json.filelink).attr('type', 'audio/wav');
                    $source.text('Your browser does not support the audio element.');
                    $aud.append($source);
                }

                var node = $aud;
                var isP = this.utils.isCurrentOrParent('P');
                if (isP)
                {
                    // will replace
                    node = $('<blockquote />').append($aud);
                }

                this.modal.close();

                this.selection.restore();
                this.buffer.set();

                this.insert.html(this.utils.getOuterHtml(node), false);

                var $audio = this.$editor.find('audio[data-redactor-inserted-audio=true]').removeAttr('data-redactor-inserted-audio');

                if (isP)
                {
                    $audio.parent().contents().unwrap().wrap('<p />');
                    $audio.parent().prepend('&nbsp;').append('&nbsp;');
                }
                else if (this.opts.linebreaks)
                {
                    if (!this.utils.isEmpty(this.code.get()))
                    {
                        $audio.before('<br>');
                    }

                    $audio.after('<br>');
                }

                if (typeof json == 'string') return;

                this.core.setCallback('fileUpload', $audio, json);

            }
		}
	}
})(jQuery);
