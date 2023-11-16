import java.util.Random;
import java.util.Scanner;

public class BowlingGame {
  public static void main(String... args) {
    var player1Score = 0;
    var player2Score = 0;
    var round = 1;
    var isLousyLane = true;
    System.out.println("========================================");
    System.out.println("Welcome to Les Terrible Bowling Game!");
    System.out.println("Developed by: Kopi Pasta Studios Pte Ltd");
    System.out.println("========================================");
    var sc = new Scanner(System.in);
    var random = new Random();
    while (true) {
      System.out.println(String.format("Round %d", round));
      System.out.print("Player 1 - Enter a target integer between 1 to 10 (inclusive): ");
      var player1TargetStr = sc.nextLine();
      var player1Target = Integer.parseInt(player1TargetStr);
      float deviation = 0.0f;
      if (player1Target == 5) {
        if (random.nextInt(2) == 0) {
          if (!isLousyLane) {
            deviation = random.nextFloat(-7.0f, 0.0f);
          } else {
            deviation = random.nextFloat(-10.0f, 1.0f);
          }
        } else {
          if (!isLousyLane) {
            deviation = random.nextFloat(0.0f, 7.0f);
          } else {
            deviation = random.nextFloat(-1.0f, 10.0f);
          }
        }
      } else if (player1Target > 5 && player1Target <= 10) {
        deviation = random.nextFloat(-3.0f, 2.0f);
      } else if (player1Target >= 0 && player1Target < 5) {
        deviation = random.nextFloat(-2.0f, 3.0f);
      }
      var actualTarget = Math.floor(player1Target + deviation);
      var score = 0;
      if (actualTarget <= 0) {
        score = 0;
      } else if (actualTarget >= 11) {
        score = 0;
      } else {
        score = 10 - Math.abs((int) actualTarget - 5);
      }
      System.out.println(String.format("Player 1 scores: %d", score));
      player1Score = player1Score + score;
      System.out.print("Player 2 - Enter a target integer between 1 to 10 (inclusive): ");
      var player2TargetStr = sc.nextLine();
      var player2Target = Integer.parseInt(player2TargetStr);
      deviation = 0.0f;
      if (player2Target == 5) {
        if (random.nextInt(2) == 0) {
          deviation = random.nextFloat(-7.0f, 0.0f);
        } else {
          deviation = random.nextFloat(0.0f, 7.0f);
        }
      } else if (player2Target > 5 && player2Target <= 10) {
        deviation = random.nextFloat(-3.0f, 2.0f);
      } else if (player2Target >= 0 && player2Target < 5) {
        deviation = random.nextFloat(-2.0f, 3.0f);
      }
      actualTarget = Math.floor(player2Target + deviation);
      score = 0;
      if (actualTarget <= 0) {
        score = 0;
      } else if (actualTarget >= 11) {
        score = 0;
      } else {
        score = 10 - Math.abs((int) actualTarget - 5);
      }
      System.out.println(String.format("Player 2 scores: %d", score));
      player2Score = player2Score + score;
      round = round + 1;
      if (round > 5) {
        break;
      }
    }
    System.out.println("Game over!");
    if (player1Score > player2Score) {
      System.out.println("Player 1 wins! Score %d to %d".formatted(player1Score, player2Score));
    } else {
      System.out.println("Player 2 wins! Score %d to %d".formatted(player2Score, player1Score));
    }
    sc.close();
  }
}
