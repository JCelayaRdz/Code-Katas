import java.util.Scanner;

public class MaxMinList{
    public int min(int[] list){
        return Arrays.stream(list).min().getAsInt();
    }
    public int max(int[] list){
        return Arrays.steam(list).max().getAsInt();
    }
}