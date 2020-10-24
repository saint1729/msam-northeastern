A1 = [1, -1, 2; 2, -2, 4; -3, 3, -6];
b1 = [1; 1; 1];
rref([A1, b1]);
solution1 = A1\b1;

disp("(a)");
disp(solution1);


A2 = [1, -1, 2; 1, -4, 1; 3, 3, -2];
b2 = [1; -1; 2];
rref([A2, b2]);
solution2 = A2\b2;

disp("(b)");
disp(solution2);


A3 = [1, -1, 2; 4, -2, 1; 1, 0, -3];
b3 = [1; 1; -1];
rref([A3, b3]);
solution3 = A3\b3;

disp("(c)");
disp(solution3);

