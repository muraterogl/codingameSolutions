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
        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int w = int.Parse(inputs[0]);
        int h = int.Parse(inputs[1]);
        inputs = Console.ReadLine().Split(' ');
        int startRow = int.Parse(inputs[0]);
        int startCol = int.Parse(inputs[1]);
        int n = int.Parse(Console.ReadLine());

        List<List<int>> results = new List<List<int>>();

        for (int i = 0; i < n; i++)
        {
            List<List<char>> currentMap = new List<List<char>>();
            for (int j = 0; j < h; j++)
            {
                List<char> row = new List<char>();
                row.AddRange(Console.ReadLine());
                currentMap.Add(row);
            }

            int currentX = startCol;
            int currentY = startRow;
            int length = 0;
            int roundCount = 0;

            while (currentMap[currentY][currentX]!= 'T' && currentMap[currentY][currentX]!= '.')
            {
                
                if (currentMap[currentY][currentX] == '^')
                {
                    currentY--;
                    length++;
                }
                else if (currentMap[currentY][currentX] == 'v')
                {
                    currentY++;
                    length++;
                }
                else if (currentMap[currentY][currentX] == '<')
                {
                    currentX--;
                    length++;
                }
                else if (currentMap[currentY][currentX] == '>')
                {
                    currentX++;
                    length++;
                }

                if (currentX == startCol && currentY == startRow)
                {
                    roundCount++;
                }
                if (roundCount > 0 || currentX >= w || currentY >= h)
                {
                    results.Add(new List<int>{i, int.MaxValue});
                    break;
                }
                if (!"^v<>".Contains(currentMap[currentY][currentX]))
                {
                    if (currentMap[currentY][currentX] != 'T')
                    {
                        length = int.MaxValue;
                    }
                    results.Add(new List<int>{i, length});
                }
            }
        }

        if (results.All(result => result[1]==int.MaxValue))
        {
            Console.WriteLine("TRAP");
        }
        else
        {
            results = results.OrderBy(result => result[1]).ToList();
            Console.WriteLine(results[0][0]);
        }

        
    }
} 
