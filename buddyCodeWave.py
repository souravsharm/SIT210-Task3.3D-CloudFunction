int Led = D7;

void setup()
{ 
	pinMode(Led, OUTPUT);
}

void blink()
{
    digitalWrite(Led, HIGH);
    delay(1000);
    digitalWrite(Led, LOW);
    delay(1000);
    }
 void loop()
 {
    if(Particle.publish("Deakin_RIOT_SIT210_Photon_Buddy", "wave")==true)
    {
        int i = 0;
        while(i < 3 )
        {
            blink();
            i++;
        }
            delay(4000);
                
    
    }    
    
  }