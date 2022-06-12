/*
    control flow code
    date: 6/1/2022
    by: daydreamer
*/

/* define pin function */
int RXLED = 17;
int play_pause_pin = 2;
int next_pin = 3;
int previous_pin = 4;
int volume_change_pin = 5;

void setup()
{
  pinMode(RXLED, OUTPUT);

  pinMode(play_pause_pin, INPUT);  // Set the button as an input
  digitalWrite(play_pause_pin, HIGH);  // Pull the button high

  pinMode(next_pin, INPUT);  // Set the button as an input
  digitalWrite(next_pin, HIGH);  // Pull the button high

  pinMode(previous_pin, INPUT);  // Set the button as an input
  digitalWrite(previous_pin, HIGH);  // Pull the button high

  pinMode(volume_change_pin, INPUT);  // Set the button as an input
  digitalWrite(volume_change_pin, HIGH);  // Pull the button high

  Serial.begin(9600); //This pipes to the serial monitor
  Serial.println("Initialize Serial Monitor");
}

void loop()
{
  if (digitalRead(play_pause_pin) == 0)
  {
    Serial.println("play_pause");
    RXLED0;
    RXLED1;
    delay(800);
    RXLED0;
  }

  if (digitalRead(next_pin) == 0)
  {
    Serial.println("next");
    RXLED0;
    RXLED1;
    delay(800);
    RXLED0;
  }

  if (digitalRead(previous_pin) == 0)
  {
    Serial.println("previous");
    RXLED0;
    RXLED1;
    delay(800);
    RXLED0;
  }

  // TODO
  if (digitalRead(volume_change_pin) == 0)
  {
    Serial.println("volume_up");
    Serial.println("volume_down");
    RXLED0;
    RXLED1;
    delay(800);
    RXLED0;
  }
}
