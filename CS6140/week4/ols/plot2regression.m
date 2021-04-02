function [] = plot2regression (X, y, w)


% prepare data for plotting
ii = 1;  
for i = 0 : 0.1 : 1
    jj = 1;
    for j = 0 : 0.1 : 1
        % w(2) <-> w(3) because of mesh/plot3 below
	    Xtemp(ii, jj) = w(1) + w(3) * i + w(2) * j; 
		jj = jj + 1;
	end
	ii = ii + 1;
end

% plot plane and points
mesh(0 : 0.1 : 1, 0 : 0.1 : 1, Xtemp)
hold on
plot3(X(:, 2), X(:, 3), y, 'ro', 'LineWidth', 2)
axis([-0.25 1.25 -0.25 1.25 -1 6]);

xlabel('x_1')
ylabel('x_2')
zlabel('y')
title('2-D linear regression');

return