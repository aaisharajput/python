#25.WAP to find mean, mode and median.
import statistics
#mean
numb = [2, 8, 5, 7, 3, 5]
no = len(numb)
summ = sum(numb)
mean = summ / no
print("The mean of ", numb, " : ", mean)

#median
numb.sort()
if no % 2 == 0:
    median1 = numb[no//2]
    median2 = numb[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = numb[no//2]
print("The median of the given set ", numb, " : ", median)

#mode
print("Mode of given set is % s" % (statistics.multimode(numb)))