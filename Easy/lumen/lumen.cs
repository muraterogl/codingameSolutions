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
        int N = int.Parse(Console.ReadLine());
        int L = int.Parse(Console.ReadLine());
        List<List<int>> cells = new List<List<int>>();
        List<List<int>> candles = new List<List<int>>();
        for (int i = 0; i < N; i++)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            List<int> rowHold = new List<int>();
            for (int j = 0; j < N; j++)
            {
                if (inputs[j] == "C")
                {
                    candles.Add(new List<int>{j, i});
                }
                rowHold.Add(0);
            }
            cells.Add(rowHold);
        }

        candles.ForEach(candle => {
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    cells[j][i] = Math.Max(cells[j][i], Math.Max(0, L - Math.Max(Math.Abs(candle[0]-j), Math.Abs(candle[1]-i))));
                }
            }
        });

        int darkCount = 0;

        cells.ForEach(row => row.ForEach(cell => {
            if (cell == 0)
            {
                darkCount++;
            }
        }));

        Console.WriteLine(darkCount);
    }
} 
