%--------------------------------------------------------------------------
% Ordinary Least Squares Regression demo
% 2-D problem
%
% Predrag Radivojac
% Northeastern University
% First completed: September, 2010 
%--------------------------------------------------------------------------

clear
clc

% data set size
n = 20000;

% vector of features; n-by-5 matrix
X = rand(n, 5);

% add a column of ones
X = [ones(n, 1) X];

% create targets (linear function of first 3 columns + Gaussian noise)
% ignore last two columns of X (irrelevant features)
y = 1 * X(:, 1) - 1.5 * X(:, 2) + 2 * X(:, 3) + 1.5 * randn(n, 1);

% calculate optimal weights
w = inv(X' * X) * X' * y
 
% plot this situation
plot2regression(X, y, w)
