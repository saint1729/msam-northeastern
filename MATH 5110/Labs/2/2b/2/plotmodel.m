function Y = plotmodel(A, P, N)
    k = size(P, 1);
    disp(N);
    Y = zeros(k, N);
    
    Populations = ["Beetles", "Frogs"]
    
    Y(:, 1) = P;
    for i = 2:N
        Y(:, i) = (A^i) * Y(:, 1);
    end
    
    for i = 1:k
        plot(Y(i, :), 'DisplayName', Populations(i));
        hold on
    end
    
    legend
    xlabel('Time')
    ylabel('Population')
    hold off
end