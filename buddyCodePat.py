int Led = D7;

void setup()
{ 
	pinMode(Led, OUTPUT);
}

void blink()
{
    digitalWrite(Led, HIGH);
    delay(250);
    digitalWrite(Led, LOW);
    delay(250);
    }
 void loop()
 {
    if(Particle.publish("Deakin_RIOT_SIT210_Photon_Buddy", "pat")==true)
    {
        int i = 0;
        while(i < 6 )
        {
            blink();
            i++;
        }
            delay(4000);
                
    
    }    
    
    
  }