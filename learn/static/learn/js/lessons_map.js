var topMargin = 5;
var totalWidth = 1000;
var lessonWidth = 200;
var lessonHeight = 100;

/**
 * Draw lessons map using specified lessons levels list in an SVG container with specified selector
 * @param lessons_levels lessons levels list - first one does not have requirement, second requires first etc.
 * @param map_selector selector to find map SVG container
 */
var drawMap = function(lessons_levels, map_selector) {
    lessons_levels = findLessonsPositions(lessons_levels);
    drawLessons(lessons_levels, map_selector);
    drawArrows(lessons_levels, map_selector);
};

/**
 * Compute distance between two lessons containers horizontally
 * @param number total number of lessons containers on a level
 * @returns {number} empty spacing that should be left between every pair of neighbour containers
 */
var computeHorizontalSpacing = function(number) {
    if (number == 0)
        return 0;
    var totalLessonWidth = number * lessonWidth;
    var totalSpace = totalWidth - totalLessonWidth;
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
        y = y + 150;
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
 * Return color to fill a lesson container dependent on lesson status
 * @param status lesson status
 * @returns {string} RGB color for style attribute
 */
var statusColor = function(status) {
    if (status == 's') {
        return "rgb(0, 250, 154)";
    } else if (status == 'f') {
        return "rgb(255, 0, 0)";
    } else {
        return "rgb(190, 190, 190)";
    }
};


/**
 * D3 plugin to add a lesson container to the SVG container that it is called on
 * @param lesson lesson that is used to generate container content
 * @returns {d3.selection} element that function is called on
 */
(function() {
  d3.selection.prototype.drawLessonContainer = function(lesson) {
    var svgGroup =
        this
        .append("a")
            .attr("xlink:href", generateLearnURL(lesson.pk))
            .append("g");

    svgGroup
        .append("rect")
            .attr("x", lesson.x)
            .attr("y", lesson.y)
            .attr("width", lessonWidth)
            .attr("height", "100")
            .attr("style", "fill:" + statusColor(lesson.status) + ";stroke-width:3;stroke:rgb(0,0,0)");
    svgGroup
        .append("text")
            .attr("x", lesson.x + lessonWidth/2)
            .attr("y", lesson.y + lessonHeight/2)
            .attr("font-family", "Verdana")
            .attr("font-size", "11s")
            .attr("fill", "black")
            .attr("style","text-anchor: middle;")
            .text(lesson.topic);

    return this;
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
            d3.select(map_selector).drawLessonContainer(lessons_levels[i][j]);
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
 * @param lesson lesson to draw an arrow to
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