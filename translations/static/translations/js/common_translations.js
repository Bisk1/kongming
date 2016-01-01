var TranslationsApi = (function () {
    var api = {};

    var emptyTranslationDiv;
    var sourceInputDiv;

    /**
     * 1) Remove all translation divs
     * 2) Create and append translation div for each translation text,
     * starting appending from source input div and number 0
     * @param translations
     */
    api.updateTranslations = function (translations) {
        $("*[id^=div_id_translation_]").remove();
        var predecessor = sourceInputDiv;
        var nextTranslationNumber = 0;
        for (var i = 0; i < translations.length; i++) {
            var nextTranslation = createTranslationDiv(nextTranslationNumber);
            populateTranslation(nextTranslation, translations[i]);
            predecessor.after(nextTranslation);
            predecessor = nextTranslation;
            nextTranslationNumber = 0;
        }
    };

    /**
     * Using empty translations as a base, creates new translation div.
     * In order to assign new unique id, takes the number of the translation
     * to create (=n) and replaces all attributes "...translation_0"
     * with next number, e.g. "...translation_1", "...translation_2"
     */
    var createTranslationDiv = function (number) {
        var newTranslation = emptyTranslationDiv.clone();
        newTranslation.find("*").andSelf().each(function () {
            $.each(this.attributes, function (i, attrib) {
                var pattern = /(.*_)(\d+)/;
                var matches = attrib.value.match(pattern);
                if (matches) {
                    attrib.value = matches[1] + number;
                }
            });
        });
        return newTranslation;
    };

    var populateTranslation = function (translationDiv, translationText) {
        translationDiv.find('input').val(translationText);
    };

    $(document).ready(function() {

        var firstTranslationDiv = $("#div_id_translation_0");
        emptyTranslationDiv = firstTranslationDiv.clone();
        emptyTranslationDiv.find("input").val("");

        var sourceInputDiv = firstTranslationDiv.prev();

        $(document).on("click", "#button-id-add", function () {
            var lastTranslationDiv = findLastTranslationDiv();
            if (lastTranslationDiv == null) { // means that there are no translations yet, this will be the first one
                var predecessor = sourceInputDiv;
                var nextTranslation = createTranslationDiv(0);
                predecessor.after(nextTranslation);
            } else {
                var lastTranslationNumber = getTranslationNumber(lastTranslationDiv);
                var nextTranslation = createTranslationDiv(lastTranslationNumber + 1);
                lastTranslationDiv.after(nextTranslation);
            }
        });
    });

    /**
     * Find the element that should be a predecessor to the next translation div.
     * If there are any existing translation divs, it is the last one.
     * Otherwise, it is the div of source input.
     */
    var findLastTranslationDiv = function () {
        var currentTranslationsDivs = $('div[id^="div_id_translation_"]');
        return currentTranslationsDivs.length > 0 ? currentTranslationsDivs.last() : null;
    };

    /**
     * Find the number of the specified translation,
     * if translation id = div_id_translation_1
     * then the number = 1
     */
    var getTranslationNumber = function (translation) {
        var id = translation.attr("id");
        var matches = id.match(/.*_(\d+)/);
        return Number(matches[1]);
    };

    return api;

})();
