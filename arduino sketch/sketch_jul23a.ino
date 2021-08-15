long x = 0;
int y = 0;


byte
    x_mask = B11000000,
    y_mask = B00001100,
    leitura = 0,
    anterior = 0;
    
  
void setup(){
    DDRD = B00000000;
    Serial.begin(9600);

  
    while(1){
        leitura = PIND;

        if (leitura != anterior){
        
            switch(leitura & x_mask){
                case 0:
                    switch(anterior & x_mask){
                        case  64: x--; break;
                        case 128: x++; break;}
                    break;
                case 64:
                    switch(anterior & x_mask){
                        case 192: x--; break;
                        case   0: x++; break;}
                    break;
                case 192:
                    switch(anterior & x_mask){
                        case 128: x--; break;
                        case  64: x++; break;}
                    break;
                case 128:
                    switch(anterior & x_mask){
                        case   0: x--; break;
                        case 192: x++; break;}
                    break;
            }
     
           
            switch(leitura & y_mask){
                case 0:
                    switch(anterior & y_mask){
                        case 4: y--; break;
                        case 8: y++; break;}
                    break;
                case 4:
                    switch(anterior & y_mask){
                        case 12: y--; break;
                        case  0: y++; break;}
                    break;
                case 12:
                    switch(anterior & y_mask){
                        case 8: y--; break;
                        case 4: y++; break;}
                    break;
                case 8:
                    switch(anterior & y_mask){
                        case  0: y--; break;
                        case 12: y++; break;}
                    break;
            }
        }
        
        anterior = leitura;
    

        if(Serial.available() && Serial.availableForWrite()){
            Serial.read();
            Serial.println(String(x) + ' ' + String(y));
        }
    }
}
