public class CaesarDecoder {
    
    /**
     * Decodes a Caesar cipher by shifting each letter by the specified amount.
     * 
     * @param ciphertext The encoded message
     * @param shift The number of positions to shift each letter
     * @return The decoded message
     */
    public static String caesarDecode(String ciphertext, int shift) {
        StringBuilder result = new StringBuilder();
        
        for (char c : ciphertext.toCharArray()) {
            if (Character.isLetter(c)) {
                // Determine ASCII offset (97 for lowercase, 65 for uppercase)
                int asciiOffset = Character.isLowerCase(c) ? 97 : 65;
                
                // Convert to 0-25, shift, and wrap around with modulo
                int shifted = (c - asciiOffset - shift) % 26;
                
                // Handle negative modulo result
                if (shifted < 0) {
                    shifted += 26;
                }
                
                // Convert back to ASCII and add to result
                result.append((char) (shifted + asciiOffset));
            } else {
                // Keep non-alphabetic characters as they are
                result.append(c);
            }
        }
        
        return result.toString();
    }
    
    public static void main(String[] args) {
        // Import Scanner for user input
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        
        // Prompt user for input
        System.out.print("Enter the encoded message: ");
        String ciphertext = scanner.nextLine();
        
        System.out.println("Trying all 26 possible Caesar cipher shifts:");
        System.out.println("-".repeat(50));
        
        // Try all possible shifts (0-25)
        for (int shift = 0; shift < 26; shift++) {
            String decoded = caesarDecode(ciphertext, shift);
            System.out.printf("Shift %2d: %s%n", shift, decoded);
        }
        
        // Close the scanner
        scanner.close();
    }
}