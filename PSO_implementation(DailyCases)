CostFunction = @(x) DailyCases_Fit(x);
nVar = 1;
VarSize = [1 nVar];
VarMin = 0;
VarMax = 100;
MaxIt = 1000;
nPop = 52;
w = 1;
c1 = 2;
c2 = 2;
MaxVelocity = 0.2*(VarMax - VarMin);
MinVelocity = - MaxVelocity;
emptyParticle.Position = [];
emptyParticle.Velocity = [];
emptyParticle.Cost = [];
emptyParticle.Best.Position = [];
emptyParticle.Best.Cost = [];
particle = repmat(emptyParticle, nPop, 1);
GlobalBest.Cost = inf;
for i=1:nPop
particle(i).Position = unifrnd(VarMin,VarMax, VarSize);
particle(i).Velocity = zeros(VarSize);
particle(i).Cost = CostFunction(particle(i).Position);
particle(i).Best.Position = particle(i).Position;
particle(i).Best.Cost = particle(i).Cost;
if particle(i).Best.Cost < GlobalBest.Cost
GlobalBest = particle(i).Best;
end
end
BestCosts = zeros(MaxIt,1);
for it=1:MaxIt
for i=1:nPop
particle(i).Velocity = w*particle(i).Velocity +c1*rand(VarSize).*(particle(i).Best.Position particle(i).Velocity = max(particle(i).Velocity, MinVelocity);
particle(i).Velocity = min(particle(i).Velocity, MaxVelocity);
particle(i).Position = particle(i).Position + particle(i).Velocity;
particle(i).Position = max(particle(i).Position, VarMin);
particle(i).Position = min(particle(i).Position, VarMax);
particle(i).Cost = CostFunction(particle(i).Position);
if particle(i).Cost < particle(i).Best.Cost
particle(i).Best.Position = particle(i).Position;
particle(i).Best.Cost = particle(i).Cost;
if particle(i).Best.Cost < GlobalBest.Cost
GlobalBest = particle(i).Best;
1
end
end
end
BestCosts(it) = GlobalBest.Cost;
disp(['Iteration' num2str(it) 'BestCost = ' num2str(BestCosts(it))]);
end
