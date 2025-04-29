import java.util.HashMap;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] array = s.split(" ");

        if(array.length != pattern.length()){
            return false;
        }


        HashMap<Character, String> hash_chr = new HashMap<>();
        HashMap<String, Character> hash_str = new HashMap<>();

        for (int i = 0; i < array.length; i++){
            char patternChar = pattern.charAt(i);
            String arrayStr = array[i];

        if(hash_chr.containsKey(patternChar) && !hash_chr.get(patternChar).equals(arrayStr)){
                return false;
            }


            if(hash_str.containsKey(arrayStr) && !hash_str.get(arrayStr).equals(patternChar)){
                return false;
            }

            hash_chr.put(patternChar, arrayStr);
            hash_str.put(arrayStr, patternChar);

        }
        return true;

        
    }
}