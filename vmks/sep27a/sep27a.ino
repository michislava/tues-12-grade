#define BUTTON1 2 //PULL-UP - ++
#define BUTTON2 3 //PULL-DOWN - --
#define LED1 4
#define LED2 5
#define LED3 6
#define LED4 7

int number, buttonState1, buttonState2;

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON1, INPUT);
  pinMode(BUTTON2, INPUT);
  for(int i; i<4; i++){
    pinMode(i, OUTPUT);
    }
}

void loop() {
  buttonState1 = digitalRead(BUTTON1);
  buttonState2 = digitalRead(BUTTON2);
  if(buttonState1 == HIGH){
    if(number==15){
      number=0; 
     }
    number++;
   }
   if(buttonState2 == HIGH){
    if(number==0){
      number=15;  
    }
    number--;
   }
   Serial.print(number);
   Serial.print("\n");
   delay(1000);
}
