library(graphics)

set_center <- function(X,k)
{
}

set_cluster <- function(X,k,center)
{
	numClu <- dim(center)[2]
	numData <- dim(X)[1]
	for(i in 1:numData)
	{
	}
}

my_kmean <- function(X,k)
{
#randomly assign center

#	
}


x <- rbind(matrix(rnorm(100, sd = 0.3), ncol = 2),
           matrix(rnorm(100, mean = 1, sd = 0.3), ncol = 2))
colnames(x) <- c("x", "y")
(cl <- kmeans(x, 2))
plot(x, col = cl$cluster)
points(cl$centers, col = 1:2, pch = 8, cex = 2)
