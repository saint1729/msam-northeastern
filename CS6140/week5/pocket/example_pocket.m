%--------------------------------------------------------------------------
% Pocket Algorithm demo
%
% Predrag Radivojac
% Northeastern University
% Last update: February 2019
%--------------------------------------------------------------------------

clear
clc

max_step = 100000; % maximum number of iterations
eta = 0.01;         % the coefficient for the update rule (0 < eta <= 1)

n0 = 250;    % number of negatives
n1 = 250;    % number of positives
m0 = [1 2]; % mean for negatives
m1 = [6 3]; % mean for positives
s0 = 1;     % std for positives
s1 = 1;     % std for negatives

% re-seed the random number generator
randn('state', 1234)

% try 10 different problems
for i = 1 : 10
    % generate n0 negatives and n1 positives (should be done better)
    X0 = randn(n0, 2) .* repmat(s0, n0, 2) + repmat(m0, n0, 1);
    X1 = randn(n1, 2) .* repmat(s1, n1, 2) + repmat(m1, n1, 1);
    
    % create X matrix
    X = [X0; X1];
    
    % create class label vector
    y = [-1 * ones(n0, 1); ones(n1, 1)];
    
    % add a column of ones to matrix X
    X = [ones(size(X, 1), 1) X];
    
    % initial coefficients using random numbers between 0 and 1
    w = 2 * rand(3, 1) - 1;
    
    % plot line
    plot_pocket_figure(X0, X1, X, w);
    
    % wait a little before updating weights
    pause(1)

    % initialize stuff
    step = 1;
    run = 0;
    best_run = 0;
    max_run = 100 * size(X, 1);
    w_pocket = w;

    % updates will stop if the number of steps exceeds some maximum number
    % or if the run is long enough
    while step <= max_step && run < max_run
        % if we want stratified sampling
        %if rand(1, 1) < (size(X0, 1)/size(X, 1))
        %    r = randi(size(X0, 1), 1);
        %else
        %    r = size(X0, 1) + randi(size(X1, 1), 1);
        %end
            
        % randomly draw a data point from X (r is its index)
        r = randi(size(X, 1), 1);
        
        % predict class label for this data point
        y_hat = sign(X(r, :) * w);
        
        % is the prediction correct (being on the decision boundary counts
        % as incorrect, given the sign function used by Matlab)
        if y(r) == y_hat
            run = run + 1;
        else
            if run > best_run
                best_run = run;
                w_pocket = w;
                run = 0;
            end
            w = w + eta * 0.5 * (y(r) - y_hat) * X(r, :)';
            plot_pocket_figure(X0, X1, X, w, w_pocket, best_run);
            pause(0.25);
        end
        
        % store w vector, normalized
        %w = w / sum(abs(w));
        
        step = step + 1;
    end
    
    if run > best_run
        w_pocket = w;
        best_run = run;
    end

    % plot final decision boundary
    plot_pocket_figure(X0, X1, X, w_pocket);

    pause
end

