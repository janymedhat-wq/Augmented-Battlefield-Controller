int button1 = 2;
int button2 = 3;
int button3 = 4;
int button4 = 5;
int button5 = 6;

void setup()
{
    Serial.begin(9600);
    pinMode(button1, INPUT_PULLUP);
    pinMode(button2, INPUT_PULLUP);
    pinMode(button3, INPUT_PULLUP);
    pinMode(button4, INPUT_PULLUP);
    pinMode(button5, INPUT_PULLUP);
}

void loop()
{
    if (digitalRead(button1) == LOW)
    {
        Serial.println("BTN1");
        delay(200);
    }
    if (digitalRead(button2) == LOW)
    {
        Serial.println("BTN2");
        delay(200);
    }
    if (digitalRead(button3) == LOW)
    {
        Serial.println("BTN3");
        delay(200);
    }
    if (digitalRead(button4) == LOW)
    {
        Serial.println("BTN4");
        delay(200);
    }
    if (digitalRead(button5) == LOW)
    {
        Serial.println("BTN5");
        delay(200);
    }
}
