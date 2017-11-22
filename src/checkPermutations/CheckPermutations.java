package checkPermutations;

import java.util.Arrays;
import java.util.HashMap;

public class CheckPermutations {
	
	public boolean check(String s1, String s2){
		if(s1.length()!=s2.length()){
			return false;
		}
		return sort(s1).equals(sort(s2));
	}
	
	private String sort(String s){
		char [] ar1= s.toCharArray();
		Arrays.sort(ar1);
		return new String(ar1);
	}
	
	public boolean check2(String s1, String s2){
		if(s1.length()!=s2.length()){
			return false;
		}
		
		int [] char_array = new int[128];
		
		for(char c: s1.toCharArray()){
			char_array[c]++;
		}
		
		for(int i=0;i<s1.length();i++){
			int c = (int) s2.charAt(i);
			char_array[c]--;
			if(char_array[c]<0){return false;}
		}
		return true;
	}
	
	public boolean check3(String s1, String s2){
		if(s1.length()!=s2.length()){
			return false;
		}
		
		HashMap<Character,Integer> char_array = new HashMap<>();
		
		for(char c: s1.toCharArray()){
			if(char_array.get(c)!=null){
				char_array.put(c,char_array.get(c)+1);
			}else{
				char_array.put(c,1);
			}
		}
		
		for(int i=0;i<s1.length();i++){
			char c = s2.charAt(i);
			char_array.put(c,char_array.get(c)-1);
			if(char_array.get(c)<0){return false;}
		}
		return true;
	}
	
	
	
	public static void main(String [] ali){
		long startTime = 0;
		long stopTime = 0;
		
		int test = 2;
		
		CheckPermutations p = new CheckPermutations();
		
		switch(test){
		
		case 1:
			startTime = System.nanoTime();
			p.check("care", "race");
			stopTime = System.nanoTime();
			System.out.println(stopTime - startTime);
			break;
		
		case 2:
			startTime = System.nanoTime();
			p.check2("care", "race");
			stopTime = System.nanoTime();
			System.out.println(stopTime - startTime);
			break;
		
		case 3:
			startTime = System.nanoTime();
			p.check3("care", "race");
			stopTime = System.nanoTime();
			System.out.println(stopTime - startTime);
			break;
		
		}		

		
	}
}
