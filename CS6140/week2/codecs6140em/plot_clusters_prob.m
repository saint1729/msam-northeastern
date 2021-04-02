function plot_clusters_prob (X, py, title_string, varargin)

[~, y] = max(py, [], 2); % get best cluster for each data point

% visualize using plot_clusters()
if nargin == 3
    plot_clusters(X, y - 1, size(py, 2), title_string);
elseif nargin == 4
    plot_clusters(X, y - 1, size(py, 2), title_string, varargin{1});
else
    error('Incorrect number of inputs');
end

return
        