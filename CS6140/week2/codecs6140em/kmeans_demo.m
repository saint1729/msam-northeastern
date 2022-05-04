function [w, mu, sse] = kmeans_demo (X, M, algorithm)

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
%
% Predrag Radivojac
% November 2015

eps = 0.000001; % tolerance level
max_step = 100; % maximum number of iterations

% seed the random number generator so that the experiment is repeatable
randn('state', 12345)

%display(algorithm);
fprintf(1, '\n\n%s\n', algorithm);

step = 0;
diff = 2 * eps; % just to ensure it is greater than eps
sse = 0;

% displacement is 1% of the mean squared error
d = 0.01 * mean(sum((X - repmat(mean(X, 1), size(X, 1), 1)) .^ 2, 2));

% initial centroids, using the splitting method
mu = [mean(X, 1)' mean(X, 1)' + d * sign(randn(1, size(X, 2)))']; 

%mu = [];
% when M > 2, we simply add some data points (we should use the full
% splitting method but this is too complicated for this demo)
for m = 3 : M
    mu = [mu X(randi(size(X, 1)), :)']; 
end

% we never visualize the initial positions of clusters, but that needs a
% special action

while diff > eps && step < max_step
    sse_old = sse;
    mu_old = mu;
    
    % calculate proximity of each data point to each of the M = 2 centroids
    for i = 1 : size(X, 1)
        mni = 1; % set best cluster and best distance to cluster 1
        mnd = (X(i, :)' - mu(:, 1))' * (X(i, :)' - mu(:, 1));
        for m = 2 : M
            if (X(i, :)' - mu(:, m))'* (X(i, :)' - mu(:, m)) < mnd
                mni = m;
                mnd = (X(i, :)' - mu(:, m))' * (X(i, :)' - mu(:, m));
            end
        end
        y(i, 1) = mni;           % set class to where minimum was
        py(i, :) = zeros(1, M);
        py(i, mni) = 1;          % set the probability to 1
    end

    % visualize this situation
    plot_clusters_prob(X, py, algorithm, step);
    pause

    % find centroids
    for m = 1 : M
        mu(:, m) = mean(X(y == m, :));
    end
    
    sse = 0;
    
    for m = 1 : M 
        sse = sse + sum(sum((X(y == m, :) - repmat(mu(:, m)', size(X(y == m, :), 1), 1)) .^ 2));
    end

    diff = abs(sse - sse_old);
    
    step = step + 1;
end

w = sum(py, 1) / size(X, 1);

return