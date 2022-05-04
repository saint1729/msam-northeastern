function [] = plot_logreg_figure (X0, X1, X, beta)

mn = - beta(1) / beta(2) - beta(3) / beta(2) * min(X(:, 3));
mx = - beta(1) / beta(2) - beta(3) / beta(2) * max(X(:, 3));
x1 = mn : (mx - mn) / 100 : mx;
x2 = - beta(1) / beta(3) - beta(2) / beta(3) * x1;
% x2 = - beta(1) / beta(3) - beta(2) / beta(3) * x1 + 0.5 / beta(3); %Fuxiao

plot(X0(:, 1), X0(:, 2), 'o', X1(:, 1), X1(:, 2), 'x', x1, x2, 'r', 'LineWidth', 2);
axis([(min(X(:, 2)) - 0.5) (max(X(:, 2)) + 0.5) (min(X(:, 3)) - 0.5) (max(X(:, 3)) + 0.5)]);
xlabel('x_1');
ylabel('x_2');

return