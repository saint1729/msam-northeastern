function Y = plotphase(A, x_range, y_range, N)
    [X, Y] = meshgrid(x_range, y_range);
    Populations = ["Beetles", "Frogs"];

    X = reshape(X, 1, numel(X));
    Y = reshape(Y, 1, numel(Y));
    XY = [X; Y];

    x = -2:0.1:8;
    y = x;

    plots = size(N, 2);
    rootN = sqrt(plots);
    for j = 1:plots
        XY_new = (A^N(j)) * XY;
        UV = XY_new - XY;
        subplot(rootN, rootN, j);
        plot(x, y, '-', 'DisplayName', 'y = x line');
        hold on;
%         plot(X, Y, '.');
        plot(X, Y, '.', 'DisplayName', strcat('N = ', int2str(N(j))));
        hold on;
        quiver(X, Y, UV(1, :), UV(2, :), 'DisplayName' , 'Quiver');
        hold on;
    end
    xlabel(Populations(1));
    ylabel(Populations(2));
    legend;
    hold off;
end