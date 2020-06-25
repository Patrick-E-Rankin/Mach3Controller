//The following code runs on an ESP32, I will make changes to make it work on an ESP8266
//It receives coordinates over UDP (port 8080) and displays it on an OLED display.
//It also monitors an input pin and sends the state over UDP (8081) as well.
//At the moment it only monitors one pin, however you can add as many as you want.
//I will be updating as I go along and improve it, sorry for the bad code, I am not a programmer.
//-Patrick https://github.com/Patrick-E-Rankin/Mach3-Controller

#include <WiFi.h>
#include <WiFiUdp.h>
#include <U8x8lib.h> //very fast library

U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE); //HW I2C is fastest, ESP8266 is software I2C, will investigate

const char* ssid     = "YOUR WIFI SSID";
const char* password = "WIFI PASSWORD";

const int buttonPin = 4;
int buttonState = 0; 
int stopsignal = 1; //directional keys need to be pressed until release they don't work like other keys.

unsigned int localPort = 8080;      // UDP Port to receive coordinates (format is: X+00.000Y+00.000Z+00.000) 8 digits per axis, or 24 digits long

char packetBuffer[30]; //buffer to hold incoming packet, needs to be at least 25, we could send more info if we wanted

WiFiUDP Udp; 
WiFiUDP SEND; 
void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  u8x8.begin();
  u8x8.setPowerSave(0);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  Udp.begin(localPort); //setup UDP receive port
  SEND.begin(8081); //setup UDP send port
  u8x8.setFont(u8x8_font_saikyosansbold8_u);
  u8x8.setCursor(0,55);
  u8x8.print("  ");
  u8x8.print(WiFi.localIP());
  u8x8.setFont(u8x8_font_px437wyse700a_2x2_f); 
}

void loop() {
  buttonState = digitalRead(buttonPin);
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    IPAddress remoteIp = Udp.remoteIP(); //records the server ip address
    int len = Udp.read(packetBuffer, 30);
    if (len > 0) {
      packetBuffer[len] = 0;
    }
        String coordinates(packetBuffer); //need to convert to string for u8x8.print
        u8x8.setCursor(0,0);
        u8x8.print(coordinates.substring(0,8));
        u8x8.setCursor(0,18);
        u8x8.print(coordinates.substring(8,16));
        u8x8.setCursor(0,36);
        u8x8.print(coordinates.substring(16,24));
        if (buttonState == 0){
          stopsignal = 0; //resets the stop signal
          SEND.beginPacket(Udp.remoteIP(), 8081);
          SEND.print("Y+"); //we are sending Y+, it is the equivalent to UP on the keyboard in our python reciever script
          SEND.endPacket();}
        else if((buttonState == 1) && (stopsignal == 0)){
          stopsignal = 1; //we are marking that we have sent the stop signal
          SEND.beginPacket(Udp.remoteIP(), 8081);
          SEND.print("STOPY+"); //equivalent to releasing the UP key on the keyboard in our python receiver script
          SEND.endPacket();
        }
  }
 }
 
  
  
