class Solution {
    public String[] solution(String[] names) {
        String[] answer;
        if(names.length%5 == 0){
            answer = new String[names.length/5];
        }    
        else {
            answer = new String[names.length/5+1];
        }
        int count = 0;
        for(int i = 0; i < answer.length; i++){
            answer[i] = names[count];
            count += 5;
        }
        return answer;
    }
}