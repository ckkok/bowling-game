import java.util.Random;
import java.util.Scanner;

public class BowlingGame {
  public static void main(String... args) {
    var s1 = 0;
    var s2 = 0;
    var rnd = 1;
    var laneFlag = true;
    System.out.println("========================================");
    System.out.println("Welcome to Les Terrible Bowling Game!");
    System.out.println("Developed by: Kopi Pasta Studios Pte Ltd");
    System.out.println("========================================");
    var sc = new Scanner(System.in);
    var rndm = new Random();
    while (true) {
      System.out.println(String.format("Round %d", rnd));
      System.out.print("Player 1 - Enter a target integer between 1 to 10 (inclusive): ");
      var t1Str = sc.nextLine();
      var t1 = Integer.parseInt(t1Str);
      float dev = 0.0f;
      if (t1 == 5) {
        if (rndm.nextInt(2) == 0) {
          if (!laneFlag) {
            dev = rndm.nextFloat(-7.0f, 0.0f);
          } else {
            dev = rndm.nextFloat(-10.0f, 1.0f);
          }
        } else {
          if (!laneFlag) {
            dev = rndm.nextFloat(0.0f, 7.0f);
          } else {
            dev = rndm.nextFloat(-1.0f, 10.0f);
          }
        }
      } else if (t1 > 5 && t1 <= 10) {
        dev = rndm.nextFloat(-3.0f, 2.0f);
      } else if (t1 >= 0 && t1 < 5) {
        dev = rndm.nextFloat(-2.0f, 3.0f);
      }
      var tgt = Math.floor(t1 + dev);
      var score = 0;
      if (tgt <= 0) {
        score = 0;
      } else if (tgt >= 11) {
        score = 0;
      } else {
        score = 10 - Math.abs((int) tgt - 5);
      }
      System.out.println(String.format("Player 1 scores: %d", score));
      s1 = s1 + score;
      System.out.print("Player 2 - Enter a target integer between 1 to 10 (inclusive): ");
      var t2Str = sc.nextLine();
      var t2 = Integer.parseInt(t2Str);
      dev = 0.0f;
      if (t2 == 5) {
        if (rndm.nextInt(2) == 0) {
          dev = rndm.nextFloat(-7.0f, 0.0f);
        } else {
          dev = rndm.nextFloat(0.0f, 7.0f);
        }
      } else if (t2 > 5 && t2 <= 10) {
        dev = rndm.nextFloat(-3.0f, 2.0f);
      } else if (t2 >= 0 && t2 < 5) {
        dev = rndm.nextFloat(-2.0f, 3.0f);
      }
      tgt = Math.floor(t2 + dev);
      score = 0;
      if (tgt <= 0) {
        score = 0;
      } else if (tgt >= 11) {
        score = 0;
      } else {
        score = 10 - Math.abs((int) tgt - 5);
      }
      System.out.println(String.format("Player 2 scores: %d", score));
      s2 = s2 + score;
      rnd = rnd + 1;
      if (rnd > 5) {
        break;
      }
    }
    System.out.println("Game over!");
    if (s1 > s2) {
      System.out.println("Player 1 wins! Score %d to %d".formatted(s1, s2));
    } else {
      System.out.println("Player 2 wins! Score %d to %d".formatted(s2, s1));
    }
    sc.close();
  }
}
