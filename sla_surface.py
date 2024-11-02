cub = [
	3.6*3.6/2,
	.44*.22/2,
	4.86*5.26,
	1.13*.53,
	.52*.54,
	-.31*.15/2,
	5.47*1.88
]

semicub = [
	0.31*0.15/2,
	.55*.6,
	.53*.53/2,
	.56*.56/2,
	.48*.63,
	.48*.48/2,
	1.18*1.12
]

sla = sum(cub) + sum(semicub)/2
print(sla, " square inches")

def f(x):
	return 4*x/3

print(f(f(sla)), " square meters")

print("living room surface ", 5.15 * 3.63, " m2")
