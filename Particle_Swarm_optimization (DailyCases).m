function [fitresult, gof] = createFit(week_no, daily_cases)
%CREATEFIT(WEEK_NO,DAILY_CASES)
% Create a fit.
%
% Data for 'DailyCasesCurveFit' fit:
% X Input : week_no
% Y Output: daily_cases
% Output:
% fitresult : a fit object representing the fit.
% gof : structure with goodness-of fit info.
%% Fit: 'DailyCasesCurveFit'.
[xData, yData] = prepareCurveData( week_no, daily_cases );
% Set up fittype and options.
ft = fittype( 'sin8' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Display = 'Off';
opts.Lower = [-Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf -Inf 0 -Inf opts.StartPoint = [18611.3701064249 0.061599855952741 -0.000182245115632104 9300.61975028072 0.246399423810964 % Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );
% Plot fit with data.
figure( 'Name', 'DailyCasesCurveFit' );
h = plot( fitresult, xData, yData );
legend( h, 'daily_cases vs. week_no', 'DailyCasesCurveFit', 'Location', 'NorthEast', 'Interpreter', % Label axes
xlabel( 'week_no', 'Interpreter', 'none' );
ylabel( 'daily_cases', 'Interpreter', 'none' );
grid on
1
