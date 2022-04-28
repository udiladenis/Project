package com.company;
import java.util.Random;
import java.util.Scanner;

public class Main {

    public static String computerMove(String [] choices){
        String move;
        move = choices[new Random().nextInt(choices.length)];

        return move;
    }

    public static String userMove(String [] choices) {
        Scanner obj = new Scanner(System.in);
        String userM;

        while (true) {
            System.out.println("Please choose from: Rock, Paper, Scissors");
            userM = obj.nextLine();

            if (userM.equals("Rock") || userM.equals("Paper") || userM.equals("Scissors")) {
                break;
            }
            else{
                System.out.println(userM + " is not a valid input!");
            }
        }
        return userM;
    }
    public static void main(String[] args) {
        String[] game_choice = {"Rock", "Paper", "Scissors"};
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter the number of games: (odd number)");
        int nr_of_games = scanner.nextInt();

        int user_points = 0;
        int comp_points = 0;

        if (nr_of_games % 2 != 0) {
            while (nr_of_games >= 1) {
                String user = userMove(game_choice);
                String comp = computerMove(game_choice);

                System.out.println("User choice: " + user + "\n" + "Computer choice: " + comp);
                //Game logic
                if (user.equals(comp)) {
                    System.out.println("It's a tie");

                    user_points+=1;
                    comp_points+=1;
                    nr_of_games-=1;
                    System.out.println("\n"+ "Computer points: " + comp_points + "\n" + "User points: " + user_points);

                }
                else if (user.equals("Rock")) {
                    if (comp.equals("Paper")) {
                        System.out.println("Computer wins this round!");
                        comp_points+=1;
                        nr_of_games-=1;
                        System.out.println("\n"+ "Computer points: " + comp_points + "\n" + "User points: " + user_points);

                    } else {
                        System.out.println("You win this round");
                        user_points+=1;
                        nr_of_games-=1;
                        System.out.println("\n"+ "Computer points: " + comp_points + "\n" + "User points: " + user_points);

                    }
                }
                else if (user.equals("Scissors")) {
                    if (comp.equals("Rock")) {
                        System.out.println("Computer wins this round!");
                        comp_points-=1;
                        nr_of_games-=1;
                        System.out.println("\n"+ "Computer points: " + comp_points + "\n" + "User points: " + user_points);

                    } else {
                        System.out.println("You win this round");
                        user_points+=1;
                        nr_of_games-=1;
                        System.out.println("\n"+ "Computer points: " + comp_points + "\n" + "User points: " + user_points);

                    }
                }
                else if (user.equals("Paper")) {
                    if (comp.equals("Rock")) {
                        System.out.println("You win this round!");
                        user_points+=1;
                        nr_of_games-=1;
                        System.out.println("\n"+ "Computer points: " + comp_points + "\n" + "User points: " + user_points);

                    } else {
                        System.out.println("Computer wins this round!");
                        System.out.println("\n"+ "Computer points: " + comp_points + "\n" + "User points: " + user_points);

                    }
                }

            }
        }
        if(comp_points > user_points){
            System.out.println("The winner of this game is computer!");
        }
        else if (user_points > comp_points){
            System.out.println("The winner of this game is user!");
        }
        else if (user_points == comp_points){
            System.out.println("There is a tie!");
        }
    }
}
