%--------------------------------------------------------------------------
% Expectation-Maximization Algorithm, demo
% 2-D problem
%
% Predrag Radivojac
% Northeastern University
%--------------------------------------------------------------------------

clear
clc

% seed the random number generator so that the experiment is repeatable
randn('state', 1235)

%% Parameters

M = 2; % mixtur e of M Gaussians, M is assumed to be known)
K = 2; % K-dimensional data (K must be 2, otherwise visualization breaks)

n = [250 750]; % number of data points (per component)

% below are four different parameter sets for data set generation 
% one must be uncommented

m = [[1 2]' [6 3]'];     % true means
S(:, :, 1) = [1 0; 0 1]; % true covariance matrices
S(:, :, 2) = [1 0; 0 1]; 

m = [[4 4]' [6 3]'];           % true means
S(:, :, 1) = [1 0.75; 0.75 1]; % true covariance matrices
S(:, :, 2) = [1 0.75; 0.75 1]; 

%m = [[4 4]' [6 3]'];             % true means
%S(:, :, 1) = [1 -0.75; -0.75 1]; % true covariance matrices
%S(:, :, 2) = [1 0.75; 0.75 1]; 

%m = [[1 2]' [6 3]'];           % true means
%S(:, :, 1) = [1 0; 0 1];       % true covariance matrices
%S(:, :, 2) = [1 0.75; 0.75 1]; 

%% Data set
% X is observable data
% y_true is generated, but is considered to be unobserved below

X = [];
y_true = [];
for k = 1 : M
    X = [X; repmat(m(:, k)', n(k), 1) + randn(n(k), 2) * chol(S(:, :, k))];
    y_true = [y_true; (k - 1) * ones(n(k), 1)];
end

% disp(y_true');
% disp(X');

% visualize true data
% plot_clusters(X, y_true, M, 'Truth')
% pause
% 
% 
% %% K-Means algorithm
[w, mu] = kmeans_demo(X, M, 'K-means algorithm');

w
mu
% 
% % pause
% 
% 
% %% Classification EM algorithm
[w, mu, sg] = cem_demo(X, M, 'Classification EM algorithm');

w
mu
sg
% 
% pause
% 
% %% EM algorithm
[w, mu, sg] = em_demo(X, M, 'The EM algorithm');

w
mu
sg
