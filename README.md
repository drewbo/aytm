## Are You The Math

Calculating probabilities for [Are You The One](https://en.wikipedia.org/wiki/Are_You_the_One%3F)

Run with:
```bash
python main.py ---use-snapshot ep4.p --save-snapshot ep5.p
```

where the snapshot flags allow you to use or save a probabilities snapshot respectively. Starting from a previous snapshot will greatly speed up the calculation.

Match Ceremony and Truth Booth "inputs" are currently stored in the file and should be edited in place. The output should appear like so (current as of week 7):

```bash
         Anthony  Clinton  Dimitri    Ethan      Joe   Kareem    Keith  Malcolm  Michael     Shad    Tyler
 Alexis    10.24     14.6     22.0     2.83     6.54    11.76      0.0     8.93      9.8     9.15     4.14
 Alivia     4.36     8.28     8.71     1.31     5.23     1.53     6.75    51.85     5.01     4.79     2.18
 Audrey     8.28     6.75     8.28     1.96      0.0      6.1     6.97     5.66     8.28    45.32      2.4
Diandra      0.0    10.68    22.44     2.18     6.54    27.23    11.98      0.0     9.15      9.8      0.0
  Geles      0.0    23.31     8.28      0.0     4.14     8.93    10.89    13.73     24.4     3.92      2.4
   Jada     7.19      0.0     0.87    81.48     1.53     2.61     1.96     1.31     1.09     1.31     0.65
 Keyana    44.88     8.71     8.06      0.0     4.79     5.23     6.97     3.49    13.07     4.79      0.0
 Nicole      0.0     3.92      0.0     0.65     0.22     3.92     2.61     0.87     1.31     3.49    83.01
  Nurys     6.32     14.6    13.51     3.05     7.84    12.85    29.85      0.0      0.0    10.46     1.53
   Uche    12.64      0.0      0.0     3.92    10.02    13.29    16.78      9.8    23.09     6.75      3.7
    Zoe      6.1     9.15     7.84     2.61    53.16     6.54     5.23     4.36     4.79     0.22      0.0
```

### Citations

This idea was taken from http://areuthe.blogspot.com/
