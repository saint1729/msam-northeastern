% Solution 1.4.1

W = 1 / 3 * [-1; -2; 2];

x0_E = 117.67 * [4; 1; 3];

P = x0_E / norm(x0_E);

Q = cross(W, P);

disp(Q);


% Solution 1.4.2

Id_UE = [P, Q, W];

disp(Id_UE);

Id_EU = Id_UE\eye(3);

disp(Id_EU);



% Solution 1.4.3


R3_0_5 = [[cos(3.91 * 0.5), -sin(3.91 * 0.5), 0];
    [sin(3.91 * 0.5), cos(3.91 * 0.5), 0];
    [0, 0, 1]];

x_0_5 = R3_0_5 * Id_UE * x0_E;

disp(x_0_5);


R3_1 = [[cos(3.91 * 1), -sin(3.91 * 1), 0];
    [sin(3.91 * 1), cos(3.91 * 1), 0];
    [0, 0, 1]];

x_1 = R3_1 * Id_UE * x0_E;

disp(x_1);


R3_1_5 = [[cos(3.91 * 1.5), -sin(3.91 * 1.5), 0];
    [sin(3.91 * 1.5), cos(3.91 * 1.5), 0];
    [0, 0, 1]];

x_1_5 = R3_1_5 * Id_UE * x0_E;

disp(x_1_5);



