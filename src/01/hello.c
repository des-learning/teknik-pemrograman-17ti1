#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *nama;
	nama = (char *)malloc(sizeof(char) * 1024);

	printf("Nama: ");
	scanf("%s", nama);

	printf("Hello: %s\n", nama);
	free(nama);
	return 0;
}
