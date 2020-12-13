clear
clc
%% comment : role of the following code ?

% The following line read the image and store the R, G, B values of pixel
% in a 3 dimensional array. The range of values in cells is 0-255.
a= imread ('apollo.png');

% Get the dimensions of the image.
[m,n,d]= size (a);

% Total posibble eigen values.
kmax = floor ((m*n)/(m+n+1) );

% Since we are working matrices, whose numbers can be real numbers, we have
% to change the datatype of each cell.
da= double (a);

% Initialize array for outputs for Singular Value Decomposition U, S, V with zeros.
% Initialize the array e with zeros, which contains ratios of singular values.
% Initialize the array cr with zeros, which stores the compression ratio.
% Initialize the array rmse with zeros, which stores the root mean square
% errors between input image and compressed image
U= zeros (m,m);S= zeros (m,n);V= zeros (n,n);e= zeros (kmax ,d);cr= zeros (kmax ,1); rmse = zeros (kmax ,d);

%% comment : SVD.
% Run SVD for each of R, G, B channels.
for i=1:d
    % Assign U, S, V after running SVD for each channel.
    [U(:,:,i),S(:,:,i),V(:,:,i)] = svd(da(:,:,i));
end

%% comment : role of the following code ?
% Run a loop to compress and store images for each channel and also all
% channels considering upto top 20 eigen values
pv = 20;
for k=1: pv
    % Initialize output image containing all (RGB) channels of same dimensions but compressed size.
    ca= zeros (m,n,d);
    % Assign compression ratio values.
    cr(k)=m*n/(k*(m+n+1));
    % Run a loop for each of the channels.
    for i=1:d
        % Initialize output image containing each of either R or G or B
        % channels of same dimensions but compressed size.
        cai= zeros(m,n,d);
        % Assign values to compressed image for each of R/G/B channels.
        [ca(:,:,i),cai(:,:,i)]= deal (U(: ,1:k,i)*S(1:k ,1:k,i)*V(: ,1:k,i)');
        % Calculate the ratio of (k + 1)th eigen value and 1st eigen values
        % for each of R/G/B channels.
        e(k,i)=S(k+1,k+1,i)/S(1,1,i);
        % Root mean square error calculation between each of R/G/B channels
        % of given image and compressed image.
        rmse (k,i)= sqrt (sum (sum ((( da (: ,:,i)-ca (: ,:,i)) .^2) ))/(m*n));
        % Save the image containing only R or G or B channels in the compressed image.
        % For eg: Values of R can be from 0-255 in which case G = B = 0.
        % Similarly, G can be from 0-255 in which case R = B = 0.
        % Likewise, if B is between 0-255 we habe R = G = 0.
        imwrite ( uint8 (cai ), sprintf ('%dk%d.png',k,i));
    end
    % Save all the channels in the compressed image.
    imwrite ( uint8 (ca), sprintf ('%dk.png', k));
end
figure
