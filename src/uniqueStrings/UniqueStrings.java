package uniqueStrings;

import java.util.HashMap;

/**
 * Two different methods for testing if a string has unique characters. 
 * Shows the speed difference in these method. The smarter method is almost 10x faster. The joy of hashmaps.
 * @author sachagunaratne  
 * */

public class UniqueStrings {
	
	/**
	 * Brute force method. O(N*N)
	 * */
	public boolean hasUniqueBruteForce(String s){
		for(int i=0;i<s.length();i++){
			for(int j=0;j<s.length();j++){
				if(s.charAt(i)==s.charAt(j)){
					return false;
				}
			}
		}
		return true;
	}
	
	/**
	 * Faster more efficient method. O(N)*O(1) = O(N)
	 * */
	public boolean hasUniqueSmart(String s){
		HashMap<Character, Integer> map = new HashMap<Character,Integer>();
		for(int i=0;i<s.length();i++){
			char chara = s.charAt(i);
			if(map.get(chara) != null){
				return false;
			}
			map.put(chara, 1);
		}
		return true;
	}
	
	/**
	 * Using a int array to keep track of the chars. Not the best idea because of the setsize. 
	 * */
	public boolean hasUniqueUseIntArray(String s){
		int [] char_array = new int[128];
		for(int i=0;i<s.length();i++){
			int chara = s.charAt(i);
			if(char_array[i]!=0){
				return false;
			}
			char_array[i]=chara;
		}
		return true;
	}
	
	public static void main(String [] args){
		long startTime = 0;
		long stopTime = 0;
		int testcase = 2;
		
		UniqueStrings test = new UniqueStrings();
		switch(testcase) {
		
		case 1:
			startTime = System.nanoTime();
			test.hasUniqueBruteForce("cahrimeykwfdyjfhfgyj");
			stopTime = System.nanoTime();
			System.out.println(stopTime - startTime);
			break;
		
		case 2:
			startTime = System.nanoTime();
			test.hasUniqueSmart("cahrimeykwfdyjfhfgyj");
			stopTime = System.nanoTime();
			System.out.println(stopTime - startTime);
			break;
		
		case 3:
			startTime = System.nanoTime();
			test.hasUniqueUseIntArray("cahrimeykwfdyjfhfgyj");
			stopTime = System.nanoTime();
			System.out.println(stopTime - startTime);
			break;
		
		}
	}
}
