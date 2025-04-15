import java.util.HashMap;
import java.util.Map;

public class Questão_4 {
    public static void main(String[] args) {

        // Mapa com os faturamentos por estado
        Map<String, Double> faturamentoEstados = new HashMap<>();
        faturamentoEstados.put("SP", 67836.43);
        faturamentoEstados.put("RJ", 36678.66);
        faturamentoEstados.put("MG", 29229.88);
        faturamentoEstados.put("ES", 27165.48);
        faturamentoEstados.put("Outros", 19849.53);

        
        double total = 0.0;
        for (double valor : faturamentoEstados.values()) {
            total += valor;
        }

        // Calcular e imprimir os percentuais
        System.out.println("Percentual de representação por estado:");
        for (Map.Entry<String, Double> entry : faturamentoEstados.entrySet()) {
            String estado = entry.getKey();
            double valor = entry.getValue();
            double percentual = (valor / total) * 100;
            System.out.printf("%s: %.2f%%%n", estado, percentual);
        }
    }
}
