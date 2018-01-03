package URLify;
/**
 * Replaces the spaces in the string with '%20'
 * */
public class URLify {
	
	public char [] replace(char[] s, int n) {
		for(int i=0;i<n;i++) {
			if(s[i]==' ') {
				for(int j=s.length-1;j>i;j--) {
					s[j]=s[j-2];
				}
				s[i]='%';	
				s[i+1]='2';
				s[i+2]='0';
			}
		}
		return s;
	}
	
	public static void main(String[] args) {
		URLify url = new URLify();
		char [] s= {'h','u','m','a','n',' ','b',' ','i','n','g','s',' ',' ',' ',' '}; 
		System.out.print(url.replace(s, 12));
	}

}
