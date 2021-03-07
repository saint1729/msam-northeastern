 %--------------------------------------------------------------------------
% Logistic Regression demo
% Maximum Likelihood (ML) optimization
% Newton-Raphson method
%
% Predrag Radivojac
% Northeastern University
% Last update: February 2019 
%--------------------------------------------------------------------------

clear 
clc

max_step = 100;     % maximum number of iterations
tolerance = 0.0001;   % threshold of change in weights (between iterations)
eta = .1; % learning rate

n0 = 250;    % number of negatives
n1 = 250;    % number of positives
m0 = [1 2]; % mean for negatives
m1 = [6 3]; % mean for positives
s0 = 1;     % std for positives
s1 = 1;     % std for negatives

% reseed the random number generator
randn('state', 1234)

% try 10 different data sets
for i = 1 : 10
    % generate n0 negatives and n1 positives (should be done better)
    X0 = randn(n0, 2) .* repmat(s0, n0, 2) + repmat(m0, n0, 1);
    X1 = randn(n1, 2) .* repmat(s1, n1, 2) + repmat(m1, n1, 1);

    % create X matrix
    X = [X0; X1];
    
    % create class label vector
    y = [zeros(n0, 1); ones(n1, 1)];

    % add a column of ones to matrix X
    X = [ones(size(X, 1), 1) X];

    % initial coefficients using ordinary least squares regression
    %w = inv(X' * X) * X' * y;
    % initial coefficients using random number generator (uniform distribution between 0 and 1)
    w = 2 * rand(3, 1) - 1; 
    
    % plot line
    plot_logreg_figure(X0, X1, X, w);

    pause(1)
    
    % calculate log-likelihood
    ll = get_log_likelihood(X, y, w);

    step = 1;
    eps = tolerance;

    % updates will stop if the number of steps exceeds some maximum number
    % or if the relative change of w is smaller than a prespecified number
    % or if the log likelihood is too close to zero (classes are separable)
    while step <= max_step && eps >= tolerance && ll < -1e-6
        % vector of posterior probabilities that class equals 1
        p = logsig(X * w);

        % store w vector, normalized
        w_old = w / sum(abs(w));

        % apply update rule and get new w
        w = w + eta * inv(X' * diag(p .* (1 - p)) * X) * X' * (y - p);
        
        % percent difference between old and new (normalized) w vectors
        eps = sum(abs(w_old - w / sum(abs(w))));

        % plot current situation
        plot_logreg_figure(X0, X1, X, w);

        % calculate log-likelihood
        ll = get_log_likelihood(X, y, w);

        step = step + 1;

        pause(0.25)
    end

    pause
end
