function Y = plotmodelsub(A, P, N)
    k = size(P, 1);
    disp(N);
    Y = zeros(k, N);
    
    Populations = ["Beetles", "Frogs"]
    
    Y(:, 1) = P;
    for i = 2:N
        Y(:, i) = (A^i) * Y(:, 1);
    end
    
    for i = 1:k
        subplot(2, 1, i);
        plot(Y(i, :), 'DisplayName', Populations(i));
        xlabel('Time')
        ylabel('Population')
        hold on
    end
    
    legend
    hold off
end