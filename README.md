# tabulate
pretty print CSV files in tabular form

## Usage
`Usage: tabulate.py <file> [optional delimiter]`

By default, the delimiter is a comma.

## Example
Input
```
name,age,state,city,sex
jeff,99,ny,nyc,m
janet,23,ny,yonkers,f
bill,40,ma,boston,m
```
Output
```
+-------+-----+-------+---------+-----+
| name  | age | state | city    | sex |
+-------+-----+-------+---------+-----+
| jeff  | 99  | ny    | nyc     | m   |
| janet | 23  | ny    | yonkers | f   |
| bill  | 40  | ma    | boston  | m   |
+-------+-----+-------+---------+-----+
```

## Other
[In Praise of CSV](https://usopendata.org/2015/03/10/csv/)
