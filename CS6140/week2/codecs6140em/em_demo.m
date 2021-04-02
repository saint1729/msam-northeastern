function [w, mu, sg] = em_demo (X, M, algorithm)

% function [w, mu, sg] = em_demo (X, M, algorithm)
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

step = 0;
diff = 2 * eps; % just to ensure it is greater than eps

while diff > eps && step < max_step
    w_old = w;
    mu_old = mu;
    sg_old = sg;
    
    % given w, mu, and sg, update "class posterior probabilities" py
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
    end

    % given "class posteriors" py, update w, mu, and sg
    sg = zeros(K, K, M);
    for k = 1 : M
        w(k) = mean(py(:, k), 1);

        mu(:, k) = zeros(K, 1);
        for i = 1 : size(X, 1)
            mu(:, k) = mu(:, k) + py(i, k) * X(i, :)';
        end
        mu(:, k) = mu(:, k) / sum(py(:, k), 1);
        
        for i = 1 : size(X, 1)
            sg(:, :, k) = sg(:, :, k) + py(i, k) * (X(i, :)' - mu(:, k)) * (X(i, :)' - mu(:, k))';
        end
        sg(:, :, k) = sg(:, :, k) / sum(py(:, k), 1);
    end

    % visualize this situation
    plot_clusters_prob(X, py, algorithm, step);
    pause
    
    diff = sum(abs(w - w_old)) + sum(sum(abs(mu - mu_old))) + sum(sum(sum(abs(sg - sg_old))));
    
    step = step + 1;
end

return
