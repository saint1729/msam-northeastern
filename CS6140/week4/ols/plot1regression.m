function [] = plot1regression (X, y, w)

% temporary matrix so we can plot
Xtemp = [ones(151, 1) (-0.25 : 0.01 : 1.25)'];

% plot this
plot(X(:, 2), y, 'o', -0.25 : 0.01 : 1.25, Xtemp * w, 'r', 'LineWidth', 2);
xlabel('x')
ylabel('y')
title('1-D linear regression');

return