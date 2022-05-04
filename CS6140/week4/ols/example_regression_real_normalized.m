%--------------------------------------------------------------------------
% Ordinary Least Squares Regression demo
% Real-life problem
%
% Predrag Radivojac
% Northeastern University
% First completed: October, 2014 
%--------------------------------------------------------------------------

clear
clc

% N-fold cross-validation
N = 10;

% if we want to do normalization use true, otherwise false
normalize_flag = true;

% load the data and produce X and y matrices
%D = load('housing.data');
D = load('concrete.txt');
X = D(:, 1 : size(D, 2) - 1);
y = D(:, size(D, 2));

% generate N folds; f{i} contains indices of data points to be a test set
% in the i-th step
q = randperm(length(y));
for i = 1 : N
    f{i} = q(i : N :length(y));
end

% initialize predictions with zeros
p = zeros(length(y), 1);

% perform cross-validation
for i = 1 : N
    % make test set (i-th fold)
    Ts = X(f{i}, :);
    ys = y(f{i}, :);
    
    % make training set (all data but the i-th fold)
    Tr = X(setdiff(1 : length(y), f{i}), :);
    yr = y(setdiff(1 : length(y), f{i}), :);
    
    % normalize data
    if normalize_flag == true
        mnX = mean(Tr, 1);
        stX = std(Tr, [], 1);
        mny = mean(yr, 1);
        sty = std(yr, [], 1);
        
        for i1 = 1 : size(Tr, 1)
            for i2 = 1 : size(Tr, 2)
                Tr(i1, i2) = (Tr(i1, i2) - mnX(i2)) / stX(i2);
            end
            yr(i1) = (yr(i1) - mny) / sty;
        end
        for i1 = 1 : size(Ts, 1)
            for i2 = 1 : size(Ts, 2)
                Ts(i1, i2) = (Ts(i1, i2) - mnX(i2)) / stX(i2);
            end
            ys(i1) = (ys(i1) - mny) / sty;
        end
    else
        mny = 0;
        sty = 1;
    end
        
    % add a column of ones to training and test
    Tr = [ones(size(Tr, 1), 1) Tr];
    Ts = [ones(size(Ts, 1), 1) Ts];
    
    % calculate optimal weights
    w = inv(Tr' * Tr) * Tr' * yr;
    
    % make predictios
    p(f{i}, :) = (Ts * w) * sty + mny;
end
   
%% Evaluate accuracy of the regression model

% treat all data as one
sse = 0;
var = 0;
err = zeros(length(y), 1);
for i = 1 : length(y)
    err(i) = y(i) - p(i);
    sse = sse + err(i) ^ 2;
    var = var + (y(i) - mean(y)) ^ 2;
end
R_square = 1 - sse / var;
fprintf(1, '\nR square = %.3f', R_square);


% calculate R square for each fold and then average over all folds
for i = 1 : N
    sse = sum((y(f{i}) - p(f{i})) .^ 2);
    var = sum((mean(y(setdiff(1 : length(y), f{i}))) - p(f{i})) .^ 2);
    R(i) = 1 - sse / var;
end
    
fprintf(1, '\n\nR square = %.3f +/- %.3f\n\n', mean(R), std(R));
