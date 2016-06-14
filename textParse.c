// ----------------------------------------------------------- 
// NAME : Andrew Higginbotham                                                       
// FILE NAME : textParse.c 
// PROGRAM PURPOSE :                                           
//    parse a text file with html elelments  
// ----------------------------------------------------------- 
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>


// ----------------------------------------------------------- 
// FUNCTION  parse                           
// 		splits one line by word or number.                            
// PARAMETER USAGE :
//    line: pointer to the start of the line                                         
//    output: the line sperated into n strings
// FUNCTION CALLED :                                           
//    
// ----------------------------------------------------------- 
void parse(char *line, char* output)
{
	while (*line != '\0') 
	{ 

		if (*line == '<')
		{
			
			while(*line!='>')
			{
				if(*line=='/')
				{
					line+=1;
					if(*line=='p')
					{
						output='\n';
						output++;
						output='\t';
						output++;
					}
				}
				line+=1;
			}
			line+=1;
		}	
		
		output = line;
		fprintf(stderr,"%c",*output);
		if(*line=='\0')
			break;
		output+=1;
		line+=1;
	}
	output = '\0'; 
} 


int main(int argc,char* argv[])
{
	char inBuff[10000];
	char outBuff[10000];
	FILE* in;
	FILE* out;
	if(argc>1)
	{
		in=open(argv[1], O_RDONLY);
		
		out=open('tmpOut.txt', O_WRONLY,O_CREAT);
	}
		
	while(read(in,inBuff,10000)!=0)
	{
		parse(inBuff,outBuff);
		fprintf(stderr,"%s",outBuff);

		write(out,outBuff,10000);
	}
	fclose(in);
	fclose(out);
	
}