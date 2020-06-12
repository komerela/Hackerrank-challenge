#include <stdio.h>
#include <string.h>

/**
 * lomuto_partition - partitions a sub-array of integers using
 *                    the lomuto partitioning scheme
 * @array: Array to sort
 * @size: Size of the array
 * @lo: low end of the partition array
 * @hi: high end of the partition array
 *
 * Return: Index of the partition
*/
int lomuto_partition(int *array, size_t size, int lo, int hi)
{
	int i, j, pivot, tmp;

	pivot = array[hi];
	i = lo - 1;
	for (j = lo; j < hi; j++)
	{
		if (array[j] < pivot)
		{
			i++;
			if (i != j)
			{
				tmp = array[i];
				array[i] = array[j];
				array[j] = tmp;
			}
		}
	}
	if (array[hi] < array[i + 1])
	{
		tmp = array[i + 1];
		array[i + 1] = array[hi];
		array[hi] = tmp;
	}
	return (i + 1);
}

/**
 * lomuto_sort - sorts an array of integers in ascending order using
 *               the quick sort algorithm with lomuto partitioning
 * @array: Array to sort
 * @size: Size of the array
 * @lo: low end of the partition array
 * @hi: high end of the partition array
 */
void lomuto_sort(int *array, size_t size, int lo, int hi)
{
	int p;

	if (lo < hi)
	{
		p = lomuto_partition(array, size, lo, hi);
		lomuto_sort(array, size, lo, p - 1);
		lomuto_sort(array, size, p + 1, hi);
	}
}

/**
 * quick_sort - sorts an array of integers in ascending order using
 *              the quick sort algorithm
 * @array: Array to sort
 * @size: Size of the array
 */
void quick_sort(int *array, size_t size)
{
	if (!array || size < 2)
		return;
	lomuto_sort(array, size, 0, size - 1);
}

/**
 * timeConvert - converts a "XX:XX" time representation to an integer 
 * @stringTime - the string to convert
 * Return: the minutes that have elapsed in a day at a certain time
 */

int timeConvert(char *stringTime){
    return (600*(stringTime[0] - '0') + 60*(stringTime[1] - '0') + 10*(stringTime[3] - '0') + (stringTime[4] - '0'));
}

/**
 * findMinDifference - returns the number of minimum minutes difference between two time points
 * @timePoints - a list of time string representations
 * @timePointsSize - Array size of timePoints
 * Return: the minumum minutes difference between any two time points in timePoints
 */

int findMinDifference(char ** timePoints, int timePointsSize){
    int i, minDifference, difference, lastMinusFirst;
    int array[timePointsSize];

    // convert timePoints array to integer minute of the day representations
    for (i = 0; i < timePointsSize; i++)
        array[i] = timeConvert(timePoints[i]);
    quick_sort(array, sizeof(array)/sizeof(array[0]));
    minDifference = 1440;
    for (i = 1; i < timePointsSize; i++)
    {
        difference = array[i] - array[i - 1];
        if (difference < minDifference)
            minDifference = difference;
    }
    lastMinusFirst = ((array[0] + 1440) - array[timePointsSize - 1]);
    if (lastMinusFirst < minDifference)
        minDifference = lastMinusFirst;
    return minDifference;
}

/**
 * main - entry point
 * Return: always 0
 */

int main(){
    char *timePoints[] = {"23:59", "10:06", "01:09", "00:01"};
    printf("The closest two times are %d minutes apart\n", findMinDifference(timePoints, sizeof(timePoints)/sizeof(timePoints[0])));
    return 0;
}