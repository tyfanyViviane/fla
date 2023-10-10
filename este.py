import turtie

ste = turtle.turtle()

    ste.forward(100)    
    ste.right(90)
    ste.forward(100)
    ste.right(90)
    ste.forward(100)
    ste.right(90)
    ste.forward(100)

import turtle

    moveForward(150)    
    turnLeft(120)
    moveForward(150)
    turnLeft(60)
    moveForward(150)
    turnLeft(60)
    turnLeft(60)
    moveForward(150)

import turtle

    moveForward(100)
    turnRight(60)
    moveForward(100)
    turnRight(60)
    moveForward(100)
    turnRight(60)
    moveForward(100)
    turnRight(60)
    moveForward(100)
    turnRight(60)
    moveForward(100)

import turtle

for (var count = 0; count < 6; count) {
  moveForward(100);
  turnRight(60);
}

/*
moveForward(100);
turnRight(60);
*/

for (var count = 0; count < 12; count) {
  moveForward(60);
  turnRight(30);
  moveForward(60);
  turnRight(150);
  moveForward(60);
  turnRight(30);
  moveForward(60);
}

for (var count2 = 0; count2 < 12; count+) {
  for (var count = 0; count < 2; count) {
      penColour(colour_random());
    moveForward(60);
    turnRight(30);
    moveForward(60);
    turnRight(150);
  }
  turnLeft(30);
}

import turtle

/*
for (var count3 = 0; count3 < 12; count3) {
  penColour(colour_random());
  moveForward(60);
  turnRight(30);
  moveForward(60);
  turnRight(150);
}

for (var count2 = 0; count2 < 6; count2) {
  for (var count = 0; count < 6; count) {
      penColour(colour_random());
    moveForward(50);
    turnRight(60);
  }
  turnRight(60);
}

function desenhe_uma_flor() {
  for (var count3 = 0; count3 < 6; count3) {
      penColour(colour_random());
    for (var count2 = 0; count2 < 8; count2) {
          moveForward(20);
      turnRight(30);
    }
    turnRight(60);
  }
}

for (var count = 0; count < 2; count) {
  desenhe_uma_flor();
  jumpForward(150);
  desenhe_uma_flor();
}


function desenhar_uma_forma() {
  for (var count4 = 0; count4 < 6; count4) {
      moveForward(25);
    turnRight(60);
  }
}

penWidth(1);
for (var count3 = 0; count3 < 6; count3) {
  for (var count2 = 0; count2 < 2; count2) {
      penColour(colour_random());
    for (var count = 0; count < 4; count) {
          desenhar_uma_forma();
      jumpForward(75);
    }
    jumpBackward(25);
    turnRight(60);
    jumpForward(25);
    turnRight(120);
  }
  jumpBackward(25);
  turnLeft(60);
  jumpForward(50);
  turnRight(60);
}