% 2.1 Solution

M = [3, 0, 11.3, 56.8;
    5, 6, 14.5, 78.3;
    7, 12, 36.9, 17.2;
    9, 18, 25.3, 33];

D = [1.2, 3.6, 62, 77;
    1.3, 6.9, 108, 81;
    1.5, 8.3, 78, 94;
    5.6, 31, 578, 204];

C1 = rref([M D(:, 1)]);
C1 = C1(:, size(C1, 2));
C2 = rref([M D(:, 2)]);
C2 = C2(:, size(C2, 2));
C3 = rref([M D(:, 3)]);
C3 = C3(:, size(C3, 2));
C4 = rref([M D(:, 4)]);
C4 = C4(:, size(C4, 2));

A = [C1';
C2';
C3';
C4';];

disp(A);



% 2.2 Solutions

newOutputs = [1.7; 9.3; 62; 66];
solution = rref([A newOutputs]);

disp(solution(:, size(solution, 2)));


