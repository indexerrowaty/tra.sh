import sys

if not sys.argv[1:]:
   a = """
   ==^==
   |[[[|
   |[[[|
   '---'
   """
   print(a)
else:
   b = f"""
   ==^==
   |[[[|  <- this is
   |[[[|  {" ".join(sys.argv[1:])}
   '---'
   """
   print(b)
