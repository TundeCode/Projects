#include <iostream>

bool validSudoku(int board[9][9]) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            int num = board[i][j];

            for (int col = 0; col < 9; col++) {
                if (col != j && board[i][col] == num) {
                    return false; //if dups are found
                }
            }

            for (int row = 0; row < 9; row++) {
                if (row != i && board[row][j] == num) {
                    return false;
                }
            }

            int subgridRow = (i / 3) * 3;
            int subgridCol = (j / 3) * 3;
            for (int row = subgridRow; row < subgridRow + 3; row++) {
                for (int col = subgridCol; col < subgridCol + 3; col++) {
                    if (row != i && col != j && board[row][col] == num) {
                        return false;
                    }
                }
            }
        }
    }
    return true; // Only if it's valid
}

int main() {
    int board[9][9];

    // Fill Sudoku matrix
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            std::cin >> board[i][j];
        }
    }

    // Print Sudoku matrix
    // for (int i = 0; i < 9; i++) {
    //     for (int j = 0; j < 9; j++) {
    //         std::cout << board[i][j];
    //     }
       
    // }
    // std::cout << std::endl;
    if (validSudoku(board)) {
        std::cout << "Solution is good!";
    } else {
        std::cout << "Wrong solution!";
    }

    return 0;
}
