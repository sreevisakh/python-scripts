def RabinKarpSet(s):
     set hsubs := emptySet
     for each sub in subs
         insert hash(sub[1..m]) into hsubs
     hs := hash(s[1..m])
     for i from 1 to n-m+1
         if hs ∈ hsubs and s[i..i+m-1] ∈ subs
             return i
         hs := hash(s[i+1..i+m])
     return not found
