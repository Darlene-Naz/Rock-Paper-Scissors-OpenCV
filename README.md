<!-- @format -->

# Rock-Paper-Scissors <img src="https://github.com/Darlene-Naz/Rock-Paper-Scissors-OpenCV/blob/master/src/utils/images/gaming.png" height="40px" width="40px"/>

A Rock-Paper-Scissors <b>Pygame</b> with a <b>CNN Multiclass Classifier</b> model built in Keras to recognize real-time hand gestures using <b>OpenCV</b>.

## Working Demo

![](readme_requirements/video/rps.gif)

## Overview

This game simply uses your computer's camera to capture realtime gestures of your hand.

The pictures taken by the camera are processed and fed to a CNN Multi-class image classifier that determines whether the gesture corresponds to "Rock", "Paper" or "Scissors" gesture.

This CNN model is made in keras. You can download the pretrained model from here.

## Origin

After completing a couple of CNN courses on coursera I wanted to hone my skills by focusing on small project. So I found 2 useful datasets and jumped straight into building my model. I didnt want to stop there... this led me to create my first pygame. I'm happy with my progress and would like to share it with you.

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
.
├───models                      # model.h5 files here
├───notebooks
│   └───.ipynb_checkpoints
├───readme_requirements
│   └───video
├───src
│   ├───components
│   │   └───__pycache__
│   └───utils
│       ├───images
│       └───__pycache__
└───tests
    ├───integration
    └───unit
```

**5. Start the server**

```bash
python src/main.py
```

## Outputs

[INFO] To get started, press 'SPACE' after adjusting hand in the box
[System] Initializing Camera...
[System] Camera Window Loaded!
[Debug] Image Saved!
[MODEL] Max Probability: 0.9817846
[GAME] Player: paper
[GAME] Computer: scissors
[GAME] Score: Computer 1 & Player 0
[GAME] Results: Computer wins this round!
[Debug] Image Saved!
[MODEL] Max Probability: 0.8957788
[GAME] Player: scissors
[GAME] Computer: scissors
[GAME] Score: Computer 1 & Player 0
[GAME] Results: Tie!
[Debug] Image Saved!
[MODEL] Max Probability: 0.6092333
[GAME] Player: paper
[GAME] Computer: paper
[GAME] Score: Computer 1 & Player 0
[GAME] Results: Tie!
[Debug] Image Saved!
[MODEL] Max Probability: 0.8689292
[GAME] Player: rock
[GAME] Computer: rock
[GAME] Score: Computer 1 & Player 0
[GAME] Results: Tie!
[Debug] Image Saved!
[MODEL] Max Probability: 0.99928963
[GAME] Player: paper
[GAME] Computer: rock
[GAME] Score: Computer 1 & Player 1
[GAME] Results: Player wins this round!
[Debug] Image Saved!
[MODEL] Max Probability: 0.5058385
[GAME] Player: scissors
[GAME] Computer: scissors
[GAME] Score: Computer 1 & Player 1
[GAME] Results: Tie!
[Debug] Image Saved!
[MODEL] Max Probability: 0.93402463
[GAME] Player: rock
[GAME] Computer: scissors
[GAME] Score: Computer 1 & Player 2
[GAME] Results: Player wins this round!
[Debug] Image Saved!
[MODEL] Max Probability: 0.6695166
[GAME] Player: scissors
[GAME] Computer: rock
[GAME] Score: Computer 2 & Player 2
[GAME] Results: Computer wins this round!
[Debug] Image Saved!
[MODEL] Max Probability: 0.9671053
[GAME] Player: rock
[GAME] Computer: rock
[GAME] Score: Computer 2 & Player 2
[GAME] Results: Tie!
[Debug] Image Saved!
[MODEL] Max Probability: 0.7444503
[GAME] Player: paper
[GAME] Computer: rock
[GAME] Score: Computer 2 & Player 3
[GAME] Results: Player wins this round!

## Task List

- [x] Create a CNN Multi-Class Classifier
- [x] Integrate it with OpenCV
- [x] Create my 1st Pygame
- [x] Structure Code!
- [x] Work more on the model
- [x] Fix bugs & Add comments to code

## References

CNN Links :

<ul>
<li>The best way to get started -> <a href="https://www.coursera.org/learn/convolutional-neural-networks/">Convolutional Neural Networks by Andrew Ng</a>
</ul>

Pygame Links :

<ul>
<li><a href="https://www.pygame.org/docs/">Pygame Docs</a> or even this <a href="https://pygame.readthedocs.io/">Pygame Guide</a></li>
<li><a href="https://www.101computing.net/getting-started-with-pygame/">A Basic Pygame Tutorial</a></li>
</ul>

## License

© 2020 Copyright
