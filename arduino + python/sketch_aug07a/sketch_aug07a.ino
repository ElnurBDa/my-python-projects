
int x = A0;
int y = A1;

void setup() {
  pinMode(x, INPUT);
  pinMode(y, INPUT);
  Serial.begin(9600);
}

void loop() {
  int rx = analogRead(x);
  int ry = analogRead(y);

  Serial.print("(");
  Serial.print(rx);
  Serial.print(", ");
  Serial.print(ry);
  Serial.print(")");
  Serial.println();
  
}
