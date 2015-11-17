/**
 * Switch Chinese input feature -
 * @param active if true - then input box works as Chinese characters input,
 * otherwise as normal input
 */
var toggleChineseInput = function (active) {
    if (active) {
        $('#proposition').chineseInput({
            debug: false, // print debug messages
            input: {
                initial: 'simplified', // or 'traditional'
                allowChange: false // allow transition between traditional and simplified
            },
            active: true // whether or not the plugin should be active by default
        });
    } else {
        $('#proposition').unbind(); // remove all events from element
    }
};