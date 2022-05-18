#include <ArduinoBLE.h>
#include <Arduino_LSM9DS1.h>
#include <MadgwickAHRS.h>


//UUID setting
BLEService CountingService("6e400001-b5a3-f393-e0a9-e50e24dcca9e");
// Characteristic setting 
BLEStringCharacteristic IMUChar("6e400001-b5a3-f393-e0a9-e50e24dcca9e",BLEWrite ,30);
//BLEStringCharacteristic PitchChar("6e400003-b5a3-f393-e0a9-e50e24dcca9e",BLEWrite ,10);
//BLEStringCharacteristic YawChar("6e400004-b5a3-f393-e0a9-e50e24dcca9e",BLEWrite ,10);

unsigned long before_t, after_t;

// initialize a Madgwick filter:
Madgwick filter;
// sensor's sample rate is fixed at 104 Hz:
const float sensorRate = 119.00;
  // values for acceleration and rotation:
  float xAcc, yAcc, zAcc;
  float xGyro, yGyro, zGyro;
//  float mx, my, mz; // Magnometer #########
  float xAcc_now, xAcc_past;
  float xVel_now, xVel_past;
  float xPos;
  unsigned long Time_past;
  unsigned long Time_now;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.print("start communication");

if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU");
    // stop here if you can't access the IMU:
    while (true);
  }
  // start the filter to run at the sample rate:
  filter.begin(sensorRate);

if (!BLE.begin()) {
    Serial.println("starting BLE failed!");

    while (1);
  }

  BLE.setLocalName("QuitSmocking");
  BLE.setAdvertisedService(CountingService); 
  CountingService.addCharacteristic(IMUChar);
//  CountingService.addCharacteristic(PitchChar);
//  CountingService.addCharacteristic(YawChar);
  
  BLE.addService(CountingService);

  BLE.advertise();
  
Serial.println("Bluetooth device active, waiting for connections...");
}

void loop() {
String x_heading, y_heading,z_heading;
String imu_msg;
  // put your main code here, to run repeatedly:
BLEDevice central = BLE.central();

  if (central) {
    Serial.print("Connected to central: ");
    Serial.println(central.address());
      
      while(central.connected()){

         if (IMU.accelerationAvailable() &&
      IMU.gyroscopeAvailable()&& IMU.magneticFieldAvailable()) {
    // read accelerometer &and gyrometer:
    IMU.readAcceleration(xAcc, yAcc, zAcc);
    IMU.readGyroscope(xGyro, yGyro, zGyro);
//    IMU.readMagneticField(mx, my, mz); // ##############

    // update the filter, which computes orientation:
    filter.updateIMU(xGyro, yGyro, zGyro, xAcc, yAcc, zAcc);

    xAcc_now = xAcc;
    
    // print the heading, pitch and roll
    x_heading = (String)filter.getRoll();
    y_heading = (String)filter.getPitch();
    z_heading = (String)filter.getYaw();
    imu_msg = x_heading + " " + y_heading + " " + z_heading;
      }
      
      /*쓰기*/
        //before_t = millis();
        IMUChar.writeValue((String)imu_msg);
        
  //    /*읽기*/
  //      if(CountingChar.written()) {
  //          if (CountingChar.value()) {
  //              
  //              float val = CountingChar.value();
  //              Serial.print("Counting: ");
  //              Serial.println(val);
  //              
  //              
  //          }//value
  //      }//written
    }//connected
  }//central
}
