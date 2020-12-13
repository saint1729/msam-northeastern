function B = OBasis(A)
    [m, n] = size(A);
    B = zeros(m, n);
    for i = 1:n
        B(:, i) = A(:, i);
        for j = 1:(i - 1)
            B(:, i) = B(:, i) - dot(B(:, j), A(:, i)) / norm(B(:, j))^2 * B(:, j);
        end
    end
return;