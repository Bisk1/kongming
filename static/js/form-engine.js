var FormEngine = {
    renderField: function (fieldSchema) {
        switch (fieldSchema.type) {
            case "text":
                return '<div id="div_' + fieldSchema.id + '" class="form-group">'
                    + '<label for="recording-text"  class="control-label col-lg-4">' + fieldSchema.label + '</label>'
                    + '<div class="col-lg-8">'
                    + '<input class="textinput textInput form-control" id="' + fieldSchema.id + '" name="text" placeholder="'
                    + fieldSchema.placeholder + '" type="text">'
                    + '</div></div>';
            case "emptyDiv":
                return '<div id="' + fieldSchema.id + '"></div>';
            case "customHtml":
                return fieldSchema.html;
            case "button":
                return this.button(fieldSchema);
            default:
                throw "Unsupported field type: " + fieldSchema.type;
        }
    },
    renderForm: function (formSchema) {
        var color = formSchema.hasOwnProperty("color") ? formSchema.color : "blue";
        var title = formSchema.title;
        var result = String()
            + '<form class="form-horizontal">'
            + '<div class="col-md-12">'
            + '<div class="widget w' + color + '"><div class="widget-head">'
            + '<div class="pull-left">' + title + '</div>'
            + '<div class="clearfix"></div>'
            + '</div></div>'
            + '<div class="widget-content"><div class="pad">';
        if (formSchema.hasOwnProperty("fields")) {
            for (var i = 0; i < formSchema.fields.length; i++) {
                result += this.renderField(formSchema.fields[i]);
            }
        }
        result += '</div></div></div></form>';
        return result;
    },

    button: function (buttonSchema) {
        return '<button type="button" class="btn btn-default" id="' + buttonSchema.id + '">' + buttonSchema.text + '</button>';
    }
};
