function [w, mu, sg] = cem_demo (X, M, algorithm)

% function [w, mu] = kmeans_demo (X, M, algorithm)
%
% This function executes K-means algorithm for 2D data
%
% Inputs:  X = n-by-2 matrix of observations
%          M = the number of clusters
%          algorithm = string to be printed
%
% Outputs: w = M-by-1 vector, fractions of data points in each cluster
%          mu = 2-by-M matrix of means for each cluster
%          sg = covariance matrices for each cluster
%
% Predrag Radivojac
% November 2015

eps = 0.000001; % tolerance level
max_step = 100; % maximum number of iterations

% seed the random number generator so that the experiment is repeatable
randn('state', 12345)

K = size(X, 2); % dimensionality of the sample

fprintf(1, '\n\n%s\n', algorithm);

% initialize w, mu, and sg
w = ones(1, M) / M;

d = 0.01 * mean(sum((X - repmat(mean(X, 1), size(X, 1), 1)) .^ 2, 2));
% initial centroids, using the splitting method
mu = [mean(X, 1)' mean(X, 1)' + d * sign(randn(1, K))']; 

%mu = [mean(X, 1)' mean(X, 1)' + [0.01 -0.01]']; 
%mu = [[4 3]' [6 4]']; % pick some 'random' means
%[~, mu] = kmeans(X, M); mu = mu'; % use K-means to find initial clusters

for m = 1 : M
    sg(:, :, m) = diag(ones(K, 1));
end

% initialize "class labels" y
y = zeros(size(X, 1), 1);

step = 0;
diff = 2 * eps; % just to ensure it is greater than eps

while diff > eps && step < max_step
    %w
    %mu
    %sg
    
    y_old = y;
    
    % given w, mu, and sg, update "class labeles" y
    for i = 1 : size(X, 1)
        Z = 0;
        for k = 1 : M
            t = X(i, :)' - mu(:, k);
            Z = Z + w(k) / sqrt((2*pi) ^ K * det(sg(:, :, k))) * exp(-0.5 * (t') * inv(sg(:, :, k)) * t);
        end
        
        for k = 1 : M
            t = X(i, :)' - mu(:, k);
            py(i, k) = w(k) / sqrt((2*pi) ^ K * det(sg(:, :, k))) * exp(-0.5 * (t') * inv(sg(:, :, k)) * t) / Z;
        end
        [~, q] = max(py(i, :));
        y(i) = q - 1;
    end

    % given "class labeles" y, update w, mu, and sg
    sg = zeros(K, K, M);
    for k = 1 : M
        w(k) = length(find(y == k - 1)) / length(y);
        q = find(y == k - 1);
        mu(:, k) = (mean(X(q, :)))';
        
        for i = 1 : length(q)
            sg(:, :, k) = sg(:, :, k) + (X(q(i), :)' - mu(:, k)) * (X(q(i), :)' - mu(:, k))';
        end
        sg(:, :, k) = sg(:, :, k) / length(q);
    end

    % visualize current situation
    plot_clusters(X, y, M, algorithm, step);
    pause

    % calculate the difference between this and previous iteration, but
    % skip the calculation if we are in the first iteration
    if step == 0
        diff = 2 * eps;
    else
        diff = sum(abs(y - y_old)) / size(X, 1);
    end
    
    step = step + 1;
end

return