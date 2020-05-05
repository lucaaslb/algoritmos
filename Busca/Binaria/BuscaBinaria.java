package algoritmos;

public class BuscaBinaria {

	public static void main(String[] args) {
		int[] dados = { 1, 2, 30, 41, 73, 81, 90, 101 };

		System.out.println(BuscaBin(dados, 81));
		System.out.println(BuscaBin(dados, 103));
	}

	public static int BuscaBin(int[] lista, int valorBuscado) {
		int cursorBaixo = 0;
		int cursorAlto = lista.length - 1;

		int meio = 0;

		while (cursorBaixo <= cursorAlto) {
			meio = (cursorBaixo + cursorAlto) / 2;
			int chute = lista[meio];

			if (chute == valorBuscado) {
				return meio;
			} else if (chute > valorBuscado) {
				cursorAlto = meio - 1;
			} else {
				cursorBaixo = meio + 1;
			}
		}

		return -1;
	}

	public static void BuscaBinRecursiva() {

	}
}
