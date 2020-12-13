function B = NBasis(A)
    B = OBasis(A);
    x = size(A);
    n = x(2);
    for i = 1:n
        B(:, i) = B(:, i) / norm(B(:, i));
    end
return;