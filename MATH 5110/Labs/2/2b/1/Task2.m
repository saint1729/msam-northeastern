A = 1/8 * [[1, 2, 1]; [3, 4, 1]; [2, 3, 4]];
u = [1; 2; 1];
w = [0; 1; 2];

B = 1/5 * u * w';

% 2.1

M1 = getMatrix(A, B, 0);

disp(eig(M1));

% 2.2

M2 = getMatrix(A, B, 1);

disp(eig(M2));

% Assumption: 'm' is positive
m = 1;

while true
    M3 = getMatrix(A, B, -m);
    eigs = eig(M3);
    if (abs(eigs(1)) >= 1) || (abs(eigs(2)) >= 1) || (abs(eigs(3)) >= 1)
        break
    end
    m = m + 1;
end

disp(m);


% 2.3

a = 0;
b = 0;
foundPositive = false;
foundNegative = false;
while true
    if ~foundPositive
        M4 = getMatrix(A, B, a);
        eigs = eig(M4);
        if (abs(eigs(1)) >= 1) || (abs(eigs(2)) >= 1) || (abs(eigs(3)) >= 1)
            foundPositive = true;
        end
        a = a - 0.01;
    end
    
    if ~foundNegative
        M4 = getMatrix(A, B, b);
        eigs = eig(M4);
        if (abs(eigs(1)) >= 1) || (abs(eigs(2)) >= 1) || (abs(eigs(3)) >= 1)
            foundNegative = true;
        end
        b = b + 0.01;
    end
    
    if foundPositive && foundNegative
        break
    end
end

disp(a);
disp(b);





