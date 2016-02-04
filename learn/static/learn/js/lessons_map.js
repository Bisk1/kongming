var LessonsMapGenerator = (function () {
    var STATUS = {
      SUCCESS : {value: 's'},
      FAILURE: {value: 'f'},
      NOT_DONE : {value: 'u'},
      LOCKED : {value: 'l'}
    };


    var topMargin = 5;
    var mapWidth = 1000;
    var lessonWidth = 200;
    var lessonHeight = 200;
    var verticalSpacing = 100;
    var verticalDistance = verticalSpacing + lessonHeight;

    /**
     * Compute distance between two lessons containers horizontally
     * @param number total number of lessons containers on a level
     * @returns {number} empty spacing that should be left between every pair of neighbour containers
     */
    var computeHorizontalSpacing = function(number) {
        if (number == 0)
            return 0;
        var totalLessonWidth = number * lessonWidth;
        var totalSpace = mapWidth - totalLessonWidth;
        return totalSpace / (number + 1);
    };

    /**
     * Find positions of lessons containers in specified lesson level on specified height
     * @param level lessons level - list of lessons on one level
     * @param y vertical position of lessons level
     * @returns {*} lessons level with x, y fields
     */
    var findLevelLessonsPositions = function(level, y) {
        var spacing = computeHorizontalSpacing(level.length);
        var x = spacing;
        for (var j = 0; j < level.length; j++) {
            level[j].x = x;
            level[j].y = y;
            x = x + spacing + lessonWidth;
        }
        return level;
    };

    /**
     * Find positions of all lessons containers in specified lessons levels
     * @param lessons_levels lessons levels - list of lessons levels
     * @returns {*} lessons levels with x, y fields
     */
    var findLessonsPositions = function(lessons_levels) {
        var y = topMargin;
        for (var i = 0; i < lessons_levels.length; i++) {
            lessons_levels[i] = findLevelLessonsPositions(lessons_levels[i], y);
            y = y + verticalDistance;
        }
        return lessons_levels;
    };

    /**
     * Find lesson with specified key in specified lessons collection
     * @param lessons_levels lessons collection (as lessons levels)
     * @param key lesson key to find
     * @returns {*} lesson with specified key
     */
    var findLessonWithKey = function(lessons_levels, key) {
        for (var i = 0; i < lessons_levels.length; i++) {
            for (var j = 0; j < lessons_levels[i].length; j++) {
                if (lessons_levels[i][j].pk == key) {
                    return lessons_levels[i][j];
                }
            }
        }
    };

    /**
     * Return image to represent lesson status:
     * 1) If lesson was opened and completed successfully: green book
     * 2) If lesson was opened but failed: red book
     * 3) If lesson was not opened and is locked: gray book
     * 3) If lesson was not opened and is available: blue book
     * @param status
     * @returns (string) image URL for the lesson
     */
    var statusImage = function(status) {
        if (status == STATUS.SUCCESS.value) {
            return STATIC_URL + "learn/img/book_green.png";
        } else if (status == STATUS.FAILURE.value) {
            return STATIC_URL + "learn/img/book_red.png";
        } else if (status == STATUS.NOT_DONE.value) {
            return STATIC_URL + "learn/img/book_blue.png";
        } else {
            return STATIC_URL + "learn/img/book_gray.png";
        }
    };

    /**
     * Create SVG group in specified container for specified lesson.
     * If the lesson is not locked, the SVG group should be embedded
     * in a link to the lesson
     * @param lesson
     * @param container
     * @returns {void|*} SVG group
     */
    var getSvgGroupForLessonContainer = function(lesson, container) {
        if (lesson.status != STATUS.LOCKED.value) {
            return container
                .append("a")
                    .attr("xlink:href", generateLearnURL(lesson.pk))
                    .append("g");
        } else {
            return container.append("g");
        }

    };

    /**
     * D3 plugin to add a lesson container to the SVG container that it is called on
     * @param lesson lesson that is used to generate container content
     * @returns {d3.selection} element that function is called on
     */
    (function() {
      d3.selection.prototype.drawLessonContainer = function(lesson) {
        var svgGroup = getSvgGroupForLessonContainer(lesson, this);

        var image =
            svgGroup
                .append("image")
                    .attr("x", lesson.x)
                    .attr("y", lesson.y)
                    .attr("width", lessonWidth)
                    .attr("height", lessonHeight)
                    .attr("xlink:href", statusImage(lesson.status));


        var textSpans = breakIntoSpanTexts(lesson.topic, 15);
        var xTextPosition = lesson.x + lessonWidth / 2;
        var yTextPosition = lesson.y + lessonHeight / 5;
        var textField =
            svgGroup
                .append("text")
                .attr("x", xTextPosition)
                .attr("y", yTextPosition)
                .attr("class","lesson-title");
        for (var i = 0; i < textSpans.length; i++) {
            textField
                .append("tspan")
                .attr("x", xTextPosition)
                .attr("dy", "1.2em")
                .text(textSpans[i]);
        }
        return this;
      };


    /**
     * Break text into pieces long enough to fit into
     * spans of specified length
     * @param fullText text to break
     * @param maxCharacters maximum number of characters in each piece
     */
    var breakIntoSpanTexts = function(fullText, maxCharacters) {
        var words = fullText.split(" ");
        var spanTexts = [""];
        var i = 0;
        for (var j = 0; j < words.length; j++) {
            if (((spanTexts[i] + words[j]).length) > maxCharacters) {
                i++;
                spanTexts[i] = words[j];
            } else {
                spanTexts[i] = spanTexts[i] + " " + words[j];
            }
        }
        return spanTexts;
    };

    })();

    /**
     * Draw lessons from specified lessons levels collection in an SVG container with specified selector
     * @param lessons_levels lessons levels
     * @param map_selector map SVG selector
     */
    var drawLessons = function(lessons_levels, map_selector) {
        for (var i = 0; i < lessons_levels.length; i++) {
            for (var j = 0; j < lessons_levels[i].length; j++) {
                var lesson = lessons_levels[i][j];
                d3.select(map_selector).drawLessonContainer(lesson);
            }
        }
    };

    /**
     * Draw an arrow in an SVG container with specified selector for specified lesson and looking for its requirement
     * in lessons from specified lessons levels collection
     * @param lesson lesson to draw an arrow to
     * @param lessons_levels lessons levels collection to find reuqirement - lesson to draw an arrow from
     * @param map_selector  map SVG selector
     */
    var drawArrow = function(lesson, lessons_levels, map_selector) {
        var requirement = findLessonWithKey(lessons_levels, lesson.requirement);
        d3.select(map_selector)
                .append("line")
                .attr("x1", requirement.x + lessonWidth/2)
                .attr("y1", requirement.y + lessonHeight)
                .attr("x2", lesson.x + lessonWidth/2)
                .attr("y2", lesson.y)
                .attr("style", "stroke:rgb(255,0,0);stroke-width:2")
    };

    /**
     * Draw arrows in an SVG container for specified lessons levels collection to join lessons with their requirements
     * @param lessons_levels lessons levels collection with lessons to join - contains both sources and destinations
     * @param map_selector  map SVG selector
     */
    var drawArrows = function(lessons_levels, map_selector) {
        for (var i = 1; i < lessons_levels.length; i++) { // omit first level as it doesn't have requirement
            for (var j = 0; j < lessons_levels[i].length; j++) {
                drawArrow(lessons_levels[i][j], lessons_levels, map_selector);
            }
        }
    };

    var adjustMapHeight = function(lessons_levels_count, map_selector) {
        var totalHeight =  (lessons_levels_count - 1) * verticalDistance + lessonHeight;
        $(map_selector).height(totalHeight);
    };
    return {
        /**
         * Draw lessons map using specified lessons levels list in an SVG container with specified selector
         * @param lessons_levels lessons levels list - first one does not have requirement, second requires first etc.
         * @param map_selector selector to find map SVG container
         */
        drawMap: function(lessons_levels, map_selector) {
            lessons_levels = findLessonsPositions(lessons_levels);
            drawLessons(lessons_levels, map_selector);
            drawArrows(lessons_levels, map_selector);
            adjustMapHeight(lessons_levels.length, map_selector);
        },

        setWidth: function(width) {
            mapWidth = width;
        }
    };
}());

