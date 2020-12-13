A = [[1, 0]; [1, 0]; [0, 1]; [2, -1]];
disp(OBasis(A));
disp(NBasis(A));
disp(projection([2, 4, 0, 2], A));

syms x y;
B = [[x, y]; [1 - x, 1 - y]];
disp(B);
[P, D] = eig(B);
disp(P);
disp(D);
disp(simplify(inv(P)));
D(2, 2) = 1;
disp(D(2, 2));
X = P * D * inv(P);
disp(simplify(X));
