function [fitresult, gof] = createFit1(week_no, DAILY_DEATHS)
%CREATEFIT1(WEEK_NO,DAILY_DEATHS)
% Create a fit.
%
% Data for 'DailyDeathsFitted' fit:
% X Input : week_no
% Y Output: DAILY_DEATHS
% Output:
% fitresult : a fit object representing the fit.
% gof : structure with goodness-of fit info.
%% Fit: 'DailyDeathsFitted'.
[xData, yData] = prepareCurveData( week_no, DAILY_DEATHS );
% Set up fittype and options.
ft = fittype( 'sin6' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Display = 'Off';
opts.Lower = [-Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf];
opts.StartPoint = [652.407938242925 0.061599855952741 0.173856901039116 263.551416590444 0.246399423810964 % Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );
% Plot fit with data.
figure( 'Name', 'DailyDeathsFitted' );
h = plot( fitresult, xData, yData );
legend( h, 'DAILY_DEATHS vs. week_no', 'DailyDeathsFitted', 'Location', 'NorthEast', 'Interpreter', % Label axes
xlabel( 'week_no', 'Interpreter', 'none' );
ylabel( 'DAILY_DEATHS', 'Interpreter', 'none' );
grid on
