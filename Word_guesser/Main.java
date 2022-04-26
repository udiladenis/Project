package com.company;
import java.util.*;

public class Main {
    public static void start_game_message(){
        System.out.println("Hello there and welcome to my first Java application! :)");
        System.out.println("This is a word guesser game! Your task is to guess the word that has been choosen from certain domain lists.");
        System.out.println("First of all you will have to choose from a category of domains. This domains contain specific words and from that choosen doamin, a random word will pe picked by computer and you will have to guess it");
        System.out.println("\n" + "Let's settle some rules: " + "\n" + "1. You will have only 3 chances to guess the word!" +" \n" + "2. If you run out of lifes, a certain message will apear and the program will end" + "\n" + "3. And the most important: Have FUN! :)");
    }

    public static void end_game(){
        System.exit(0);
    }

    public static void start_game(){
        Scanner obj = new Scanner(System.in);
        System.out.println("\n" + "Do you want to play a game?");

        String answer = obj.nextLine();
       if(answer.equals("Yes") || (answer.equals("Y"))) {
           String[] C = {"memory_management", "pointers", "game_dev"};
           String[] oop = {"encapsulation", "inheritance", "polymorphism", "abstraction"};
           String[] python = {"data-science", "AI", "easy language"};

           while (true) {
               System.out.println("Please select one of the next: C, OOP, Python");
               String choice = obj.nextLine();
               String random;

               int lifes = 3;

               if (choice.equals("C")) {
                   Random randomizer = new Random();
                   random = C[randomizer.nextInt(C.length)];

                   System.out.println("You selected: " + choice);
                   while(true) {
                       System.out.println("Choose a word from the next list: ");
                       System.out.println(Arrays.toString(C));
                       String user_choice = obj.nextLine();

                       if (lifes >= 0) {
                           if (user_choice.equals(random)) {
                               System.out.println("Congrats! You guessed it!");
                               break;
                           } else {
                               System.out.println("Wrong!");
                               lifes -= 1;
                               System.out.println("Remained lifes " + lifes);
                           }
                       }
                       else{
                           System.out.println("You just runned out of your lifes!");
                           end_game();
                       }
                   }
                   break;

               }
               else if (choice.equals("oop")) {
                   Random randomizer = new Random();
                   random = oop[randomizer.nextInt(oop.length)];

                   System.out.println("You selected: " + choice);
                   while(true) {
                       System.out.println("Choose a word from the next list: ");
                       System.out.println(Arrays.toString(oop));
                       String user_choice = obj.nextLine();

                       if (lifes >= 0) {
                           if (user_choice.equals(random)) {
                               System.out.println("Congrats! You guessed it!");
                               break;
                           } else {
                               System.out.println("Wrong!");
                               lifes -= 1;
                               System.out.println("Remained lifes " + lifes);
                           }
                       }
                       else{
                           System.out.println("You just runned out of your lifes!");
                           end_game();
                       }
                   }
                   break;

               }
               else if (choice.equals("Python")) {
                   Random randomizer = new Random();
                   random = python[randomizer.nextInt(python.length)];

                   System.out.println("You selected: " + choice);
                   while(true) {
                       System.out.println("Choose a word from the next list: ");
                       System.out.println(Arrays.toString(python));
                       String user_choice = obj.nextLine();

                       if (lifes >= 0) {
                           if (user_choice.equals(random)) {
                               System.out.println("Congrats! You guessed it!");
                               break;
                           } else {
                               System.out.println("Wrong!");
                               lifes -= 1;
                               System.out.println("Remained lifes " + lifes);
                           }
                       }

                       else{
                           System.out.println("You just runned out of lifes!");
                           end_game();
                       }
                   }
                   break;

               }
               else {
                   System.out.println("Unknown filed! Please try again!" + "\n");
               }
           }
       }
       else{
           System.out.println("Have a nice day then! :)");
           end_game();
       }
    }

    public static void main(String[] args) {
	start_game_message();
    start_game();
    }
}
