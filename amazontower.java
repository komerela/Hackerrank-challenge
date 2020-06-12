public class Main{

     public static void main(String []args){
        
        
        int length=6;
        int width=7;
        int servers[][]=new int[length][width];
        for(int i=0;i<length;i++){
            for(int j=0;j<width;j++){
                servers[i][j]=(int) Math.round( Math.random() );
            }
        }
        

        boolean done=true;
        int count=0;
        while(done){
            for(int i=0;i<length;i++){
                for(int j=0;j<width;j++){
                    servers=updateNeighbors(servers,i,j,length,width);
                }
            }
            
            if(hasOnesOnly(servers,length,width)){
                done=false;
            }
            count++;
        }
        
        System.out.println("Count "+count);
        
     }
     
     public static boolean hasOnesOnly(int[][] base,int rows,int columns){
         boolean x=true;
            for(int i=0;i<rows;i++){
                for(int j=0;j<columns;j++){
                    if(base[i][j]==0){
                        return false;
                    }
                }
            }
         return x;
     }
     
     public static int[][] updateNeighbors(int[][] base, int i,int j,int length,int width){
         if(base[i][j]==1){
            int[][] _temp=base;
            if(i==0 && j==0){
                _temp[i+1][j]=1;
                _temp[i][j+1]=1;
            }else if(i==length-1 && j==0){
                _temp[i-1][j]=1;
                _temp[i][j+1]=1;
            }else if(i==0 && j==width-1){
                _temp[i+1][j]=1;
                _temp[i][j-1]=1;
            }else if(i==length-1&&j==width-1){
                _temp[i-1][j]=1;
                _temp[i][j-1]=1;
                
            }else{
                try {
                    _temp[i+1][j]=1;
                    _temp[i][j-1]=1;
                    _temp[i][j+1]=1;
                    _temp[i-1][j]=1;
                    
                } catch(Exception e) {
                }
            }
            
            return _temp;
         }
         else{
            return base;
         }
         
         
         
     }
}

