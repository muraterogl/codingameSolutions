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
        List<List<int>> grid = new List<List<int>>();

        //Creating grid while checking row errors
        for (int i = 0; i < 9; i++)
        {
            List<int> inputs = Console.ReadLine().Split(' ').ToList().Select(i => int.Parse(i)).ToList();
            
            if (inputs.ToHashSet().Count == 9) grid.Add(inputs);
            else {
                Console.WriteLine("false");
                return;
            }
        }

        //Checking column errors
        for (int i = 0; i < 9; i++)
        {
            HashSet<int> column = new HashSet<int>();
            for (int j = 0; j < 9; j++)
            {
                column.Add(grid[j][i]);
            }
            
            if (column.Count != 9)
            {
                Console.WriteLine("false");
                return;
            }
        }

        //Checking subgrid errors
        for (int i = 0; i < 9; i+=3)
        {
            for (int j = 0; j < 9; j+=3)
            {
                HashSet<int> subgrid = new HashSet<int>();
                for (int k = i; k < i+3; k++)
                {
                    for (int l = j; l < j+3; l++)
                    {
                        subgrid.Add(grid[k][l]);
                    }
                }
                if (subgrid.Count != 9)
                {
                    Console.WriteLine("false");
                    return;
                }
            }
        }

        Console.WriteLine("true");
    }
} 
