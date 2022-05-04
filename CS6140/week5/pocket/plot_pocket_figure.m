function [] = plot_pocket_figure (X0, X1, X, beta, varargin)

% function [] = plot_pocket_figure (X0, X1, X, beta, beta_pocket, best_run)

title_string = 'Pocket Algorithm';

% line #1
mn = - beta(1) / beta(2) - beta(3) / beta(2) * min(X(:, 3));
mx = - beta(1) / beta(2) - beta(3) / beta(2) * max(X(:, 3));
x1 = mn : (mx - mn) / 100 : mx;
x2 = - beta(1) / beta(3) - beta(2) / beta(3) * x1;

% line #2
if nargin > 4
    beta_pocket = varargin{1};
    mnp = - beta_pocket(1) / beta_pocket(2) - beta_pocket(3) / beta_pocket(2) * min(X(:, 3));
    mxp = - beta_pocket(1) / beta_pocket(2) - beta_pocket(3) / beta_pocket(2) * max(X(:, 3));
    x1p = mnp : (mxp - mnp) / 100 : mxp;
    x2p = - beta_pocket(1) / beta_pocket(3) - beta_pocket(2) / beta_pocket(3) * x1p;

    plot(X0(:, 1), X0(:, 2), 'o', X1(:, 1), X1(:, 2), 'x', x1, x2, 'r', x1p, x2p, 'b.', 'LineWidth', 2);
    
    if nargin == 6
        best_run = varargin{2};
        xc = min(X(:, 2)) + 0.025 * (max(X(:, 2)) - min(X(:, 2)));
        yc = max(X(:, 3)) - 0.025 * (max(X(:, 3)) - min(X(:, 3)));
        text(xc, yc, ['best run = ' num2str(best_run)]);
    end
else
    plot(X0(:, 1), X0(:, 2), 'o', X1(:, 1), X1(:, 2), 'x', x1, x2, 'r', 'LineWidth', 2);
end
    
axis([(min(X(:, 2)) - 0.5) (max(X(:, 2)) + 0.5) (min(X(:, 3)) - 0.5) (max(X(:, 3)) + 0.5)]);
xlabel('x_1');
ylabel('x_2');
title(title_string, 'FontSize', 14);
    
return