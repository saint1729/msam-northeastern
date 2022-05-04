function ll = get_log_likelihood (X, y, beta)

% ll = 0;
% for i = 1 : size(X, 1)
%     ll = ll + (y(i) - 1) * beta' * X(i, :)' + log(logsig(beta' * X(i, :)'));
% end

t = X * beta;
ll = sum((y - 1) .* t + log(logsig(t)));

return