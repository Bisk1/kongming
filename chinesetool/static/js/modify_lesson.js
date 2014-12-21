$(document).ready(function() {

    function FieldCounter() {
        this.count = 1; // initial input boxes count
        this.max = 10; // maximum input boxes count allowed
        this.isFull = function() {
            return (this.count >= this.max);
        }
    }

    var addFieldHandler = function(e, wrapper, counter, input) {
        e.preventDefault();
        if(!counter.isFull()){
            $(wrapper).append('<div>' + input + '<a href="#" class="remove_field">Remove</a></div>'); //add input box
            counter.count++;
        }
    };

    var removeFieldHandler = function(e, element, counter) {
        e.preventDefault(); element.parent('div').remove();
        counter.count--;
    }

    var wordZhWrapper        = $(".word_zh_fields_wrap");
    var wordZhAddButton      = $(".add_word_zh_button");
    var wordZhFieldCounter   = new FieldCounter();
    var wordZhInput          = '<input type="text" name="word_zh[]"/>';

    $(wordZhAddButton).click(function(e){
        addFieldHandler(e, wordZhWrapper, wordZhFieldCounter, wordZhInput);
    })

    $(wordZhWrapper).on("click",".remove_field", function(e) {
        removeFieldHandler(e, $(this), wordZhFieldCounter);
    })

    var wordReqWrapper        = $(".requirement_fields_wrap");
    var wordReqAddButton      = $(".add_requirement_button");
    var wordReqFieldCounter   = new FieldCounter();
    var wordReqInput          = '<input type="text" name="requirement[]"/>';


    $(wordReqAddButton).click(function(e){
        addFieldHandler(e, wordReqWrapper, wordReqFieldCounter, wordReqInput);
    })

    $(wordReqWrapper).on("click",".remove_field", function(e) {
        removeFieldHandler(e, $(this), wordReqFieldCounter);
    })

});