
def truncate(f, n):
  '''Truncates/pads a float f to n decimal places without rounding'''
  s = '%.12f' % f
  i, p, d = s.partition('.')
  return str('.'.join([i, (d+'0'*n)[:n]]))

value_ok = 1719950565.5638983
value_one_zero = 1719950565.5030283
value_all_zero = 1719950565.0000000


print("value_ok",truncate(value_ok, 8))
print("value_one_zero",truncate(value_one_zero, 8))
print("value_all_zero",truncate(value_all_zero, 8))
