function [] = plot1curvefitting (X, y, wt, w)

% temporary matrix so we can plot
Xtemp = [(-0.25 : 0.01 : 10.25)'];

d = size(X, 2) - 1;
F = [];
for i = 0 : d
    F = [F Xtemp .^ i];
end

d = length(wt) - 1;
T = [];
for i = 0 : d
    T = [T Xtemp .^ i];
end

% plot this
plot(X(:, 2), y, 'o', -0.25 : 0.01 : 10.25, F * w, 'r', 'LineWidth', 2);
axis([-0.5 11 min(y) - 10 max(y) + 10]);
hold on
plot(-0.25 : 0.01 : 10.25, T * wt, 'g', 'LineWidth', 2);
hold off
%min(y) - 0.1 * abs(min(y))
xlabel('x')
ylabel('y')
title('1-D polynomial curve fitting');

return