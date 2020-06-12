int strStr(char * haystack, char * needle){
	int i, j;

	if (!needle[0])
		return (0);

	for (i = 0; haystack[i]; i++)
		if (haystack[i] == needle[0])
		{
			for (j = 0; needle[j] == haystack[i + j] && needle[j]; j++)
                ;
			if (!needle[j])
				return (i);
		}
	return (-1);
}