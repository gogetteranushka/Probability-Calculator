# Probability-Calculator

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

First, create a _Hat_ class in _main.py_. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. 
For example, a class object could be created in any of these ways:

<img width="436" alt="image" src="https://github.com/gogetteranushka/Probability-Calculator/assets/109903993/66550ca8-232c-47d5-8794-4f458201c698">

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].

The _Hat_ class should have a _draw_ method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an experiment function in main.py (not inside the Hat class). This function should accept the following arguments:

(•)  _hat_: A hat object containing balls that should be copied inside the function.
(•) _expected_balls_: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
(•)  _num_balls_drawn_: The number of balls to draw out of the hat in each experiment.
(•) _num_experiments_: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The experiment function should return a probability.

For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

Here is how you would call the experiment function based on the example above with 2000 experiments:

<img width="462" alt="image" src="https://github.com/gogetteranushka/Probability-Calculator/assets/109903993/dd6d511b-6485-41cb-a121-adc50e0e8c33">

The output would be something like this:

<img width="184" alt="image" src="https://github.com/gogetteranushka/Probability-Calculator/assets/109903993/162f48cf-dc09-4240-926a-6194e9a24f6d">

Since this is based on random draws, the probability will be slightly different each time the code is run.


_Hint_: Consider using the modules that are already imported at the top. Do not initialize random seed within the file.




