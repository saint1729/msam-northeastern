%--------------------------------------------------------------------------
% Polynomial Curve Fitting using OLS Regression
% 1-D problem
%
% Predrag Radivojac
% Northeastern University
% First completed: September, 2011
%--------------------------------------------------------------------------

clear
clc

% data set size
n = 20;

% noise parameter (standard deviation of Gaussian noise)
sg = 5;

% degree of polynomial to learn target
p = 8;

% vector of features; n-by-1 matrix with numbers between 0 and 10
X = 10 * rand(n, 1);

% create true target function (quadratic function of x)
wt = [2 3 1]';
t = wt(1) + wt(2) * X(:, 1) + wt(3) * X(:, 1) .^ 2;

% create target values (t + Gaussian noise)
y = t + sg * randn(n, 1);

% create 'feature' matrix F of dimension n-by-(p+1)
F = [];
for i = 0 : p
    F = [F X .^ i];
end

% calculate optimal weights
w = inv(F' * F) * F' * y
%w = pinv(F) * y;

% plot this situation
plot1curvefitting(F, y, wt, w)