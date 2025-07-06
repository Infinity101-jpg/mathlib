import ezMath as ez

print('\nPi is approximately equal to ',end='')
ez.printNum(
  ez.PI                         ### PI
)    

print('\nSin of 1.2 Radians = ', end='')
ez.printNum (
  ez.sin (1.2 * ez.RADIANS)                     ### Sin ( 1.2 Radians )                       
)


print('\nSin of 30 Degrees = ', end ='')
ez.printNum (
  ez.sin (30 * ez.DEGREES)                     ### Sin (30 Degrees)
)

print('\nCos of 1.2 Radians = ', end='')
ez.printNum (
  ez.cos (1.2 * ez.RADIANS)                     ### Cos ( 1.2 Radians )                       
)

print('\nCos of 30 Degrees = ', end ='')
ez.printNum (
  ez.cos (30 * ez.DEGREES)                     ### cos (30 Degrees)
)

print('\nTan of 1.2 Radians = ', end='')
ez.printNum (
  ez.tan (1.2 * ez.RADIANS)                     ### Tan ( 1.2 Radians )                       
)

print('\nTan of 30 Degrees = ', end ='')
ez.printNum (
  ez.tan (30 * ez.DEGREES)                     ### Tan (30 Degrees)
)
