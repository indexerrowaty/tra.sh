import sys

if not sys.argv[1:]:
   aytch = """
   ==^==
   |[[[|
   |[[[|
   '---'
   """
   print(aytch)
else:
   aitch = f"""
   ==^==
   |[[[|  <- this is
   |[[[|  {" ".join(sys.argv[1:])}
   '---'
   """
   print(aitch)
