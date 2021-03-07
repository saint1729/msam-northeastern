%--------------------------------------------------------------------------
% Ordinary Least Squares Regression demo
% 1-D problem
%
% Predrag Radivojac
% Northeastern University
% First completed: September, 2010 
%--------------------------------------------------------------------------

clear
clc

% data set size
n = 20000;

% vector of features; n random numbers between 0 and 1
X = rand(n, 1);

% add a column of ones
X = [ones(n, 1) X];

% create targets (linear function + Gaussian noise)
y = 1 * X(:, 1) + 3 * X(:, 2) + 1.5 * randn(n, 1);

% calculate optimal weights
w = inv(X' * X) * X' * y

% plot this situation
plot1regression(X, y, w)
