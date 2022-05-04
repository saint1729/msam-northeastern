function plot_clusters (X, y, M, title_string, varargin)

if M < 2 || M > 6
    error('I can only visualize between 2 and 6 clusters');
end

% Seven colors and symbols maximum
colors = 'rbgmcyk';
symbols = 'ox+*sdv';

% create a data set for each cluster
for i = 1 : M
    q = find(y == i - 1);
    D{i} = X(q, :);
    s{i} = [colors(i) symbols(i)];
end
    
% hard coded visualization
if M == 2
    plot(D{1}(:, 1), D{1}(:, 2), s{1}, D{2}(:, 1), D{2}(:, 2), s{2});
elseif M == 3
    plot(D{1}(:, 1), D{1}(:, 2), s{1}, D{2}(:, 1), D{2}(:, 2), s{2}, ...
        D{3}(:, 1), D{3}(:, 2), s{3});
elseif M == 4
    plot(D{1}(:, 1), D{1}(:, 2), s{1}, D{2}(:, 1), D{2}(:, 2), s{2}, ...
        D{3}(:, 1), D{3}(:, 2), s{3}, D{4}(:, 1), D{4}(:, 2), s{4});
elseif M == 5
    plot(D{1}(:, 1), D{1}(:, 2), s{1}, D{2}(:, 1), D{2}(:, 2), s{2}, ...
        D{3}(:, 1), D{3}(:, 2), s{3}, D{4}(:, 1), D{4}(:, 2), s{4}, ...
        D{5}(:, 1), D{5}(:, 2), s{5});
elseif M == 6
    plot(D{1}(:, 1), D{1}(:, 2), s{1}, D{2}(:, 1), D{2}(:, 2), s{2}, ...
        D{3}(:, 1), D{3}(:, 2), s{3}, D{4}(:, 1), D{4}(:, 2), s{4}, ...
        D{5}(:, 1), D{5}(:, 2), s{5}, D{6}(:, 1), D{6}(:, 2), s{6});
else
    error('This function is unfinished');
end

% add cluster centers to the plot
for i = 1 : M
    hold('on')
    plot(mean(D{i}(:, 1)), mean(D{i}(:, 2)), '+k', ...
        'MarkerSize', 15, 'LineWidth', 3);
end
hold('off')
    

%xlabel('$x_{1}$', 'Interpreter', 'LaTex', 'FontSize', 16);
%ylabel('$x_{2}$', 'Interpreter', 'LaTex', 'FontSize', 16);
xlabel('x_1');
ylabel('x_2');
axis([(min(X(:, 1)) - 0.25) (max(X(:, 1)) + 0.25) (min(X(:, 2)) - 0.25) (max(X(:, 2)) + 0.25)]);
title(title_string, 'FontSize', 14);

if nargin == 5
    step = varargin{1};
    xc = min(X(:, 1)) + 0.05 * (max(X(:, 1)) - min(X(:, 1)));
    yc = max(X(:, 2)) - 0.05 * (max(X(:, 2)) - min(X(:, 2)));
    text(xc, yc, ['step = ' num2str(step)]);
end

return
