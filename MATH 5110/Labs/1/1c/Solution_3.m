% Solution 1.3.4

R = [0.67; 0.33];
B = [0.14; 0.08];
G = [0.21; 0.71];

RBG = [R, B, G];

X = [0.3; 0.5];

M = [RBG; [1, 1, 1]];

rbg = M\([X; 1]);

disp(rbg);


% Solution 1.3.5

X_prime = 2 * ((R + B + G) / 3 - X / 2);

disp(X_prime);

disp(M\([X_prime; 1]));


