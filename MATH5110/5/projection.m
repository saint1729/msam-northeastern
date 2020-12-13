function prj = projection(y, A)
    [m, n] = size(A);
    prj = zeros(m, 1);
    B = NBasis(A);
    for i = 1:n
        prj = prj + dot(y, B(:, i)) * B(:, i);
    end
    return;