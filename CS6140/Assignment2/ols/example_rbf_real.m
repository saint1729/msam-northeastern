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

% RBF dimensionality
P = 25;

% if we want to do normalization use true, otherwise false
normalize_flag = true;

% load the data and produce X and y matrices
%D = load('housing.data');
D = load('concrete.txt');
X = D(:, 1 : size(D, 2) - 1);
y = D(:, size(D, 2));

% generate 10-folds, f{i} contains indices of data points to be a test set
% in the i-th step
q = randperm(length(y));
for i = 1 : N
    f{i} = q(i : N :length(y));
end

% predictions
p = zeros(length(y), 1);

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
     
    % determine P cluster centers
    [labels, C] = kmeans(Tr, P);
    
    % calculate normalization parameters
    for i1 = 1 : P
        q = find(labels == i1);
        s(i1) = 0;
        for i2 = 1 : length(q)
            s(i1) = s(i1) + (Tr(i2, :) - C(i1, :)) * (Tr(i2, :) - C(i1, :))';
        end
        s(i1) = s(i1) / (length(q) - 1);
    end
    

    % generate the data matrix in the transformed space
    Fr = [];
    Fs = [];
    for i1 = 1 : size(Tr, 1)
        for i2 = 1 : P
            Fr(i1, i2) = exp(-(Tr(i1, :) - C(i2, :)) * (Tr(i1, :) - C(i2, :))' / 2 / s(i2));
        end
    end
    for i1 = 1 : size(Ts, 1)
        for i2 = 1 : P
            Fs(i1, i2) = exp(-(Ts(i1, :) - C(i2, :)) * (Ts(i1, :) - C(i2, :))' / 2 / s(i2));
        end
    end

    % normalize that data, but not the target values (already normalized)
    if normalize_flag == true
        mnX = mean(Fr, 1);
        stX = std(Fr, [], 1);
        
        for i1 = 1 : size(Fr, 1)
            for i2 = 1 : size(Fr, 2)
                Fr(i1, i2) = (Fr(i1, i2) - mnX(i2)) / stX(i2);
            end
        end
        for i1 = 1 : size(Fs, 1)
            for i2 = 1 : size(Fs, 2)
                Fs(i1, i2) = (Fs(i1, i2) - mnX(i2)) / stX(i2);
            end
        end
    end
    
    % add a column of ones to training and test
    Fr = [ones(size(Fr, 1), 1) Fr];
    Fs = [ones(size(Fs, 1), 1) Fs];
    
    % calculate optimal weights
    w = inv(Fr' * Fr) * Fr' * yr;
    
    % make predictios
    p(f{i}, :) = (Fs * w) * sty + mny;
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
% for i = 1 : N
%     sse = sum((y(f{i}) - p(f{i})) .^ 2);
%     var = sum((mean(y(setdiff(1 : length(y), f{i}))) - p(f{i})) .^ 2);
%     R(i) = 1 - sse / var;
% end
%     
% fprintf(1, '\n\nR square = %.3f +/- %.3f\n\n', mean(R), std(R));
% 
