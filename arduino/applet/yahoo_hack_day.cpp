/*
 Controlador de LED's (Arduino) - Yahoo Hack Day -  09/11/2008
 
 Luiz Vitor Martinez Cardoso <grabber@gmail.com> e Leandro Lameiro <lameiro@gmail.com>

*/

#include "WProgram.h"
void playTone(int tone);
void playNote(char note);
void setup();
void loop();
int ledY = 13;               // LED's - "Y"
int ledO = 10;               // LED's - "O"
int ledA = 11;               // LED's - "A"
int ledH = 8;                // LED's - "H"
int ledO2 = 9;               // LED's - "O2"
int ledexc = 12;             // LED's - "!"

int leddebug = 7;             // debug
int DEBUG = 1;

boolean ativado[6];

long blinkInterval = 200;


int value = LOW;                // previous value of the LED
long previousMillis = 0;        // will store last time LED was updated
byte range = 1;




int note_to_play = -1;
int speakerPin = 5;

int length = 15; // the number of notes
char notes[] = "ccggaagffeeddc "; // a space represents a rest
int beats[] = { 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 };

int beats_to_play = 0;

void playTone(int tone) {
  for (long i = 0; i < blinkInterval * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}

void playNote(char note) {
  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };

    if (note == ' ') {
      delay(blinkInterval); // rest
    } else {
  // play the tone corresponding to the note name
      for (int i = 0; i < 8; i++) {
        if (names[i] == note) {
          playTone(tones[i]);
        }
      }
  }
}

void setup()
{
  int i;
  pinMode(ledY, OUTPUT);      // sets the digital pin as output
  pinMode(ledO, OUTPUT);      // sets the digital pin as output
  pinMode(ledA, OUTPUT);      // sets the digital pin as output
  pinMode(ledH, OUTPUT);      // sets the digital pin as output
  pinMode(ledO2, OUTPUT);      // sets the digital pin as output
  pinMode(ledexc, OUTPUT);      // sets the digital pin as output
  
  pinMode(leddebug, OUTPUT);      // sets the digital pin as output
  pinMode(speakerPin, OUTPUT);
  
  
  ativado[0] = true;
  ativado[1] = true;
  
  
  for (i = 2; i < 6; i++){
      ativado[i] = false;
  }
  
 Serial.begin(9600);
 
 digitalWrite(leddebug, LOW);
 
 
  
}

void loop()
{
  int i;
  int lixo;
  // here is where you'd put code that needs to be running all the time.

  // check to see if it's time to blink the LED; that is, is the difference
  // between the current time and last time we blinked the LED bigger than
  // the interval at which we want to blink the LED.
  
  // check if data has been sent from the computer
  if (Serial.available() >=2) {
    // read the most recent byte (which will be from 0 to 255)
    range = Serial.read();
    
    for (i = 0; i<6;i++){
      ativado[i] = false;
    }
    
    ativado[0] = true;
    
    for (i = 1; i<=range;i++){
      ativado[i] = true;
    }
    
    blinkInterval = Serial.read() * 8;
    
  }  
  
  if (millis() - previousMillis > blinkInterval) {
    previousMillis = millis();   // remember the last time we blinked the LED

    // if the LED is off turn it on and vice-versa.
    if (value == LOW)
      value = HIGH;
    else
      value = LOW;
    
    if (ativado[0]){
      digitalWrite(ledY, value);
    } else {
      digitalWrite(ledY, LOW);
    }
    
    
    if (ativado[1]){
      digitalWrite(ledA, value);
    } else {
      digitalWrite(ledA, LOW);
    }
    
    if (ativado[2]){
      digitalWrite(ledH, value);
    } else {
      digitalWrite(ledH, LOW);
    }
    
    if (ativado[3]){
      digitalWrite(ledO, value);
    } else {
      digitalWrite(ledO, LOW);
    }
    
    if (ativado[4]){
      digitalWrite(ledO2, value);  
    } else {
      digitalWrite(ledO2, LOW);
    }
    
    if (ativado[5]){
      digitalWrite(ledexc, value);
    } else {
      digitalWrite(ledexc, LOW);
    }
  }
  
  if (beats_to_play == 0){
    note_to_play = (note_to_play+1) % length;
    beats_to_play = beats[note_to_play];
  }
  
  playNote(notes[note_to_play]);
  beats_to_play--;
  if (beats_to_play == 0){
    delay(blinkInterval/10);
  } 
  
}

int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

