//define diodes pin
#define dH 7
#define dPWM 3
#define dB 2

//potentiometer
#define pot 1

int statePot, vol, pwm;

void setup() {
  Serial.begin(9600);
  pinMode(pot, INPUT);
  pinMode(dH, OUTPUT);
  pinMode(dPWM, OUTPUT);
  pinMode(dB, OUTPUT);
}

void loop() {
  statePot = analogRead(pot); //0 to 1023 -> 5V
  vol = map(statePot, 0, 1023, 0, 5000); //Voltage in mv
  pwm = map(statePot, 0, 1023, 0, 255);
  
  analogWrite(dPWM, pwm); //Diode PWM

  if(vol>2500){
    digitalWrite(dH, HIGH);
  }
  if(vol<1300){
    digitalWrite(dH, LOW);
  }
  if(vol>>1300 and vol<<2500){
    digitalWrite(dB, HIGH);
  }
}