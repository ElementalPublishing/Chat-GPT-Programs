#include <stdio.h>
#include <stdlib.h>

#define BUFSIZE 30000

char *p;
unsigned char buf[BUFSIZE];

int main(int argc, char *argv[])
{
    FILE *fp;
    int c;

    if (argc != 2) {
        printf("Usage: brainfuck filename\n");
        return 1;
    }

    if ((fp = fopen(argv[1], "r")) == NULL) {
        printf("Error: Cannot open file.\n");
        return 1;
    }

    p = buf;
    while ((c = getc(fp)) != EOF) {
        switch (c) {
            case '>': ++p; break;
            case '<': --p; break;
            case '+': ++*p; break;
            case '-': --*p; break;
            case '.': putchar(*p); break;
            case ',': *p = getchar(); break;
            case '[':
                if (*p) {
                    break;
                }
                else {
                    int brackets = 1;
                    while (brackets) {
                        c = getc(fp);
                        if (c == '[') {
                            ++brackets;
                        }
                        else if (c == ']') {
                            --brackets;
                        }
                    }
                }
                break;
            case ']':
                if (*p) {
                    int brackets = 1;
                    while (brackets) {
                        c = getc(fp);
                        if (c == '[') {
                            ++brackets;
                        }
                        else if (c == ']') {
                            --brackets;
                        }
                    }
                }
                else {
                    break;
                }
        }
    }

    fclose(fp);
    return 0;
}