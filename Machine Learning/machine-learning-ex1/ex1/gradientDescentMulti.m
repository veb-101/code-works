function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %
    % X' * (h - y) = sum((h - y) .* X)'
    
    h = X * theta;% 3*47 x 47*1 - 3*47 x 47*1
    delta = (1 / m) * (X' * h - X' *y );
    % delta = (1 / m) * ((h - y) * X') 
    % row1 = feature1; ..
    % delta = [delta0; delta1; delta2]
    % delta0 = row1 of X' i.e. feature1 * predictions 
    theta -= (alpha * delta);
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCostMulti(X, y, theta);

end

end
