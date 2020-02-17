/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


package com.mycompany.rk2;

import java.util.regex.Matcher;  
import java.util.regex.Pattern;

class Date {
    
    byte day;
    byte month;
    short year;
    char delimiter;
    
    static Date stringToDate (String str) {
        String temp = "";
        int i = 0;
        
        Date Ret = new Date();
        
        //day
        for ( ; Character.isDigit(str.charAt(i)) && i < str.length(); i++){
            temp += str.charAt(i);
        }
        
        
        //no delimiter
        if (i == str.length()) return null;
        
        //not value
        for (int j = 0; j < temp.length(); j++){
            if (!Character.isDigit(temp.charAt(j))) return null;
        }
        
        
        //length
        if (1 > temp.length() || temp.length() > 2) return null;
        
        //saving
        Ret.day = Byte.parseByte(temp);
        Ret.delimiter = str.charAt(i);
        if (Ret.day > 31 || Ret.day < 1) return null;
        temp = "";
        
        i++;
        
        //month
        for ( ; Character.isDigit(str.charAt(i)) && i < str.length(); i++){
            temp += str.charAt(i);
        }
        
        
        //no second delimiter
        if (i == str.length() || str.charAt(i) != Ret.delimiter) return null;
        
        //not value
        for (int j = 0; j < temp.length(); j++){
            if (!Character.isDigit(temp.charAt(j))) return null;
        }
        
        //length
        if (1 > temp.length() || temp.length() > 2) return null;
        
        //saving
        Ret.month = Byte.parseByte(temp);
        if (Ret.month > 12 || Ret.month < 1) return null;
        temp = "";
        
        i++;
        //year
        for ( ; i < str.length(); i++){
            temp += str.charAt(i);
        }
        
        //not value
        for (int j = 0; j < temp.length(); j++){
            if (!Character.isDigit(temp.charAt(j))) return null;
        }
        
        //length
        if (2 != temp.length() && temp.length() != 4) return null;
        
        //saving
        Ret.year = Short.parseShort(temp);
        
        
        return Ret;
         
    }
}

public class MainClass {
    
    public static void main(String[] args) {
        
        String[] Str = new String[5];
        Str[0] = "31/12/01"; Str[1] = "1/3/1925"; Str[2] = "5/5,12"; Str[3] = "32/1/09"; Str[4] = "30.13.2012";
        
        for (int i = 0; i < Str.length; i++){
            if (Date.stringToDate(Str[i]) == null) System.out.print(Str[i] + " invalid\n");
            else System.out.print(Str[i] + " valid\n");
        }
        for (int i = 0; i < Str.length; i++){
            System.out.println(Pattern.matches("(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((\\d{2})|(\\d{4}))",Str[i]));
                }
        // (0?[1-9]|[12][0-9]|3[01])[^\d](0?[1-9]|1[012])[^\d](\d\d\d\d)
    }
    
}
