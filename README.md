# Sample variance for normal random variables

As you will have seen when you looked at the graph of the sample mean, and as we have seen for most of the other random variables that we have looked at, the value of the sample mean is (on average) closer to the value of the expectation when we compute it from a larger number of random variables.  In other words, the sample mean converges to the expectation when it is computed from a large number of random variables.

In this next exercise, we are going to examine how the sample variance depends on the number of random variables that we compute it from in much the same way that we examined the behaviour of the sample mean.  This exercise will hopefully clarify what the central limit theorem is not.

With that in mind remember that the sample variance is defined as:

![](https://render.githubusercontent.com/render/math?math=\sigma^2=\frac{n}{n-1}\left[\frac{1}{n}\sum_{i=1}^{n}X_i^2-\left(\frac{1}{n}\sum_{i=1}^{n}X_i\right)^2\right])

To complete the exercise you need to:

1. Write a function called `normal` that takes two variables `mu` (the expectation of the variable) and `sigma2` (the variance of the random variable) as input and that returns a normal random variable with expectation `mu` and variance `sigma2`.
2. Set the first element of the list called `indices` equal to 2, the second element of the list called `indices` to 3 and so on.
3. Set the second element of the list called `svariance` equal to a sample variance calculated by generating 2 normal random variables with parameters `expectation` and `variance`, the third element of the list `svariance` equal to a sample variance calculated by generating 3 normal random variables with parameters `expectation` and `variance`, set the fourth element of the list called `svariance` equal to a sample mean calculated by generating 4 normal random variables with parameters `expectation` and `variance` and so on until you have computed an sample by generating 200 normal random variables with parameters `expectation` and `varianc`e.

Notice that I have created two variables called `ssum` and `ssum2`, which you can use to accumulate the sum of all the random variables you generate and the sum of the squares of all the random variables you generate.  You can then use these accumulated sums to compute the sample variance using the formula given above.
