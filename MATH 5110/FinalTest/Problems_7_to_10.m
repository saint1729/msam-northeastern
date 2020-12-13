problem_7 = true;
problem_8 = true;
problem_9 = true;
problem_10 = true;

% Problem 7
A = [[1, 1, 6]; [1, 2, 7]; [1, 3, 8]; [1, 4, 9]; [1, 5, 0]];

[U, S, V] = svd(A);

if problem_7 == true
    disp("Problem 7 begins here")
    disp(round(U, 2));
    disp(round(S, 2));
    disp(round(V', 2));
    disp("Problem 7 ends here")
end


% Problem 8
B = [[2, 1, 1, 1, 1]; [1, 2, 1, 1, 1]; [1, 1, 2, 1, 1]; [1, 1, 1, 2, 1]; [1, 1, 1, 1, 2]];

[U1, D] = eig(B);

if problem_8 == true
    disp("Problem 8 begins here")
    disp(D);
    % Here U1 is obtained from MATLAB. Fortunately, it is already
    % Orthogonal, but I am not using it :)
    P1 = NBasis(U1);
    % U2 is obtained by me by calculating eigen vectors. It is not
    % orthogonal. Hence, using Gram-Schmidt.
    U2 = [[-1, -1, -1, -1, 1]; [1, 0, 0, 0, 1]; [0, 1, 0, 0, 1]; [0, 0, 1, 0, 1]; [0, 0, 0, 1, 1]];
    P2 = NBasis(U2);
    disp(sym(P2));
    disp("Problem 8 ends here")
end


% Problem 9 (This is just for verification)
M = 1/7 * (B + eye(5));

if problem_9 == true
    disp("Problem 9 begins here")
    ones = [1; 1; 1; 1; 1];
    disp(ones);
    disp(M^100);
    disp("Problem 9 ends here")
end


% Problem 10
A = [[1, 1, 1]; [1, 1, 2]; [1, 2, 1]; [1, 3, 4]; [1, 3, 2]];
v = [3; 6; 9; 3; 0];
if problem_10 == true
    disp("Problem 10 begins here")
    w = A \ v;
    disp(w);
    disp(norm(v - A * w)^2);
    disp("Problem 10 ends here")
end




