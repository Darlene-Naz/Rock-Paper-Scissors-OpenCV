<!-- @format -->

# Rock-Paper-Scissors <img src="https://github.com/Darlene-Naz/Rock-Paper-Scissors-OpenCV/blob/master/utils/images/gaming.png" height="40px" width="40px"/>

A Rock-Paper-Scissors <b>Pygame</b> with a <b>CNN Multiclass Classifier</b> model built in Keras to recognize real-time hand gestures using <b>OpenCV</b>.

## Working Demonstration

![]()

## Overview

This game simply uses your computer's camera to capture realtime gestures of your hand.

The pictures taken by the camera are processed and fed to a CNN Multi-class image classifier that determines whether the gesture corresponds to "Rock", "Paper" or "Scissors" gesture.

This CNN model is made in keras. You can download the pretrained model from here.

## Getting Started

**1. Clone the repository**

```bash
git clone <this_repo_url>
```

**2. Start a virtual environment eg. conda (Recommended)**

```bash
conda activate <my_virtual_env>
```

**3. Download the requirements**

```bash
cd Rock-Paper-Scissors-OpenCV
pip install requirements.txt
```

**4. Download the model**

```bash
cd Rock-Paper-Scissors-OpenCV
pip install requirements.txt
```

**4. Start the server**

```bash
python game.py
```

## Task List

- [x] Create a CNN Multi-Class Classifier
- [x] Integrate it with OpenCV
- [x] Create my 1st Pygame
- [x] Structure Code!
- [x] Work more on the model
- [x] Fix bugs & Add comments to code

## References

CNN Links :

<li>The best way to get started -> <a href="https://www.coursera.org/learn/convolutional-neural-networks/">Convolutional Neural Networks by Andrew Ng</a>

OpenCV Links :

<ul>
<li><a href="https://www.pygame.org/docs/">Pygame Docs</a> or even this <a href="https://pygame.readthedocs.io/">Pygame Guide</a></li>
<li><a href="https://www.101computing.net/getting-started-with-pygame/">A Basic Pygame Tutorial</a></li>
</ul>

Pygame Links :

<ul>
<li><a href="https://www.pygame.org/docs/">Pygame Docs</a> or even this <a href="https://pygame.readthedocs.io/">Pygame Guide</a></li>
<li><a href="https://www.101computing.net/getting-started-with-pygame/">A Basic Pygame Tutorial</a></li>
</ul>

## License

© 2020 Copyright
