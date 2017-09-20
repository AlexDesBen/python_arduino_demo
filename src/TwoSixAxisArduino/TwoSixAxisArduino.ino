#define FASTADC 1

// defines for setting and clearing register bits
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

#include<Wire.h>

// Global variables
uint16_t Combien = 0;
const int MPU_addr1=0x68;  // I2C address of the MPU-6050
const int MPU_addr2=0x69;  // I2C address of the second MPU-6050
// Explanation : http://playground.arduino.cc/Main/MPU-6050

int16_t AcX,AcY,AcZ,GyX,GyY,GyZ;
int16_t AcX2,AcY2,AcZ2,GyX2,GyY2,GyZ2;
uint32_t LastTime = 0;
uint32_t maxIter = 2*1000*1000;

// Setup function
void setup() {
  #if FASTADC
    // set prescale to 16
    sbi(ADCSRA,ADPS2) ;
    cbi(ADCSRA,ADPS1) ;
    cbi(ADCSRA,ADPS0) ;
  #endif
  Wire.begin();
  Wire.beginTransmission(MPU_addr1);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Wire.beginTransmission(MPU_addr2);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(115200);
}

// Main loop
void loop() {
  if (Serial.available()) {
    int c = Serial.read();
    if (c == 100) { //d = 100
      Wire.beginTransmission(MPU_addr1);
      Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
      Wire.endTransmission(false);
      Wire.requestFrom(MPU_addr1,14,true);  // request a total of 14 registers
      AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)     
      AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
      AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
      Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
      GyX=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
      GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
      GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
      Wire.beginTransmission(MPU_addr2);
      Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
      Wire.endTransmission(false);
      Wire.requestFrom(MPU_addr2,14,true);  // request a total of 14 registers
      AcX2=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)     
      AcY2=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
      AcZ2=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
      Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
      GyX2=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
      GyY2=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
      GyZ2=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
      LastTime = millis();
      Serial.print(AcX);Serial.print(",");
      Serial.print(AcY);Serial.print(",");
      Serial.print(AcZ);Serial.print(",");
      Serial.print(GyX);Serial.print(",");
      Serial.print(GyY);Serial.print(",");
      Serial.print(GyZ);Serial.print(",");
      Serial.print(AcX2);Serial.print(",");
      Serial.print(AcY2);Serial.print(",");
      Serial.print(AcZ2);Serial.print(",");
      Serial.print(GyX2);Serial.print(",");
      Serial.print(GyY2);Serial.print(",");
      Serial.println(GyZ2);
    }
    else if (c == 122) { // z = 122
      Combien = 0;
      Serial.println('k');
    }
    else if (c == 98) { // b = 98
      byte dataToSend[24];
      Wire.beginTransmission(MPU_addr1);
      Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
      Wire.endTransmission(false);
      Wire.requestFrom(MPU_addr1,14,true);  // request a total of 14 registers
      dataToSend[0] = Wire.read();
      dataToSend[1] = Wire.read();     
      dataToSend[2] = Wire.read();
      dataToSend[3] = Wire.read();
      dataToSend[4] = Wire.read();
      dataToSend[5] = Wire.read();
      Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
      dataToSend[6] = Wire.read();
      dataToSend[7] = Wire.read();
      dataToSend[8] = Wire.read();
      dataToSend[9] = Wire.read();
      dataToSend[10] = Wire.read();
      dataToSend[11] = Wire.read();
      Wire.beginTransmission(MPU_addr2);
      Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
      Wire.endTransmission(false);
      Wire.requestFrom(MPU_addr2,14,true);  // request a total of 14 registers
      dataToSend[12] = Wire.read();
      dataToSend[13] = Wire.read();     
      dataToSend[14] = Wire.read();
      dataToSend[15] = Wire.read();
      dataToSend[16] = Wire.read();
      dataToSend[17] = Wire.read();
      Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
      dataToSend[18] = Wire.read();
      dataToSend[19] = Wire.read();
      dataToSend[20] = Wire.read();
      dataToSend[21] = Wire.read();
      dataToSend[22] = Wire.read();
      dataToSend[23] = Wire.read();
      Serial.write(dataToSend,24);
    }
    else {
      Serial.println(c);
    }
  }
  Combien++;
}

