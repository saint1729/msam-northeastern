function Y = plotquiver(A, P, N)
    k = size(P, 1);
    cols = size(P, 2);
    disp(k);
    disp(N);
    disp(cols);
    Y = zeros(k, N, cols);
    
    Populations = ["Beetles", "Frogs"];
    
    for j = 1:cols
        Y(:, 1, j) = P(:, j);
        for i = 2:N
            Y(:, i, j) = (A^i) * Y(:, 1, j);
        end
    end
    
    figure;
    for k = 1:cols
        scatter(Y(1, :, k), Y(2, :, k), 'filled');
        hold on;
        x = Y(1, 1:N-1, k);
        y = Y(2, 1:N-1, k);
        u = Y(1, 2:N, k) - Y(1, 1:N-1, k);
        v = Y(2, 2:N, k) - Y(2, 1:N-1, k);
        quiver(x, y, u, v);
    end
        
    legend;
    xlabel(Populations(1));
    ylabel(Populations(2));
    hold off;
end