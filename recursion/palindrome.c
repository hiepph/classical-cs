#include <stdio.h>
#include <string.h>
#include <assert.h>

/*
 * recursion helper for is_palindrome with start and end indices
 */
int
is_palindrome_rec(char *s, int l, int h)
{
  if (l == h) return 1;
  return s[l] == s[h] &&
    is_palindrome_rec(s, l+1, h-1);
}

/*
 * check if a string is a palindrome,
 * returns 1 if true, 0 if false
 */
int
is_palindrome(char* s)
{
  return is_palindrome_rec(s, 0, strlen(s) - 1);
}

int
main()
{
  assert(is_palindrome("racecar"));
  return 0;
}
