
import java.util.HashMap;
import model.CommonModel;
public class Roulette extends MyMethods {
	public CommonModel MainRoutelle(CommonModel model) {
		int[][] rouletteNumbers = { {0, 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36},//こっちが赤
				{00, 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}}; //こっちが黒
		HashMap<Integer, Integer> userSelecRed = new HashMap<Integer, Integer>();
		userSelecRed.put(1, 1);
		userSelecRed.put(3, 2);
		userSelecRed.put(5, 3);
		userSelecRed.put(7, 4);
		userSelecRed.put(9, 5);
		userSelecRed.put(12, 6);
		userSelecRed.put(14, 7);
		userSelecRed.put(16, 8);
		userSelecRed.put(18, 9);
		userSelecRed.put(19, 10);
		userSelecRed.put(21, 11);
		userSelecRed.put(23, 12);
		userSelecRed.put(25, 13);
		userSelecRed.put(27, 14);
		userSelecRed.put(30, 15);
		userSelecRed.put(32, 16);
		userSelecRed.put(34, 17);
		userSelecRed.put(36, 18);
		HashMap<Integer, Integer> userSelecBlack = new HashMap<Integer, Integer>();
		userSelecBlack.put(2, 1);
		userSelecBlack.put(4, 2);
		userSelecBlack.put(6, 3);
		userSelecBlack.put(8, 4);
		userSelecBlack.put(10, 5);
		userSelecBlack.put(11, 6);
		userSelecBlack.put(13, 7);
		userSelecBlack.put(15, 8);
		userSelecBlack.put(17, 9);
		userSelecBlack.put(20, 10);
		userSelecBlack.put(22, 11);
		userSelecBlack.put(24, 12);
		userSelecBlack.put(26, 13);
		userSelecBlack.put(28, 14);
		userSelecBlack.put(29, 15);
		userSelecBlack.put(31, 16);
		userSelecBlack.put(33, 17);
		userSelecBlack.put(35, 18);
		System.out.println("ではルーレットを始めよう！");
		System.out.println("最初にいくら賭けるか入力してね");
		while (true) {
			System.out.println("現在の所持金: " + model.getMoney());
			int bitMoney = intKey();
			System.out.println("");
			//入力チェック
			if (bitMoney > model.getMoney()) {
				System.out.println("そんなに持ってないよ！また入力してね");
				continue;
			}  else if (bitMoney == 0) {
				System.out.println("必ず何か賭けてね");
				System.out.println("いくら賭ける？");
				continue;
			}
			System.out.println("賭け金: " + bitMoney);
			model.setMoney(model.getMoney() - bitMoney);
			System.out.println("次に、どこに賭けるか決めてね");
			System.out.println("1: 0   2: 00,   3: 赤   4: 黒");
			int chooseBit = intKey();
			//勝ち負けのための初期化
			//あまりいいアイディアであるとは思えない・・・
			int bit = 0;
			switch (chooseBit) {
			case 1:
				System.out.println("選んだ数字: 0");
				break;
			case 2:
				System.out.println("選んだ数字: 00");
				break;
			case 3://赤
				System.out.println("赤のどれを選ぶ？");
				for (int i = 1; i < 19; i++) {
					System.out.println(rouletteNumbers[0][i] + " ");
				}
				int playerBitRed = intKey();
				bit = rouletteNumbers[0][userSelecRed.get(playerBitRed)];
				System.out.println("選んだ数字: 赤の" + bit);
				break;
			case 4:
				System.out.println("黒のどれを選ぶ？");
				for (int i = 1; i < 19; i++) {
					System.out.println(rouletteNumbers[1][i] + " ");
				}
				int playerBitBlack = intKey();
				bit = rouletteNumbers[0][userSelecBlack.get(playerBitBlack)];
				System.out.println("選んだ数字: 黒の" + bit);
				break;
			}//Switchの終わり
			/**
			 * 当選番号の決定
			 * 行と列のインデックスを乱数で指定
			 */
			int computerBit;
			//行のインデックス
			int computerBit1 = rand(2);
			//列のインデックス
			int computerBit2 = rand(18) + 1;
			//2次元配列から取り出す
			computerBit = rouletteNumbers[computerBit1][computerBit2];
			//当選番号の発表
			for (int i = 0; i < 5; i++) {
				System.out.println("・");
			}
			switch (computerBit1) {
			case 0:
				if (computerBit1 == 0) {
					if (computerBit2 == 0) {
						System.out.println("当たり番号: " + computerBit);
					} else {
						System.out.println("当たり番号: 赤" + computerBit);
					}
				}//ifの終わり
			case 1:
				if (computerBit1 == 1) {
					if (computerBit2 == 0) {
						System.out.println("当たり番号: " + computerBit);
					} else {
						System.out.println("当たり番号: 黒" + computerBit);
					}
				}
			}//switchの終わり
			//勝ち負け
			if (bit == computerBit) {
				System.out.println("おめでとう！君の勝ちだ！");
				model.setMoney(model.getMoney() + bitMoney*36);
				System.out.println("所持金: " + model.getMoney());
			} else {
				System.out.println("残念！君の負けだ");
				model.setMoney(model.getMoney());
				System.out.println("所持金: " + model.getMoney());
			}
			System.out.println("遊んでくれてありがとう！");
			//model.setTurn(model.getTurn() + 1);
			return model;
		}//whileの終わり
	}//メソッドの終わり
}//クラスの終わり