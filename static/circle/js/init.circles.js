$(document).ready(function(){

    /*
     * Will initialize all existing players
     */

    $(".cp_container").each( function() {
        new CirclePlayer(this);
});