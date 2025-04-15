import java.util.Scanner;

public class Questão_5 {

    private static void inverte(String entrada) {
        int tamanho = entrada.length();
        for(int i = 0; i < tamanho / 2; i++) {
            char aux = entrada.charAt(i);
            
            entrada = entrada.substring(0, i) + entrada.charAt(tamanho - 1 - i) + entrada.substring(i + 1, tamanho - 1 - i) + aux + entrada.substring(tamanho - i);

        }

        System.out.println("String invertida: " + entrada);
    }
     public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);

        System.out.println("Informe uma string: ");
        String entrada = leitura.nextLine();

        inverte(entrada);
        leitura.close();
    }
}
