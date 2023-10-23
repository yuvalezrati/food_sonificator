import processing.core.*;
import processing.serial.*;
import processing.sound.*;

Serial arduino; // Serial object for reading data from Arduino
SoundFile player; // SoundFile object for playing the song
SoundFile player2; // SoundFile object for playing the song
float distance; // Variable to store the sonar distance
int count = 0;
int i= 0;
int userInput; // Variable to store user input from the keypad
void setup() {
  size(400, 400);
  noStroke();
  
  // Open serial communication with Arduino
  print(Serial.list());
  arduino = new Serial(this, "/dev/cu.usbmodem214101", 9600);
  // Initialize SoundFile and load the song
  player = new SoundFile(this, "/Users/yuval/Downloads/mambo1.mp3");
  player2 = new SoundFile(this, "/Users/yuval/Downloads/gf.mp3");
}

void draw() {
  background(255);
  // Read sonar data from Arduino
  if (arduino.available() > 0) {
    String data = arduino.readStringUntil('\n'); // Read the data until a newline character
    if (data != null) {
       if (data.startsWith("The number is")) {
        String lastItem = data.substring(data.lastIndexOf(" ") + 1);
        i=Integer.parseInt(lastItem.trim());  
        println("number chosen");
       }


      data = data.trim(); // Remove leading/trailing whitespaces
      float distance = float(data); // Convert the data to float
      //println("Sonar Distance: " + distance + " cm"+count); // Print the sonar distance to the console
      count = count + 1;
   if(distance<10 && distance >0 && !player.isPlaying() &&!player2.isPlaying() && count>50)
   {
     println(i);
     if(i == 1)
     {
      player.play();
    }
        else if(i == 2)
     {
      player2.play();
   }
  }
     if((player.isPlaying() && distance > 20) || (player2.isPlaying() && distance > 20))
   {
     player.pause();
     player2.pause();
  }
}
}
}
