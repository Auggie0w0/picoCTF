import java.util.Scanner;

public class Caesar {

    // ONE unified shiftChar: handles letters (A–Z, a–z) and digits (0–9)
    static char shiftChar(char c, int shift) {
        // Letters
        if (Character.isLetter(c)) {
            int k = ((shift % 26) + 26) % 26; // normalize for 26 letters
            if (Character.isUpperCase(c)) {
                int base = 'A';
                int idx = c - base;               // 0..25
                int newIdx = (idx + k) % 26;
                return (char) (base + newIdx);
            } else {
                int base = 'a';
                int idx = c - base;               // 0..25
                int newIdx = (idx + k) % 26;
                return (char) (base + newIdx);
            }
        }

        // Digits
        if (Character.isDigit(c)) {
            int k = ((shift % 10) + 10) % 10;     // normalize for 10 digits
            int base = '0';
            int idx = c - base;                   // 0..9
            int newIdx = (idx + k) % 10;
            return (char) (base + newIdx);
        }

        // Everything else unchanged
        return c;
    }

    static String encrypt(String text, int shift) {
        StringBuilder sb = new StringBuilder(text.length());
        for (int i = 0; i < text.length(); i++) {
            sb.append(shiftChar(text.charAt(i), shift));
        }
        return sb.toString();
    }

    static String decrypt(String text, int shift) {
        return encrypt(text, -shift);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Caesar Cipher ===");
        System.out.println("1) cipher (encrypt)");
        System.out.println("2) decipher (decrypt, with known shift)");
        System.out.println("3) brute-force decipher (unknown shift)");
        System.out.print("Choose 1, 2, or 3: ");
        String choice = sc.nextLine().trim();

        if (choice.equals("1")) {
            // Encrypt
            int shift = readShift(sc);
            if (shift == Integer.MIN_VALUE) { sc.close(); return; }
            System.out.print("Enter the text: ");
            String text = sc.nextLine();
            System.out.println("Encrypted: " + encrypt(text, shift));

        } else if (choice.equals("2")) {
            // Decrypt with known shift
            int shift = readShift(sc);
            if (shift == Integer.MIN_VALUE) { sc.close(); return; }
            System.out.print("Enter the cipher text: ");
            String cipher = sc.nextLine();
            System.out.println("Decrypted: " + decrypt(cipher, shift));

        } else if (choice.equals("3")) {
            // Brute-force decrypt: try all shifts
            System.out.print("Enter the cipher text: ");
            String cipher = sc.nextLine();
            System.out.println("\nTrying all possible shifts (1–25):");
            for (int shift = 1; shift < 26; shift++) {
                String guess = decrypt(cipher, shift);
                System.out.println("Shift " + shift + ": " + guess);
            }

        } else {
            System.out.println("Invalid choice.");
        }

        sc.close();
    }

    // small helper to safely read an integer shift
    private static int readShift(Scanner sc) {
        System.out.print("Enter shift (integer, e.g., 3 or -1): ");
        String shiftStr = sc.nextLine().trim();
        try {
            return Integer.parseInt(shiftStr);
        } catch (NumberFormatException e) {
            System.out.println("Invalid shift. Please run again and enter a whole number.");
            return Integer.MIN_VALUE;
        }
    }
}