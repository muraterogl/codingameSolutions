using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int h = int.Parse(inputs[0]);
        int w = int.Parse(inputs[1]);
        int n = int.Parse(inputs[2]);
        string alive = Console.ReadLine();
        string dead = Console.ReadLine();
        char[,] cells = new char[h, w];
        for (int i = 0; i < h; i++)
        {
            string line = Console.ReadLine();
            for(int j = 0; j < line.Length; j++)
            {
                cells[i,j] = line[j];
            }
        }

        for (int x = 0; x < n; x++)
        {
            char[,] newCells = new char[h, w];
            for (int i = 0; i < h; i++)
            {
                for (int j = 0; j < w; j++)
                {
                    char currentCell = cells[i, j];
                    int neighborCount = 0;
                    for (int k = Math.Max(0, i-1); k < Math.Min(h, i+2); k++)
                    {
                        for (int l = Math.Max(0, j-1); l < Math.Min(w, j+2); l++)
                        {
                            if (cells[k, l] == 'O')
                                neighborCount++;
                        }
                    }
                    if (currentCell == 'O')
                    {
                        neighborCount--;
                        if (alive[neighborCount] == '0')
                            currentCell = '.';
                    }
                    else
                    {
                        if (dead[neighborCount] == '1')
                            currentCell = 'O';
                    }
                    newCells[i, j] = currentCell;
                }
            }
            cells = newCells;
        }

        for(int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                Console.Write(cells[i, j]);
            }
            Console.WriteLine();
        }

        
    }
}