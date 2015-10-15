# KongMing - website for learning Chinese

This web application follows the example of Duolingo language-learning website and its success in bringing  people opportunity to easily learn language with practical examples:

 * User can create an account to track his progress
 * Learning material is organized into lessons with specific topics
 * Every lesson is a set of exercises, each of them provides student with new information or test his knowledge
 * Lessons are organized in tree hierarchy - user can start from basic topics and progress to more advanced ones

The base language is English.

Technologies used:

 * Django 1.8
 * jQuery
 * Bootstrap
 * MySQL

The project core is structured into several Django apps:

 * words - maintains all the words used by the site, handles access to translation API and caches words in database
 * translations - holds all the texts (words, sentences, grammar structures examples) which are translated by user
 * lessons
 * exercises - contains models for all the exercises types and API to prepare and check them
 * learn - controls the process of learning by presenting lessons and taking user through the lesson flow
 
 
