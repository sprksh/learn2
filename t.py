    var i=0,j=1,count=0;
    
    while(j < n) {
        var diff = nums[j] - nums[i];
        
        if (diff == k) {
            count++;
            j++;
        } else if (diff > k) {
            i++;
        } else if (diff < k) {
            j++;
        }
    }

i = 0
j = 0
count = 0

while j<n:
    dif = lis[j] - lis[i]

    if dif == k:
        count += 1
        j += 1
    elif dif > k:
        i += 1
    elif dif < k:
        j += 1